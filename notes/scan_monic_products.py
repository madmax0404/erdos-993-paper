from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations_with_replacement, product
from random import Random
from typing import Iterable, Sequence


Poly = tuple[int, ...]


def admissible_factors(degree: int, cap: int) -> list[Poly]:
    if degree < 2:
        raise ValueError("degree must be at least 2")

    factors: list[Poly] = []
    interior_len = degree - 1

    def rec(prefix: list[int]) -> None:
        index = len(prefix) + 1
        if len(prefix) == interior_len:
            if prefix[-2] >= prefix[-1]:
                factors.append((1, *prefix, 1))
            return

        upper = cap
        if index == interior_len and prefix:
            upper = min(upper, prefix[-1])

        for value in range(1, upper + 1):
            if len(prefix) >= 1:
                prev_prev = 1 if len(prefix) == 1 else prefix[-2]
                prev = prefix[-1]
                if prev * prev < prev_prev * value:
                    continue
            rec([*prefix, value])

    rec([])
    return factors


def random_factor(degree: int, first_cap: int, rng: Random) -> Poly:
    if degree < 2:
        raise ValueError("degree must be at least 2")

    while True:
        interior = [rng.randint(1, first_cap)]
        valid = True
        for index in range(2, degree):
            upper = interior[-1] * interior[-1]
            upper //= 1 if len(interior) == 1 else interior[-2]
            if index == degree - 1:
                upper = min(upper, interior[-1])
            if upper < 1:
                valid = False
                break
            interior.append(rng.randint(1, upper))
        if valid:
            return (1, *interior, 1)


def mul(p: Sequence[int], q: Sequence[int]) -> Poly:
    result = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return tuple(result)


def is_unimodal(seq: Sequence[int]) -> bool:
    falling = False
    for left, right in zip(seq, seq[1:]):
        if right < left:
            falling = True
        elif falling and right > left:
            return False
    return True


def signs(differences: Sequence[int]) -> str:
    return "".join("+" if x > 0 else "-" if x < 0 else "0" for x in differences)


def differences(seq: Sequence[int]) -> tuple[int, ...]:
    return tuple(right - left for left, right in zip(seq, seq[1:]))


def pair_iter(factors_a: Sequence[Poly], factors_b: Sequence[Poly], ordered: bool) -> Iterable[tuple[Poly, Poly]]:
    if factors_a is factors_b and not ordered:
        return combinations_with_replacement(factors_a, 2)
    return product(factors_a, factors_b)


def summarize_pairs(
    degree_a: int,
    degree_b: int,
    pairs: Iterable[tuple[Poly, Poly]],
    top: int,
    header: Sequence[str],
) -> None:
    pair_count = 0
    pattern_counts: Counter[str] = Counter()
    central_pattern_counts: Counter[str] = Counter()
    first_failure: tuple[Poly, Poly, Poly, str] | None = None
    adjacent_min: dict[int, tuple[int, int, Poly, Poly, Poly]] = {}
    diff_min: dict[int, tuple[int, Poly, Poly, Poly]] = {}
    diff_max: dict[int, tuple[int, Poly, Poly, Poly]] = {}

    for p, q in pairs:
        pair_count += 1
        r = mul(p, q)
        d = differences(r)
        pattern = signs(d)
        pattern_counts[pattern] += 1
        central_pattern_counts[pattern[2:-3]] += 1

        if first_failure is None and not is_unimodal(r):
            first_failure = (p, q, r, pattern)

        for index, value in enumerate(d):
            if index not in diff_min or value < diff_min[index][0]:
                diff_min[index] = (value, p, q, r)
            if index not in diff_max or value > diff_max[index][0]:
                diff_max[index] = (value, p, q, r)

        for index in range(len(d) - 1):
            if d[index + 1] > 0:
                previous = d[index]
                if index not in adjacent_min or previous < adjacent_min[index][0]:
                    adjacent_min[index] = (previous, d[index + 1], p, q, r)

    print(f"degrees: ({degree_a},{degree_b})")
    for line in header:
        print(line)
    print(f"pairs checked: {pair_count}")
    print(f"first non-unimodal product: {first_failure}")
    print()

    print("top full sign patterns:")
    for pattern, count in pattern_counts.most_common(top):
        print(f"  {pattern}: {count}")
    print()

    print("top central sign patterns (drop first 2 and last 3 differences):")
    for pattern, count in central_pattern_counts.most_common(top):
        print(f"  {pattern}: {count}")
    print()

    print("adjacent implication minima: diff[i+1] > 0 => min diff[i]")
    for index in sorted(adjacent_min):
        previous, later, p, q, r = adjacent_min[index]
        print(f"  i={index}: min previous={previous}, later={later}, p={p}, q={q}, product={r}")
    print()

    print("difference ranges:")
    for index in sorted(diff_min):
        minimum = diff_min[index][0]
        maximum = diff_max[index][0]
        print(f"  diff[{index}]: min={minimum}, max={maximum}")


def scan(degree_a: int, degree_b: int, cap: int, ordered: bool, top: int) -> None:
    factors_a = admissible_factors(degree_a, cap)
    factors_b = factors_a if degree_a == degree_b else admissible_factors(degree_b, cap)
    pairs = pair_iter(factors_a, factors_b, ordered)
    summarize_pairs(
        degree_a,
        degree_b,
        pairs,
        top,
        [
            f"cap: {cap}",
            f"factors A: {len(factors_a)}",
            f"factors B: {len(factors_b)}",
        ],
    )


def random_scan(degree_a: int, degree_b: int, trials: int, first_cap: int, seed: int, top: int) -> None:
    rng = Random(seed)
    pairs = (
        (
            random_factor(degree_a, first_cap, rng),
            random_factor(degree_b, first_cap, rng),
        )
        for _ in range(trials)
    )
    summarize_pairs(
        degree_a,
        degree_b,
        pairs,
        top,
        [
            f"random trials: {trials}",
            f"first coefficient cap: {first_cap}",
            f"seed: {seed}",
        ],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("degree_a", type=int)
    parser.add_argument("degree_b", type=int)
    parser.add_argument("--cap", type=int, default=10)
    parser.add_argument("--ordered", action="store_true")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--random-trials", type=int, default=0)
    parser.add_argument("--first-cap", type=int, default=200)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if args.random_trials:
        random_scan(args.degree_a, args.degree_b, args.random_trials, args.first_cap, args.seed, args.top)
    else:
        scan(args.degree_a, args.degree_b, args.cap, args.ordered, args.top)


if __name__ == "__main__":
    main()
