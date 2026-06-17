"""Mechanism map for the four-condition inconsistency (Lemma A' core).

At a tight not-two-cluster config with positions x < y < z, the four
non-improvement conditions confine rho-hat = W2/W1^2 to
[S, min(B_b, B_o, B_om)] (one spread lower-bound from T_s, three
balance upper-bounds).  The verified dichotomy says rho-hat never
lies there.  The proof's case split, by mechanism:

  (M1) interval empty via the x-balances:  S > min(B_b, B_o);
  (M2) pair-drag below:                    rho-hat < S;
  (M3) pair-drag above the om-bound:       rho-hat > B_om
       (with S <= min(B_b, B_o), i.e. M1 fails).

This probe computes the exact linearized bounds at every tight
not-two-cluster config in the extreme grid, classifies the
mechanism, and maps the case-split boundary in terms of the
structural parameters (bulk size p_x, gaps y-x and z-y, k-position)
-- the input the analytic proof needs to choose its estimates.

Output: logs/993_mechanism_map.json
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
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def main():
    rows, unclassified = 0, []
    mech = Counter()
    boundary = []
    for h in (8, 16, 24, 40):
        shapes = []
        for a in (2, 4, 8, 16):
            shapes += [
                {a: h - 2, a + 1: 1, a + 2: 1},
                {a: 1, a + 1: h - 2, a + 2: 1},
                {a: h - 2, a + 2: 1, a + 4: 1},
                {a: h - 2, a + 4: 1, a + 8: 1},
                {a: h - 2, 3 * a: 1, 6 * a: 1},
                {a: h - 2, 2 * a: 1, 4 * a: 1},
                {a: h - 3, 2 * a: 2, 4 * a: 1},
                {a: h - 3, a + 2: 1, a + 4: 1, a + 6: 1},
                {a: h - 2, 2 * a: 1, 2 * a + 1: 1},
            ]
        for counts0 in shapes:
            counts = Counter({v: m for v, m in counts0.items()
                              if m > 0})
            if len(counts) < 3:
                continue
            h_ = sum(counts.values())
            C = sum(v * m for v, m in counts.items())
            if C > 700:
                continue
            kA = band_kA(C, h_)
            ks = sorted({kA // 2, 2 * kA // 3, 3 * kA // 4,
                         5 * kA // 6, min(kA, 350)})
            for k in (kk for kk in ks if 8 <= kk <= min(kA, 350)):
                x = [f(c, C - c, k - 1) for c in range(C + 1)]
                yy = [f(m, C - m, k - 2) for m in range(C + 1)]
                A = [f(t, C - t - 1, k - 2) for t in range(C)]
                dy = [f(m, C - m - 1, k - 3) for m in range(C)]
                vals = sorted(counts)
                W1 = sum(counts[v] * x[v] for v in vals)
                if W1 == 0:
                    continue
                W2 = 0
                for i, v in enumerate(vals):
                    if counts[v] >= 2:
                        W2 += comb(counts[v], 2) * yy[2 * v]
                    for w in vals[i + 1:]:
                        W2 += counts[v] * counts[w] * yy[v + w]
                g = comb(C, k) << k
                ratio = float(Fraction(2 * g * W2, W1 * W1))
                if ratio < 0.7:
                    continue
                rows += 1
                rho_hat = Fraction(W2, W1 * W1)
                xb, ym, zt = vals[0], vals[len(vals) // 2], vals[-1]

                def bound(u, w):
                    d1 = A[u - 1] - A[w]
                    Sy_u1 = sum(m * dy[v + u - 1]
                                for v, m in counts.items())
                    Sy_w = sum(m * dy[v + w]
                               for v, m in counts.items())
                    d2 = (Sy_u1 - Sy_w) - dy[2 * u - 1] \
                        - dy[u + w - 1] + dy[u + w] + dy[2 * w]
                    den = 2 * W1 * d1 + d1 * d1
                    if den == 0:
                        return None, 0
                    return Fraction(d2, den), den

                S, dS = bound(ym, zt)
                Bb, dB = bound(ym, xb)
                Bo, dO = bound(zt, xb)
                Bom, dM = bound(zt, ym)
                # types: S lower (den>0), B's upper (den<0)
                if S is None or dS <= 0:
                    unclassified.append(["S-degenerate",
                                         dict(counts), k])
                    continue
                uppers = [b for b, dd in ((Bb, dB), (Bo, dO))
                          if b is not None and dd < 0]
                if not uppers:
                    unclassified.append(["no-x-upper",
                                         dict(counts), k])
                    continue
                minB = min(uppers)
                m1 = S > minB
                m2 = rho_hat < S
                m3 = (Bom is not None and dM < 0
                      and rho_hat > Bom)
                tag = ("M1" if m1 else
                       "M2" if m2 else
                       "M3" if m3 else "NONE")
                mech[tag] += 1
                if tag == "NONE":
                    unclassified.append(["NONE", dict(counts), C,
                                         h_, k, ratio])
                else:
                    gap_xy, gap_yz = ym - xb, zt - ym
                    boundary.append([tag, counts[xb], gap_xy,
                                     gap_yz, round(k / kA, 2)])
    bnd = Counter((row[0], row[2] >= 2 * row[3]) for row in boundary)
    out = {"tight_configs": rows, "mechanisms": dict(mech),
           "unclassified": unclassified[:20],
           "n_unclassified": len(unclassified),
           "boundary_sample":
               {str(key): v for key, v in bnd.most_common(12)}}
    print(f"[mechanism] {rows} tight configs; map {dict(mech)}; "
          f"unclassified {len(unclassified)}", flush=True)
    for row in unclassified[:6]:
        print("   UNCLASSIFIED:", row, flush=True)
    path = REPO / "logs" / "993_mechanism_map.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
