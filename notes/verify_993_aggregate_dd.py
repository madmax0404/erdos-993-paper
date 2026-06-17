"""Aggregate DD (flow log-concavity) scan: the reform candidate.

The weighted per-pair E-core is refuted (see
logs/993_purepair_reduction.json): honest in-band violations at
1-heavy backgrounds, e.g. (1,27,1^24) k=6 ratio 1.18 and
(128,128,1^192) k=7 ratio 2.53.  The TRUE requirement of the pipeline
is the aggregate

    (G')^2 - G G'' >= 0,   G(t) = [prod_i (E_i + t b_i)]_k,

equivalently sum_{i!=j}(G y_ij - x_i x_j) <= sum_i x_i^2 with
x_i = [b_i prod_{l!=i} A_l]_k, y_ij = [b_i b_j prod_{l!=i,j} A_l]_k.
This script scans the aggregate EXACTLY across t in {0,1/2,1,3/2,2}:

1. Sanity: at uniform multisets (c^h) the aggregate ratio equals the
   symmetric per-pair ratio (the split is exact by symmetry); checked
   against an independent two-base-f computation.
2. Danger families (c,c,1^A), (1,c,1^A), (2,c,1^A) on c/A grids,
   in-band k (sampled), full t-grid.
3. Every per-pair violation instance from the first log, full t-grid.
4. Random mixed multisets (h in [3,10], c_i in [1,12]), in-band k,
   full t-grid.
5. A -> infinity probe on (c,c,1^A), A up to 1024.
6. Smallest-n per-pair violation witness (for the paper).

Aggregate ratio reported: sum_{i!=j}(G y - x x) / sum_i x_i^2
(violation iff > 1).  Output: logs/993_aggregate_dd.json
"""

from __future__ import annotations

import json
import random
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(9931)
TGRID = [(0, 1), (1, 2), (1, 1), (3, 2), (2, 1)]
TNAMES = ["0", "1/2", "1", "3/2", "2"]


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


def ksample(kA, kcap=40):
    base = [2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 26, 32, 40]
    ks = sorted({k for k in base if k <= min(kA, kcap)} |
                ({min(kA, kcap)} if kA >= 2 else set()))
    return [k for k in ks if k >= 2]


def pmul(p, q, kmax):
    out = [0] * (kmax + 1)
    for i, a in enumerate(p[: kmax + 1]):
        if a:
            for j, bc in enumerate(q[: kmax + 1 - i]):
                if bc:
                    out[i + j] += a * bc
    return out


def ppow(p, e, kmax):
    out = [1]
    base = p[: kmax + 1]
    while e:
        if e & 1:
            out = pmul(out, base, kmax)
        e >>= 1
        if e:
            base = pmul(base, base, kmax)
    return out


def poly_E(c):
    return [comb(c, m) << m for m in range(c + 1)]


def poly_b(c):
    return [0] + [comb(c, m) for m in range(c + 1)]


def slot_poly(c, p, q):
    E, B = poly_E(c), poly_b(c)
    n = max(len(E), len(B))
    return [q * (E[m] if m < len(E) else 0) +
            p * (B[m] if m < len(B) else 0) for m in range(n)]


def aggregate_ratio(cs, k, p, q):
    """Exact aggregate-DD ratio for multiset cs at t = p/q, position k.

    Returns (violates, ratio_float) with
    ratio = sum_{i!=j}(G y_ij - x_i x_j) / sum_i x_i^2."""
    types = sorted(Counter(cs).items())
    kmax = k
    A = {c: slot_poly(c, p, q) for c, _ in types}
    B = {c: poly_b(c) for c, _ in types}
    Pw = {}
    for c, m in types:
        Pw[c] = {m: ppow(A[c], m, kmax)}
        for down in (1, 2):
            if m - down >= 0:
                Pw[c][m - down] = ppow(A[c], m - down, kmax)
    mults = dict(types)

    def prodbr(extra, repl, k_):
        """[ prod_extra * prod_c A_c^{mults[c] - repl.get(c,0)} ]_{k_}"""
        w = [1]
        for pol in extra:
            w = pmul(w, pol, kmax)
        for c, m in types:
            w = pmul(w, Pw[c][m - repl.get(c, 0)], kmax)
        return w[k_] if k_ < len(w) else 0

    G = prodbr([], {}, k)
    xs = {c: prodbr([B[c]], {c: 1}, k) for c, _ in types}
    sum_x = sum(m * xs[c] for c, m in types)
    sum_x2 = sum(m * xs[c] ** 2 for c, m in types)
    lhs = 0
    for ci, mi in types:
        for cj, mj in types:
            if ci == cj:
                cnt = mi * (mi - 1)
                if cnt == 0:
                    continue
                y = prodbr([B[ci], B[ci]], {ci: 2}, k)
            else:
                cnt = mi * mj
                y = prodbr([B[ci], B[cj]], {ci: 1, cj: 1}, k)
            lhs += cnt * (G * y - xs[ci] * xs[cj])
    if sum_x2 == 0:
        return False, None
    return lhs > sum_x2, float(Fraction(lhs, sum_x2))


