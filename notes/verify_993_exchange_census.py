"""Exchange census at scale: classify local maximizers of the rung-1
ratio over the transfer graph.

The reshaped architecture (logs/993_giant_vs_bal.json) rests on the
exchange lemma: every local maximizer with ratio >= theta_0 is
adjacent-two-value (max - min <= 1) or bulk+giant (a^{h-1}, M),
M >= a+2.  The exhaustive census (h <= 5, C <= 24) saw exactly
these.  This census stress-tests the classification at scale by
exact hill-climbing (first-improvement over single transfers, with
grouped incremental updates), from seeded and random starts.  Any
tight OTHER endpoint (ratio >= 0.7 outside the two shapes) is the
headline finding and reshapes Lemma A.

Output: logs/993_exchange_census.json
"""

from __future__ import annotations

import json
import random
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(99316001)


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


def classify(counts):
    vals = sorted(counts)
    if vals[-1] - vals[0] <= 1:
        return "adjacent_two_value"
    if len(vals) == 2 and counts[vals[0]] == sum(counts.values()) - 1:
        return "bulk_giant"
    return "OTHER"


def climb(start, x, y, h):
    counts = Counter(start)
    W1 = sum(m * x[v] for v, m in counts.items())
    W2 = 0
    vals = sorted(counts)
    for i, v in enumerate(vals):
        if counts[v] >= 2:
            W2 += comb(counts[v], 2) * y[2 * v]
        for w in vals[i + 1:]:
            W2 += counts[v] * counts[w] * y[v + w]

    def delta(ci, cj):
        dW1 = (x[ci + 1] - x[ci]) + (x[cj - 1] - x[cj])
        dW2 = y[ci + 1 + cj - 1] - y[ci + cj]
        for v, m in counts.items():
            mv = m - (v == ci) - (v == cj)
            if mv:
                dW2 += mv * ((y[v + ci + 1] - y[v + ci])
                             + (y[v + cj - 1] - y[v + cj]))
        return dW1, dW2

    improved = True
    steps = 0
    while improved and steps < 6000:
        improved = False
        pres = sorted(counts)
        cands = [(ci, cj) for ci in pres for cj in pres
                 if cj >= 2 and cj != ci + 1
                 and not (ci == cj and counts[ci] < 2)]
        random.shuffle(cands)
        for ci, cj in cands:
            dW1, dW2 = delta(ci, cj)
            nW1, nW2 = W1 + dW1, W2 + dW2
            if nW1 > 0 and nW2 * W1 * W1 > W2 * nW1 * nW1:
                counts[ci] -= 1
                counts[cj] -= 1
                counts[ci + 1] += 1
                counts[cj - 1] += 1
                for v in (ci, cj, ci + 1, cj - 1):
                    if counts[v] == 0:
                        del counts[v]
                W1, W2 = nW1, nW2
                improved = True
                steps += 1
                break
    return counts, W1, W2


def main():
    rows, others_tight = [], []
    combos = []
    for h in (6, 10, 16, 24):
        for mult in (2, 4, 8):
            C = h * mult
            if C > 128:
                continue
            kA = band_kA(C, h)
            ks = sorted({4, kA // 2, 3 * kA // 4, min(kA, 64)})
            for k in (kk for kk in ks if 4 <= kk <= min(kA, 64)):
                combos.append((C, h, k))
    for (C, h, k) in combos:
        x = [f(c, C - c, k - 1) for c in range(C + 1)]
        y = [f(m, C - m, k - 2) for m in range(C + 1)]
        g = comb(C, k) << k
        a0, r = divmod(C, h)
        starts = [[a0] * (h - r) + [a0 + 1] * r,
                  [1] * (h - 1) + [C - h + 1]]
        for a in range(1, min(6, (C - 2) // h) + 1):
            M = C - (h - 1) * a
            if M >= a + 2:
                starts.append([a] * (h - 1) + [M])
        for _ in range(12):
            cs = [1] * h
            for _ in range(C - h):
                cs[random.randrange(h)] += 1
            starts.append(cs)
        seen = set()
        for st in starts:
            counts, W1, W2 = climb(st, x, y, h)
            key = tuple(sorted(counts.elements()))
            if key in seen or W1 == 0:
                continue
            seen.add(key)
            ratio = float(Fraction(2 * g * W2, W1 * W1))
            cls = classify(counts)
            rows.append([ratio, cls, C, h, k])
            if cls == "OTHER" and ratio >= 0.7:
                others_tight.append([ratio, list(key), C, h, k])
    cnt = Counter(r[1] for r in rows)
    tight = [r for r in rows if r[0] >= 0.7]
    cnt_tight = Counter(r[1] for r in tight)
    out = {"combos": len(combos), "distinct_local_maxima": len(rows),
           "class_counts": dict(cnt),
           "tight_local_maxima": len(tight),
           "tight_class_counts": dict(cnt_tight),
           "tight_OTHER": others_tight[:40],
           "n_tight_OTHER": len(others_tight)}
    print(f"[census] {len(combos)} combos, {len(rows)} distinct local "
          f"maxima; classes {dict(cnt)}; tight: {len(tight)} classes "
          f"{dict(cnt_tight)}; tight OTHER: {len(others_tight)}",
          flush=True)
    for row in others_tight[:10]:
        print("   TIGHT OTHER:", row, flush=True)
    path = REPO / "logs" / "993_exchange_census.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
