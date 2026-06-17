"""The factorial ladder: a t-free sufficient route to hypothesis (ii).

LEMMA (factorial criterion).  Let G(t) = sum_s W_s t^s with W_s >= 0
and contiguous support.  If (s! W_s) is log-concave, then G is
log-concave on (0, infinity).

Proof.  With rho_s = (s! W_s)/((s-1)! W_{s-1}) = s W_s / W_{s-1}
nonincreasing in s (this IS log-concavity of s!W_s), write
(ln G)'(t) = G'/G = E_t[rho_{S+1}] under the tilted law
P_t(S = s) prop. to W_s t^s.  The family (P_t) is increasing in the
likelihood-ratio order as t grows, hence stochastically increasing,
and rho_{S+1} is nonincreasing, so E_t[rho_{S+1}] is nonincreasing
in t (Shaked--Shanthikumar 1.C).  Hence (ln G)'' <= 0.  QED

Consequently hypothesis (ii) at position k follows from the LADDER

    (L_s)   s W_s^2 >= (s+1) W_{s-1} W_{s+1},  1 <= s <= min(h,k)-1,

where W_s = W_s(k) = sum_{|S|=s}[prod_{i in S} b_i prod_{not S} E_i]_k
is the class-mass profile.  Exact consistencies:
  - rung s=1 is EXACTLY the aggregate at t = 0 (W_1^2 >= 2 W_0 W_2);
  - at h = 2 the single rung is EXACTLY Theorem L3's inequality;
  - at uniform multisets rung 1 is EXACTLY the symmetric E-core
    (W_s = C(h,s)u_s turns L_1 into h u_1^2 >= (h-1) u_0 u_2).

This script tests the ladder EXACTLY (integer arithmetic) across:
1. uniform multisets (c <= 12, h <= 12), all band k, all rungs;
2. the (a,b,1^A) closed-form families: the 200 per-pair violation
   witnesses, the danger grids (c,c,1^A), and rays (1,c),(2,c);
3. 60 random mixed multisets (h in [3,10], c_i <= 12), direct
   bivariate (x,t) expansion;
4. a Schur probe: all partitions of C into h parts at small (C,h),
   locating the partition that maximizes each rung ratio (is the
   balanced partition always the worst?);
5. consistency: rung-1 sign vs the aggregate-at-t0 sign (sample),
   and the h=2 rung vs Theorem L3's display.

Rung ratio reported: (s+1) W_{s-1} W_{s+1} / (s W_s^2)  (<= 1 ok).
Output: logs/993_factorial_ladder.json
"""

from __future__ import annotations

import json
import random
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(99312)
KCAP = 40