def scan_family(name, multisets, out, kcap=40, tgrid=TGRID):
    worst, viols, n = [], [], 0
    for cs in multisets:
        C, h = sum(cs), len(cs)
        kA = band_kA(C, h)
        for k in ksample(kA, kcap):
            for (p, q), tn in zip(tgrid, TNAMES):
                n += 1
                bad, r = aggregate_ratio(cs, k, p, q)
                if r is not None:
                    worst.append([r, sorted(Counter(cs).items()), k, tn])
                    worst.sort(key=lambda z: -z[0])
                    del worst[8:]
                if bad:
                    viols.append([r, sorted(Counter(cs).items()), k, tn])
    out[name] = {"checked": n, "n_violations": len(viols),
                 "violations": viols[:50], "worst": worst}
    print(f"[{name}] {n} checked, {len(viols)} violations, "
          f"worst {worst[0] if worst else None}", flush=True)


def main():
    out = {}

    # 1. uniform sanity: aggregate == symmetric per-pair at (c^h), t=0
    mism = []
    for cv in (1, 2, 3, 4, 6):
        for h in (3, 4, 6, 8):
            cs = [cv] * h
            kA = band_kA(cv * h, h)
            for k in ksample(kA, 24):
                _, ragg = aggregate_ratio(cs, k, 0, 1)
                A_ = (h - 2) * cv
                P = f(2 * cv, A_, k - 2)
                QE = comb(cv * h, k) << k
                X0 = f(cv, cv + A_, k - 1)
                pair = float(Fraction((P * QE - X0 * X0) * (h - 1), X0 * X0))
                if ragg is None or abs(ragg - pair) > 1e-9 * max(1, abs(pair)):
                    mism.append([cv, h, k, ragg, pair])
    out["uniform_sanity"] = {"mismatches": mism}
    print(f"[uniform sanity] mismatches: {len(mism)}", flush=True)

    # 2. danger families, full t-grid
    fam = []
    for cv in (2, 4, 8, 16, 32, 64, 128):
        for A_ in (1, 2, 4, 8, 16, 32, 64, 128, 192, 256):
            fam.append([cv, cv] + [1] * A_)
    scan_family("cc1A", fam, out)
    fam = []
    for cv in (2, 4, 8, 16, 32, 64, 128):
        for A_ in (1, 2, 4, 8, 16, 32, 64, 128, 256):
            fam.append([1, cv] + [1] * A_)
            fam.append([2, cv] + [1] * A_)
    scan_family("ray1c2c", fam, out)

    # 3. per-pair violation witnesses from the first log
    log1 = json.loads((REPO / "logs" / "993_purepair_reduction.json")
                      .read_text())
    inst = set()
    for row in log1["danger_cc1A"]["violations"]:
        _, cv, A_, k = row
        inst.add((cv, cv, A_, k))
    for key in ("1c", "2c"):
        for row in log1["rays"][key]["violations"]:
            _, a, b, A_, k = row
            inst.add((a, b, A_, k))
    for row in log1["dense"]["violations"]:
        _, a, b, A_, k = row
        inst.add((a, b, A_, k))
    worst, viols, n = [], [], 0
    for (a, b, A_, k) in sorted(inst):
        cs = [a, b] + [1] * A_
        for (p, q), tn in zip(TGRID, TNAMES):
            n += 1
            bad, r = aggregate_ratio(cs, k, p, q)
            if r is not None:
                worst.append([r, a, b, A_, k, tn])
                worst.sort(key=lambda z: -z[0])
                del worst[8:]
            if bad:
                viols.append([r, a, b, A_, k, tn])
    out["perpair_witnesses"] = {"instances": len(inst), "checked": n,
                                "n_violations": len(viols),
                                "violations": viols[:50], "worst": worst}
    print(f"[witnesses] {len(inst)} instances, {len(viols)} aggregate "
          f"violations, worst {worst[0] if worst else None}", flush=True)

    # smallest-n per-pair violation (paper witness)
    best = None
    for row in log1["dense"]["violations"]:
        r, a, b, A_, k = row
        C, h = a + b + A_, A_ + 2
        n_v = 1 + h + 2 * C
        if best is None or n_v < best[0]:
            best = [n_v, a, b, A_, k, r]
    out["smallest_perpair_witness"] = best
    print(f"[witness] smallest-n per-pair violation: n={best[0]} at "
          f"(a,b,A,k)=({best[1]},{best[2]},{best[3]},{best[4]}) "
          f"ratio {best[5]:.4f}", flush=True)

    # 4. random mixed multisets
    fam = []
    for _ in range(40):
        h = random.randint(3, 10)
        fam.append([random.randint(1, 12) for _ in range(h)])
    scan_family("random_mixed", fam, out, kcap=30)

    # 5. A -> infinity probe on (c,c,1^A)
    probes = {}
    for cv in (4, 16, 64):
        for k in (3, 6, 12, 24):
            seq = []
            for A_ in (128, 256, 512, 1024):
                cs = [cv, cv] + [1] * A_
                if k > band_kA(sum(cs), len(cs)):
                    continue
                _, r = aggregate_ratio(cs, k, 0, 1)
                seq.append([A_, r])
            probes[f"c={cv},k={k}"] = seq
    out["A_limit"] = probes
    mx = max((r for s_ in probes.values() for _, r in s_ if r is not None),
             default=None)
    print(f"[A-limit] max aggregate ratio = {mx}", flush=True)

    path = REPO / "logs" / "993_aggregate_dd.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
