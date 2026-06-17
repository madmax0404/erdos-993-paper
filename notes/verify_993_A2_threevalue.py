"""Sub-lemma A.2 (three-value kill): statement-pinning probe.

Lemma A's remaining case after A.1: a config with >= 3 distinct
values is never a local maximum of the rung-1 ratio.  (Together with
A.1 -- two values with gap >= 2 require q = 1 -- this gives exactly
the census shapes: adjacent-two-value or bulk+giant.)

This probe sweeps three-value configs (v1^p1, v2^p2, v3^p3),
v1 < v2 < v3, over gaps (1..12), multiplicity patterns, h <= 40,
band k (k >= 4), and tests the COMPLETE single-transfer move set
(all ordered value pairs, including self-pairs where multiplicity
allows).  For each config: does some move strictly improve?  Which
moves improve (the drain map, for the proof's case split)?  Any
config with NO improving move is a counterexample to A.2 (a
three-value local maximum) and reshapes Lemma A.

Output: logs/993_A2_threevalue.json
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def band_kA(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(lBG - 1, k0 - 1, C - 1)


def f(alpha, beta, m):
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def masses(counts, C, k):
    vals = sorted(counts)
    W1 = sum(counts[v] * f(v, C - v, k - 1) for v in vals)
    W2 = 0
    for i, v in enumerate(vals):
        if counts[v] >= 2:
            W2 += comb(counts[v], 2) * f(2 * v, C - 2 * v, k - 2)
        for w in vals[i + 1:]:
            W2 += counts[v] * counts[w] * f(v + w, C - v - w, k - 2)
    return W1, W2


def improving_moves(counts, C, k):
    """All (giver_value, receiver_value) single transfers that
    strictly improve the ratio."""
    W1, W2 = masses(counts, C, k)
    if W1 == 0:
        return None, []
    out = []
    vals = sorted(counts)
    for u in vals:           # giver (u -> u-1), needs u >= 2
        if u < 2:
            continue
        for v in vals:       # receiver (v -> v+1)
            if u == v and counts[u] < 2:
                continue
            if v + 1 == u:
                continue
            c2 = Counter(counts)
            c2[u] -= 1
            c2[v] -= 1
            c2[u - 1] += 1
            c2[v + 1] += 1
            for t in (u, v, u - 1, v + 1):
                if c2[t] == 0:
                    del c2[t]
            nW1, nW2 = masses(c2, C, k)
            if nW1 > 0 and nW2 * W1 * W1 > W2 * nW1 * nW1:
                out.append((u, v))
    return (W1, W2), out


def main():
    rows, none_cases = 0, []
    drain = Counter()
    for h in (4, 6, 8, 12, 24, 40):
        for v1 in (1, 2, 3):
            for g1 in (1, 2, 3, 6, 12):
                for g2 in (1, 2, 3, 6, 12):
                    v2, v3 = v1 + g1, v1 + g1 + g2
                    pats = [(h - 2, 1, 1), (1, h - 2, 1), (1, 1, h - 2),
                            (h - 4, 2, 2), (2, h - 4, 2), (2, 2, h - 4)]
                    third = h // 3
                    if third >= 1 and h - 2 * third >= 1:
                        pats.append((third, third, h - 2 * third))
                    for (p1, p2, p3) in pats:
                        if min(p1, p2, p3) < 1 or p1 + p2 + p3 != h:
                            continue
                        counts = Counter({v1: p1, v2: p2, v3: p3})
                        if len(counts) != 3:
                            continue
                        C = p1 * v1 + p2 * v2 + p3 * v3
                        kA = band_kA(C, h)
                        ks = sorted({4, kA // 2, min(kA, 64)})
                        for k in (kk for kk in ks
                                  if 4 <= kk <= min(kA, 64)):
                            W, imps = improving_moves(counts, C, k)
                            if W is None:
                                continue
                            rows += 1
                            if not imps:
                                g = comb(C, k) << k
                                ratio = float(
                                    Fraction(2 * g * W[1], W[0] * W[0]))
                                none_cases.append(
                                    [ratio, v1, v2, v3, p1, p2, p3, k])
                            else:
                                # classify the drain move(s)
                                for (u, v) in imps[:1]:
                                    tag = ("mid-give" if u == v2 else
                                           "top-give" if u == v3 else
                                           "bot-give")
                                    tag += ("/mid-recv" if v == v2 else
                                            "/top-recv" if v == v3 else
                                            "/bot-recv")
                                    drain[tag] += 1
    out = {"configs": rows, "no_improver": none_cases[:30],
           "n_no_improver": len(none_cases),
           "first_drain_move_tags": dict(drain)}
    print(f"[A.2] {rows} three-value configs; NO improving move at "
          f"{len(none_cases)}; drain tags {dict(drain)}", flush=True)
    for row in none_cases[:10]:
        print("   THREE-VALUE LOCAL MAX:", row, flush=True)
    path = REPO / "logs" / "993_A2_threevalue.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
