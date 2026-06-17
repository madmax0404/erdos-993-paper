"""Local-maxima census for the rung-1 ratio over the transfer graph.

The variational route to DOM': characterize local maximizers of
ratio_1 at fixed (C, h, k) under single transfers.  RESULT (this
census, exact): in every tight case (ratio(bal) >= 0.7) the GLOBAL
maximizer is bal; the local maxima are rigid -- bal is usually
unique, and the only other local maxima (appearing only at the band
top k = kA) have the bulk-plus-giant form (a, a, ..., a, M), always
globally below bal.  Hence the DOM' proof program:

  A (exchange lemma): at a tight local maximum the multiset is
    adjacent-two-value or bulk+giant (first-order transfer
    conditions);
  B (giant comparison): the one-parameter bulk+giant family never
    beats bal when tight (canonical-pair comparison, like the
    band-bottom rho-bar).

Output: logs/993_locmax_census.json
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


def f(alpha, beta, m):
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def parts(C, h, lo=1):
    if h == 1:
        if C >= lo:
            yield (C,)
        return
    for first in range(lo, C // h + 1):
        for rest in parts(C - first, h - 1, first):
            yield (first,) + rest


def neighbors(p):
    out = set()
    h = len(p)
    for i in range(h):
        for j in range(h):
            if i != j and p[i] >= 2:
                q = list(p)
                q[i] -= 1
                q[j] += 1
                out.add(tuple(sorted(q)))
    out.discard(tuple(sorted(p)))
    return out


def is_bulk_giant(p):
    return len(set(p[:-1])) == 1 and p[-1] > p[0] + 1


def is_adj_two_value(p):
    return p[-1] - p[0] <= 1


def main():
    summary = []
    for h in (3, 4, 5):
        for C in (12, 16, 20, 24):
            kA = band_kA(C, h)
            for k in sorted({kA, 2 * kA // 3, kA // 2}):
                if k < 3:
                    continue
                x = [f(c, C - c, k - 1) for c in range(C + 1)]
                y = [f(m, C - m, k - 2) for m in range(C + 1)]
                g = comb(C, k) << k
                vals = {}
                for p in parts(C, h):
                    W1 = sum(x[c] for c in p)
                    W2 = sum(y[p[i] + p[j]] for i in range(h)
                             for j in range(i + 1, h))
                    if W1:
                        vals[p] = Fraction(2 * g * W2, W1 * W1)
                locmax = [p for p in vals
                          if all(vals[p] >= vals[q]
                                 for q in neighbors(p) if q in vals)]
                bal = tuple(sorted([C // h] * (h - C % h)
                                   + [C // h + 1] * (C % h)))
                globmax = max(vals, key=lambda p: vals[p])
                summary.append({
                    "C": C, "h": h, "k": k, "k_is_band_top": k == kA,
                    "ratio_bal": float(vals[bal]),
                    "tight": float(vals[bal]) >= 0.7,
                    "n_locmax": len(locmax),
                    "locmax": [list(p) for p in locmax],
                    "locmax_all_classified":
                        all(is_bulk_giant(p) or is_adj_two_value(p)
                            for p in locmax),
                    "globmax": list(globmax),
                    "glob_is_bal": globmax == bal})
    tight = [r for r in summary if r["tight"]]
    out = {
        "cases": len(summary), "tight_cases": len(tight),
        "tight_glob_always_bal": all(r["glob_is_bal"] for r in tight),
        "tight_locmax_always_classified":
            all(r["locmax_all_classified"] for r in tight),
        "tight_multi_locmax_only_at_band_top":
            all(r["k_is_band_top"] for r in tight if r["n_locmax"] > 1),
        "rows": summary}
    print(f"{len(summary)} cases, {len(tight)} tight; "
          f"glob==bal in all tight: {out['tight_glob_always_bal']}; "
          f"locmax classified (adj-2-value or bulk+giant) in all "
          f"tight: {out['tight_locmax_always_classified']}; "
          f"multi-locmax only at band top: "
          f"{out['tight_multi_locmax_only_at_band_top']}", flush=True)
    path = REPO / "logs" / "993_locmax_census.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
