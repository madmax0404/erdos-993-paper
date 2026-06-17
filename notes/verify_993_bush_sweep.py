"""Phase-3 cross-validation sweep: mixed-depth spiders, orders <= 64.

Prompted by the external repo's bush-family search (re-derived
independently here; no external data used).  Family: root + h
branches, h in [2,5]; each branch a hub with c pendant paths of
length ell (c in [2,6], ell in [1,3]).  Branch polynomials via
path DP: A = I(P_ell)^c + x I(P_{ell-1})^c (hub free),
B = I(P_ell)^c (hub excluded); tree: I = prod A_i + x prod B_i.
ell = 2 recovers hub spiders (A = H_c).

For every tree with n <= 64: exact I; log-concavity failures
(positions, widths); unimodality; balance = min(a_{k-1},a_{k+1})/a_k
at each failure.  Cross-validation targets:
- zero non-unimodal members (Phase-3 negative space);
- the offset law on the pure-depth-2 subfamily (failures at
  h-2 below top);
- the balance record vs our 0.04512 (the 48-vertex junction tree);
- how mixed depths shift failure positions (new structural data).

Output: logs/993_bush_sweep.json
"""

from __future__ import annotations

import json
from itertools import combinations_with_replacement
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def polymul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return out


def path_polys(maxlen):
    P = [[1], [1, 1]]
    for m in range(2, maxlen + 1):
        P.append([a + (P[m - 2][i - 1] if 1 <= i <= len(P[m - 2])
                       else 0)
                  for i, a in enumerate(P[m - 1] + [0])])
    return P


def main():
    P = path_polys(3)
    # branch types: (c, ell) -> (A, B, size)
    types = {}
    for c in range(2, 7):
        for ell in (1, 2, 3):
            Aout = [1]
            for _ in range(c):
                Aout = polymul(Aout, P[ell])
            Bin = [1]
            for _ in range(c):
                Bin = polymul(Bin, P[ell - 1])
            A = [a + (Bin[i - 1] if 1 <= i <= len(Bin) else 0)
                 for i, a in enumerate(Aout + [0])]
            types[(c, ell)] = (A, Aout, 1 + c * ell)
    tkeys = sorted(types)
    n_trees = 0
    nonlc, nonuni = [], []
    best_balance = None
    offset_law_depth2 = {"checked": 0, "violations": []}
    for h in range(2, 6):
        for combo in combinations_with_replacement(tkeys, h):
            n = 1 + sum(types[t][2] for t in combo)
            if n > 64:
                continue
            n_trees += 1
            Aprod, Bprod = [1], [1]
            for t in combo:
                Aprod = polymul(Aprod, types[t][0])
                Bprod = polymul(Bprod, types[t][1])
            I = [a + (Bprod[i - 1] if 1 <= i <= len(Bprod) else 0)
                 for i, a in enumerate(Aprod + [0])]
            while I and I[-1] == 0:
                I.pop()
            alpha = len(I) - 1
            fails = [k for k in range(1, alpha)
                     if I[k] * I[k] < I[k - 1] * I[k + 1]]
            rising, uni = True, True
            for i in range(1, len(I)):
                if rising and I[i] < I[i - 1]:
                    rising = False
                elif not rising and I[i] > I[i - 1]:
                    uni = False
            if not uni:
                nonuni.append([list(combo), n])
            if fails:
                bal = max(min(I[k - 1], I[k + 1]) / I[k]
                          for k in fails)
                nonlc.append([list(combo), n, fails,
                              round(bal, 5)])
                if best_balance is None or bal > best_balance[0]:
                    best_balance = [bal, list(combo), n, fails]
                if all(t[1] == 2 for t in combo):
                    offset_law_depth2["checked"] += 1
                    if fails != [alpha - (h - 2)] and \
                            fails != [alpha - h + 2]:
                        if not (len(fails) == 1 and
                                fails[0] == alpha - (h - 2)):
                            offset_law_depth2["violations"].append(
                                [list(combo), fails, alpha])
    out = {"trees": n_trees, "non_log_concave": len(nonlc),
           "non_unimodal": len(nonuni),
           "non_unimodal_list": nonuni[:10],
           "best_balance": best_balance,
           "offset_law_depth2": offset_law_depth2,
           "worst_25": sorted(nonlc, key=lambda r: -r[3])[:25]}
    print(f"[bush] {n_trees} trees (n <= 64); non-LC {len(nonlc)}; "
          f"NON-UNIMODAL {len(nonuni)}; best balance "
          f"{best_balance[:1] + best_balance[2:] if best_balance else None}; "
          f"depth-2 offset-law checks "
          f"{offset_law_depth2['checked']} with "
          f"{len(offset_law_depth2['violations'])} violations",
          flush=True)
    path = REPO / "logs" / "993_bush_sweep.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
