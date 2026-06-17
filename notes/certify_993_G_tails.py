"""Symbolic certification of the five G-closure tail branches.

The CHAIN's X >= 0 branch needs G = vA - M >= 0 (A = h(k+2h-10)+k,
M = (k+1-4q)(k+h-6) + 2(q-2)(k-3)) at every in-band X-feasible
tuple.  G is linear increasing in v, and the feasible v is bounded
below by the band bound v_b = (3k+1-2h-4q)/(2h) and (when
k >= 2h+3) the X-bound v_X = s/(k-2-2h), s = 4q-k-1.  The five
branches, each reduced to ONE polynomial on a quadrant (upper
constraints dropped -- proving more):

B1a: k in [2h+3, 4h-5], q at its worst (linear in q, coefficient
     4(h-k) < 0) = (k+1)/4; poly 2(k-h)A - h(k-7)(k-3) with
     k = 2h+3+t.
B1b: k >= 4h-5, q* = h-1: poly (3k-6h+5)A - 2h(k-4h+5)(k+h-6)
     - 4h(h-3)(k-3) with k = 4h-5+t.   [k <= 12h dropped; k > 12h
     is Tail 1, proved by hand: v_band >= (3k-6h)/2h >= (k+3h)/h
     >= v_G.]
B2:  k in [2h+3, 4h-5], q = (k+1+4r)/4, r > 0 (i.e. s = 4r >= 1):
     evaluate G at the average (v_b+v_X)/2 <= max(v_b, v_X) <=
     feasible v; poly F2 = A[(k-h-2r)(k-2-2h) + 4hr]
     - 2h(k-2-2h) M with k = 2h+3+t.  (Scaled by 4 to clear /4's.)
B3a: k <= 2h+2, v = 1 feasible: region k >= h+2q+1 (X(1) >= 0),
     3k <= 4h+4q-1 (band at v=1): parametrize k = h+2q+1+u,
     h = 2q+4+3u+w: poly G(1).
B3b: k <= 2h+2, v_min = 2: region 3k >= 4h+4q+3 (X(2) >= 0),
     k <= 2h+2: parametrize 3k = 4h+4q+3+u (with 3 | alignment
     handled by certifying in the real relaxation), k = 2h+2-w':
     poly G(2) in the quadrant variables.

Certification: expand each branch polynomial in its quadrant
variables, optionally shift the h-like variable by up to 200
(licensed by the exhaustive base logs/993_G_closure.json), and
check ALL coefficients >= 0.  Any branch that fails the shift test
is reported honestly (the method is sufficient, not complete).

Output: logs/993_G_tails_certification.json
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[1]

h, t, r, q, u, w = sp.symbols('h t r q u w', nonnegative=True)


def quadrant_nonneg(P, vars_, shifts):
    """All coefficients of P(vars + shifts) nonnegative?"""
    sub = {v_: v_ + s_ for v_, s_ in zip(vars_, shifts)}
    Pe = sp.expand(P.subs(sub))
    poly = sp.Poly(Pe, *vars_)
    return all(c >= 0 for c in poly.coeffs()), poly


def try_certify(name, P, vars_, base_shifts, results):
    """Try shifts of the h-like first variable: 0, 3, 13, 50, 200."""
    for s0 in (0, 3, 13, 50, 100, 200):
        shifts = [base_shifts[0] + s0] + list(base_shifts[1:])
        ok, _ = quadrant_nonneg(P, vars_, shifts)
        if ok:
            results[name] = {"certified": True, "h_shift": shifts[0]}
            print(f"[{name}] certified with shifts {shifts}",
                  flush=True)
            return
    results[name] = {"certified": False}
    print(f"[{name}] NOT certified by coefficient method", flush=True)


def main():
    results = {}

    # B1a: k = 2h+3+t, q = (k+1)/4 worst case
    k_ = 2 * h + 3 + t
    A = h * (k_ + 2 * h - 10) + k_
    P_b1a = sp.expand(2 * (k_ - h) * A - h * (k_ - 7) * (k_ - 3))
    try_certify("B1a", P_b1a, (h, t), (3, 0), results)

    # B1b: k = 4h-5+t, q = h-1
    k_ = 4 * h - 5 + t
    A = h * (k_ + 2 * h - 10) + k_
    P_b1b = sp.expand((3 * k_ - 6 * h + 5) * A
                      - 2 * h * (k_ - 4 * h + 5) * (k_ + h - 6)
                      - 4 * h * (h - 3) * (k_ - 3))
    try_certify("B1b", P_b1b, (h, t), (3, 0), results)

    # B2: k = 2h+3+t, q = (k+1)/4 + r (so s = 4r), r >= 1/4 -> use
    # 4r' = s integer >= 1; work with rr := s (>= 1) to stay integral:
    # q = (k+1+rr)/4 ... clear denominators by scaling: multiply
    # G-average poly by 16.
    rr = sp.symbols('rr', nonnegative=True)   # rr = s = 4q-k-1 >= 1
    k_ = 2 * h + 3 + t
    A = h * (k_ + 2 * h - 10) + k_
    M = -rr * (k_ + h - 6) + 2 * ((k_ + 1 + rr) / 4 - 2) * (k_ - 3)
    kk = k_ - 2 - 2 * h           # = t + 1 > 0
    F2 = sp.expand(4 * (A * ((k_ - h - rr / 2) * kk + h * rr)
                        - 2 * h * kk * M))
    # substitute rr -> 1 + rr2 to encode s >= 1
    rr2 = sp.symbols('rr2', nonnegative=True)
    F2 = sp.expand(F2.subs(rr, 1 + rr2))
    try_certify("B2", F2, (h, t, rr2), (3, 0, 0), results)

    # B3a: v = 1; k = h+2q+1+u; h = 2q+4+3u+w  (q >= 2)
    q2 = sp.symbols('q2', nonnegative=True)   # q = 2 + q2
    qv = 2 + q2
    hv = 2 * qv + 4 + 3 * u + w
    kv = hv + 2 * qv + 1 + u
    A = hv * (kv + 2 * hv - 10) + kv
    P_b3a = sp.expand(A - (kv + 1 - 4 * qv) * (kv + hv - 6)
                      - 2 * (qv - 2) * (kv - 3))
    try_certify("B3a", P_b3a, (q2, u, w), (0, 0, 0), results)

    # B3b: v = 2; 3k = 4h+4q+3+u, k = 2h+2-w  =>  parametrize via
    # (q, u, w): h = (3(2h+2-w) - 4q - 3 - u)/4 ... solve: 3k = 4h+
    # 4q+3+u and k = 2h+2-w  => 3(2h+2-w) = 4h+4q+3+u =>
    # 2h = 4q + u + 3w - 3  => h = 2q + (u + 3w - 3)/2.  Use
    # integral parametrization u = 3 + 2u2 - 3w + ... simpler: certify
    # in the real relaxation with h free: variables (h, q, w) with
    # k = 2h+2-w and the constraint 3k >= 4h+4q+3 encoded as
    # u = 3k-4h-4q-3 = 2h+3-3w-4q-... = 2h - 4q - 3w + 3 >= 0:
    # substitute h = 2q + (3w + u2 - 3)/2 ... to keep it polynomial,
    # certify P_b3b in (q2, w, u2) with h = 2q + 2*w2... fall back:
    # h = 2q + s3 where 2 s3 = u2 + 3w - 3, i.e. certify with
    # s3 >= 0 free (covers all integer cases with u2 >= 0 since
    # s3 ranges over half-integers >= (3w-3)/2... we instead certify
    # for ALL h >= 2q + (3w-3)/2 by treating s3 as a free
    # nonnegative variable -- a superset of the true region.
    # Clean parametrization of the region {3k >= 4h+4q+3, k <= 2h+2,
    # q >= 2}: k = 2h+2-tau (tau >= 0), and the X(2)-constraint
    # 3(2h+2-tau) >= 4h+4q+3 <=> 2h >= 4q+3 tau - 3 ... with q = 2+q2:
    # 2h = 5 + 4 q2 + 3 tau + s2, s2 >= 0 (s2 carries the parity;
    # certifying all real s2 >= 0 covers the integers).
    tau, s2 = sp.symbols('tau s2', nonnegative=True)
    qv = 2 + q2
    hv = (5 + 4 * q2 + 3 * tau + s2) / 2
    kv = 2 * hv + 2 - tau
    A2 = hv * (kv + 2 * hv - 10) + kv
    P_b3b = sp.expand(4 * (2 * A2 - (kv + 1 - 4 * qv)
                           * (kv + hv - 6)
                           - 2 * (qv - 2) * (kv - 3)))
    try_certify("B3b", P_b3b, (q2, tau, s2), (0, 0, 0), results)

    path = REPO / "logs" / "993_G_tails_certification.json"
    path.write_text(json.dumps(results, indent=2))
    n_ok = sum(1 for v_ in results.values() if v_["certified"])
    print(f"TOTAL: {n_ok}/{len(results)} branches certified; "
          f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
