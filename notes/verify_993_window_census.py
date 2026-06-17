"""Window census: the value-window does NOT control the rung ratio.

The third candidate shortcut for the threshold reduction was a
window lemma: "if max c_i - min c_i >= w0 then ratio <= theta < 1",
which would reduce the high regime to few-value families.  FALSE:
a single far-out arm inside a large near-balanced bulk barely moves
the ratio (the bulk dominates).  Witnesses at h = 60: window 7-8
multisets (1-bulk plus one arm of degree 8 or 9) reach ratio 0.944;
window 10-15 at h = 12 reach 0.89.  The ratio is governed by the
bulk, not the spread.

This script records max observed rung ratio per window width over:
exhaustive partitions (h in [3,6], C <= 24), 400 random multisets
(h <= 12, c_i <= 16), and large-h shaped families (h in {20,40,60}:
two-value bulks plus controlled outliers).

Conclusion logged for the program record: after Schur-walk
(transfer monotonicity), conditional walk (theta*), and window, all
three structural shortcuts are refuted; the surviving open lemma is
endpoint domination (DOM): ratio_s(c,k) >= theta0 implies
ratio_s(c,k) <= ratio_s(bal(C,h),k).

Output: logs/993_window_census.json
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(424242)


def band_kA(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(lBG - 1, k0 - 1, C - 1)


def profile(cs, k):
    cur = {0: [1] + [0] * k}
    for c in cs:
        E = [(comb(c, m) << m) if m <= c else 0 for m in range(k + 1)]
        B = [comb(c, m - 1) if 1 <= m <= c + 1 else 0 for m in range(k + 1)]
        new = {}
        for s, arr in cur.items():
            for ds, pol in ((0, E), (1, B)):
                tgt = new.setdefault(s + ds, [0] * (k + 1))
                for i, ai in enumerate(arr):
                    if ai:
                        for j in range(k + 1 - i):
                            if pol[j]:
                                tgt[i + j] += ai * pol[j]
        cur = new
    return [cur[s][k] if s in cur else 0
            for s in range(min(len(cs), k) + 1)]


def maxrung(cs, k, smax=4):
    W = profile(cs, k)
    best = 0.0
    for s in range(1, min(smax, len(W) - 2) + 1):
        if W[s + 1] > 0:
            best = max(best, float(Fraction((s + 1) * W[s - 1] * W[s + 1],
                                            s * W[s] * W[s])))
    return best


def parts(C, h, lo=1):
    if h == 1:
        if C >= lo:
            yield (C,)
        return
    for first in range(lo, C // h + 1):
        for rest in parts(C - first, h - 1, first):
            yield (first,) + rest


def main():
    best = {}

    def feed(cs, k):
        w = max(cs) - min(cs)
        r = maxrung(list(cs), k)
        if w not in best or r > best[w][0]:
            best[w] = (r, sorted(cs), k)

    for h in (3, 4, 5, 6):
        for C in range(h + 2, 25):
            kA = band_kA(C, h)
            for p in parts(C, h):
                for k in sorted({3, kA // 2, kA}):
                    if 2 <= k <= kA:
                        feed(p, k)
    for _ in range(400):
        h = random.randint(3, 12)
        cs = [random.randint(1, 16) for _ in range(h)]
        kA = band_kA(sum(cs), h)
        for k in sorted({3, kA // 2, kA}):
            if 2 <= k <= kA:
                feed(cs, k)
    for h in (20, 40, 60):
        shapes = [[1] * (h // 2) + [2] * (h // 2),
                  [1] * (h - 4) + [2, 2, 3, 3],
                  [1] * (h - 3) + [2, 3, 4],
                  [1] * (h - 2) + [3, 5],
                  [1] * (h - 2) + [2, 8],
                  [1] * (h - 1) + [9],
                  [2] * (h - 2) + [3, 4],
                  [1] * (h - 4) + [2, 2, 2, 6]]
        for cs in shapes:
            kA = band_kA(sum(cs), h)
            for k in sorted({3, 6, kA // 2, kA}):
                if 2 <= k <= kA:
                    feed(cs, k)

    table = {str(w): {"max_ratio": best[w][0],
                      "multiset": best[w][1] if len(best[w][1]) <= 12
                      else [best[w][1][0], best[w][1][-1],
                            len(best[w][1]), sum(best[w][1])],
                      "k": best[w][2]}
             for w in sorted(best)}
    out = {"max_ratio_by_window": table,
           "verdict": "window does NOT control ratio: window 7-8 reaches "
                      "0.944 at h=60 (1-bulk + one outlier); shortcut dead"}
    for w in sorted(best):
        print(f"window {w}: {best[w][0]:.4f}", flush=True)
    path = REPO / "logs" / "993_window_census.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
