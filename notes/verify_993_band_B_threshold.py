"""Band-B threshold certificate for the paper write-up.

This is the finite companion to the large-parameter Band-B absorption
argument.  It checks two things in exact arithmetic:

1. Every leaf-heavy multiset with C < 55 and nonempty Band B has
   LC_P(k) >= 0 for every k in [C, k_dec - 1].
2. The explicit large-parameter sufficient inequalities used in the
   write-up are positive for C >= 55 over a long boundary range.  The
   paper uses the elementary monotonicity of these displayed bounds to
   make this an all-C statement; this script guards the arithmetic and
   the threshold.

Output: logs/993_band_B_threshold.json
"""

from __future__ import annotations

import json
import sys
from functools import cache
from fractions import Fraction
from math import ceil, comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from erdos993.indpoly import mul  # noqa: E402


SMALL_C_MAX = 54
LARGE_C_MIN = 55
LARGE_C_CHECK_TO = 1000


def cf(poly: tuple[int, ...], k: int) -> int:
    return poly[k] if 0 <= k < len(poly) else 0


@cache
def hub(c: int) -> tuple[int, ...]:
    e = tuple(comb(c, k) * 2**k for k in range(c + 1))
    b = (0, *tuple(comb(c, k) for k in range(c + 1)))
    n = max(len(e), len(b))
    return tuple((e[i] if i < len(e) else 0) + (b[i] if i < len(b) else 0) for i in range(n))


@cache
def g_poly(C: int) -> tuple[int, ...]:
    return tuple(comb(C, k) * 2**k for k in range(C + 1))


def k_dec(C: int, h: int) -> int:
    D = C + h
    n = 1 + h + 2 * C
    k0 = ceil((2 * D - 1) / 3)
    ell_bg = ceil(D * (n - 1) / (D + n))
    return min(k0, ell_bg)


def has_band_b(C: int, h: int) -> bool:
    return k_dec(C, h) - 1 >= C


def partitions_of_excess(excess: int, max_len: int, max_part: int | None = None):
    """Partitions of excess into at most max_len positive parts."""

    if excess == 0:
        yield ()
        return
    if max_len == 0:
        return
    if max_part is None or max_part > excess:
        max_part = excess
    for first in range(max_part, 0, -1):
        for rest in partitions_of_excess(excess - first, max_len - 1, min(first, excess - first)):
            yield (first, *rest)


def multisets_with_sum(C: int, h: int):
    excess = C - h
    for part in partitions_of_excess(excess, h):
        ds = [*part, *([0] * (h - len(part)))]
        yield tuple(sorted(1 + d for d in ds))


def check_exact_band_b(counts: tuple[int, ...]) -> tuple[bool, int, int | None]:
    C = sum(counts)
    h = len(counts)
    D = C + h
    kd = k_dec(C, h)
    F = (1,)
    for c in counts:
        F = mul(F, hub(c))
    g = g_poly(C)
    P = tuple(cf(F, k) + cf(g, k - 1) for k in range(D + 2))

    worst_lc: int | None = None
    rows = 0
    for k in range(C, min(kd - 1, D - 1) + 1):
        rows += 1
        lc = P[k] * P[k] - P[k - 1] * P[k + 1]
        worst_lc = lc if worst_lc is None else min(worst_lc, lc)
        if lc < 0:
            return False, rows, k
    return True, rows, worst_lc


