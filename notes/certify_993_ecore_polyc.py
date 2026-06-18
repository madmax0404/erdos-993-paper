"""Exact certification of the E-core inequality as polynomials in c.

For uniform arm count c, fixed k, h, and vertex-background W-pattern
E^{h-2-w} H2^w (H2 = E + 2b), the three brackets

    N1 = [b^2 W]_k,   N2 = [E^2 W]_k,   Dq = [b E W]_k

are polynomials in c (degree <= k): every factor coefficient is a
polynomial in c (binomials C(c,m), C(2c,m) etc. at fixed m), and the
bracket is a finite convolution.  The E-core

    (h-1) N1(c) N2(c)  <=  h  Dq(c)^2      for all integer c >= 1

is therefore decidable per vertex-background instance (k, h, w) by
exact real-root isolation on
R(c) = h Dq^2 - (h-1) N1 N2: we verify R(1) >= 0 and that R has no
real root in (1, oo) (or only roots where R stays >= 0, checked by
sign evaluation between isolated roots).  A certified instance is the
E-core proved for ALL c at that vertex-background instance (k, h, w).

Output: the certified region and any failures, to
logs/993_ecore_polyc_certification.json.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[1]

c = sp.symbols('c', positive=True)


def binom_poly(top_mult, m):
    """C(top_mult * c, m) as a polynomial in c."""
    out = sp.Integer(1)
    for i in range(m):
        out *= (top_mult * c - i)
    return sp.expand(out / sp.factorial(m))


def factor_coeffs(kind, kmax):
    """Coefficient list (index 0..kmax) of one factor, as polys in c.

    kind: 'E'  -> (1+2x)^c        : C(c,m) 2^m
          'H2' -> E + 2b          : C(c,m) 2^m + 2 C(c,m-1)
          'b'  -> x(1+x)^c        : C(c,m-1)
    """
    out = []
    for m in range(kmax + 1):
        if kind == 'E':
            out.append(binom_poly(1, m) * 2**m)
        elif kind == 'H2':
            v = binom_poly(1, m) * 2**m
            if m >= 1:
                v += 2 * binom_poly(1, m - 1)
            out.append(sp.expand(v))
        elif kind == 'b':
            out.append(binom_poly(1, m - 1) if m >= 1 else sp.Integer(0))
        else:
            raise ValueError(kind)
    return out


def conv(a, b_, kmax):
    out = [sp.Integer(0)] * (kmax + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b_):
            if i + j > kmax:
                break
            if bj == 0:
                continue
            out[i + j] += ai * bj
    return [sp.expand(x) for x in out]


def brackets(k, h, w):
    """N1, N2, Dq as polynomials in c at position k, W = E^{h-2-w} H2^w."""
    kmax = k
    E = factor_coeffs('E', kmax)
    H2 = factor_coeffs('H2', kmax)
    b = factor_coeffs('b', kmax)
    W = [sp.Integer(1)] + [sp.Integer(0)] * kmax
    for _ in range(h - 2 - w):
        W = conv(W, E, kmax)
    for _ in range(w):
        W = conv(W, H2, kmax)
    bb = conv(b, b, kmax)
    EE = conv(E, E, kmax)
    bE = conv(b, E, kmax)
    N1 = conv(bb, W, kmax)[k]
    N2 = conv(EE, W, kmax)[k]
    Dq = conv(bE, W, kmax)[k]
    return N1, N2, Dq


def certify_instance(k, h, w):
    """Certify R(c) = h Dq^2 - (h-1) N1 N2 >= 0 for ALL INTEGER c >= 1.

    Rigorous integer-c check: (i) leading coefficient > 0 (R > 0 for c
    beyond any root); (ii) Cauchy root bound C* = 1 + max|a_i|/|a_lead|;
    (iii) exact evaluation R(ci) >= 0 for every integer 1 <= ci <= C*.
    (Arm counts are integers; non-integer c is irrelevant.)"""
    N1, N2, Dq = brackets(k, h, w)
    R = sp.expand(h * Dq**2 - (h - 1) * N1 * N2)
    if R == 0:
        return True
    P = sp.Poly(R, c)
    coeffs = P.all_coeffs()
    if coeffs[0] <= 0:
        return False
    # locate roots approximately to size the check range
    import numpy as np
    arr = np.array([float(a) / float(abs(coeffs[0])) for a in coeffs])
    finite = np.isfinite(arr).all()
    B = 4
    if finite:
        try:
            roots = np.roots(arr)
            rr = [r.real for r in roots if abs(r.imag) < 1e-6 * max(1.0, abs(r))]
            if rr:
                B = max(B, int(1.5 * max(rr)) + 2)
        except Exception:
            pass
    # rigorous positivity beyond B via Taylor shift: P(c+B) has all
    # nonnegative coefficients => P > 0 for c > B; else double B (cap 2^12)
    while B <= 4096:
        shifted = sp.Poly(sp.expand(R.subs(c, c + B)), c)
        if all(a >= 0 for a in shifted.all_coeffs()):
            break
        B *= 2
    else:
        return False
    return all(P.eval(ci) >= 0 for ci in range(1, B + 1))


def instance_grid(h_min, h_max, k_min, k_max):
    for h in range(h_min, h_max + 1):
        upper = k_max if k_max is not None else min(28, 6 * h)
        for k in range(k_min, upper + 1):
            for w in range(0, h - 1):
                yield k, h, w


def topup_grid():
    for k in range(19, 29):
        for w in range(0, 2):
            yield k, 3, w
    for k in range(25, 29):
        for w in range(0, 3):
            yield k, 4, w


def main():
    import argparse
    import time

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--h-min", type=int, default=3)
    parser.add_argument("--h-max", type=int, default=7)
    parser.add_argument("--k-min", type=int, default=2)
    parser.add_argument(
        "--k-max",
        type=int,
        default=None,
        help="fixed k maximum; default is min(28, 6*h) for each h",
    )
    parser.add_argument("--out", type=str, default="993_ecore_polyc_certification.json")
    parser.add_argument(
        "--topup",
        action="store_true",
        help="regenerate the top-up range h=3,k=19..28 and h=4,k=25..28",
    )
    args = parser.parse_args()

    results = {"certified": [], "failed": []}
    t0 = time.time()

    if args.topup:
        args.out = "993_ecore_polyc_topup.json" if args.out == "993_ecore_polyc_certification.json" else args.out
        instances = list(topup_grid())
    else:
        instances = list(instance_grid(args.h_min, args.h_max, args.k_min, args.k_max))

    done_by_h = {}
    for k, h, w in instances:
        ok = certify_instance(k, h, w)
        (results["certified"] if ok else results["failed"]).append([k, h, w])
        done_by_h[h] = done_by_h.get(h, 0) + 1
        if done_by_h[h] == sum(1 for _, hh, _ in instances if hh == h):
            print(f"h={h} done ({time.time()-t0:.0f}s): "
                  f"certified {sum(1 for r in results['certified'] if r[1]==h)}, "
                  f"failed {sum(1 for r in results['failed'] if r[1]==h)}", flush=True)

    out = REPO / "logs" / args.out
    out.write_text(json.dumps(results, indent=2))
    print(f"TOTAL certified: {len(results['certified'])}, failed: {len(results['failed'])}")
    if results["failed"]:
        print("failed instances (k,h,w):", results["failed"][:20])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
