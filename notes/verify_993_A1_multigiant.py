"""Sub-lemma A.1 (multi-giant kill): statement-pinning probe.

Lemma A's two-value case: a config (v^p, M^q) with M >= v+2 violates
the classification iff q >= 2 (q = 1 IS bulk+giant).  A.1 claims no
tight such config is a local maximum, and the census suggests the
improving move is one of:

  T1 (giant-giant spread): (M, M) -> (M-1, M+1)
      dW1 = A(M-1) - A(M) >= 0,
      dW2 = p D2y(v+M-1) + (q-2) D2y(2M-1) >= 0,
  T2 (pair balance):       (v, M) -> (v+1, M-1)
      dW1 = A(M-1) - A(v) <= 0,
      dW2 = (p-1)[dy(v+M-1) - dy(2v)]
            + (q-1)[dy(2M-1) - dy(v+M)] <= 0,

with A(t) = f(t,C-t-1,k-2), dy(m) = f(m,C-m-1,k-3),
D2y(m-1) = dy(m-1) - dy(m) = f(m-1, C-m-1, k-4).
Improvement is the exact test (W2+dW2) W1^2 > W2 (W1+dW1)^2.

This probe sweeps (v, M, p, q, k) exactly:
- closed-form sanity of dW1/dW2 against direct recomputation;
- for every tight config (ratio >= 0.65): does T1 or T2 improve?
  record which, and any config where NEITHER does (a counterexample
  to A.1's dichotomy -- would mean another move carries the kill);
- the improving-move map as a function of the parameters (for the
  proof's case split).

Output: logs/993_A1_multigiant.json
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


def masses(v, M, p, q, C, k):
    x_v = f(v, C - v, k - 1)
    x_M = f(M, C - M, k - 1)
    W1 = p * x_v + q * x_M
    W2 = (comb(p, 2) * f(2 * v, C - 2 * v, k - 2)
          + p * q * f(v + M, C - v - M, k - 2)
          + comb(q, 2) * f(2 * M, C - 2 * M, k - 2))
    return W1, W2


def improves(W1, W2, dW1, dW2):
    nW1, nW2 = W1 + dW1, W2 + dW2
    return nW1 > 0 and nW2 * W1 * W1 > W2 * nW1 * nW1


def main():
    rows, neither, sanity_bad = [], [], 0
    checked = 0
    for h in (4, 6, 8, 12, 16, 24, 40):
        for v in (1, 2, 3, 4, 6):
            for gap in (2, 3, 4, 6, 10, 20):
                M = v + gap
                for q in range(2, min(h - 1, 6) + 1):
                    p = h - q
                    C = p * v + q * M
                    kA = band_kA(C, h)
                    ks = sorted({4, kA // 2, 3 * kA // 4, min(kA, 80)})
                    for k in (kk for kk in ks if 4 <= kk <= min(kA, 80)):
                        A = lambda t: f(t, C - t - 1, k - 2)
                        dy = lambda m: f(m, C - m - 1, k - 3)
                        W1, W2 = masses(v, M, p, q, C, k)
                        if W1 == 0:
                            continue
                        g = comb(C, k) << k
                        ratio = float(Fraction(2 * g * W2, W1 * W1))
                        # closed-form deltas
                        d1W1 = A(M - 1) - A(M)
                        d1W2 = (p * (dy(v + M - 1) - dy(v + M))
                                + (q - 2) * (dy(2 * M - 1) - dy(2 * M)))
                        d2W1 = A(M - 1) - A(v)
                        d2W2 = ((p - 1) * (dy(v + M - 1) - dy(2 * v))
                                + (q - 1) * (dy(2 * M - 1) - dy(v + M)))
                        # sanity vs direct recomputation (spread + balance)
                        Ws1 = masses_after_spread = None
                        # direct: spread (M,M)->(M-1,M+1)
                        xs = {t: f(t, C - t, k - 1)
                              for t in {v, M - 1, M, M + 1, v + 1}}
                        # build directly
                        def direct(parts):
                            W1d = sum(xs.get(t) or f(t, C - t, k - 1)
                                      for t in parts)
                            W2d = 0
                            for i in range(len(parts)):
                                for j in range(i + 1, len(parts)):
                                    W2d += f(parts[i] + parts[j],
                                             C - parts[i] - parts[j],
                                             k - 2)
                            return W1d, W2d
                        if C <= 260:  # sanity only on small cases
                            base = [v] * p + [M] * q
                            sp = [v] * p + [M - 1, M + 1] + [M] * (q - 2)
                            ba = [v] * (p - 1) + [v + 1, M - 1] \
                                + [M] * (q - 1)
                            W1d, W2d = direct(base)
                            s1, s2 = direct(sp)
                            b1, b2 = direct(ba)
                            if (W1d, W2d) != (W1, W2) or \
                               (s1 - W1d, s2 - W2d) != (d1W1, d1W2) or \
                               (b1 - W1d, b2 - W2d) != (d2W1, d2W2):
                                sanity_bad += 1
                        checked += 1
                        if ratio < 0.65:
                            continue
                        t1 = improves(W1, W2, d1W1, d1W2)
                        t2 = improves(W1, W2, d2W1, d2W2)
                        rows.append([ratio, v, M, p, q, k,
                                     bool(t1), bool(t2)])
                        if not (t1 or t2):
                            neither.append([ratio, v, M, p, q, k])
    from collections import Counter
    which = Counter(("T1" if r[6] else "") + ("T2" if r[7] else "")
                    for r in rows)

    # CORE inequality stage: at every config (no tightness filter),
    #   LHS = dW2^(1) * |dW1^(2)|   vs   RHS = |dW2^(2)| * dW1^(1):
    # CORE claims LHS > RHS (this + quadratic bookkeeping => A.1).
    core_fail, core_min = [], None
    for h in (4, 6, 8, 12, 16, 24, 40):
        for v in (1, 2, 3, 4, 6):
            for gap in (2, 3, 4, 6, 10, 20):
                M = v + gap
                for q in range(2, min(h - 1, 6) + 1):
                    p = h - q
                    C = p * v + q * M
                    kA = band_kA(C, h)
                    ks = sorted({4, kA // 2, 3 * kA // 4, min(kA, 80)})
                    for k in (kk for kk in ks if 4 <= kk <= min(kA, 80)):
                        A_ = lambda t: f(t, C - t - 1, k - 2)
                        dy = lambda m: f(m, C - m - 1, k - 3)
                        d1W1 = A_(M - 1) - A_(M)
                        d1W2 = (p * (dy(v + M - 1) - dy(v + M))
                                + (q - 2) * (dy(2 * M - 1) - dy(2 * M)))
                        a2 = A_(v) - A_(M - 1)
                        d2W2a = ((p - 1) * (dy(2 * v) - dy(v + M - 1))
                                 + (q - 1) * (dy(v + M) - dy(2 * M - 1)))
                        lhs = d1W2 * a2
                        rhs = d2W2a * d1W1
                        if lhs <= rhs:
                            core_fail.append([v, M, p, q, k])
                        if rhs > 0:
                            r_ = float(Fraction(lhs, rhs))
                            if core_min is None or r_ < core_min[0]:
                                core_min = [r_, v, M, p, q, k]
    print(f"[CORE] fails: {len(core_fail)}; min LHS/RHS ratio: "
          f"{core_min}", flush=True)

    out = {"configs_checked": checked, "sanity_mismatches": sanity_bad,
           "tight_configs": len(rows),
           "improver_counts": dict(which),
           "neither_improves": neither[:30],
           "n_neither": len(neither),
           "core": {"fails": core_fail[:30], "n_fails": len(core_fail),
                    "min_ratio": core_min}}
    print(f"[A.1] {checked} configs, sanity mismatches {sanity_bad}; "
          f"tight {len(rows)}; improvers {dict(which)}; "
          f"NEITHER: {len(neither)}", flush=True)
    for row in neither[:8]:
        print("   NEITHER:", row, flush=True)
    path = REPO / "logs" / "993_A1_multigiant.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
