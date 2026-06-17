"""Symbolic certificate for the starred Newton coefficients.

This complements ``verify_starred_newton.py``.  It proves the exact Newton
coefficient formulas are nonnegative by rewriting the exponentials as

    2^(N+3) = 8 * (sum_{j=0}^3 binom(N, j) + nonnegative_tail).

After this substitution, all relevant coefficient formulas have nonnegative
coefficients in a binomial basis.

Run from the repo root with:

    uv run python notes/certify_starred_newton.py
"""

from __future__ import annotations

import sympy as sp


a, b, r, t = sp.symbols("a b r t")


def add_terms(*polys: dict[int, sp.Expr]) -> dict[int, sp.Expr]:
    result: dict[int, sp.Expr] = {}
    for poly in polys:
        for exponent, coeff in poly.items():
            result[exponent] = result.get(exponent, 0) + coeff
    return {
        exponent: sp.expand(coeff)
        for exponent, coeff in result.items()
        if sp.expand(coeff) != 0
    }


def scale_terms(poly: dict[int, sp.Expr], factor: sp.Expr) -> dict[int, sp.Expr]:
    return {
        exponent: sp.expand(factor * coeff)
        for exponent, coeff in poly.items()
        if factor * coeff != 0
    }


def derivative_terms(
    poly: dict[int, sp.Expr],
    total_degree: sp.Expr,
    order: int,
) -> dict[int, sp.Expr]:
    out = poly
    for _ in range(order):
        derived: dict[int, sp.Expr] = {}
        for exponent, coeff in out.items():
            derived[exponent - 1] = derived.get(exponent - 1, 0) + coeff * (
                total_degree + exponent
            )
        out = {
            exponent: sp.expand(coeff)
            for exponent, coeff in derived.items()
            if sp.expand(coeff) != 0
        }
    return out


def base_terms(
    aa: sp.Expr,
    bb: sp.Expr,
    rr: sp.Expr,
    tt: sp.Expr,
) -> dict[int, sp.Expr]:
    """Terms relative to x^(aa+bb) for H_* Delta^a H_1 Delta^b H_1."""

    h_star = [1, 9, 28, 36, 17, 1]
    left = [rr, 2 * rr + 1, 1]
    right = [tt, 2 * tt + 1, 1]
    coeffs = [0] * (len(h_star) + len(left) + len(right) - 2)
    for i, h_coeff in enumerate(h_star):
        for j, left_coeff in enumerate(left):
            for k, right_coeff in enumerate(right):
                coeffs[i + j + k] += h_coeff * left_coeff * right_coeff
    return {
        exponent: sp.expand(coeff)
        for exponent, coeff in enumerate(coeffs)
        if sp.expand(coeff) != 0
    }


def make_stencil(function):
    def stencil(
        aa: sp.Expr,
        bb: sp.Expr,
        rr: sp.Expr,
        tt: sp.Expr,
    ) -> dict[int, sp.Expr]:
        center = function(aa, bb, rr, tt)
        left = {
            exponent - 1: coeff
            for exponent, coeff in function(aa - 1, bb, rr / 2, tt).items()
        }
        right = {
            exponent - 1: coeff
            for exponent, coeff in function(aa, bb - 1, rr, tt / 2).items()
        }
        return add_terms(
            scale_terms(center, aa + bb + 4),
            scale_terms(left, aa),
            scale_terms(right, bb),
        )

    return stencil


def make_derivative(function, order: int):
    return lambda aa, bb, rr, tt: derivative_terms(
        function(aa, bb, rr, tt),
        aa + bb,
        order,
    )


def make_x_shift(shift: int, function):
    return lambda aa, bb, rr, tt: {
        exponent + shift: coeff
        for exponent, coeff in function(aa, bb, rr, tt).items()
    }


def newton_coefficients() -> dict[int, sp.Expr]:
    """Return C exponent formulas relative to x^(a+b)."""

    p = base_terms
    p1 = make_derivative(p, 1)
    p2 = make_derivative(p, 2)
    p3 = make_derivative(p, 3)
    s_x2_p2 = make_stencil(make_x_shift(2, p2))
    s_p1 = make_stencil(p1)
    s2_p1 = make_stencil(s_p1)
    s_p = make_stencil(p)
    s2_p = make_stencil(s_p)
    s3_p = make_stencil(s2_p)

    return add_terms(
        scale_terms(make_x_shift(2, p3)(a, b, r, t), -1),
        scale_terms(make_x_shift(3, p3)(a, b, r, t), -2),
        scale_terms(s_x2_p2(a, b, r, t), 2),
        scale_terms(make_x_shift(2, p2)(a, b, r, t), -4),
        scale_terms(s2_p1(a, b, r, t), 4),
        scale_terms(s_p1(a, b, r, t), 12),
        scale_terms(p1(a, b, r, t), 8),
        scale_terms(make_x_shift(1, s2_p1)(a, b, r, t), 8),
        scale_terms(make_x_shift(1, s_p1)(a, b, r, t), 28),
        scale_terms(make_x_shift(1, p1)(a, b, r, t), 20),
        scale_terms(s3_p(a, b, r, t), -8),
        scale_terms(s2_p(a, b, r, t), -40),
        scale_terms(s_p(a, b, r, t), -64),
        scale_terms(p(a, b, r, t), -32),
    )


