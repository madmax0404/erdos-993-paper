from __future__ import annotations

import sympy as sp


def main() -> None:
    a, b, g, p, q, s0, u, y0 = sp.symbols("a b g p q s0 u y0")

    # Generic normalized first-product slice.
    # a is the scaled first mass G_1, b is the scaled second mass G_2,
    # p=p_1, q=p_2, and all later terms are frozen.
    s = s0 + a * p
    y = y0 - (a - b) * p + a**2 * p**2 / q
    residual = sp.expand(g**2 * s - y**2 * u)

    certificate = sp.factor(
        sp.diff(residual, p, 2)
        + 2 * u * ((2 * a**2 * p / q - (a - b)) ** 2 + 2 * a**2 * y / q)
    )
    assert certificate == 0

    print("first-product S-bound concavity certificate")
    print("S =", s)
    print("Y =", y)
    print("F = g^2*S - Y^2*u")
    print("F_pp = -2*u*((2*a^2*p/q-(a-b))^2 + 2*a^2*Y/q)")
    print("Thus F is concave on the hard region Y>=0.")


if __name__ == "__main__":
    main()