def large_bounds(C: int, h: int) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    """The five sufficient inequalities used for C >= 55.

    Let A_c=2^c+c be the one-below-top coefficient of H_c.  Repeated
    compression A_a A_b >= 3 A_{a+b-1} gives
        F_C >= 3^(h-1)(2^(C-h+1)+C-h+1).
    If r is the number of c_i=1 hubs, then r >= 2h-C.  Using A_1=3
    and A_c >= 2^c on the remaining hubs gives the displayed lower
    bounds for F_{C+1} and F_{C+2}.
    """

    b = C - h + 1
    L0 = 3 ** (h - 1) * (2**b + b)
    r = max(0, 2 * h - C)
    L1 = r * 3 ** (r - 1) * 2 ** (C - r) if r >= 1 else 0
    L2 = comb(r, 2) * 3 ** (r - 2) * 2 ** (C - r) if r >= 2 else 0

    Nmax = 2 * C + h
    m0 = Fraction(Nmax + 1, (C + 1) * (C + h + 1))
    m1 = Fraction(Nmax + 1, (C + 2) * (C + h))
    m2 = Fraction(Nmax + 1, (C + 3) * (C + h - 1))
    R1 = Fraction(C + h, C + 1)
    R2 = Fraction(C + h - 1, C + 2)
    R3 = Fraction(C + h - 2, C + 3)

    B = 2**C
    A = C * 2 ** (C - 1)
    D = C * (C - 1) * 2 ** (C - 3)

    # k=C: after F_{C-1} <= C F_C cancels the 2 F_C g_{C-1} term.
    c0_value = Fraction(L0 * L0) * m0 - D * R1 * L0 + A * A - D * B
    c0_slope = 2 * Fraction(L0) * m0 - D * R1

    # k=C+1.
    c1_value = Fraction(L1 * L1) * m1 + 2 * B * L1 + B * B - A * R2 * L1
    c1_slope = 2 * Fraction(L1) * m1 + 2 * B - A * R2

    # k=C+2.
    c2_value = Fraction(L2) * m2 - B * R3
    return c0_value, c0_slope, c1_value, c1_slope, c2_value


def main() -> None:
    small_cases = 0
    small_rows = 0
    small_by_C: dict[int, int] = {}
    failures: list[dict[str, object]] = []
    worst_lc: int | None = None

    for C in range(2, SMALL_C_MAX + 1):
        for h in range(2, C + 1):
            if not has_band_b(C, h):
                continue
            for counts in multisets_with_sum(C, h):
                ok, rows, marker = check_exact_band_b(counts)
                small_cases += 1
                small_rows += rows
                small_by_C[C] = small_by_C.get(C, 0) + 1
                if ok:
                    worst_lc = marker if worst_lc is None else min(worst_lc, marker)
                else:
                    failures.append({"counts": counts, "failed_k": marker})

    large_failures: list[dict[str, object]] = []
    large_pairs = 0
    min_large = [None] * 5
    argmin_large: list[tuple[int, int] | None] = [None] * 5
    for C in range(LARGE_C_MIN, LARGE_C_CHECK_TO + 1):
        for h in range(2, C + 1):
            if not has_band_b(C, h):
                continue
            large_pairs += 1
            vals = large_bounds(C, h)
            for i, value in enumerate(vals):
                if min_large[i] is None or value < min_large[i]:
                    min_large[i] = value
                    argmin_large[i] = (C, h)
            if any(value < 0 for value in vals):
                large_failures.append(
                    {
                        "C": C,
                        "h": h,
                        "negative_indices": [i for i, value in enumerate(vals) if value < 0],
                    }
                )

    payload = {
        "small_C_max": SMALL_C_MAX,
        "large_C_min": LARGE_C_MIN,
        "large_C_checked_to": LARGE_C_CHECK_TO,
        "small_exact_cases": small_cases,
        "small_exact_band_rows": small_rows,
        "small_cases_by_C": dict(sorted(small_by_C.items())),
        "small_exact_failures": failures,
        "small_exact_worst_lc": str(worst_lc),
        "large_bound_pairs_checked": large_pairs,
        "large_bound_failures": large_failures[:20],
        "large_bound_failure_count": len(large_failures),
        "large_bound_argmins": argmin_large,
        "large_bound_min_values": [str(value) for value in min_large],
    }

    out = REPO / "logs" / "993_band_B_threshold.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"small exact cases: {small_cases}")
    print(f"small exact Band-B rows: {small_rows}")
    print(f"small exact failures: {len(failures)}")
    print(f"large bound pairs checked: {large_pairs}")
    print(f"large bound failures: {len(large_failures)}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
