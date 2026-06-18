"""Export one E-core Taylor-shift positivity certificate as data.

This is the bridge from the existing SymPy certification scripts to the Lean
checker in `formal/Erdos993Formal/PolynomialCertificate.lean`.  It does not
itself prove the certificate in Lean; it emits the exact data that generated
Lean files will instantiate:

* ascending coefficients of the target integer polynomial `R(c)`;
* the finite check bound `B`;
* exact samples `R(1), ..., R(B)`;
* ascending coefficients of the shifted tail polynomial `R(c+B)`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "notes"))

import certify_993_ecore_polyc as ecore  # noqa: E402


def coeffs_ascending(expr: sp.Expr) -> list[int]:
    poly = sp.Poly(sp.expand(expr), ecore.c)
    return [int(x) for x in reversed(poly.all_coeffs())]


def positivity_bound(expr: sp.Expr) -> int:
    expr = sp.expand(expr)
    if expr == 0:
        return 1
    poly = sp.Poly(expr, ecore.c)
    coeffs = poly.all_coeffs()
    if coeffs[0] <= 0:
        raise ValueError("leading coefficient is not positive")

    import numpy as np

    bound = 4
    try:
        arr = np.array([float(x) / float(abs(coeffs[0])) for x in coeffs])
        if np.isfinite(arr).all():
            roots = np.roots(arr)
            real_roots = [
                r.real for r in roots
                if abs(r.imag) < 1e-6 * max(1.0, abs(r))
            ]
            if real_roots:
                bound = max(bound, int(1.5 * max(real_roots)) + 2)
    except Exception:
        pass

    while bound <= 4096:
        shifted = sp.Poly(sp.expand(expr.subs(ecore.c, ecore.c + bound)), ecore.c)
        if all(x >= 0 for x in shifted.all_coeffs()):
            return bound
        bound *= 2
    raise ValueError("no Taylor-shift nonnegative tail found up to 4096")


def build_payload(k: int, h: int, w: int) -> dict:
    n1, n2, dq = ecore.brackets(k, h, w)
    expr = sp.expand(h * dq**2 - (h - 1) * n1 * n2)
    bound = positivity_bound(expr)
    poly = sp.Poly(expr, ecore.c)
    shifted = sp.expand(expr.subs(ecore.c, ecore.c + bound))
    return {
        "family": "ecore",
        "instance": {"k": k, "h": h, "w": w},
        "variable": "c",
        "bound": bound,
        "polynomial_coefficients_ascending": coeffs_ascending(expr),
        "samples": [int(poly.eval(i)) for i in range(1, bound + 1)],
        "shifted_coefficients_ascending": coeffs_ascending(shifted),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--h", type=int, required=True)
    parser.add_argument("--w", type=int, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    payload = build_payload(args.k, args.h, args.w)
    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.write_text(text + "\n")
    else:
        print(text)


if __name__ == "__main__":
    main()
