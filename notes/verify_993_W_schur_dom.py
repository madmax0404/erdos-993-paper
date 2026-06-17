"""W-Schur (proved) + the DOM' formulation: exact verification.

LEMMA (W-Schur).  At fixed (C, h, k, s), the class mass
W_s = sum_{|S|=s} f(sigma_S, C - sigma_S, k - s),  sigma_S = sum_{i in S} c_i,
is Schur-convex in (c_1..c_h): spreading the multiset (away from
balance) never decreases it.

Proof.  (a) A Robin Hood transfer toward balance on slots (i, j)
(c_i < c_j) induces on the s-subset sums the simultaneous transfers
(sigma_{S+i}, sigma_{S+j}) -> (sigma_{S+i}+1, sigma_{S+j}-1) over
all S avoiding i, j, each toward balance since
sigma_S + c_i < sigma_S + c_j; subsets containing both or neither
are unchanged.  Hence the subset-sum multiset of the more spread
multiset majorizes that of the less spread one.  (b) The summand
u(sigma) = f(sigma, C-sigma, m) is convex in sigma: the exact second
difference is Delta^2 u = f(sigma, C-sigma-2, m-2) >= 0 for m >= 2,
u is linear for m = 1 (u = 2C - sigma) and constant for m = 0.
(c) Karamata: majorization + convex summand => the sum is larger on
the spread side.  QED

Consequently W_s(c) >= W_s(bal(C,h)) for every multiset c -- both
sides of every rung grow away from balance, and DOM is a
relative-rate statement.  The cleaner conditioning is on the
balanced companion itself:

    (DOM')  if ratio_s(bal(C,h), k) >= theta_0, then
            ratio_s(c, k) <= ratio_s(bal(C,h), k) for ALL c with
            sum C and h parts.

This script:
1. sanity-verifies W-Schur on random transfers (exact);
2. scans DOM' exhaustively (h in [3,6], C <= 24, every band k,
   rungs s <= 4): for each (C,h,k,s), compares max over ALL
   partitions to bal, recording the conditional landscape --
   sup over cases with ratio(bal) >= x of [max_c ratio(c) -
   ratio(bal)], reported for x in {0.5, 0.6, 0.65, 0.7};
3. spot-checks DOM' at large h (the high-regime families, h <= 40).

Output: logs/993_W_schur_dom.json
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(99312099)


def band_kA(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(lBG - 1, k0 - 1, C - 1)


def profile(cs, k):
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


def rung_ratios(cs, k, smax):
    W = profile(cs, k)
    out = {}
    for s in range(1, min(smax, len(W) - 2) + 1):
        if W[s + 1] > 0:
            out[s] = Fraction((s + 1) * W[s - 1] * W[s + 1],
                              s * W[s] * W[s])
    return out


def parts(C, h, lo=1):
    if h == 1:
        if C >= lo:
            yield (C,)
        return
    for first in range(lo, C // h + 1):
        for rest in parts(C - first, h - 1, first):
            yield (first,) + rest


def balanced(C, h):
    a, r = divmod(C, h)
    return [a] * (h - r) + [a + 1] * r


def main():
    out = {}

    # 1. W-Schur sanity: spreading transfer never decreases any W_s
    fails, n = [], 0
    for _ in range(300):
        h = random.randint(3, 9)
        cs = [random.randint(1, 12) for _ in range(h)]
        C = sum(cs)
        kA = band_kA(C, h)
        if kA < 2:
            continue
        k = random.choice(range(2, kA + 1))
        # pick a spreading transfer: c_i <= c_j -> (c_i - 1, c_j + 1)
        idx = sorted(range(h), key=lambda t: cs[t])
        i, j = idx[0], idx[-1]
        if cs[i] < 2:
            continue
        cs2 = list(cs)
        cs2[i] -= 1
        cs2[j] += 1
        Wa, Wb = profile(cs, k), profile(cs2, k)
        for s in range(min(len(Wa), len(Wb))):
            n += 1
            if Wb[s] < Wa[s]:
                fails.append([cs, k, s])
    out["w_schur_sanity"] = {"checked": n, "fails": fails[:20],
                             "n_fails": len(fails)}
    print(f"[W-Schur] {n} (multiset,k,s) checks under spreading, "
          f"{len(fails)} failures", flush=True)

    # 2. DOM' exhaustive landscape
    grid = []          # rows: (ratio_bal, max_ratio_other, C, h, k, s)
    for h in (3, 4, 5, 6):
        for C in range(h + 2, 25):
            kA = band_kA(C, h)
            bal = balanced(C, h)
            for k in range(2, kA + 1):
                rb = rung_ratios(bal, k, 4)
                best = {}
                for p in parts(C, h):
                    if list(p) == sorted(bal):
                        continue
                    rc = rung_ratios(list(p), k, 4)
                    for s, r in rc.items():
                        if s not in best or r > best[s]:
                            best[s] = r
                for s, r in best.items():
                    if s in rb:
                        grid.append([float(rb[s]), float(r), C, h, k, s])
    thresholds = {}
    for x in (0.5, 0.6, 0.65, 0.7):
        rows = [g for g in grid if g[0] >= x]
        exceed = [g for g in rows if g[1] > g[0]]
        thresholds[str(x)] = {
            "cases": len(rows), "exceedances": len(exceed),
            "max_excess": max((g[1] - g[0] for g in exceed), default=0.0),
            "examples": exceed[:10]}
    # unconditional: worst bal-ratio at which ANY partition beats bal
    beat = [g for g in grid if g[1] > g[0]]
    out["dom_prime"] = {
        "grid_cases": len(grid),
        "by_threshold": thresholds,
        "max_bal_ratio_when_beaten":
            max((g[0] for g in beat), default=None),
        "max_beating_ratio": max((g[1] for g in beat), default=None)}
    print(f"[DOM'] {len(grid)} (C,h,k,s) cases; "
          f"max bal-ratio ever beaten: "
          f"{out['dom_prime']['max_bal_ratio_when_beaten']:.4f}; "
          f"per-threshold exceedances: "
          f"{[(x, thresholds[x]['exceedances']) for x in thresholds]}",
          flush=True)

    # 3. large-h spot checks
    rows, exceed = 0, []
    for h in (12, 20, 30, 40):
        for q in (2, h // 3, h // 2, h - 2):
            bal = [1] * (h - q) + [2] * q
            C = sum(bal)
            kA = band_kA(C, h)
            ks = [k for k in sorted({3, 5, kA // 2, kA}) if 2 <= k <= kA]
            variants = [
                sorted([1] * (h - q + 1) + [2] * (q - 2) + [3]),
                sorted([1] * (h - q + 2) + [2] * (q - 4) + [3, 3])
                if q >= 4 else None,
                sorted([1] * (h - q) + [2] * (q - 2) + [4])
                if q >= 2 else None,
                sorted([1] * (h - 2) + [2, C - h])
                if C - h >= 3 else None,
            ]
            for k in ks:
                rb = rung_ratios(bal, k, 3)
                for cs in variants:
                    if cs is None or sum(cs) != C or len(cs) != h:
                        continue
                    rc = rung_ratios(cs, k, 3)
                    for s, r in rc.items():
                        if s in rb:
                            rows += 1
                            if r > rb[s]:
                                exceed.append([float(rb[s]), float(r),
                                               h, q, k, s])
    out["large_h"] = {"checked": rows, "exceedances": exceed[:20],
                      "n_exceed": len(exceed),
                      "max_bal_ratio_beaten":
                          max((e[0] for e in exceed), default=None)}
    print(f"[large-h] {rows} comparisons, {len(exceed)} exceedances, "
          f"max bal-ratio beaten: "
          f"{out['large_h']['max_bal_ratio_beaten']}", flush=True)

    # 4. classify ALL exceedances by k - s; band-bottom census
    km_ex = {}
    for h in (3, 4, 5, 6):
        for C in range(h + 2, 25):
            kA = band_kA(C, h)
            bal = balanced(C, h)
            for k in range(2, kA + 1):
                rb = rung_ratios(bal, k, 4)
                for p in parts(C, h):
                    rc = rung_ratios(list(p), k, 4)
                    for s, r in rc.items():
                        if s in rb and r > rb[s]:
                            km_ex[k - s] = km_ex.get(k - s, 0) + 1
    for h in (12, 20, 30, 40):
        for q in (2, h // 3, h // 2, h - 2):
            bal = [1] * (h - q) + [2] * q
            C = sum(bal)
            kA = band_kA(C, h)
            ks = [k for k in sorted({3, 5, kA // 2, kA}) if 2 <= k <= kA]
            variants = [
                sorted([1] * (h - q + 1) + [2] * (q - 2) + [3]),
                sorted([1] * (h - q + 2) + [2] * (q - 4) + [3, 3])
                if q >= 4 else None,
                sorted([1] * (h - q) + [2] * (q - 2) + [4])
                if q >= 2 else None,
                sorted([1] * (h - 2) + [2, C - h]) if C - h >= 3 else None,
            ]
            for k in ks:
                rb = rung_ratios(bal, k, 3)
                for cs in variants:
                    if cs is None or sum(cs) != C or len(cs) != h:
                        continue
                    rc = rung_ratios(cs, k, 3)
                    for s, r in rc.items():
                        if s in rb and r > rb[s]:
                            km_ex[k - s] = km_ex.get(k - s, 0) + 1
    out["exceedance_km_histogram"] = km_ex
    print(f"[classify] exceedances by k-s: {km_ex}", flush=True)

    # band-bottom census: how high do k-s <= 2 rung ratios climb?
    bb = []
    for h in (12, 40, 100, 200):
        for q in (2, h // 2, h - 2):
            base = [1] * (h - q) + [2] * q
            C = sum(base)
            kA = band_kA(C, h)
            for cs in (base, sorted([1] * (h - 2) + [2, C - h])
                       if C - h >= 3 else None):
                if cs is None:
                    continue
                W = profile(list(cs), min(kA, 8))
                for s in range(1, min(6, len(W) - 2) + 1):
                    for k in (s + 1, s + 2):
                        if k > kA or k > 8:
                            continue
                        Wk = profile(list(cs), k)
                        if s + 1 < len(Wk) and Wk[s + 1] > 0:
                            r = float(Fraction(
                                (s + 1) * Wk[s - 1] * Wk[s + 1],
                                s * Wk[s] * Wk[s]))
                            bb.append([r, h, q, k, s, k - s])
    bb.sort(key=lambda z: -z[0])
    out["band_bottom_census"] = {"max": bb[0] if bb else None,
                                 "top10": bb[:10]}
    print(f"[band-bottom] max k-s<=2 ratio observed: "
          f"{bb[0] if bb else None}", flush=True)

    path = REPO / "logs" / "993_W_schur_dom.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
