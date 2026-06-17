"""A.1 general gap: probe the regrouped expansion's structure.

The general-gap CORE regrouping (proved identity):

  LHS - RHS = p sum_t D_t + (q-2) sum_t D'_t
              + B(M-1) sum_j [E(2v+j) - E(v+M+j)],

t in [v, M-2], j in [0, d-2], d = M - v >= 2.  Structure claims to
verify before proving (the gap-2 pipeline, one level up):

1. t-interval: the per-t deficit condition is monotone -- D_t < 0
   only on an upper interval [t*, M-2] (and similarly D'_t);
2. aggregated compensation: the total negative part
   p sum |D_t|^- + (q-2) sum |D'_t|^- never exceeds a fraction
   theta < 1 of the positive term, across all gaps (the gap-2
   worst was 0.133);
3. margins by d: how does the worst compensation ratio scale with
   the gap d (expect improvement: telescoping slack grows);
4. the exact CORE (general gap) never fails (re-verification at
   wider gaps than the original probe).

Output: logs/993_A1_generalgap.json
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


def main():
    interval_bad, core_fail = [], []
    worst_comp = None
    by_d = {}
    n = 0
    for h in (4, 6, 8, 12, 16, 24, 40):
        for v in (1, 2, 3, 4, 6, 10):
            for d in (2, 3, 4, 6, 8, 12, 20, 32):
                M = v + d
                for q in (2, 3, min(6, h - 1)):
                    if not 2 <= q <= h - 1:
                        continue
                    p = h - q
                    C = p * v + q * M
                    kA = band_kA(C, h)
                    ks = sorted({6, 8, kA // 2, 3 * kA // 4,
                                 min(kA, 80)})
                    for k in (kk for kk in ks
                              if 6 <= kk <= min(kA, 80)):
                        n += 1
                        B = {t: f(t, C - t - 2, k - 3)
                             for t in range(v, M)}
                        E = {m: f(m, C - m - 2, k - 4)
                             for m in range(2 * v, 2 * M)}
                        EvM1, E2M1 = E[v + M - 1], E[2 * M - 1]
                        BM1 = B[M - 1]
                        Dts = [EvM1 * B[t] - E[v + t] * BM1
                               for t in range(v, M - 1)]
                        Dps = [E2M1 * B[t] - E[t + M] * BM1
                               for t in range(v, M - 1)]
                        # 1. interval structure
                        for seq in (Dts, Dps):
                            signs = [x < 0 for x in seq]
                            # negatives must form a suffix
                            if any(signs[i] and not signs[i + 1]
                                   for i in range(len(signs) - 1)):
                                interval_bad.append([h, p, q, v, d, k])
                                break
                        # 2. aggregated compensation
                        neg = p * sum(max(0, -x) for x in Dts) \
                            + (q - 2) * sum(max(0, -x) for x in Dps)
                        pos = BM1 * sum(E[2 * v + j] - E[v + M + j]
                                        for j in range(d - 1))
                        if pos > 0:
                            ratio = float(Fraction(neg, pos))
                            rec = by_d.setdefault(d, [0.0, 0])
                            rec[1] += 1
                            if ratio > rec[0]:
                                rec[0] = ratio
                            if worst_comp is None or \
                                    ratio > worst_comp[0]:
                                worst_comp = [ratio, h, p, q, v, d, k]
                        # 4. exact CORE
                        lhs = (p * EvM1 + (q - 2) * E2M1) \
                            * sum(B[t] for t in range(v, M - 1))
                        rhs = ((p - 1) * sum(E[m] for m in
                                             range(2 * v, v + M - 1))
                               + (q - 1) * sum(E[m] for m in
                                               range(v + M, 2 * M - 1))
                               ) * BM1
                        if lhs <= rhs:
                            core_fail.append([h, p, q, v, d, k])
    out = {"configs": n,
           "interval_structure_violations": interval_bad[:20],
           "n_interval_bad": len(interval_bad),
           "worst_compensation": worst_comp,
           "compensation_by_gap":
               {str(d): {"max_ratio": rec[0], "cases": rec[1]}
                for d, rec in sorted(by_d.items())},
           "core_failures": core_fail[:20],
           "n_core_failures": len(core_fail)}
    print(f"[general-gap] {n} configs; interval violations "
          f"{len(interval_bad)}; CORE failures {len(core_fail)}; "
          f"worst compensation {worst_comp}", flush=True)
    print("compensation by gap d:",
          {d: round(rec[0], 4) for d, rec in sorted(by_d.items())},
          flush=True)
    path = REPO / "logs" / "993_A1_generalgap.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
