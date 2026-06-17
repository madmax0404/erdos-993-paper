"""Explicit dual certificates for the master inequality (M), exactly verified.

For each (multiset, k) in band A this script constructs an explicit
certificate from one of two families and verifies it in exact rational
arithmetic (fractions.Fraction throughout; no floats in any verified
inequality):

T2 (quadratic-majorant certificate), multipliers (mu, y1, y2, yt, u_s):
    pointwise   mu + y1 s + y2 s(s-1) + yt 2^s + u_s  >=  cap(s),  1 <= s <= smax
    objective   mu eps + y1 R1 + y2 R2 + yt ((1+eps)^2 - 1) + sum_s u_s B_s
                <=  RHS(M) = (1-lam)(1+eps) + rho_k m_k (1+eps)^2
  where R1 = eps(2+eps)/2 >= sum s W_s (P5 + trapezoid bound
  ln(1+x) <= x(2+x)/(2(1+x))), R2 = eps^2(2+eps)^2/(4(1+eps)) >=
  sum s(s-1) W_s (flow concavity + the same bound), B_s = C(h,s) q_k^s
  (E1e; used only when q_k < 1), and cap(s) are the proved per-class
  charges (E1a/exact-mean ceilings, exact-mean Jensen floors).
  Construction: anchor the quadratic at s = 1, 2; y2 is the maximal
  second divided difference against the chord (clamped so y1 >= 0);
  the residual tail is covered by u_s or yt, whichever is cheaper.

T1 (Case L' certificate), from the eps-identity and r_{k+1} <= r_k:
    lam (1+eps)[(1+slack)(1+eps)/(1+eps') - 1] + (eps' - eps)^+
        <=  RHS(M),
  with eps' = eps_{k-1} and slack = rho_k/rho_{k+1} - 1.

The point passes if T1 or T2 verifies.  Output: per-case worst slack,
JSON log.  Zero failures = priority 2 of notes/993-GOAL.md.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from math import comb, ceil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
from erdos993.indpoly import mul  # noqa: E402


EXT_MIXED_CASES = [
    [2, 4, 4, 4, 5, 5, 6, 8],
    [3, 4, 9, 10, 11, 11],
    [1, 1, 3, 4, 5, 8],
    [2, 2, 3, 6, 6, 7],
    [4, 4, 4, 5, 8, 9],
    [2, 4],
    [2, 2, 8, 9, 9, 10, 12],
    [2, 2, 4, 6, 10, 12, 12, 12],
    [2, 2, 5, 8, 9],
    [1, 2, 6, 7, 9, 9, 10],
    [4, 4, 7, 8, 9, 10],
    [1, 1, 1, 3, 7, 8, 11],
    [6, 12],
    [1, 2, 5, 7, 8, 9, 10, 12],
    [2, 3, 5, 8, 9, 11, 12],
    [1, 8],
    [1, 1, 7, 10],
    [1, 1, 2, 3, 4, 8, 11, 12],
    [2, 2, 3, 7, 8],
    [2, 4, 5],
    [1, 3, 3],
    [4, 11],
    [7, 7, 10, 10, 12, 12],
    [2, 5, 8, 9, 10],
    [5, 5, 5, 7, 8, 9],
    [1, 1, 1, 2, 4, 8, 10, 12],
    [1, 2, 11],
    [4, 9],
    [2, 2, 3, 5, 7, 7, 11],
    [4, 7, 8, 9, 12],
    [2, 5, 5, 6, 6, 7, 9, 11],
    [5, 6, 12],
    [7, 8, 9, 9, 9, 11, 12],
    [5, 7, 9, 12, 12],
    [2, 2, 3, 3, 5, 5, 11],
    [1, 4, 10, 12],
    [1, 9, 9, 10, 10, 11],
    [10, 12],
    [11, 12],
    [1, 3, 3, 5, 6, 9, 11, 11],
]


def binp(c, b):
    return tuple(comb(c, k) * b**k for k in range(c + 1))


def cf(p, k):
    return p[k] if 0 <= k < len(p) else 0


def Nc(c):
    return c + 1 + (c + 29) // 30


def floor_v2(s, a, k, C):
    j = k - s
    if j <= 1:
        return None
    rho_k = Fraction(2 * (C - k + 1), k)
    Em = Fraction(a * (j - 1), (j - 1) + 2 * (C - j + 1))
    mm = j - Em
    base = Fraction(0)
    if mm > 0:
        base = Fraction(2) * max(Fraction(0), C - a - mm + 1) / mm / rho_k
    f1 = (1 + Fraction(s, k - s)) * (1 + Fraction(s, C - k + 1)) / 2 if k - s >= 1 else Fraction(0)
    f2 = Fraction(k, k - s) * Fraction(max(0, C - a - k + s + 1), C - k + 1) if k - s >= 1 else Fraction(0)
    return max(base, f1, f2)


def ceiling_v2(s, a, k1, C):
    """Exact-mean reverse-Jensen ceiling on growth into position k1, or
    None when the formula provides no valid bound (caller must fall
    back to the Q-ceiling alone).  AUDIT FIX 2026-06-12: the former
    BIG=10 sentinel acted as a false constraint at class-birth
    positions (true growth can exceed any constant)."""
    j = k1 - s
    if j <= 0:
        return None
    Ep = Fraction(a * j, C)
    if Ep >= j:
        return None
    mm = j - Ep
    num = C - a - mm + 1
    if num <= 0:
        return None
    rho = Fraction(2 * (C - k1 + 1), k1)
    return Fraction(2) * num / mm / rho


def caps_exact(counts, k):
    h, C = len(counts), sum(counts)
    lam = Fraction((k - 1) * (C - k), (k + 1) * (C - k + 2))
    rho_k = Fraction(2 * (C - k + 1), k)
    rho_k1 = Fraction(2 * (C - k), k + 1)
    rho_slack = rho_k / rho_k1 - 1
    smax = min(h, k)
    asets = {s: set() for s in range(1, smax + 1)}
    if len(set(counts)) == 1:
        for s in range(1, smax + 1):
            asets[s] = {counts[0] * s}
    else:
        for s in range(1, smax + 1):
            for S in combinations(range(h), s):
                asets[s].add(sum(counts[i] for i in S))
    caps = [Fraction(0)] * (smax + 1)
    for s in range(1, smax + 1):
        QA = (1 + Fraction(s, k + 1 - s)) * (1 + Fraction(s, C - k)) if (k + 1 - s >= 1 and C - k >= 1) else Fraction(4)
        QB = (1 + Fraction(s, k - s)) * (1 + Fraction(s, C - k + 1)) if k - s >= 1 else Fraction(4)
        best = None
        for a in asets[s]:
            fl = floor_v2(s, a, k, C) if s < k else None
            wf = fl if (fl is not None and fl > 0) else Fraction(1, 2)
            dip = max(Fraction(0), 1 - wf) / wf if s < k else Fraction(0)
            cv = ceiling_v2(s, a, k + 1, C)
            ceilA = min(QA, cv) if cv is not None else QA
            cA = lam * max(Fraction(0), ceilA - 1) + dip
            cv0 = ceiling_v2(s, a, k, C)
            ceil0 = min(QB, cv0) if cv0 is not None else QB
            # AUDIT FIX: dev must majorize |g0 - 1| with the K-LEVEL
            # ceiling (g0 <= ceil0), not the k+1 ceiling.
            dev = max(max(Fraction(0), ceil0 - 1), 1 - wf)
            cB = lam * (ceil0 * rho_slack + dev * dev / wf) + (1 - lam) * dip
            cap_a = min(cA, cB)
            if best is None or cap_a > best:
                best = cap_a
        caps[s] = best if best is not None else Fraction(0)
    return caps, lam, rho_k, rho_slack


def build_T2(caps, eps, h, k, C):
    """Explicit quadratic-majorant certificate; returns (lhs_objective, detail)."""
    smax = len(caps) - 1
    if smax < 2:
        return None, None
    delta = caps[2] - caps[1]
    y2 = Fraction(0)
    for s in range(3, smax + 1):
        num = caps[s] - caps[1] - (s - 1) * delta
        if num > 0:
            y2 = max(y2, num / Fraction((s - 1) * (s - 2)))
    # clamp so y1 >= 0
    y2 = min(y2, max(Fraction(0), delta / 2))
    mu = caps[1] - delta + 2 * y2
    y1 = delta - 2 * y2
    if y1 < 0:
        y1 = Fraction(0)
        mu = caps[1] - 0  # fallback: flat line through cap(1)... keep mu = cap(1) - y1
        mu = caps[1]
    def quad(s):
        return mu + y1 * s + y2 * s * (s - 1)
    # residual tail cover: u_s (class bounds, only valid if q < 1) or yt*2^s
    q_num, q_den = k, 2 * (C - k + 1)
    q = Fraction(q_num, q_den)
    use_class = q < 1
    resid = [(s, caps[s] - quad(s)) for s in range(1, smax + 1) if caps[s] > quad(s)]
    cost_u = None
    if use_class:
        cost_u = sum(r * comb(h, s) * q**s for s, r in resid)
    yt = Fraction(0)
    for s, r in resid:
        yt = max(yt, r / Fraction(2**s))
    cost_t = yt * ((1 + eps) ** 2 - 1)
    if cost_u is not None and cost_u <= cost_t:
        tail_cost, mode = cost_u, "class"
        yt = Fraction(0)
        u = {s: r for s, r in resid}
    else:
        tail_cost, mode = cost_t, "t2"
        u = {}
    # pointwise check (exact)
    for s in range(1, smax + 1):
        lhs_pw = quad(s) + yt * 2**s + u.get(s, Fraction(0))
        if lhs_pw < caps[s]:
            return None, f"pointwise fail at s={s}"
    R1 = eps * (2 + eps) / 2
    R2 = eps * eps * (2 + eps) ** 2 / (4 * (1 + eps))
    obj = mu * eps + y1 * R1 + y2 * R2 + tail_cost
    return obj, mode


def verify_case(counts):
    h, C = len(counts), sum(counts)
    D = h + C
    NF = sum(Nc(cc) for cc in counts)
    n_vertices = 1 + h + 2 * C
    kA = min(ceil(D * (n_vertices - 1) / (D + n_vertices)) - 1, ceil((2 * D - 1) / 3) - 1, C - 1)
    F = (1,)
    for cc in counts:
        F = mul(F, tuple(x + y for x, y in zip(list(binp(cc, 2)) + [0], [0] + list(binp(cc, 1)), strict=True)))
    g = binp(C, 2)
    worst = None
    fail = None
    for k in range(2, kA + 1):
        caps, lam, rho_k, rho_slack = caps_exact(counts, k)
        m = Fraction(NF + 1, (k + 1) * (NF - k + 1))
        eps = Fraction(cf(F, k) - cf(g, k), cf(g, k))
        eps1 = Fraction(cf(F, k - 1) - cf(g, k - 1), cf(g, k - 1))
        if eps <= 0:
            continue
        rhs = (1 - lam) * (1 + eps) + rho_k * m * (1 + eps) ** 2
        # T1
        lhsT1 = lam * (1 + eps) * ((1 + rho_slack) * (1 + eps) / (1 + eps1) - 1) + max(Fraction(0), eps1 - eps)
        okT1 = lhsT1 <= rhs
        # T2
        objT2, mode = build_T2(caps, eps, h, k, C)
        okT2 = objT2 is not None and objT2 <= rhs
        if not (okT1 or okT2):
            fail = (k, float(eps), float(lhsT1 / rhs), float(objT2 / rhs) if objT2 is not None else None)
            break
        used = min([x for x in [lhsT1 if okT1 else None, objT2 if okT2 else None] if x is not None])
        ratio = used / rhs
        if worst is None or ratio > worst[0]:
            worst = (ratio, k, float(eps))
    return worst, fail


def default_cases():
    import random
    cases = []
    for c in range(1, 9):
        for h in range(2, 40):
            if h + c * h <= 120:
                cases.append([c] * h)
    rng = random.Random(55)
    for _ in range(50):
        h = rng.randint(2, 7)
        cases.append(sorted(rng.randint(1, 10) for _ in range(h)))
    return cases


def extended_cases():
    cases = []
    for c in range(1, 11):
        first_h = 3 if c == 1 else 2
        max_h = 159 // (1 + 2 * c)
        for h in range(first_h, max_h + 1):
            cases.append([c] * h)
    cases.extend(EXT_MIXED_CASES)
    return cases


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ext", action="store_true", help="regenerate logs/993_M_dual_certificates_ext.json")
    args = parser.parse_args()

    cases = extended_cases() if args.ext else default_cases()

    results, failures = [], []
    global_worst = (Fraction(0), None)
    for counts in cases:
        worst, fail = verify_case(counts)
        if fail is not None:
            failures.append({"counts": counts, "at": fail})
            continue
        if worst is None:
            continue
        results.append({"counts": counts, "max_ratio": float(worst[0]), "k": worst[1], "eps": worst[2]})
        if worst[0] > global_worst[0]:
            global_worst = (worst[0], (tuple(counts), worst[1], round(worst[2], 3)))

    if args.ext:
        payload = {
            "cases": len(results),
            "failures": failures,
            "worst": float(global_worst[0]),
            "per_case": [
                {"counts": r["counts"], "max_ratio": r["max_ratio"]}
                for r in results
            ],
        }
        out = REPO / "logs" / "993_M_dual_certificates_ext.json"
    else:
        payload = {
            "certificates": ["T1 (Case L', exact rational)", "T2 (quadratic majorant + tail, exact rational)"],
            "cases": len(results),
            "failures": failures,
            "worst_ratio": float(global_worst[0]),
            "worst_at": str(global_worst[1]),
            "per_case": results,
        }
        out = REPO / "logs" / "993_M_dual_certificates.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"cases verified: {len(results)}, failures: {len(failures)}")
    if failures:
        for f in failures[:5]:
            print("  FAIL:", f)
    print(f"worst exact certificate-ratio = {float(global_worst[0]):.4f} at {global_worst[1]}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
