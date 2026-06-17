"""Scope extension: the four mixed-arm h=2 grid members.

Theorem h2mixed (notes/993_purepair_reduction.md, L3) supplies
hypothesis (ii) of the reduction theorem unconditionally for h = 2
with even total degree.  The certificate grid contains exactly four
mixed h=2 multisets of even total degree: (2,4), (6,8), (6,12),
(10,12).  This script verifies, for each:

1. grid membership with passing certificate ratio (hypothesis (i)),
   read from logs/993_M_dual_certificates*.json;
2. band-B emptiness: k_dec <= C (h = 2 is never leaf-heavy here), so
   the band-A + decreasing-zone + seam composition needs no band-B
   step;
3. end-to-end brute force: I(S(c1,c2)) = H_{c1}H_{c2} + x E_{c1}E_{c2}
   computed exactly and checked unimodal (the audit invariant).

Also: the odd-total-degree mixed h=2 grid members (pending the odd
core) are listed for the record.

Output: logs/993_h2mixed_scope.json
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

EVEN = [(2, 4), (6, 8), (6, 12), (10, 12)]


def polymul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return out


def H(c):
    # (1+2x)^c + x(1+x)^c
    out = [comb(c, m) << m for m in range(c + 1)] + [0]
    for m in range(c + 1):
        out[m + 1] += comb(c, m)
    return out


def E(c):
    return [comb(c, m) << m for m in range(c + 1)]


def unimodal(a):
    rising = True
    for i in range(1, len(a)):
        if rising and a[i] < a[i - 1]:
            rising = False
        elif not rising and a[i] > a[i - 1]:
            return False
    return True


def band_data(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return k0, lBG, min(k0, lBG)


def main():
    out = {"even_mixed": [], "odd_mixed_pending": []}
    grid = {}
    for path in ("993_M_dual_certificates.json",
                 "993_M_dual_certificates_ext.json"):
        d = json.loads((REPO / "logs" / path).read_text())
        for case in d["per_case"]:
            cs = tuple(sorted(case["counts"]))
            r = case["max_ratio"]
            grid[cs] = max(grid.get(cs, 0.0), r)
    for (c1, c2) in EVEN:
        C, h = c1 + c2, 2
        k0, lBG, kdec = band_data(C, h)
        bandB_empty = kdec <= C
        in_grid = (c1, c2) in grid
        ratio = grid.get((c1, c2))
        # brute force
        P = polymul(H(c1), H(c2))
        xg = [0] + polymul(E(c1), E(c2))
        I = [a + (xg[i] if i < len(xg) else 0) for i, a in enumerate(P)]
        I = [1 * v for v in I]  # ints
        uni = unimodal(I)
        rec = {"arms": [c1, c2], "n": 1 + h + 2 * C, "C": C,
               "in_grid": in_grid, "certificate_max_ratio": ratio,
               "k0": k0, "lBG": lBG, "k_dec": kdec,
               "bandB_empty": bandB_empty, "brute_force_unimodal": uni}
        out["even_mixed"].append(rec)
        print(rec, flush=True)
    for cs, r in sorted(grid.items()):
        if len(cs) == 2 and cs[0] != cs[1] and sum(cs) % 2 == 1:
            out["odd_mixed_pending"].append(
                {"arms": list(cs), "certificate_max_ratio": r})
    ok = all(r["in_grid"] and r["certificate_max_ratio"] < 1
             and r["bandB_empty"] and r["brute_force_unimodal"]
             for r in out["even_mixed"])
    out["all_checks_pass"] = ok
    path = REPO / "logs" / "993_h2mixed_scope.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"ALL CHECKS PASS: {ok}; wrote {path}", flush=True)


if __name__ == "__main__":
    main()
