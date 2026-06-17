"""Scope extension: h=3 adjacent-two-value spiders, incl. the
Kadrawi-Levit trees T_{3,4,4} and T_{3,3,4}.

Prompted by the external search repo
github.com/willblair0708/verified-combinatorics (erdos-993), whose
order-26 seed T_3_4_4 is S(3,4,4) in our notation; its independence
polynomial was re-verified exactly against our closed form
(I = H_3 H_4^2 + x (1+2x)^11), and its log-concavity failure sits at
offset h-2 = 1 below the top degree, confirming our offset law on
independently generated data.

The extension chain, per multiset (a^p, (a+1)^q), h = 3, a <= 8:
  (i)  T1/T2 certificates at every band position (verify_case from
       extract_993_M_dual_certificates);
  (ii) the flow concavity: adjacent-two-value rungs are certified
       for all integer a at (h=3, p in {1,2}, k <= 28) in
       logs/993_ladder_polyc_h3-10_k28.json + Lemma FL; this script
       confirms each multiset's k_A <= 28 and rung count <= 2;
  (iii) band B empty: k_dec <= C;
  (iv) end-to-end brute force (the audit invariant).

Output: logs/993_kl_scope.json
"""

from __future__ import annotations

import json
import sys
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "notes"))
from extract_993_M_dual_certificates import verify_case  # noqa: E402


def band_data(C, h):
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(k0 - 1, lBG - 1, C - 1), min(k0, lBG)


def polymul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                out[i + j] += a * b
    return out


def H(c):
    out = [comb(c, m) << m for m in range(c + 1)] + [0]
    for m in range(c + 1):
        out[m + 1] += comb(c, m)
    return out


def unimodal(seq):
    rising = True
    for i in range(1, len(seq)):
        if rising and seq[i] < seq[i - 1]:
            rising = False
        elif not rising and seq[i] > seq[i - 1]:
            return False
    return True


def main():
    rows, all_ok = [], True
    for a in range(1, 9):
        for p in (1, 2):
            counts = sorted([a] * p + [a + 1] * (3 - p))
            C, h = sum(counts), 3
            kA, kdec = band_data(C, h)
            worst, fail = verify_case(counts)
            P = polymul(polymul(H(counts[0]), H(counts[1])),
                        H(counts[2]))
            xg = [0] + [comb(C, m) << m for m in range(C + 1)]
            I = [v + (xg[i] if i < len(xg) else 0)
                 for i, v in enumerate(P)]
            bandB_ok = kdec <= C
            bandB_positions = []
            if not bandB_ok:
                # verify each band-B position k in [C, k_dec-1]
                # directly: lc_P(k) >= 0, exact
                bandB_ok = True
                for kk in range(C, kdec):
                    lc = I[kk] * I[kk] - I[kk - 1] * I[kk + 1] \
                        if kk + 1 < len(I) else I[kk] * I[kk]
                    bandB_positions.append([kk, int(lc >= 0)])
                    if lc < 0:
                        bandB_ok = False
            rec = {"counts": counts, "n": 1 + h + 2 * C,
                   "cert_pass": not fail,
                   "cert_worst": float(worst[0]) if not fail else None,
                   "kA": kA, "kA_le_28": kA <= 28,
                   "rungs": min(h, kA) - 1,
                   "bandB_empty": kdec <= C,
                   "bandB_positions_checked": bandB_positions,
                   "bandB_ok": bandB_ok,
                   "brute_force_unimodal": unimodal(I)}
            ok = (rec["cert_pass"] and rec["kA_le_28"]
                  and rec["bandB_ok"]
                  and rec["brute_force_unimodal"])
            all_ok = all_ok and ok
            rows.append(rec)
            print(f"  {counts}: cert {rec['cert_worst']}, kA={kA}, "
                  f"bandB empty {rec['bandB_empty']}, brute "
                  f"{rec['brute_force_unimodal']}", flush=True)
    out = {"families": rows, "all_checks_pass": all_ok,
           "note": "hypothesis (ii) via the adjacent-two-value "
                   "ladder certificates (h=3, p in {1,2}, k <= 28, "
                   "all integer a) + Lemma FL; external prompt: "
                   "github.com/willblair0708/verified-combinatorics"}
    print(f"ALL CHECKS PASS: {all_ok} ({len(rows)} families)",
          flush=True)
    path = REPO / "logs" / "993_kl_scope.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
