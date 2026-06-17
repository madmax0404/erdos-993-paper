"""Exact Newton-basis verifier for the starred first-margin target.

This is scratch/research code for Erdős #993 notes. It verifies coefficientwise
nonnegativity of the Newton coefficients C_{a,b} for

    F_{m,n}=O_{m+n+2}(H_* H_m H_n).

Run from the repo root with:

    uv run python notes/verify_starred_newton.py
"""

from __future__ import annotations

from functools import lru_cache


Poly = tuple[int, ...]


def trim(poly: Poly) -> Poly:
    while len(poly) > 1 and poly[-1] == 0:
        poly = poly[:-1]
    return poly


def add(left: Poly, right: Poly) -> Poly:
    length = max(len(left), len(right))
    return trim(
        tuple(
            (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
            for i in range(length)
        )
    )


def sum_poly(polys: list[Poly]) -> Poly:
    total = (0,)
    for poly in polys:
        total = add(total, poly)
    return total


def scale(poly: Poly, factor: int) -> Poly:
    return trim(tuple(factor * coeff for coeff in poly))


def mul(left: Poly, right: Poly) -> Poly:
    out = [0] * (len(left) + len(right) - 1)
    for i, left_coeff in enumerate(left):
        for j, right_coeff in enumerate(right):
            out[i + j] += left_coeff * right_coeff
    return trim(tuple(out))


def derivative(poly: Poly, order: int = 1) -> Poly:
    for _ in range(order):
        poly = tuple((i + 1) * poly[i + 1] for i in range(len(poly) - 1)) or (0,)
    return poly


def x_power(exponent: int) -> Poly:
    return (0,) * exponent + (1,)


B = (1, 2)
A = (1, 1)
X = (0, 1)
H_STAR = (1, 9, 28, 36, 17, 1)


@lru_cache(maxsize=None)
def base(a: int, b: int) -> Poly:
    """Newton coefficient of H_* H_m H_n before applying O."""

    if a < 0 or b < 0:
        return (0,)
    left = add(scale(B, 2**a), mul(X, A))
    right = add(scale(B, 2**b), mul(X, A))
    return mul(mul(mul(H_STAR, x_power(a + b)), left), right)


def memo(function):
    return lru_cache(maxsize=None)(function)


def stencil_value(sequence, a: int, b: int) -> Poly:
    """Newton-coordinate action of multiplication by s=m+n+2."""

    return sum_poly(
        [
            scale(sequence(a, b), a + b + 4),
            scale(sequence(a - 1, b), a),
            scale(sequence(a, b - 1), b),
        ]
    )


def deriv_sequence(sequence, order: int):
    return memo(lambda a, b: derivative(sequence(a, b), order))


def mul_sequence(poly: Poly, sequence):
    return memo(lambda a, b: mul(poly, sequence(a, b)))


def stencil(sequence):
    return memo(lambda a, b: stencil_value(sequence, a, b))


P = memo(base)
P1 = deriv_sequence(P, 1)
P2 = deriv_sequence(P, 2)
P3 = deriv_sequence(P, 3)
S_X2_P2 = stencil(mul_sequence((0, 0, 1), P2))
S_P1 = stencil(P1)
S2_P1 = stencil(S_P1)
S_P = stencil(P)
S2_P = stencil(S_P)
S3_P = stencil(S2_P)


@lru_cache(maxsize=None)
def c(a: int, b: int) -> Poly:
    """Newton coefficient C_{a,b} for F_{m,n}."""

    return sum_poly(
        [
            mul((0, 0, -1, -2), P3(a, b)),
            scale(S_X2_P2(a, b), 2),
            scale(mul((0, 0, 1), P2(a, b)), -4),
            scale(S2_P1(a, b), 4),
            scale(S_P1(a, b), 12),
            scale(P1(a, b), 8),
            scale(mul((0, 1), S2_P1(a, b)), 8),
            scale(mul((0, 1), S_P1(a, b)), 28),
            scale(mul((0, 1), P1(a, b)), 20),
            scale(S3_P(a, b), -8),
            scale(S2_P(a, b), -40),
            scale(S_P(a, b), -64),
            scale(P(a, b), -32),
        ]
    )


def verify_nonnegative(limit: int) -> None:
    for a in range(limit + 1):
        for b in range(limit + 1):
            coeffs = c(a, b)
            minimum = min(coeffs)
            if minimum < 0:
                index = coeffs.index(minimum)
                raise AssertionError((a, b, index, minimum, coeffs))


def verify_relative_monotonicity(limit: int) -> None:
    for a in range(3, limit):
        for b in range(3, limit):
            for relative_degree in range(2, 14):
                index = a + b - 4 + relative_degree
                current = c(a, b)[index]
                if c(a + 1, b)[index + 1] < current:
                    raise AssertionError(("a", a, b, relative_degree))
                if c(a, b + 1)[index + 1] < current:
                    raise AssertionError(("b", a, b, relative_degree))


if __name__ == "__main__":
    verify_nonnegative(120)
    verify_relative_monotonicity(50)
    print("C_{a,b} >= 0 verified for 0 <= a,b <= 120")
    print("relative Q_{a,b} monotonicity verified for 3 <= a,b <= 50")
