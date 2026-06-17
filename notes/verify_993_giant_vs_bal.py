"""Step B of the DOM' variational program: bulk+giant vs balanced.

The local-maxima census (logs/993_locmax_census.json) shows every
tight local maximizer of the rung-1 ratio is adjacent-two-value or
bulk+giant G(a,M) = (a^{h-1}, M).  Step B is the canonical
comparison: G never beats bal(C,h) when bal is tight.  This script
pins the exact statement.

Closed forms at rung 1 (x(c) = f(c,C-c,k-1), y(m) = f(m,C-m,k-2),
g = 2^k C(C,k)):

    G:   W1 = (h-1) x(a) + x(M),
         W2 = C(h-1,2) y(2a) + (h-1) y(a+M)
    bal: a0 = C//h, r = C%h:
         W1 = (h-r) x(a0) + r x(a0+1),
         W2 = C(h-r,2) y(2a0) + (h-r) r y(2a0+1) + C(r,2) y(2a0+2)

Stages (exact arithmetic):
1. extended y-log-concavity check (Lemma y-LC numeric companion):
   C in {50,100,200,400,800}, several k, all m;
2. the sweep: h in {6,8,10,12,16,24,40,60,100}, a in 1..6,
   M >= a+2 sampled to C <= 1200, k sampled in the band with k >= 4
   (k - s >= 3 at rung 1); per instance record
   (ratio_bal, ratio_G, h, a, M, k); report exceedances
   ratio_G > ratio_bal conditioned on ratio_bal >= {0.6,0.65,0.7},
   the unconditional max of ratio_G, and the binding (M - a)
   pattern among any exceedances.

Output: logs/993_giant_vs_bal.json
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


def ratio_G(C, h, a, M, k):
    x_a = f(a, C - a, k - 1)
    x_M = f(M, C - M, k - 1)
    W1 = (h - 1) * x_a + x_M
    W2 = comb(h - 1, 2) * f(2 * a, C - 2 * a, k - 2) \
        + (h - 1) * f(a + M, C - a - M, k - 2)
    if W1 == 0:
        return None
    g = comb(C, k) << k
    return Fraction(2 * g * W2, W1 * W1)


def ratio_bal(C, h, k):
    a0, r = divmod(C, h)
    x0 = f(a0, C - a0, k - 1)
    x1 = f(a0 + 1, C - a0 - 1, k - 1)
    W1 = (h - r) * x0 + r * x1
    W2 = (comb(h - r, 2) * f(2 * a0, C - 2 * a0, k - 2)
          + (h - r) * r * f(2 * a0 + 1, C - 2 * a0 - 1, k - 2)
          + comb(r, 2) * f(2 * a0 + 2, C - 2 * a0 - 2, k - 2))
    if W1 == 0:
        return None
    g = comb(C, k) << k
    return Fraction(2 * g * W2, W1 * W1)


def main():
    out = {}

    # 1. extended y-LC check
    bad, n = [], 0
    for C in (50, 100, 200, 400, 800):
        for k in (4, 8, max(4, C // 8), max(4, C // 4), max(4, C // 3)):
            j = k - 2
            y = [f(m, C - m, j) for m in range(C + 1)]
            for m in range(1, C):
                if y[m - 1] and y[m + 1]:
                    n += 1
                    if y[m] * y[m] < y[m - 1] * y[m + 1]:
                        bad.append([C, k, m])
    out["y_lc_extended"] = {"checked": n, "n_fails": len(bad),
                            "fails": bad[:20]}
    print(f"[y-LC] {n} checks, {len(bad)} fails", flush=True)

    # 2. the sweep
    rows = []
    CAP = 1200
    for h in (6, 8, 10, 12, 16, 24, 40, 60, 100):
        for a in range(1, 7):
            base = (h - 1) * a
            Ms, d = [], 2
            while base + a + d <= CAP:
                Ms.append(a + d)
                d = d + 1 if d < 6 else (d * 3) // 2
            for M in Ms:
                C = base + M
                kA = band_kA(C, h)
                ks = sorted({4, 6, kA // 3, kA // 2, 2 * kA // 3,
                             min(kA, 100)})
                for k in (kk for kk in ks if 4 <= kk <= min(kA, 100)):
                    rb = ratio_bal(C, h, k)
                    rg = ratio_G(C, h, a, M, k)
                    if rb is None or rg is None:
                        continue
                    rows.append([float(rb), float(rg), h, a, M, k])
    out["sweep_rows"] = len(rows)
    rep = {}
    for th in (0.6, 0.65, 0.7):
        sel = [r for r in rows if r[0] >= th]
        exc = [r for r in sel if r[1] > r[0]]
        rep[str(th)] = {
            "cases": len(sel), "exceedances": len(exc),
            "max_excess": max((r[1] - r[0] for r in exc), default=0.0),
            "examples": exc[:10]}
    beats = [r for r in rows if r[1] > r[0]]
    out["thresholds"] = rep
    out["unconditional"] = {
        "max_ratio_G": max((r[1] for r in rows), default=None),
        "argmax_G": max(rows, key=lambda r: r[1]) if rows else None,
        "n_beats": len(beats),
        "max_balratio_when_beaten":
            max((r[0] for r in beats), default=None),
        "max_G_when_beating":
            max((r[1] for r in beats), default=None),
        "beat_gap_pattern_Mminusa":
            sorted({r[4] - r[3] for r in beats})[:20]}
    print(f"[sweep] {len(rows)} instances; per-threshold exceedances: "
          f"{[(t, rep[t]['exceedances']) for t in rep]}; "
          f"max ratio_G overall {out['unconditional']['max_ratio_G']:.4f}; "
          f"beats: {len(beats)} (max bal-ratio when beaten "
          f"{out['unconditional']['max_balratio_when_beaten']}, "
          f"max G when beating "
          f"{out['unconditional']['max_G_when_beating']})", flush=True)

    path = REPO / "logs" / "993_giant_vs_bal.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
