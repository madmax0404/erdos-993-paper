"""The odd core: proof-step verification and the h=2 scope completion.

THE LEMMA (odd core).  For m >= 1, s = 2m+1,
T_n = [x^n](1+3x+2x^2)^m, and all k >= 2:

    2 C(s,k-2) 2^k C(s,k) <= (2 T_{k-1} + 3 T_{k-2})^2 .

PROOF.  For k > s the left side vanishes; let 2 <= k <= s and put
a = C(2m,k-2) >= 1, b = C(2m,k-1) >= 1.
(1) Pascal + log-concavity of the row C(2m,.):
    C(s,k-2) = a + C(2m,k-3) <= a(1 + a/b),
    C(s,k)   = b + C(2m,k)   <= b(1 + b/a),
    so C(s,k-2) C(s,k) <= (a+b)^2.
(2) AM-GM + Vandermonde (the even-core bound): T_n >= 2^{n/2} C(2m,n).
(3) Hence U := 2T_{k-1} + 3T_{k-2}
           >= 2^{k/2}( sqrt2 * b + (3/2) a )
           >= 2^{k/2} * sqrt2 * (a + b),       since 3/2 > sqrt2,
    so U^2 >= 2 * 2^k (a+b)^2 >= 2 C(s,k-2) 2^k C(s,k).  QED

This script verifies exactly, for all m <= 80 (s <= 161) and all
2 <= k <= s+2:
  (a) T_n^2 >= 2^n C(2m,n)^2 for all n <= s   [step (2), squared];
  (b) C(s,k-2) C(s,k) b a <= a(a+b) * b(a+b)  [step (1), integerized];
  (c) U^2 >= 2^{k+1} (a+b)^2                  [step (3), squared];
  (d) the lemma itself: U^2 >= 2^{k+1} C(s,k-2) C(s,k).

Then the SCOPE COMPLETION: with the odd core proved, Theorem L3 (the
h=2 flow concavity) holds for ALL arms (c1,c2), so the seven
odd-total-degree mixed h=2 grid members join the unconditional scope.
For each: grid membership + certificate ratio (hypothesis (i)),
band-B emptiness (k_dec <= C), and end-to-end brute-force
unimodality.

Output: logs/993_oddcore.json
"""

from __future__ import annotations

import json
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

ODD = [(1, 8), (3, 4), (4, 7), (4, 9), (4, 11), (7, 8), (11, 12)]


def T_row(m, nmax):
    # coefficients of (1+3x+2x^2)^m = (1+x)^m (1+2x)^m up to nmax
    out = []
    for n in range(nmax + 1):
        out.append(sum(comb(m, j) * comb(m, n - j) << (n - j)
                       for j in range(max(0, n - m), min(m, n) + 1)))
    return out


def main():
    out = {}
    # ---- proof-step verification ----
    fails = {"a": [], "b": [], "c": [], "d": []}
    for m in range(1, 81):
        s = 2 * m + 1
        T = T_row(m, s + 2)
        for n in range(s + 1):
            if T[n] ** 2 < (comb(2 * m, n) ** 2) << n:
                fails["a"].append([m, n])
        for k in range(2, s + 3):
            a = comb(2 * m, k - 2)
            b = comb(2 * m, k - 1)
            U = 2 * (T[k - 1] if k - 1 <= s + 2 else 0) + 3 * T[k - 2]
            lhs = (comb(s, k - 2) * comb(s, k)) << (k + 1)
            if U * U < lhs:
                fails["d"].append([m, k])
            if k <= s:
                # step (1): C(s,k-2)C(s,k) * ab <= a(a+b)*b(a+b)
                if comb(s, k - 2) * comb(s, k) * a * b > a * b * (a + b) ** 2:
                    fails["b"].append([m, k])
                # step (3): U^2 >= 2^{k+1}(a+b)^2
                if U * U < ((a + b) ** 2) << (k + 1):
                    fails["c"].append([m, k])
    out["proof_steps"] = {"m_max": 80,
                          "fails": {key: v[:20] for key, v in fails.items()},
                          "n_fails": {key: len(v) for key, v in fails.items()}}
    print("[proof steps] fails:", {key: len(v) for key, v in fails.items()},
          flush=True)

    # ---- scope completion ----
    grid = {}
    for path in ("993_M_dual_certificates.json",
                 "993_M_dual_certificates_ext.json"):
        d = json.loads((REPO / "logs" / path).read_text())
        for case in d["per_case"]:
            cs = tuple(sorted(case["counts"]))
            grid[cs] = max(grid.get(cs, 0.0), case["max_ratio"])

    def polymul(p, q):
        r = [0] * (len(p) + len(q) - 1)
        for i, x in enumerate(p):
            if x:
                for j, y in enumerate(q):
                    r[i + j] += x * y
        return r

    def H(c):
        r = [comb(c, mm) << mm for mm in range(c + 1)] + [0]
        for mm in range(c + 1):
            r[mm + 1] += comb(c, mm)
        return r

    def E(c):
        return [comb(c, mm) << mm for mm in range(c + 1)]

    def unimodal(seq):
        rising = True
        for i in range(1, len(seq)):
            if rising and seq[i] < seq[i - 1]:
                rising = False
            elif not rising and seq[i] > seq[i - 1]:
                return False
        return True

    out["odd_scope"] = []
    for (c1, c2) in ODD:
        C, h = c1 + c2, 2
        D, n = h + C, 1 + h + 2 * C
        k0 = -(-(2 * D - 1) // 3)
        lBG = -(-(D * (n - 1)) // (D + n))
        kdec = min(k0, lBG)
        P = polymul(H(c1), H(c2))
        xg = [0] + polymul(E(c1), E(c2))
        I = [v + (xg[i] if i < len(xg) else 0) for i, v in enumerate(P)]
        rec = {"arms": [c1, c2], "n": n, "C": C,
               "in_grid": (c1, c2) in grid,
               "certificate_max_ratio": grid.get((c1, c2)),
               "k_dec": kdec, "bandB_empty": kdec <= C,
               "brute_force_unimodal": unimodal(I)}
        out["odd_scope"].append(rec)
        print(rec, flush=True)

    ok = (all(len(v) == 0 for v in fails.values())
          and all(r["in_grid"] and r["certificate_max_ratio"] < 1
                  and r["bandB_empty"] and r["brute_force_unimodal"]
                  for r in out["odd_scope"]))
    out["all_checks_pass"] = ok
    path = REPO / "logs" / "993_oddcore.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"ALL CHECKS PASS: {ok}; wrote {path}", flush=True)


if __name__ == "__main__":
    main()
