"""Certify rung 1 on the bulk+giant family G(a, a+d) = (a^{h-1}, a+d).

The reshaped DOM' architecture needs per-family rung bounds for the
two candidate-maximizer shapes.  Adjacent two-value is certified
(logs/993_ladder_polyc_h3-10_k28.json); this script certifies the
bulk+giant family: with C = h a + d,

    W1 = (h-1) x(a) + x(a+d),
    W2 = C(h-1,2) y(2a) + (h-1) y(2a+d),
    P(a) = W1^2 - 2 g W2  >=  0   for all integers a >= 1,

where x(c) = [x^{k-1}](1+x)^c(1+2x)^{C-c},
y(m) = [x^{k-2}](1+x)^m(1+2x)^{C-m}, g = 2^k C(C,k).  At fixed
(k, h, d) every quantity is a polynomial in a, so the Taylor-shift
certification of certify_993_ladder_polyc.py applies verbatim.

Grid: h in [3,10], d in [2,8], k in [2,28].  The large-d tail
(observed to cap near ratio 0.78) is left to a limit lemma.

Output: logs/993_giant_certification.json
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[1]
a = sp.symbols('a', positive=True)


def binom_lin(expr, u):
    out = sp.Integer(1)
    for r in range(u):
        out *= (expr - r)
    return sp.expand(out / sp.factorial(u))


def f_poly(alpha, beta, m):
    if m < 0:
        return sp.Integer(0)
    tot = sp.Integer(0)
    for u in range(m + 1):
        tot += binom_lin(alpha, u) * binom_lin(beta, m - u) * 2 ** (m - u)
    return sp.expand(tot)


def certify_poly(R):
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
        arr = np.array([float(z) / float(abs(coeffs[0])) for z in coeffs])
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
        if all(z >= 0 for z in shifted.all_coeffs()):
            break
        B *= 2
    else:
        return False
    return all(P.eval(ai) >= 0 for ai in range(1, B + 1))


def main():
    t0 = time.time()
    results = {"certified": [], "failed": []}
    for h in range(3, 11):
        for d in range(2, 9):
            C = h * a + d
            for k in range(2, 29):
                x_a = f_poly(a, C - a, k - 1)
                x_M = f_poly(a + d, C - (a + d), k - 1)
                y_2a = f_poly(2 * a, C - 2 * a, k - 2)
                y_2ad = f_poly(2 * a + d, C - (2 * a + d), k - 2)
                g = binom_lin(C, k) * 2 ** k
                W1 = (h - 1) * x_a + x_M
                W2 = sp.binomial(h - 1, 2) * y_2a + (h - 1) * y_2ad
                P = sp.expand(W1 * W1 - 2 * g * W2)
                ok = certify_poly(P)
                (results["certified"] if ok
                 else results["failed"]).append([h, d, k])
            print(f"h={h} d={d} done ({time.time()-t0:.0f}s): "
                  f"cert {len(results['certified'])}, "
                  f"fail {len(results['failed'])}", flush=True)
    out = REPO / "logs" / "993_giant_certification.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"TOTAL certified {len(results['certified'])}, "
          f"failed {len(results['failed'])}; wrote {out}", flush=True)
    if results["failed"]:
        print("failed:", results["failed"][:20], flush=True)


if __name__ == "__main__":
    main()
