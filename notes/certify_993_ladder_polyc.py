"""Exact certification of the ladder rungs on two-value multisets.

After the Ladder-Schur reduction (conjectured; 15/15 in probes), the
mixed case of the ladder rests on the two-adjacent-value families
(a^p, (a+1)^q), p + q = h.  At fixed (k, h, p, s) every class mass

    W_s(a) = sum_{i+j=s} C(p,i) C(q,j) [x^{k-s}]
             (1+x)^{ia+j(a+1)} (1+2x)^{(p-i)a+(q-j)(a+1)}

is a polynomial in a (degree <= k-s), so the rung

    R(a) = s W_s(a)^2 - (s+1) W_{s-1}(a) W_{s+1}(a)  >=  0
           for all integers a >= 1

is decidable exactly by the Taylor-shift method of
certify_993_ecore_polyc.py: positive leading coefficient, a
numerically located root bound B, rigorous positivity beyond B via
nonnegativity of all coefficients of R(a+B), and exact evaluation at
every integer in [1, B].  p = h is the uniform family a^h, so this
also certifies the uniform higher rungs (s >= 2).

Proof-of-concept range: h in [3,6], p in [1,h], k in [2,16],
s in [1, min(h,k)-1].  Plus one Schur consistency datapoint:
the rung-1 ratio at (1^4, 2^254) (the balanced partition matching
the scanned (128,128,1^256) worst case) computed exactly.

Output: logs/993_ladder_polyc_certification.json
"""

from __future__ import annotations

import json
import time
from fractions import Fraction
from math import comb
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[1]

a = sp.symbols('a', positive=True)


def binom_lin(expr, u):
    """C(expr, u) as a polynomial in a (expr linear in a, u an int)."""
    out = sp.Integer(1)
    for r in range(u):
        out *= (expr - r)
    return sp.expand(out / sp.factorial(u))


def f_poly(alpha, beta, m):
    """[x^m](1+x)^alpha (1+2x)^beta as a polynomial in a."""
    if m < 0:
        return sp.Integer(0)
    tot = sp.Integer(0)
    for u in range(m + 1):
        tot += binom_lin(alpha, u) * binom_lin(beta, m - u) * 2 ** (m - u)
    return sp.expand(tot)


def W_poly(p, q, s, k):
    """Class mass W_s for (a^p, (a+1)^q) at position k, in a."""
    tot = sp.Integer(0)
    for i in range(min(p, s) + 1):
        j = s - i
        if j < 0 or j > q:
            continue
        alpha = i * a + j * (a + 1)
        beta = (p - i) * a + (q - j) * (a + 1)
        tot += sp.binomial(p, i) * sp.binomial(q, j) * f_poly(alpha, beta,
                                                              k - s)
    return sp.expand(tot)


def certify_poly(R):
    """R(a) >= 0 for all integer a >= 1, rigorously."""
    R = sp.expand(R)
    if R == 0:
        return True
    P = sp.Poly(R, a)
    coeffs = P.all_coeffs()
    if coeffs[0] <= 0:
        return False
    import numpy as np
    B = 4
    try:
        arr = np.array([float(x) / float(abs(coeffs[0])) for x in coeffs])
        if np.isfinite(arr).all():
            roots = np.roots(arr)
            rr = [r.real for r in roots
                  if abs(r.imag) < 1e-6 * max(1.0, abs(r))]
            if rr:
                B = max(B, int(1.5 * max(rr)) + 2)
    except Exception:
        pass
    while B <= 4096:
        shifted = sp.Poly(sp.expand(R.subs(a, a + B)), a)
        if all(x >= 0 for x in shifted.all_coeffs()):
            break
        B *= 2
    else:
        return False
    return all(P.eval(ai) >= 0 for ai in range(1, B + 1))


def f_int(alpha, beta, m):
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def W_int(av, p, q, s, k):
    tot = 0
    for i in range(min(p, s) + 1):
        j = s - i
        if j < 0 or j > q:
            continue
        tot += (comb(p, i) * comb(q, j) *
                f_int(i * av + j * (av + 1),
                      (p - i) * av + (q - j) * (av + 1), k - s))
    return tot


def main():
    import sys
    hmin, hmax, kmax = 3, 6, 16
    outname = "993_ladder_polyc_certification.json"
    if len(sys.argv) >= 4:
        hmin, hmax, kmax = map(int, sys.argv[1:4])
        outname = sys.argv[4] if len(sys.argv) >= 5 else \
            f"993_ladder_polyc_h{hmin}-{hmax}_k{kmax}.json"
    t0 = time.time()
    results = {"range": [hmin, hmax, kmax], "certified": [], "failed": []}
    for h in range(hmin, hmax + 1):
        for p in range(1, h + 1):
            q = h - p
            for k in range(2, kmax + 1):
                smax = min(h, k) - 1
                Ws = {s: W_poly(p, q, s, k) for s in range(min(h, k) + 1)}
                for s in range(1, smax + 1):
                    R = s * Ws[s] ** 2 - (s + 1) * Ws[s - 1] * Ws[s + 1]
                    ok = certify_poly(R)
                    (results["certified"] if ok
                     else results["failed"]).append([h, p, k, s])
            print(f"h={h} p={p} done ({time.time()-t0:.0f}s): "
                  f"cert {len(results['certified'])}, "
                  f"fail {len(results['failed'])}", flush=True)

    # Schur consistency datapoint: (1^4, 2^254), k = 40, rung 1
    p_, q_, k_ = 4, 254, 40
    W0 = W_int(1, p_, q_, 0, k_)
    W1 = W_int(1, p_, q_, 1, k_)
    W2 = W_int(1, p_, q_, 2, k_)
    ratio = float(Fraction(2 * W0 * W2, W1 * W1))
    results["schur_datapoint"] = {
        "family": "(1^4,2^254)", "k": k_, "rung1_ratio": ratio,
        "compare_cc1A_worst": 0.9710875510972633,
        "balanced_is_worse": ratio >= 0.9710875510972633}
    print(f"(1^4,2^254) k=40 rung-1 ratio: {ratio:.6f} "
          f"(vs (128,128,1^256): 0.971088)", flush=True)

    out = REPO / "logs" / outname
    out.write_text(json.dumps(results, indent=2))
    print(f"TOTAL certified {len(results['certified'])}, "
          f"failed {len(results['failed'])}; wrote {out}", flush=True)
    if results["failed"]:
        print("failed:", results["failed"][:20])


if __name__ == "__main__":
    main()