def binomial_polynomial(symbol: sp.Symbol, degree: int) -> sp.Expr:
    out = 1
    for offset in range(degree):
        out *= symbol - offset
    return sp.expand(out / sp.factorial(degree))


def truncated_exp_tail_base(symbol: sp.Symbol) -> sp.Expr:
    return sum(binomial_polynomial(symbol, degree) for degree in range(4))


def assert_nonnegative_binomial_basis(
    expr: sp.Expr,
    base_symbols: tuple[sp.Symbol, ...],
    tail_symbols: tuple[sp.Symbol, ...],
    *,
    max_degree: int,
) -> None:
    """Assert nonnegative coefficients in binomial(base) * monomial(tail)."""

    basis = [
        (
            degrees,
            sp.prod(
                binomial_polynomial(symbol, degree)
                for symbol, degree in zip(base_symbols, degrees, strict=True)
            ),
        )
        for degrees in _degree_grid(len(base_symbols), max_degree)
    ]
    points = list(_degree_grid(len(base_symbols), max_degree))
    matrix = sp.Matrix(
        [
            [
                basis_expr.subs(
                    dict(zip(base_symbols, point, strict=True)),
                )
                for _, basis_expr in basis
            ]
            for point in points
        ]
    )
    inverse = matrix.inv()

    poly = sp.Poly(sp.expand(expr), *tail_symbols)
    for tail_monomial, tail_coeff in poly.terms():
        if tail_coeff == 0:
            continue
        values = sp.Matrix(
            [
                tail_coeff.subs(dict(zip(base_symbols, point, strict=True)))
                for point in points
            ]
        )
        coefficients = inverse * values
        for base_degrees, coefficient in zip(
            (degrees for degrees, _ in basis),
            coefficients,
            strict=True,
        ):
            coefficient = sp.simplify(coefficient)
            if coefficient < 0:
                raise AssertionError((tail_monomial, base_degrees, coefficient, expr))


def _degree_grid(width: int, max_degree: int):
    if width == 1:
        for i in range(max_degree + 1):
            yield (i,)
        return
    if width == 2:
        for i in range(max_degree + 1):
            for j in range(max_degree + 1):
                yield (i, j)
        return
    raise ValueError("only one- and two-dimensional grids are needed here")


def certify_interior(coefficients: dict[int, sp.Expr]) -> None:
    aa, bb, u, v = sp.symbols("A B U V")
    left_tail = truncated_exp_tail_base(aa) + u
    right_tail = truncated_exp_tail_base(bb) + v
    for exponent in range(-2, 10):
        expr = coefficients[exponent].subs(
            {
                a: aa + 3,
                b: bb + 3,
                r: 8 * left_tail,
                t: 8 * right_tail,
            }
        )
        assert_nonnegative_binomial_basis(
            expr,
            (aa, bb),
            (u, v),
            max_degree=7,
        )


def certify_boundary(coefficients: dict[int, sp.Expr]) -> None:
    bb, u = sp.symbols("B U")
    tail = truncated_exp_tail_base(bb) + u

    for fixed_a in (0, 1, 2):
        for exponent in range(-2, 10):
            if fixed_a == 2 and exponent == 2:
                continue
            expr = coefficients[exponent].subs(
                {
                    a: fixed_a,
                    b: bb,
                    r: 2**fixed_a,
                    t: tail,
                }
            )
            assert_nonnegative_binomial_basis(
                expr,
                (bb,),
                (u,),
                max_degree=7,
            )

    # The lone coefficient not covered by the b>=0 boundary certificate above
    # is fixed_a=2 and exponent=2. It is positive at b=0, and has a
    # nonnegative certificate after shifting to b=B+1.
    exceptional_at_zero = coefficients[2].subs({a: 2, b: 0, r: 4, t: 1})
    if exceptional_at_zero < 0:
        raise AssertionError(("exceptional boundary", exceptional_at_zero))
    expr = coefficients[2].subs(
        {
            a: 2,
            b: bb + 1,
            r: 4,
            t: 2 * tail,
        }
    )
    assert_nonnegative_binomial_basis(
        expr,
        (bb,),
        (u,),
        max_degree=7,
    )


if __name__ == "__main__":
    coeffs = newton_coefficients()
    certify_interior(coeffs)
    certify_boundary(coeffs)
    print("interior certificate verified for a,b >= 3")
    print("boundary certificate verified for min(a,b) <= 2")
