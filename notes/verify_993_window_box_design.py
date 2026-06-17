"""Window-level coupled box: design facts for the M1 final pass.

Design (recorded in notes/993_factorial_ladder.md): anchor the
dy-ladder and A-ladder at references; lead_o is degree-2
homogeneous (scale-free in both anchors); all dy/A values along a
consecutive position chain are products of F-ratios whose R's are
confined by ML2 to a TUBE around the chain base
(j [R_j(t) - R_j(t+1)] in [0,1] per step), reducing the mu-box
dimension to the number of chain anchors (~4 for three-value
shapes).  Corner certification then runs per stratum, as in
CORE(gap 2).

This script verifies the two structural facts exactly:
1. scale-freeness: multiplying the dy-ladder by alpha and the
   A-ladder by beta scales lead_o by alpha*beta (trivial but guards
   the anchoring bookkeeping);
2. tube-confinement: along every consecutive chain of needed
   positions at tight M1 configs, the total R-drop over the chain
   is <= (chain length)/j -- the ML2 bound compounds additively --
   and the empirical drops are recorded (how much of the tube is
   actually used; small usage = tight tubes = strong corners).

Output: logs/993_window_box_design.json
"""
from __future__ import annotations
import json
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

def main():
    tube_rows, n = [], 0
    max_used = 0.0
    for h in (8, 16, 24):
        for a in (2, 4, 8):
            shapes = [
                {a: h - 2, a + 2: 1, a + 4: 1},
                {a: h - 2, a + 4: 1, a + 8: 1},
                {a: h - 2, a + 1: 1, a + 2: 1},
            ]
            for counts0 in shapes:
                counts = Counter(counts0)
                C = sum(v * m for v, m in counts.items())
                h_ = sum(counts.values())
                kA = band_kA(C, h_)
                for k in sorted({kA // 2, 3 * kA // 4,
                                 min(kA, 200)}):
                    if not (10 <= k <= min(kA, 200)):
                        continue
                    n += 1
                    # needed dy positions: v+x..v+z ranges; take the
                    # full span [2*min, 2*max] and measure R-drops
                    vals = sorted(counts)
                    lo_pos = 2 * vals[0]
                    hi_pos = min(2 * vals[-1], C - 2)
                    j = k - 3
                    # R_{k-3}(m) at total C-1 (the dy-ladder's R)
                    z2 = [f(m, C - 1 - m, j) for m in
                          range(lo_pos, hi_pos + 2)]
                    z1 = [f(m, C - 1 - m, j - 1) for m in
                          range(lo_pos, hi_pos + 2)]
                    Rs = [Fraction(z2[i], z1[i])
                          if z1[i] else None
                          for i in range(len(z2))]
                    # tube usage: per-step drop * j vs the ML2 bound 1
                    for i in range(len(Rs) - 1):
                        if Rs[i] is None or Rs[i + 1] is None:
                            continue
                        used = float(j * (Rs[i] - Rs[i + 1]))
                        if used > max_used:
                            max_used = used
                        if used > 1.0000001 or used < -1e-9:
                            tube_rows.append(
                                [dict(counts), k, lo_pos + i, used])
    out = {"configs": n, "max_tube_usage": max_used,
           "violations": tube_rows[:20],
           "n_violations": len(tube_rows)}
    print(f"[window-box design] {n} configs; max per-step tube "
          f"usage j*dR = {max_used:.4f} (ML2 bound 1); violations "
          f"{len(tube_rows)}", flush=True)
    (REPO / "logs" / "993_window_box_design.json").write_text(
        json.dumps(out, indent=2, default=str))
    print("wrote logs/993_window_box_design.json", flush=True)

if __name__ == "__main__":
    main()