def f(alpha, beta, m):
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def band_kA(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(lBG - 1, k0 - 1, C - 1)


def ksample(kA, kcap=KCAP):
    base = [2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 26, 32, 40]
    ks = sorted({k for k in base if k <= min(kA, kcap)} |
                ({min(kA, kcap)} if kA >= 2 else set()))
    return [k for k in ks if k >= 2]


def profile_uniform(c, h, k):
    return [comb(h, s) * f(s * c, (h - s) * c, k - s)
            for s in range(min(h, k) + 1)]


def profile_ab1A(a, b, A, k):
    out = []
    for s in range(min(A + 2, k) + 1):
        tot = 0
        for ia in (0, 1):
            for ib in (0, 1):
                j = s - ia - ib
                if j < 0 or j > A:
                    continue
                alpha = j + ia * a + ib * b
                beta = (A - j) + (1 - ia) * a + (1 - ib) * b
                tot += comb(A, j) * f(alpha, beta, k - s)
        out.append(tot)
    return out


def profile_general(cs, k):
    """Class-mass profile via bivariate (x,t) expansion, exact."""
    cur = {0: [1] + [0] * k}
    for c in cs:
        E = [(comb(c, m) << m) if m <= c else 0 for m in range(k + 1)]
        B = [comb(c, m - 1) if 1 <= m <= c + 1 else 0 for m in range(k + 1)]
        new = {}
        for s, arr in cur.items():
            for ds, pol in ((0, E), (1, B)):
                tgt = new.setdefault(s + ds, [0] * (k + 1))
                for i, ai in enumerate(arr):
                    if ai:
                        for j in range(k + 1 - i):
                            if pol[j]:
                                tgt[i + j] += ai * pol[j]
        cur = new
    return [cur[s][k] if s in cur else 0
            for s in range(min(len(cs), k) + 1)]


def ladder(W):
    """Check all rungs; return (n_fail, worst_ratio, worst_s)."""
    worst, worst_s, nf = None, None, 0
    for s in range(1, len(W) - 1):
        if W[s + 1] == 0:
            break
        lhs = s * W[s] * W[s]
        rhs = (s + 1) * W[s - 1] * W[s + 1]
        r = float(Fraction(rhs, lhs))
        if worst is None or r > worst:
            worst, worst_s = r, s
        if rhs > lhs:
            nf += 1
    return nf, worst, worst_s


def scan(name, items, prof, out):
    """items: list of (label, profile_args, C, h)."""
    worst, viols, n = [], [], 0
    for label, args, C, h in items:
        kA = band_kA(C, h)
        for k in ksample(kA):
            n += 1
            W = prof(*args, k)
            nf, r, s = ladder(W)
            if r is not None:
                worst.append([r, label, k, s])
                worst.sort(key=lambda z: -z[0])
                del worst[10:]
            if nf:
                viols.append([r, label, k, s])
    out[name] = {"checked": n, "n_violations": len(viols),
                 "violations": viols[:60], "worst": worst}
    print(f"[{name}] {n} profiles, {len(viols)} with rung failures, "
          f"worst {worst[0] if worst else None}", flush=True)


def partitions(C, h, lo=1):
    if h == 1:
        if C >= lo:
            yield (C,)
        return
    for first in range(lo, C // h + 1):
        for rest in partitions(C - first, h - 1, first):
            yield (first,) + rest


def main():
    out = {}

    # 1. uniform
    items = [(f"u({c}^{h})", ((c, h)), c * h, h)
             for c in range(1, 13) for h in range(3, 13)]
    scan("uniform", [(lab, args, C, h) for lab, args, C, h in
                     [(l, a, C, h) for l, a, C, h in items]],
         lambda c, h, k: profile_uniform(c, h, k), out)

    # 2. (a,b,1^A) families
    items = []
    log1 = json.loads((REPO / "logs" / "993_purepair_reduction.json")
                      .read_text())
    wit = set()
    for row in log1["danger_cc1A"]["violations"]:
        _, cv, A_, k = row
        wit.add((cv, cv, A_))
    for key in ("1c", "2c"):
        for row in log1["rays"][key]["violations"]:
            _, a, b, A_, k = row
            wit.add((a, b, A_))
    for row in log1["dense"]["violations"]:
        _, a, b, A_, k = row
        wit.add((a, b, A_))
    for (a, b, A_) in sorted(wit):
        items.append((f"wit({a},{b},1^{A_})", (a, b, A_), a + b + A_, A_ + 2))
    for cv in (2, 4, 8, 16, 32, 64, 128):
        for A_ in (1, 2, 4, 8, 16, 32, 64, 128, 256):
            items.append((f"(c,c)({cv},{A_})", (cv, cv, A_),
                          2 * cv + A_, A_ + 2))
            items.append((f"(1,c)({cv},{A_})", (1, cv, A_),
                          1 + cv + A_, A_ + 2))
            items.append((f"(2,c)({cv},{A_})", (2, cv, A_),
                          2 + cv + A_, A_ + 2))
    scan("ab1A", items, profile_ab1A, out)

    # 3. random mixed
    items = []
    for _ in range(60):
        h = random.randint(3, 10)
        cs = tuple(random.randint(1, 12) for _ in range(h))
        items.append((f"r{sorted(cs)}", (list(cs),), sum(cs), h))
    scan("random_mixed", items, lambda cs, k: profile_general(cs, k), out)

    # 4. Schur probe
    schur = {}
    for C, h in ((12, 3), (12, 4), (18, 3), (18, 4), (24, 4)):
        kA = band_kA(C, h)
        for k in (3, max(3, kA // 2), kA):
            if k < 3:
                continue
            rows = []
            for part in partitions(C, h):
                W = profile_general(list(part), k)
                nf, r, s = ladder(W)
                rows.append((r, part, s))
            rows.sort(key=lambda z: -z[0])
            spread = lambda p: sum(x * x for x in p)
            most_balanced = min((spread(p), p) for _, p, _ in rows)[1]
            schur[f"C={C},h={h},k={k}"] = {
                "top3": [[r, list(p), s] for r, p, s in rows[:3]],
                "most_balanced_partition": list(most_balanced),
                "argmax_is_most_balanced":
                    list(rows[0][1]) == list(most_balanced)}
    out["schur_probe"] = schur
    nbal = sum(1 for v in schur.values() if v["argmax_is_most_balanced"])
    print(f"[schur] {nbal}/{len(schur)} cases: worst partition is the "
          f"most balanced one", flush=True)

    # 5. consistency checks
    cons = {"rung1_vs_aggregate": [], "h2_vs_L3": []}
    for cs in ([4, 4, 1, 1], [1, 8, 1, 1], [2, 5, 3], [6, 6, 6]):
        C, h = sum(cs), len(cs)
        for k in ksample(band_kA(C, h), 12):
            W = profile_general(cs, k)
            r1_ok = W[1] * W[1] >= 2 * W[0] * W[2]
            # aggregate at t=0 directly
            g = comb(C, k) << k
            xs = [f(c, C - c, k - 1) for c in cs]
            agg = 0
            for i in range(h):
                for j in range(h):
                    if i != j:
                        y = f(cs[i] + cs[j], C - cs[i] - cs[j], k - 2)
                        agg += g * y - xs[i] * xs[j]
            agg_ok = agg <= sum(x * x for x in xs)
            cons["rung1_vs_aggregate"].append(
                [cs, k, r1_ok, agg_ok, r1_ok == agg_ok])
    for (c1, c2) in ((3, 4), (2, 7)):
        s_ = c1 + c2
        for k in range(2, s_):
            W = profile_general([c1, c2], k)
            lhs_l3 = 2 * f(s_, 0, k - 2) * (comb(s_, k) << k)
            x0 = f(c1, c2, k - 1)
            y0 = f(c2, c1, k - 1)
            cons["h2_vs_L3"].append(
                [c1, c2, k,
                 (W[1] ** 2 - 2 * W[0] * W[2]) ==
                 ((x0 + y0) ** 2 - lhs_l3)])
    bad = ([row for row in cons["rung1_vs_aggregate"] if not row[4]] +
           [row for row in cons["h2_vs_L3"] if not row[3]])
    out["consistency"] = {"n_checks":
                          len(cons["rung1_vs_aggregate"]) +
                          len(cons["h2_vs_L3"]),
                          "mismatches": bad[:10], "n_mismatch": len(bad)}
    print(f"[consistency] {out['consistency']['n_checks']} checks, "
          f"{len(bad)} mismatches", flush=True)

    path = REPO / "logs" / "993_factorial_ladder.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
