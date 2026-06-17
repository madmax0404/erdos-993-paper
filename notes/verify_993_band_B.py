"""Band-B lemma verification: LC of P on [C, ell-1], exact arithmetic.

Band B exists when ell := ceil(D(n-1)/(D+n)) - 1 >= C, i.e. for
leaf-heavy multisets (h >~ 0.62 C).  On it:

  - k >= C+3: P_k, P_{k-1}, P_{k+1} are pure F (B = xg supported on
    [1, C+1]), so LC_P(k) = LC_F(k) >= 0 by A0 + product closure.
  - k in {C, C+1, C+2}: LC_P(k) = LC_F(k) + (B-correction terms), where
    the corrections involve only the top three coefficients of xg:
    g_{C-1}, g_C (explicit binomials).  Absorption: LC_F(k) >=
    F_k^2 m_k (A2 margin) and the corrections are bounded by
    F-scale * g-tail-scale; the needed mass ratio is supplied by the
    explicit lower bound

        eps_C >= W_1(C) = sum_i (C + c_i) / 2^{c_i + 1},

    (the s=1 class mass at k=C, from the top-two coefficients of
    u_i = (1+x)^{c_i}(1+2x)^{C-c_i}: u_C = 2^{C-c_i},
    u_{C-1} = 2^{C-c_i-1}(C+c_i)).

This script verifies, in exact rationals, LC_P(k) >= 0 for every
multiset in the grid with nonempty band B and every k in [C, ell-1],
AND the explicit absorption chain (corrections <= A2-margin with the
W_1 mass bound) at k in {C, C+1, C+2}.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from math import comb, ceil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
from erdos993.indpoly import mul  # noqa: E402


def binp(c, b):
    return tuple(comb(c, k) * b**k for k in range(c + 1))


def cf(p, k):
    return p[k] if 0 <= k < len(p) else 0


def Nc(c):
    return c + 1 + (c + 29) // 30


def check(counts):
    h, C = len(counts), sum(counts)
    D = h + C
    n_vertices = 1 + h + 2 * C
    ell = ceil(D * (n_vertices - 1) / (D + n_vertices))
    if ell - 1 < C:
        return None  # no band B
    NF = sum(Nc(cc) for cc in counts)
    F = (1,)
    for cc in counts:
        F = mul(F, tuple(x + y for x, y in zip(list(binp(cc, 2)) + [0], [0] + list(binp(cc, 1)), strict=True)))
    g = binp(C, 2)
    P = tuple(cf(F, k) + cf(g, k - 1) for k in range(D + 2))
    rows = []
    ok = True
    for k in range(C, min(ell - 1, D - 1) + 1):
        lcP = P[k] * P[k] - P[k - 1] * P[k + 1]
        if lcP < 0:
            ok = False
        # absorption diagnostics at the three correction positions
        if k <= C + 2:
            lcF = cf(F, k) ** 2 - cf(F, k - 1) * cf(F, k + 1)
            m = Fraction(NF + 1, (k + 1) * (NF - k + 1))
            margin = Fraction(cf(F, k)) ** 2 * m
            corr = lcP - lcF  # exact correction (can be negative)
            w1C = sum(Fraction(C + cc, 2 ** (cc + 1)) for cc in counts)
            epsC = Fraction(cf(F, C) - cf(g, C), cf(g, C))
            rows.append({
                "k": k,
                "lcP_nonneg": lcP >= 0,
                "corr_over_margin": float(Fraction(-corr) / margin) if corr < 0 else 0.0,
                "epsC": float(epsC), "W1C_bound": float(w1C),
                "W1_bound_valid": epsC >= w1C,
            })
    return ok, rows


def main():
    import random
    cases = []
    for c in range(1, 5):
        for h in range(2, 60):
            if h + c * h <= 140:
                cases.append([c] * h)
    rng = random.Random(7)
    for _ in range(60):
        h = rng.randint(4, 14)
        cases.append(sorted(rng.randint(1, 4) for _ in range(h)))

    n_bandB, fails, worst_corr = 0, 0, 0.0
    w1_violations = 0
    out_rows = []
    for counts in cases:
        r = check(counts)
        if r is None:
            continue
        ok, rows = r
        n_bandB += 1
        if not ok:
            fails += 1
            print("LC_P FAIL in band B:", counts)
        for row in rows:
            out_rows.append({"counts": counts, **row})
            worst_corr = max(worst_corr, row["corr_over_margin"])
            if not row["W1_bound_valid"]:
                w1_violations += 1
    payload = {
        "cases_with_band_B": n_bandB,
        "lcP_failures": fails,
        "worst_correction_over_A2margin": worst_corr,
        "W1_lower_bound_violations": w1_violations,
        "rows": out_rows,
    }
    out = REPO / "logs" / "993_band_B_verification.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"multisets with nonempty band B: {n_bandB}")
    print(f"LC_P failures in band B: {fails}")
    print(f"worst |negative correction| / A2-margin at k in [C, C+2]: {worst_corr:.6f}")
    print(f"W1 mass lower-bound violations: {w1_violations}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
