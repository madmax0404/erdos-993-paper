"""A.1 at gap 2: the k-stratified proof casing.

CORE at gap 2 (M = v+2), with e_j = E(2v+j) = f(2v+j, C-2v-j-2, k-4)
and B(t) = f(t, C-t-2, k-3):

    [p e_1 + (q-2) e_3] B(v)  >  [(p-1) e_0 + (q-1) e_2] B(v+1).

Stratification by k:
- k = 4: E-level is 0, so e_j = 1 and CORE <=> (h-2) B(v) >
  (h-2) B(v+1) <=> B strictly decreasing, which is exact:
  B(t) - B(t+1) = f(t, C-t-3, k-4) = 1 > 0.  PROVED.
- k = 5: E-level 1, e_j = 2C - 4 - 2v - j (linear).  CORE becomes a
  polynomial inequality in (v, p, q); this script certifies it (and
  its quadratic-corrected version) over a grid and reports the
  symbolic shape for the hand proof.
- k >= 6: genuine curvature; this script maps the exact CORE margin
  and the CORRECTED margin (with the quadratic terms
  2 W1 S_B - S_B^2 vs 2 W1 B(M-1) + B(M-1)^2) stratified by k, to
  confirm a uniform gap above 1 once k >= 6.

Also re-verifies the k=4 collapse identity exactly on a sweep.

Output: logs/993_A1_gap2.json
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
    out = {}

    # k = 4 collapse identity, exact sweep
    bad4, n4 = [], 0
    for h in (4, 8, 16, 40, 100):
        for v in (1, 2, 4, 8, 16):
            for q in (2, 3, h // 2, h - 1):
                if not 2 <= q <= h - 1:
                    continue
                p = h - q
                C = p * v + q * (v + 2)
                if 4 > band_kA(C, h):
                    continue
                k = 4
                n4 += 1
                e = [f(2 * v + j, C - 2 * v - j - 2, k - 4)
                     for j in range(4)]
                B = lambda t: f(t, C - t - 2, k - 3)
                lhs = (p * e[1] + (q - 2) * e[3]) * B(v)
                rhs = ((p - 1) * e[0] + (q - 1) * e[2]) * B(v + 1)
                ident = (e == [1, 1, 1, 1] and
                         B(v) - B(v + 1) == 1 and lhs > rhs)
                if not ident:
                    bad4.append([v, p, q])
    out["k4_collapse"] = {"checked": n4, "fails": bad4[:10],
                          "n_fails": len(bad4)}
    print(f"[k=4] {n4} checks, {len(bad4)} fails (E==1, B-step==1, "
          f"CORE strict)", flush=True)

    # k = 5 symbolic certification over (p, q) grid, polynomial in v
    import sympy as sp
    vv = sp.symbols('v', positive=True)
    k5_cert, k5_fail = 0, []
    for h in (4, 6, 8, 12, 20, 40, 80):
        for q in (2, 3, h // 2, h - 1):
            if not 2 <= q <= h - 1:
                continue
            p = h - q
            C = p * vv + q * (vv + 2)
            # k=5: e_j = 2C-4-2v-j; B(t) = f(t, C-t-2, 2)
            e = [2 * C - 4 - 2 * vv - j for j in range(4)]

            def Bpoly(t):
                # f(t, C-t-2, 2) = C(t,2) + 2 t (C-t-2) + 4 C(C-t-2,2)
                bt = C - t - 2
                return sp.expand(t * (t - 1) / 2 + 2 * t * bt
                                 + 2 * bt * (bt - 1))
            lhs = sp.expand((p * e[1] + (q - 2) * e[3]) * Bpoly(vv))
            rhs = sp.expand((p - 1) * e[0] + (q - 1) * e[2]) \
                * Bpoly(vv + 1)
            R = sp.expand(lhs - sp.expand(rhs))
            P = sp.Poly(R, vv)
            cs = P.all_coeffs()
            ok = cs[0] > 0 and all(
                P.eval(t) > 0 for t in range(1, 40))
            # rigorous beyond 40 via Taylor shift
            if ok:
                sh = sp.Poly(sp.expand(R.subs(vv, vv + 40)), vv)
                ok = all(c >= 0 for c in sh.all_coeffs()) and ok
            (k5_fail, None) if not ok else None
            if ok:
                k5_cert += 1
            else:
                k5_fail.append([h, p, q])
    out["k5_certified"] = {"certified": k5_cert, "fails": k5_fail[:10],
                           "n_fails": len(k5_fail)}
    print(f"[k=5] certified {k5_cert} (p,q) families (all v >= 1), "
          f"fails {len(k5_fail)}", flush=True)

    # k >= 6: stratified exact margins, CORE and corrected
    strat = {}
    for h in (4, 6, 8, 12, 16, 24, 40):
        for v in (1, 2, 3, 4, 6, 10):
            for q in range(2, min(h - 1, 6) + 1):
                p = h - q
                M = v + 2
                C = p * v + q * M
                kA = band_kA(C, h)
                for k in sorted({6, 8, 12, kA // 2, 3 * kA // 4,
                                 min(kA, 80)}):
                    if not 6 <= k <= min(kA, 80):
                        continue
                    e = [f(2 * v + j, C - 2 * v - j - 2, k - 4)
                         for j in range(4)]
                    B = lambda t: f(t, C - t - 2, k - 3)
                    x_v = f(v, C - v, k - 1)
                    x_M = f(M, C - M, k - 1)
                    W1 = p * x_v + q * x_M
                    core_l = (p * e[1] + (q - 2) * e[3]) * B(v)
                    core_r = ((p - 1) * e[0] + (q - 1) * e[2]) * B(v + 1)
                    SB = B(v)            # gap 2: S_B = B(v) single term
                    corr_l = (p * e[1] + (q - 2) * e[3]) \
                        * SB * (2 * W1 - SB)
                    corr_r = ((p - 1) * e[0] + (q - 1) * e[2]) \
                        * B(v + 1) * (2 * W1 + B(v + 1))
                    key = str(k) if k <= 12 else (
                        "mid" if k < 3 * kA // 4 else "top")
                    rec = strat.setdefault(key, [None, None])
                    if core_r > 0:
                        rc = float(Fraction(core_l, core_r))
                        if rec[0] is None or rc < rec[0]:
                            rec[0] = rc
                    if corr_r > 0:
                        rq = float(Fraction(corr_l, corr_r))
                        if rec[1] is None or rq < rec[1]:
                            rec[1] = rq
    out["k6plus_min_margins"] = {key: {"core_min": rec[0],
                                       "corrected_min": rec[1]}
                                 for key, rec in sorted(strat.items())}
    print("[k>=6] min CORE / corrected-CORE ratios by k-stratum:",
          flush=True)
    for key, rec in sorted(strat.items()):
        print(f"   k={key}: core {rec[0]:.4f}  corrected {rec[1]:.4f}",
              flush=True)

    path = REPO / "logs" / "993_A1_gap2.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
