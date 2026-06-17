"""The beyond-grid tail chain for CORE(gap 2): verification.

The sufficiency chain (all steps elementary, derived in
notes/993_factorial_ladder.md):

  (*) <=  [drop (1+R40)(1+R41)/((2+R41)(2+R42)) <= 1 and
           (3+R40+R41) >= 2+R41]
  suffices:  p (R3-R40)^+ + (q-2)(R3-R42)^+  <=  1 + R3,
  then with the coupled numerators ((k-3)mu4 - (k-4)mu3 <= k-5) and
  the worst-corner bound 1 + R3 >= (2C3 - v - k + 5)/(k-3):

  (CHAIN)  p X^+ + (q-2)(X + 2(k-3))^+
              <= (k-4) (v(2h-1) - k + 4q - 1),
           X := v(k-2-2h) + k + 1 - 4q,  C3 = pv + q(v+2) - 3.

This script:
1. verifies CHAIN => the exact coupled-box corner inequality
   (i.e. chain-validity implies the corner check passes) on the
   full grid -- consistency of the derivation;
2. maps where CHAIN itself holds: expected to cover all in-band
   (v,p,q,k) outside a small explicit region (small v,k) that the
   exact corner certificate already covers;
3. confirms the union (CHAIN region) + (exact-corner grid) covers
   every in-band gap-2 multi-giant configuration in a wide sweep --
   the two-piece proof of CORE(gap 2).

Output: logs/993_tail_chain.json
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


def chain_holds(v, p, q, k):
    h = p + q
    X = v * (k - 2 - 2 * h) + k + 1 - 4 * q
    lhs = p * max(0, X) + (q - 2) * max(0, X + 2 * (k - 3))
    rhs = (k - 4) * (v * (2 * h - 1) - k + 4 * q - 1)
    return lhs <= rhs


def corner_exact(v, p, q, k):
    """The exact coupled-box corner check (as in the certified
    sweep)."""
    C = p * v + q * (v + 2)
    C3 = C - 3

    def R(t, j, mu):
        return Fraction(2 * C3 - t - mu, j)

    def star(R3, R40, R41, R42):
        lhs = p * max(Fraction(0), R3 - R40) * (2 + R41) \
            + (q - 2) * (1 + R40) * (1 + R41) \
            * max(Fraction(0), R3 - R42) / (2 + R42)
        return lhs <= (3 + R40 + R41) * (1 + R3)

    for m3 in (k - 4, 2 * (k - 4)):
        hi4, lo4 = min(2 * (k - 5), m3 - 1), k - 5
        if hi4 < lo4:
            continue
        for m40 in (lo4, hi4):
            for m41 in (lo4, hi4):
                for m42 in (lo4, hi4):
                    if not star(R(v, k - 3, m3),
                                R(2 * v, k - 4, m40),
                                R(2 * v + 1, k - 4, m41),
                                R(2 * v + 2, k - 4, m42)):
                        return False
    return True


def main():
    out = {}
    # 1+2+3 combined sweep
    n_all, chain_ok, corner_ok, neither = 0, 0, 0, []
    chain_implies_corner_bad = []
    for h in (3, 4, 5, 6, 8, 12, 16, 24, 40, 64):
        for v in (1, 2, 3, 4, 6, 10, 16, 24, 40):
            for q in range(2, min(h - 1, 8) + 1):
                p = h - q
                C = p * v + q * (v + 2)
                kA = band_kA(C, h)
                ks = sorted({6, 8, 10, kA // 3, kA // 2, 2 * kA // 3,
                             5 * kA // 6, min(kA, 120)})
                for k in (kk for kk in ks if 6 <= kk <= min(kA, 120)):
                    n_all += 1
                    ch = chain_holds(v, p, q, k)
                    co = corner_exact(v, p, q, k)
                    chain_ok += ch
                    corner_ok += co
                    if ch and not co:
                        chain_implies_corner_bad.append([h, p, q, v, k])
                    if not (ch or co):
                        neither.append([h, p, q, v, k])
    out["sweep"] = {
        "cases": n_all, "chain_holds": chain_ok,
        "corner_holds": corner_ok,
        "chain_but_not_corner": chain_implies_corner_bad[:15],
        "n_chain_but_not_corner": len(chain_implies_corner_bad),
        "covered_by_neither": neither[:25],
        "n_uncovered": len(neither)}
    print(f"[tail] {n_all} in-band gap-2 cases; CHAIN holds {chain_ok}; "
          f"exact-corner holds {corner_ok}; chain-but-not-corner "
          f"{len(chain_implies_corner_bad)}; UNCOVERED by both: "
          f"{len(neither)}", flush=True)
    for row in neither[:10]:
        print("   UNCOVERED:", row, flush=True)
    path = REPO / "logs" / "993_tail_chain.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
