"""A.1 gap-2 endgame: D-sign map and compensation margins.

Two exact regroupings of the CORE difference (gap 2, e_j = E(2v+j)):

  (G1)  LHS - RHS = p D1 + (q-2) D3 + (e0 - e2) B(v+1)
  (G2)  LHS - RHS = (p-1) D1 + (q-1) D3 + (e1 - e3) B(v)

with D1 = e1 B(v) - e0 B(v+1), D3 = e3 B(v) - e2 B(v+1); both
identities verified exactly here.  The positive terms are always
> 0; the D's can be negative in a corner.  Useful clean bounds when
negative:  |D1|^- <= (e0 - e1) B(v+1),  |D3|^- <= (e2 - e3) B(v+1)
(proved: e1 B(v) >= e1 B(v+1), e3 B(v) >= e3 B(v+1)) -- this alone
closes (p,q) = (1,2).

This probe maps, over the full gap-2 grid with corner emphasis
(h in [3,8] at large k; also the bulk grid):
1. identity checks for G1 and G2 (exact);
2. sign census of D1, D3 by (h, k-regime, v);
3. where any D < 0: the compensation ratios
   neg(G1)/(e0-e2)B(v+1) and neg(G2)/(e1-e3)B(v) -- max over the
   grid (need < 1 for at least one grouping at every config);
4. the (p,q) profile of the D<0 region (is p small there?).

Output: logs/993_A1_dsign.json
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def band_kA(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(lBG - 1, k0 - 1, C - 1)


def f(alpha, beta, m):
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def main():
    ident_bad = 0
    rows = 0
    d1_neg, d3_neg = [], []
    worst_comp = {"G1": None, "G2": None, "best": None}
    pq_profile = {}
    for h in (3, 4, 5, 6, 8, 12, 16, 24, 40):
        for v in (1, 2, 3, 4, 6, 10, 16):
            for q in range(2, min(h - 1, 8) + 1):
                p = h - q
                M = v + 2
                C = p * v + q * M
                kA = band_kA(C, h)
                ks = sorted({4, 6, 8, kA // 2, 2 * kA // 3,
                             5 * kA // 6, min(kA, 100)})
                for k in (kk for kk in ks if 4 <= kk <= min(kA, 100)):
                    e = [f(2 * v + j, C - 2 * v - j - 2, k - 4)
                         for j in range(4)]
                    Bv = f(v, C - v - 2, k - 3)
                    Bv1 = f(v + 1, C - v - 3, k - 3)
                    lhs = (p * e[1] + (q - 2) * e[3]) * Bv
                    rhs = ((p - 1) * e[0] + (q - 1) * e[2]) * Bv1
                    D1 = e[1] * Bv - e[0] * Bv1
                    D3 = e[3] * Bv - e[2] * Bv1
                    g1 = p * D1 + (q - 2) * D3 + (e[0] - e[2]) * Bv1
                    g2 = (p - 1) * D1 + (q - 1) * D3 + (e[1] - e[3]) * Bv
                    if g1 != lhs - rhs or g2 != lhs - rhs:
                        ident_bad += 1
                        continue
                    rows += 1
                    if D1 < 0:
                        d1_neg.append([h, p, q, v, k])
                    if D3 < 0:
                        d3_neg.append([h, p, q, v, k])
                    # compensation ratios (negative part over positive term)
                    negG1 = max(0, -(p * D1)) + max(0, -((q - 2) * D3))
                    posG1 = (e[0] - e[2]) * Bv1
                    negG2 = max(0, -((p - 1) * D1)) \
                        + max(0, -((q - 1) * D3))
                    posG2 = (e[1] - e[3]) * Bv
                    r1 = float(Fraction(negG1, posG1)) if posG1 else None
                    r2 = float(Fraction(negG2, posG2)) if posG2 else None
                    for key, r in (("G1", r1), ("G2", r2)):
                        if r is not None and (worst_comp[key] is None
                                              or r > worst_comp[key][0]):
                            worst_comp[key] = [r, h, p, q, v, k]
                    rb = min(x for x in (r1, r2) if x is not None) \
                        if (r1 is not None or r2 is not None) else None
                    if rb is not None and (worst_comp["best"] is None
                                           or rb > worst_comp["best"][0]):
                        worst_comp["best"] = [rb, h, p, q, v, k]
                    if D1 < 0 or D3 < 0:
                        pq_profile[(p, q)] = pq_profile.get((p, q), 0) + 1
    out = {"rows": rows, "identity_failures": ident_bad,
           "n_D1_negative": len(d1_neg), "D1_neg_sample": d1_neg[:20],
           "n_D3_negative": len(d3_neg), "D3_neg_sample": d3_neg[:20],
           "worst_compensation": worst_comp,
           "pq_profile_where_D_negative":
               {str(key): val for key, val in sorted(pq_profile.items())}}
    print(f"[D-sign] {rows} configs, identity failures {ident_bad}; "
          f"D1<0 at {len(d1_neg)}, D3<0 at {len(d3_neg)}", flush=True)
    print(f"[comp] worst G1 {worst_comp['G1']}; worst G2 "
          f"{worst_comp['G2']}; worst BEST-of-two "
          f"{worst_comp['best']}", flush=True)
    print(f"[pq] D<0 region (p,q) profile: "
          f"{out['pq_profile_where_D_negative']}", flush=True)
    path = REPO / "logs" / "993_A1_dsign.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
