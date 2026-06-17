"""Systematic maximizer census at extreme parameters (Lemma A').

After the ninth/tenth refutations, the corrected conjecture is the
TWO-CLUSTER classification: every tight local maximizer of the
rung-1 ratio has values within {a, a+1} union {b, b+1}.  Today's
lesson: census the extreme-parameter landscape BEFORE proof
investment.  This census hill-climbs (exact, first-improvement,
value-grouped) at C up to 720 and k up to the band top, from seeds
including all shapes that have ever appeared as maxima:

  bal, spread extreme, bulk+giant (several a), bulk+two-giants,
  bulk+near-equal giant pairs, two-cluster splits, random.

Endpoints are classified: one_cluster (adjacent two-value),
two_cluster (values in {a,a+1} union {b,b+1} with b >= a+2), or
OTHER.  Any tight OTHER is the headline finding.

Output: logs/993_maximizer_census.json
"""

from __future__ import annotations

import json
import random
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(99320001)


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
        return "one_cluster"
    # try all splits into low cluster / high cluster
    for cut in range(1, len(vals)):
        lo, hi = vals[:cut], vals[cut:]
        if lo[-1] - lo[0] <= 1 and hi[-1] - hi[0] <= 1 \
                and hi[0] - lo[-1] >= 2:
            return "two_cluster"
    return "OTHER"


def climb(start, x, y):
    counts = Counter(start)
    vals = sorted(counts)
    W1 = sum(counts[v] * x[v] for v in vals)
    W2 = 0
    for i, v in enumerate(vals):
        if counts[v] >= 2:
            W2 += comb(counts[v], 2) * y[2 * v]
        for w in vals[i + 1:]:
            W2 += counts[v] * counts[w] * y[v + w]

    def delta(ci, cj):
        dW1 = (x[ci + 1] - x[ci]) + (x[cj - 1] - x[cj])
        dW2 = 0
        for v, m in counts.items():
            mv = m - (v == ci) - (v == cj)
            if mv:
                dW2 += mv * ((y[v + ci + 1] - y[v + ci])
                             + (y[v + cj - 1] - y[v + cj]))
        return dW1, dW2

    steps, improved = 0, True
    while improved and steps < 8000:
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
    for h in (8, 16, 24, 40):
        for mult in (2, 4, 8, 16):
            C = h * mult
            if C > 720:
                continue
            kA = band_kA(C, h)
            ks = sorted({kA // 2, 3 * kA // 4, 5 * kA // 6,
                         min(kA, 400)})
            for k in (kk for kk in ks if 8 <= kk <= min(kA, 400)):
                combos.append((C, h, k))
    for (C, h, k) in combos:
        x = [f(c, C - c, k - 1) for c in range(C + 1)]
        y = [f(m, C - m, k - 2) for m in range(min(2 * C, C) + 1)]
        # pair sums never exceed C in a valid multiset
        g = comb(C, k) << k
        a0, r0 = divmod(C, h)
        starts = [[a0] * (h - r0) + [a0 + 1] * r0,
                  [1] * (h - 1) + [C - h + 1]]
        for a in (1, 2, 4, a0 // 2, a0 - 2):
            if a < 1:
                continue
            M = C - (h - 1) * a
            if M >= a + 2:
                starts.append([a] * (h - 1) + [M])
            # two giants
            M2 = (C - (h - 2) * a)
            if M2 >= 2 * (a + 2) and M2 % 2 == 0:
                starts.append([a] * (h - 2) + [M2 // 2, M2 // 2])
            # near-equal giant pair
            if M2 >= 2 * a + 5:
                starts.append([a] * (h - 2)
                              + [(M2 - 1) // 2, M2 - (M2 - 1) // 2])
        for _ in range(8):
            cs = [1] * h
            for _ in range(C - h):
                cs[random.randrange(h)] += 1
            starts.append(cs)
        seen = set()
        for st in starts:
            if sum(st) != C or len(st) != h or min(st) < 1:
                continue
            counts, W1, W2 = climb(st, x, y)
            key = tuple(sorted(counts.elements()))
            if key in seen or W1 == 0:
                continue
            seen.add(key)
            ratio = float(Fraction(2 * g * W2, W1 * W1))
            cls = classify(counts)
            rows.append([ratio, cls, C, h, k])
            if cls == "OTHER" and ratio >= 0.7:
                others_tight.append([ratio, list(key)[:12],
                                     len(key), C, h, k])
    cnt = Counter(r[1] for r in rows)
    tight = [r for r in rows if r[0] >= 0.7]
    cnt_t = Counter(r[1] for r in tight)
    out = {"combos": len(combos), "distinct_maxima": len(rows),
           "classes": dict(cnt), "tight": len(tight),
           "tight_classes": dict(cnt_t),
           "tight_OTHER": others_tight[:40],
           "n_tight_OTHER": len(others_tight)}
    print(f"[census-XL] {len(combos)} combos, {len(rows)} distinct "
          f"maxima; classes {dict(cnt)}; tight classes {dict(cnt_t)}; "
          f"tight OTHER: {len(others_tight)}", flush=True)
    for row in others_tight[:8]:
        print("   TIGHT OTHER:", row, flush=True)
    path = REPO / "logs" / "993_maximizer_census.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
