"""The window form: every transfer delta as uniform E/B-windows.

Corollary of the collapse lemma, verified exactly here.  With
Win_E(s, L) = sum_{m=s}^{s+L-1} E(m), Win_B analogous, and
m-hat_v = m_v - [v=u] - [v=w]:

  spread (u < w-? i.e. receiver above giver-1: u < w, w != u-1):
      d2(u,w)  = sum_v m-hat_v Win_E(v+u-1, w-u+1),
      d1(u,w)  = -Win_B(u-1, ...)+...: d1 = A(u-1)-A(w)
               = -Win_B(u-1, w-u+1) when w > u-1: NEGATIVE?  No:
      A(u-1) - A(w) = +Win_B(u-1, w-u+1) when u-1 < w i.e. always
      for spread (A decreasing, u-1 < w => A(u-1) > A(w)): d1 > 0.
  balance (u > w+1):
      |d2(u,w)| = sum_v m-hat_v Win_E(v+w, u-w-1),
      |d1(u,w)| = Win_B(w, u-w-1).

The general M1 leading form is then a comparison of window-sum
products at multiset-determined positions -- the per-window
generalization of the cross-level minor, with all sequences (E at
level k-4, B at level k-3) log-concave by Lemma y-LC.

Output: logs/993_window_form.json
"""
from __future__ import annotations
import json, random
from collections import Counter
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(99324001)

def f(alpha, beta, m):
    if m < 0 or beta < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))

def main():
    bad, n = [], 0
    for _ in range(300):
        h = random.randint(3, 10)
        counts = Counter(random.randint(1, 20) for _ in range(h))
        C = sum(v * m for v, m in counts.items())
        k = random.randint(5, max(5, min(C - 1, 50)))
        vmax = max(counts)
        L = 2 * vmax + 4
        yv = [f(m, C - m, k - 2) if m <= C else 0
              for m in range(L + 2)]
        dy = [yv[m] - yv[m + 1] for m in range(L + 1)]
        E = [dy[m] - dy[m + 1] for m in range(L)]
        Av = [f(t, C - t - 1, k - 2) for t in range(C + 1)]
        B = [Av[t] - Av[t + 1] for t in range(C)]
        WinE = lambda s, ln: sum(E[s:s + ln])
        WinB = lambda s, ln: sum(B[s:s + ln])
        Sy = lambda t: sum(m * dy[v + t] for v, m in counts.items())
        vals = sorted(counts)
        for u in vals:
            if u < 2:
                continue
            for w in vals:
                if u == w or w + 1 == u:
                    continue
                raw2 = (Sy(u - 1) - Sy(w)) - dy[2 * u - 1] \
                    - dy[u + w - 1] + dy[u + w] + dy[2 * w]
                raw1 = Av[u - 1] - Av[w]
                mhat = {v: m - (v == u) - (v == w)
                        for v, m in counts.items()}
                n += 1
                if u < w:        # spread
                    win2 = sum(m * WinE(v + u - 1, w - u + 1)
                               for v, m in mhat.items())
                    win1 = WinB(u - 1, w - u + 1)
                    ok = (raw2 == win2 and raw1 == win1)
                else:            # balance, u > w+1
                    win2 = -sum(m * WinE(v + w, u - w - 1)
                                for v, m in mhat.items())
                    win1 = -WinB(w, u - w - 1)
                    ok = (raw2 == win2 and raw1 == win1)
                if not ok:
                    bad.append([dict(counts), u, w, k])
    out = {"checked": n, "fails": bad[:20], "n_fails": len(bad)}
    print(f"[window form] {n} checks, {len(bad)} failures",
          flush=True)
    (REPO / "logs" / "993_window_form.json").write_text(
        json.dumps(out, indent=2))
    print("wrote logs/993_window_form.json", flush=True)

if __name__ == "__main__":
    main()
