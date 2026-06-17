"""The threshold landscape: pinning the correct reduction statement.

After the Ladder-Schur refutation, the open reduction must be a
threshold statement.  Candidate form:

    (T)  ratio_s(c, k) <= max( ratio_s(bal(C,h), k), c0 )

for every multiset c with sum C and h parts, where bal(C,h) is the
balanced two-value partition and c0 < 1 an absolute constant.  This
scan answers, exactly:

1. Over exhaustive partition spaces (h in [3,6], C <= 24, every band
   k, rungs s <= 4): the max over partitions of
   [ratio_s(c,k) - ratio_s(bal,k)]_+ , the max ratio among
   non-balanced-dominated cases (the empirical c0), and where
   (h, C, k, s) those live.
2. The high-ratio census: every exhaustive case with
   ratio_s(c,k) >= 0.7 -- is c always two-value (hence certified),
   and is it always dominated by bal?
3. Large-h spot checks along the dangerous direction ((1^p,2^q) and
   neighbors with a few 3's), h up to 40: does balanced dominance
   hold whenever ratio >= 0.7?

Output: logs/993_threshold_landscape.json
"""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


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


def rungs(cs, k, smax):
    W = profile(cs, k)
    out = {}
    for s in range(1, min(smax, len(W) - 2) + 1):
        if W[s + 1] > 0:
            out[s] = Fraction((s + 1) * W[s - 1] * W[s + 1],
                              s * W[s] * W[s])
    return out


def parts(C, h, lo=1):
    if h == 1:
        if C >= lo:
            yield (C,)
        return
    for first in range(lo, C // h + 1):
        for rest in parts(C - first, h - 1, first):
            yield (first,) + rest


def balanced(C, h):
    a, r = divmod(C, h)
    return [a] * (h - r) + [a + 1] * r


def main():
    out = {}

    # 1+2. exhaustive landscape
    max_excess = None          # max ratio(c) - ratio(bal) over all cases
    c0_cases = []              # cases where c beats bal: (ratio, ...)
    high_census = []           # all cases with ratio >= 0.7
    ncase = 0
    for h in (3, 4, 5, 6):
        for C in range(h + 2, 25):
            kA = band_kA(C, h)
            bal = balanced(C, h)
            for k in range(2, kA + 1):
                rb = rungs(bal, k, 4)
                for p in parts(C, h):
                    rc = rungs(list(p), k, 4)
                    for s, r in rc.items():
                        ncase += 1
                        fr = float(r)
                        if fr >= 0.7:
                            high_census.append(
                                [fr, list(p), C, h, k, s,
                                 len(set(p)) <= 2,
                                 s in rb and r <= rb[s]])
                        if s in rb and r > rb[s]:
                            exc = float(r - rb[s])
                            c0_cases.append([fr, exc, list(p), C, h, k, s])
                            if max_excess is None or exc > max_excess[0]:
                                max_excess = [exc, fr, list(p), C, h, k, s]
    c0_cases.sort(key=lambda z: -z[0])
    out["exhaustive"] = {
        "cases": ncase,
        "n_beats_balanced": len(c0_cases),
        "max_ratio_when_beating_balanced":
            c0_cases[0][0] if c0_cases else None,
        "max_excess_over_balanced": max_excess,
        "top_beating_cases": c0_cases[:25],
        "n_high_ratio": len(high_census),
        "high_ratio_all_twovalue":
            all(row[6] for row in high_census) if high_census else True,
        "high_ratio_all_bal_dominated":
            all(row[7] for row in high_census) if high_census else True,
        "high_census_sample": high_census[:25]}
    print(f"[exhaustive] {ncase} cases; beats-balanced: {len(c0_cases)} "
          f"(max ratio among them "
          f"{c0_cases[0][0] if c0_cases else None}); "
          f"high(>=0.7): {len(high_census)}, all two-value: "
          f"{out['exhaustive']['high_ratio_all_twovalue']}, "
          f"all bal-dominated: "
          f"{out['exhaustive']['high_ratio_all_bal_dominated']}",
          flush=True)

    # 3. large-h spot checks: (1^p, 2^q) neighborhoods, h to 40
    rows = []
    for h in (12, 20, 30, 40):
        for q in (2, h // 3, h // 2, h - 2):
            base = [1] * (h - q) + [2] * q
            C = sum(base)
            kA = band_kA(C, h)
            ks = sorted({3, 5, kA // 2, kA})
            variants = {
                "balanced(two-value)": base,
                "one-three": sorted([1] * (h - q + 1) + [2] * (q - 2) + [3]),
                "spread": sorted([1] * (h - q + 2) + [2] * (q - 4) +
                                 [3, 3]) if q >= 4 else None,
                "heavy-tail": sorted([1] * (h - 2) + [C - h + 1 - 1, 2])
                if C - h - 1 >= 3 else None,
            }
            for k in ks:
                if not (2 <= k <= kA):
                    continue
                rb = rungs(base, k, 3)
                for name, cs in variants.items():
                    if cs is None or sum(cs) != C or len(cs) != h:
                        continue
                    rc = rungs(cs, k, 3)
                    for s, r in rc.items():
                        dom = (s in rb and r <= rb[s])
                        rows.append([float(r), name, h, q, k, s, dom])
    viol = [row for row in rows
            if row[0] >= 0.7 and row[1] != "balanced(two-value)"
            and not row[6]]
    mx = max((row[0] for row in rows if row[1] != "balanced(two-value)"),
             default=None)
    out["large_h"] = {"checked": len(rows),
                      "max_nonbalanced_ratio": mx,
                      "high_not_dominated": viol[:25],
                      "n_high_not_dominated": len(viol)}
    print(f"[large-h] {len(rows)} rows; max non-balanced ratio {mx}; "
          f"high-and-not-dominated: {len(viol)}", flush=True)

    path = REPO / "logs" / "993_threshold_landscape.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
