"""The Ladder-Schur step and the global argmax: BOTH REFUTED as stated.

The hoped-for reduction was: (step) every Robin Hood transfer toward
balance increases the rung ratio

    W_{s-1}' W_{s+1}' / (W_s')^2  >=  W_{s-1} W_{s+1} / W_s^2 ,

hence (global) the ratio is maximized at the most balanced partition
of (C, h), reducing the ladder for all multisets to the certified
two-value families.  VERDICT (this script, exact arithmetic):

- The STEP claim is FALSE: violations at all rungs (mostly s >= 2,
  small k, but also s = 1), margins to -0.23.
- The GLOBAL claim is FALSE as stated: in roughly a fifth of
  exhaustive (C,h,k,s) cases the argmax partition is NOT the most
  balanced one (typically lopsided shapes like (1,1,c) at small k).
- BUT every argmax-not-balanced case has rung ratio <= ~0.43, far
  from binding.  Empirically: balanced dominates exactly where the
  ratio approaches 1 (the dangerous large-h corners); elsewhere
  everything is far below 1.  The usable reduction must be a
  THRESHOLD statement (e.g. ratio(multiset) <= max(ratio(balanced
  companion), 1/2)), not a Schur monotonicity.

Stages:
1. step probe, exhaustive: h in [3,5], C <= 18, all transfers, all
   band k (sampled), rungs s <= 3;
2. step probe, random: h in [3,9], c_i <= 14;
3. GLOBAL argmax scan, exhaustive: h in [3,5], C <= 20, ALL band k,
   per-rung argmax over ALL partitions vs the balanced one; records
   every argmax-not-balanced case with its ratio, and the maximum
   such ratio.

Output: logs/993_ladder_schur_step.json
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(993125)


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


def steps(cs):
    """All distinct transfers toward balance: indices (i,j) with
    c_i + 2 <= c_j, dedup by value pair."""
    seen = set()
    for i in range(len(cs)):
        for j in range(len(cs)):
            if cs[i] + 2 <= cs[j] and (cs[i], cs[j]) not in seen:
                seen.add((cs[i], cs[j]))
                yield i, j


def check_steps(cs, ks, smax, rows, viols):
    h = len(cs)
    for i, j in steps(cs):
        cs2 = list(cs)
        cs2[i] += 1
        cs2[j] -= 1
        for k in ks:
            W = profile(cs, k)
            W2 = profile(cs2, k)
            for s in range(1, min(smax, min(h, k) - 1) + 1):
                if W[s + 1] == 0 or W2[s + 1] == 0:
                    continue
                lhs = W2[s - 1] * W2[s + 1] * W[s] * W[s]
                rhs = W[s - 1] * W[s + 1] * W2[s] * W2[s]
                margin = float(Fraction(lhs - rhs, rhs)) if rhs else None
                rows.append(margin)
                if lhs < rhs:
                    viols.append([list(cs), [cs[i], cs[j]], k, s, margin])


def gen_multisets(C, h, lo=1):
    if h == 1:
        if C >= lo:
            yield (C,)
        return
    for first in range(lo, C // h + 1):
        for rest in gen_multisets(C - first, h - 1, first):
            yield (first,) + rest


def main():
    out = {}
    # 1. exhaustive small
    rows, viols, nm = [], [], 0
    for h in (3, 4, 5):
        for C in range(h + 2, 19):
            for cs in gen_multisets(C, h):
                nm += 1
                kA = band_kA(C, h)
                ks = sorted({2, 3, max(2, kA // 2), kA})
                ks = [k for k in ks if 2 <= k <= kA]
                check_steps(list(cs), ks, 3, rows, viols)
    out["exhaustive"] = {"multisets": nm, "steps_checked": len(rows),
                         "violations": viols[:50],
                         "n_violations": len(viols),
                         "min_margin": min(rows) if rows else None}
    print(f"[exhaustive] {nm} multisets, {len(rows)} step checks, "
          f"{len(viols)} violations, min margin "
          f"{min(rows) if rows else None:.3e}", flush=True)

    # 2. random larger
    rows2, viols2 = [], []
    for _ in range(300):
        h = random.randint(3, 9)
        cs = [random.randint(1, 14) for _ in range(h)]
        C = sum(cs)
        kA = band_kA(C, h)
        ks = [k for k in {2, 3, 5, 8, max(2, kA // 2), kA}
              if 2 <= k <= min(kA, 24)]
        check_steps(cs, sorted(ks), 4, rows2, viols2)
    out["random"] = {"steps_checked": len(rows2),
                     "violations": viols2[:50],
                     "n_violations": len(viols2),
                     "min_margin": min(rows2) if rows2 else None}
    print(f"[random] {len(rows2)} step checks, {len(viols2)} violations, "
          f"min margin {min(rows2) if rows2 else None:.3e}", flush=True)

    # 3. global argmax scan
    bad, ncase, worst_bad = [], 0, 0.0
    for h in (3, 4, 5):
        for C in range(h + 2, 21):
            kA = band_kA(C, h)
            for k in range(2, kA + 1):
                best = {}
                for p in gen_multisets(C, h):
                    W = profile(list(p), k)
                    for s in range(1, min(h, k)):
                        if s + 1 < len(W) and W[s + 1] > 0:
                            r = Fraction((s + 1) * W[s - 1] * W[s + 1],
                                         s * W[s] * W[s])
                            if s not in best or r > best[s][0]:
                                best[s] = (r, p)
                balanced = min(gen_multisets(C, h),
                               key=lambda p: sum(x * x for x in p))
                for s, (r, p) in best.items():
                    ncase += 1
                    if list(p) != list(balanced):
                        bad.append([C, h, k, s, list(p), list(balanced),
                                    float(r)])
                        worst_bad = max(worst_bad, float(r))
    out["global_argmax"] = {"cases": ncase, "argmax_not_balanced": len(bad),
                            "max_ratio_among_those": worst_bad,
                            "examples": bad[:60]}
    print(f"[global] {ncase} cases, argmax!=balanced in {len(bad)}, "
          f"max ratio among those {worst_bad:.4f}", flush=True)

    path = REPO / "logs" / "993_ladder_schur_step.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
