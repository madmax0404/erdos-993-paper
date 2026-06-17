"""The N-profile and the Jensen reduction probe.

By the vertex reduction (993_m1_proof.md Sec. 6.2), lead_o over
all multisets at fixed (x, y, z, C, h, k) is minimized at
two-value backgrounds; by linearity the minimum equals

    const + (h-3) * conv(N)(mbar),

where N_v = WsW(v) D1O - WoW(v) D1S is the per-value profile,
conv(N) its lower convex envelope on [x, z], and
mbar = (C-x-y-z)/(h-3) the background mean.  If v -> N_v is
CONVEX, Jensen collapses the vertex family to SINGLE-background
shapes (x, y, z, u^{h-3}) (adjacent-integer mixes at fractional
mbar).

Structural support: the collapse lemma iterates.  E(m) =
f(m, C-m-2, k-4) = D^2_m f(m, C-m, k-2), and one level down
D^2_m E(m) = f(m, C-4-m, k-6) >= 0 -- both windows WsW, WoW are
convex in v.  N-convexity is then the comparison
D^2 WsW(v) * D1O >= D^2 WoW(v) * D1S, the lead_o comparison one
collapse level down (self-similar structure).

This probe, all exact:
(1) the iterated collapse identity D^2_v E(v) = f(v, C-4-v, k-6)
    at every position used;
(2) D^2_v N_v >= 0 across (x, g1, g2, h, mbar-regime, k) grids;
    failures recorded with position and relative depth;
(3) at small h: full vertex enumeration vs the single-value
    (Jensen) minimum -- does concentration at the mean attain
    the polytope minimum?

Output: logs/993_N_convexity.json
"""
from __future__ import annotations

import itertools
import json
import time
from collections import Counter
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
    if m < 0 or beta < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def profile(xb, ym, zt, C, k):
    """D1O, D1S, and N_v for v in [xb, zt]; plus the E-cache."""
    L, G = zt - ym + 1, zt - xb - 1
    yc, ac = {}, {}

    def yv(m):
        if m not in yc:
            yc[m] = f(m, C - m, k - 2) if m <= C else 0
        return yc[m]

    def Av(t):
        if t not in ac:
            ac[t] = f(t, C - t - 1, k - 2)
        return ac[t]

    E = lambda m: yv(m) - 2 * yv(m + 1) + yv(m + 2)
    B = lambda t: Av(t) - Av(t + 1)
    WE = lambda s, ln: sum(E(s + i) for i in range(ln))
    WB = lambda s, ln: sum(B(s + i) for i in range(ln))
    D1O, D1S = WB(xb, G), WB(ym - 1, L)
    N = {v: WE(v + ym - 1, L) * D1O - WE(v + xb, G) * D1S
         for v in range(xb, zt + 1)}
    return D1O, D1S, N, E


def backgrounds(nparts, total, lo, hi):
    if nparts == 0:
        if total == 0:
            yield ()
        return
    for v in range(lo, hi + 1):
        if v * nparts > total:
            break
        if total - v > hi * (nparts - 1):
            continue
        for rest in backgrounds(nparts - 1, total - v, v, hi):
            yield (v,) + rest


def main():
    t0 = time.time()
    id_n = id_ok = 0
    cx_n = cx_ok = 0
    cx_fail = []
    js_n = js_ok = 0
    rows = []
    shapes = [(x, x + g1, x + g1 + g2)
              for x in (1, 2, 4, 8)
              for (g1, g2) in ((1, 1), (2, 2), (1, 3), (3, 1),
                               (4, 8), (8, 4), (2, 6))]
    for (xb, ym, zt) in shapes:
        for h in (6, 10, 16, 28):
            nbg = h - 3
            for frac in (0, 1, 2, 3, 4):
                mbar = xb + (zt - xb) * frac // 4
                R = nbg * mbar
                C = xb + ym + zt + R
                kA = band_kA(C, h)
                for kf in (2, 3, 5):
                    k = max(6, kf * kA // 6)
                    if k > kA or k < 6:
                        continue
                    D1O, D1S, N, E = profile(xb, ym, zt, C, k)
                    # (1) iterated collapse identity
                    for v in range(xb, zt - 1):
                        id_n += 1
                        lhs = E(v) - 2 * E(v + 1) + E(v + 2)
                        rhs = f(v, C - 4 - v, k - 6)
                        id_ok += (lhs == rhs)
                    # (2) convexity of N
                    bad = []
                    scale = max(abs(N[v]) for v in N) or 1
                    for v in range(xb, zt - 1):
                        cx_n += 1
                        d2 = N[v] - 2 * N[v + 1] + N[v + 2]
                        if d2 >= 0:
                            cx_ok += 1
                        else:
                            bad.append(
                                [v, float(Fraction(-d2, scale))])
                    if bad:
                        cx_fail.append(
                            {"xyz": [xb, ym, zt], "h": h,
                             "mbar": mbar, "k": k,
                             "n_bad": len(bad),
                             "worst": max(b[1] for b in bad),
                             "bad_at": [b[0] for b in bad[:6]]})
                    rows.append({"xyz": [xb, ym, zt], "h": h,
                                 "mbar": mbar, "k": k,
                                 "convex": not bad})
    # (3) Jensen check at small h: single-value (or adjacent
    # mix) attains the enumeration minimum
    for (xb, ym, zt, h) in ((1, 3, 6, 6), (2, 5, 9, 6),
                            (1, 4, 9, 7), (3, 6, 12, 6),
                            (2, 6, 10, 7), (1, 5, 12, 7)):
        nbg = h - 3
        R = nbg * (xb + zt) // 2
        allbg = list(backgrounds(nbg, R, xb, zt))
        if not allbg:
            continue
        C = xb + ym + zt + R
        kA = band_kA(C, h)
        for kf in (2, 3):
            k = max(6, kf * kA // 3)
            if k > kA:
                continue
            D1O, D1S, N, _ = profile(xb, ym, zt, C, k)
            vals = {}
            for bg in allbg:
                s = sum(N[v] for v in bg)
                vals[bg] = s
            mn_all = min(vals.values())
            # single-value or adjacent-pair (Jensen candidates)
            mn_j = min(s for bg, s in vals.items()
                       if len(set(bg)) == 1
                       or (len(set(bg)) == 2
                           and max(bg) - min(bg) == 1))
            js_n += 1
            js_ok += (mn_all == mn_j)
    out = {"collapse_identity": [id_ok, id_n],
           "convexity": [cx_ok, cx_n],
           "n_nonconvex_configs": len(cx_fail),
           "nonconvex_sample": cx_fail[:25],
           "jensen": [js_ok, js_n],
           "n_configs": len(rows)}
    print(f"[N-profile] collapse identity {id_ok}/{id_n}; "
          f"convexity {cx_ok}/{cx_n} "
          f"({len(cx_fail)} configs with failures); "
          f"Jensen min {js_ok}/{js_n} ({time.time()-t0:.0f}s)",
          flush=True)
    for r in cx_fail[:8]:
        print("   NONCONVEX:", r, flush=True)
    (REPO / "logs" / "993_N_convexity.json").write_text(
        json.dumps(out, indent=2))
    print("wrote logs/993_N_convexity.json", flush=True)


if __name__ == "__main__":
    main()
