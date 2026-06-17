"""The band-bottom reduction: rho(c) <= rho-bar(C,h,k,s) via W-Schur.

LEMMA (BB-reduction; immediate from W-Schur).  For every multiset c
with sum C and h parts, every k, s:

    rho_s(c,k) <= rho-bar(C,h,k,s)
               := (s+1) W_{s-1}(ext) W_{s+1}(ext) / (s W_s(bal)^2),

where ext = (1^{h-1}, C-h+1) majorizes every multiset and
bal = bal(C,h) is majorized by every multiset: the numerator masses
are bounded above at ext and the denominator below at bal, each by
Lemma W-Schur.  At k-s = 1, W_s and W_{s+1} are partition-free, so
rho-bar = rho(ext) exactly.

The BAND-BOTTOM LEMMA then reduces to the explicit two-canonical-
multiset inequality "rho-bar <= theta_bb < 1 at k-s <= 2", whose
k-s = 1 large-C asymptote is (2 - 1.5 lam)/(2 - lam)^2 <= 9/16
(lam = (s-1)/h).

This script, exact arithmetic throughout:
1. sanity: rho(c) <= rho-bar on random multisets (the three Schur
   applications);
2. maps rho-bar at k-s in {1,2}: h <= 60, all/sampled s, C sampled
   to 2000, in-band k only; records the global max and the
   asymptote agreement at k-s = 1;
3. curiosity map at k-s in {3,4}: where does rho-bar cross 1 (i.e.
   how far does the elementary reduction reach)?

Output: logs/993_bandbottom.json
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(993151)


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


def W_ext(C, h, s, k):
    """Class mass W_s of ext = (1^{h-1}, C-h+1): big slot in or out."""
    b = C - h + 1
    tot = 0
    for ib in (0, 1):
        j = s - ib
        if j < 0 or j > h - 1:
            continue
        alpha = j + ib * b
        beta = (h - 1 - j) + (1 - ib) * b
        tot += comb(h - 1, j) * f(alpha, beta, k - s)
    return tot


def W_bal(C, h, s, k):
    a, r = divmod(C, h)
    p, q = h - r, r          # p slots of a, q slots of a+1
    tot = 0
    for i in range(min(p, s) + 1):
        j = s - i
        if j < 0 or j > q:
            continue
        alpha = i * a + j * (a + 1)
        beta = (p - i) * a + (q - j) * (a + 1)
        tot += comb(p, i) * comb(q, j) * f(alpha, beta, k - s)
    return tot


def rho_bar(C, h, k, s):
    num = (s + 1) * W_ext(C, h, s - 1, k) * W_ext(C, h, s + 1, k)
    den = s * W_bal(C, h, s, k) ** 2
    if den == 0:
        return None
    return Fraction(num, den)


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


def main():
    out = {}

    # 1. sanity: rho(c) <= rho-bar
    fails, n = [], 0
    for _ in range(250):
        h = random.randint(3, 9)
        cs = [random.randint(1, 12) for _ in range(h)]
        C = sum(cs)
        kA = band_kA(C, h)
        if kA < 2:
            continue
        k = random.randint(2, kA)
        W = profile(cs, k)
        for s in range(1, len(W) - 1):
            if W[s + 1] == 0:
                continue
            rb = rho_bar(C, h, k, s)
            if rb is None:
                continue
            n += 1
            rho = Fraction((s + 1) * W[s - 1] * W[s + 1], s * W[s] * W[s])
            if rho > rb:
                fails.append([cs, k, s, float(rho), float(rb)])
    out["sanity"] = {"checked": n, "fails": fails[:20],
                     "n_fails": len(fails)}
    print(f"[sanity] {n} rho<=rho-bar checks, {len(fails)} failures",
          flush=True)

    # 2. rho-bar map at k-s in {1,2}
    HS = []
    for h in list(range(3, 13)) + [16, 24, 40, 60]:
        svals = sorted({1, 2, 3, h // 3, h // 2, 2 * h // 3, h - 2, h - 1})
        HS.append((h, [s for s in svals if 1 <= s <= h - 1]))
    res = {}
    for dm in (1, 2, 3, 4):
        worst, n, crossed = None, 0, []
        for h, svals in HS:
            for s in svals:
                k = s + dm
                Cs = sorted({h + 1, h + 2, h + 3, 2 * h, 3 * h, 5 * h,
                             10 * h, 20 * h, 2000})
                for C in Cs:
                    if C < h + 1 or C > 2000:
                        continue
                    if k > band_kA(C, h):
                        continue
                    rb = rho_bar(C, h, k, s)
                    if rb is None:
                        continue
                    n += 1
                    fr = float(rb)
                    if worst is None or fr > worst[0]:
                        worst = [fr, C, h, k, s]
                    if fr > 1:
                        crossed.append([fr, C, h, k, s])
        res[f"k-s={dm}"] = {"checked": n, "max": worst,
                            "n_above_1": len(crossed),
                            "above_1_sample": crossed[:10]}
        print(f"[rho-bar k-s={dm}] {n} cases, max {worst}, "
              f"above 1: {len(crossed)}", flush=True)
    out["rho_bar_map"] = res

    # asymptote check at k-s=1: C = 2000, compare to (2-1.5lam)/(2-lam)^2
    rows = []
    for h in (12, 40, 60):
        for s in (1, h // 3, 2 * h // 3, h - 1):
            if not 1 <= s <= h - 1:
                continue
            k = s + 1
            C = 2000
            if k > band_kA(C, h):
                continue
            rb = rho_bar(C, h, k, s)
            lam = (s - 1) / h
            asym = (2 - 1.5 * lam) / (2 - lam) ** 2
            rows.append([h, s, float(rb), asym])
    out["asymptote_check"] = rows
    print("[asymptote] (h, s, rho-bar@C=2000, (2-1.5lam)/(2-lam)^2):",
          flush=True)
    for row in rows:
        print(f"   h={row[0]:3d} s={row[1]:3d} "
              f"rho-bar={row[2]:.4f} asym={row[3]:.4f}", flush=True)

    path = REPO / "logs" / "993_bandbottom.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
