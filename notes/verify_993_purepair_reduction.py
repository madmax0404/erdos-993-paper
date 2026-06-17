"""Pure-pair reduction of the weighted E-core: exact scans.

Contents
--------
1. t-cancellation sanity (Lemma L1): for a FIXED background W, the pair
   defect [b_i b_j W][A_i A_j W] - [b_i A_j W][b_j A_i W] with
   A = E + t b on the two pair slots is independent of t (the t-update
   is a unipotent congruence of the 2x2 bracket matrix).  Verified
   exactly on random instances, including mixed per-slot backgrounds.
2. Cross-check against the reformed-E-core sweep's worst instance
   ((1,64,1^6), k=4, t=0): expect ratio ~ 0.7870.
3. Danger scan: honest multisets (c,c,1^A) (h = A+2 -- heaviest pair
   over the lightest background, never swept before), slot-t = 0
   (covers all slot-t by L1), all-E background (diagonal t = 0),
   in-band k.  Any per-pair violation triggers an aggregate-DD check.
4. Rays (1,c,1^A) and (2,c,1^A) extending the lopsided sweep.
5. Dense (**) sweep: all pairs a <= b with s = a+b <= 28, A <= 24,
   in-band k, budget denominator 2(A+1) (the worst case h = A+2;
   passing at h = A+2 implies all smaller h at the same A).
6. Honest (c,c,m^u) scan with the true denominator 2(u+1).
7. A -> infinity probes at fixed (a,b,k).
8. Aggregate DD scan over the danger family regardless of per-pair.
9. Schur-S check (Lemma L2): coefficients of
   S(a,b) = (1+x)^a(1+2x)^b + (1+x)^b(1+2x)^a are coefficientwise
   minimized over a+b = s at the balanced split; plus the
   factorization identity S(a,b) = (1+3x+2x^2)^a T_{b-a}.
10. Even-core regression (proved) + odd-core candidate:
    2 C(s,k-2) 2^k C(s,k) <= U_{k-1}^2 for odd s,
    U = coeffs of (1+3x+2x^2)^{(s-1)/2}(2+3x).
11. Diagonal-t profile: ratio(t) along the common background t for
    sample multisets (is t = 0 always the max?).
12. Per-slot convexity probe: is the violation function
    defect*2(h-1) - (X^2+Y^2) convex in each background slot's t
    (quadratic; 3-point test)?  If yes, box-vertex reduction holds.

Output: logs/993_purepair_reduction.json
"""

from __future__ import annotations

import json
import random
from fractions import Fraction
from math import comb
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
random.seed(993)
KCAP = 48


def f(alpha, beta, m):
    """[x^m] (1+x)^alpha (1+2x)^beta, exact."""
    if m < 0:
        return 0
    lo, hi = max(0, m - beta), min(alpha, m)
    if lo > hi:
        return 0
    return sum(comb(alpha, j) * comb(beta, m - j) << (m - j)
               for j in range(lo, hi + 1))


def band_kA(C, h):
    """Top of band A for total arm degree C and hub count h."""
    D, n = h + C, 1 + h + 2 * C
    k0 = -(-(2 * D - 1) // 3)
    lBG = -(-(D * (n - 1)) // (D + n))
    return min(lBG - 1, k0 - 1, C - 1)


def pair_check(a, b, A, k, hm1):
    """Pure-pair weighted E-core at pair (a,b), all-E background degree A,
    position k, budget denominator 2*hm1.  Returns (violates, ratio)."""
    P = f(a + b, A, k - 2)
    QE = comb(a + b + A, k) << k
    X0 = f(a, b + A, k - 1)
    Y0 = f(b, a + A, k - 1)
    bud2 = X0 * X0 + Y0 * Y0
    if bud2 == 0:
        return False, None
    lhs = (P * QE - X0 * Y0) * 2 * hm1
    return lhs > bud2, float(Fraction(lhs, bud2))


# ---------- generic poly helpers (for L1 sanity / t-profiles) ----------

def poly_E(c):
    return [comb(c, m) << m for m in range(c + 1)]


def poly_b(c):
    return [0] + [comb(c, m) for m in range(c + 1)]


def slot_poly(c, p, q):
    """q*E_c + p*b_c as an integer coefficient list (t = p/q, scaled)."""
    E, B = poly_E(c), poly_b(c)
    n = max(len(E), len(B))
    return [q * (E[m] if m < len(E) else 0) +
            p * (B[m] if m < len(B) else 0) for m in range(n)]


def pmul(p, q, kmax):
    out = [0] * (kmax + 1)
    for i, a in enumerate(p[: kmax + 1]):
        if a:
            for j, bc in enumerate(q[: kmax + 1 - i]):
                if bc:
                    out[i + j] += a * bc
    return out


def bracket(polys, k):
    w = [1]
    for pp in polys:
        w = pmul(w, pp, k)
    return w[k] if k < len(w) else 0


def topk_push(lst, item, K=8):
    lst.append(item)
    lst.sort(key=lambda r: -(r[0] if r[0] is not None else -1e18))
    del lst[K:]


# ---------------------------- stages ----------------------------------

def stage_t_cancellation(out):
    fails = 0
    trials = 200
    for _ in range(trials):
        h = random.randint(2, 7)
        cs = [random.randint(1, 9) for _ in range(h)]
        # fixed background: arbitrary per-slot (p_l, q_l) mixtures
        W = [slot_poly(cs[l], random.randint(0, 3), random.randint(1, 3))
             for l in range(2, h)]
        p, q = random.randint(0, 4), random.randint(1, 3)  # slot t = p/q
        C = sum(cs)
        k = random.randint(2, min(C + h, 20))
        bi, bj = poly_b(cs[0]), poly_b(cs[1])
        Ei, Ej = poly_E(cs[0]), poly_E(cs[1])
        Ai = slot_poly(cs[0], p, q)
        Aj = slot_poly(cs[1], p, q)
        dt = (bracket([bi, bj] + W, k) * bracket([Ai, Aj] + W, k)
              - bracket([bi, Aj] + W, k) * bracket([bj, Ai] + W, k))
        d0 = (bracket([bi, bj] + W, k) * bracket([Ei, Ej] + W, k)
              - bracket([bi, Ej] + W, k) * bracket([bj, Ei] + W, k))
        if dt != q * q * d0:
            fails += 1
    out["t_cancellation"] = {"trials": trials, "fails": fails}
    print(f"[1] t-cancellation: {trials} trials, {fails} fails", flush=True)


def stage_crosscheck(out):
    _, r = pair_check(1, 64, 6, 4, 7)
    out["crosscheck_1_64_A6_k4"] = r
    print(f"[2] cross-check (1,64,1^6) k=4: ratio = {r:.4f} (expect ~0.787)",
          flush=True)


def stage_danger_cc1A(out):
    CSET = list(range(2, 33)) + [40, 48, 64, 96, 128]
    ASET = list(range(1, 33)) + [48, 64, 96, 128, 192, 256]
    worst, viols, n = [], [], 0
    agg_results = []
    for cv in CSET:
        for A in ASET:
            C, h = 2 * cv + A, A + 2
            kA = min(band_kA(C, h), KCAP)
            for k in range(2, kA + 1):
                n += 1
                bad, r = pair_check(cv, cv, A, k, h - 1)
                if r is not None:
                    topk_push(worst, [r, cv, A, k])
                if bad:
                    viols.append([r, cv, A, k])
                    ok, ar = aggregate_t0([(cv, 2), (1, A)], k)
                    agg_results.append([cv, A, k, ok, ar])
    out["danger_cc1A"] = {"checked": n, "violations": viols[:50],
                          "n_violations": len(viols), "worst": worst,
                          "aggregate_at_violations": agg_results[:50]}
    print(f"[3] danger (c,c,1^A): {n} checked, {len(viols)} violations, "
          f"worst {worst[0] if worst else None}", flush=True)


def stage_rays(out):
    res = {}
    for name, amaker in [("1c", lambda cv: (1, cv)), ("2c", lambda cv: (2, cv))]:
        CSET = list(range(2, 33, 2)) + [48, 64, 96, 128]
        ASET = list(range(1, 33, 2)) + [48, 64, 96, 128, 192, 256]
        worst, viols, n = [], [], 0
        for cv in CSET:
            a, b = amaker(cv)
            for A in ASET:
                C, h = a + b + A, A + 2
                kA = min(band_kA(C, h), KCAP)
                for k in range(2, kA + 1):
                    n += 1
                    bad, r = pair_check(a, b, A, k, h - 1)
                    if r is not None:
                        topk_push(worst, [r, a, b, A, k])
                    if bad:
                        viols.append([r, a, b, A, k])
        res[name] = {"checked": n, "n_violations": len(viols),
                     "violations": viols[:50], "worst": worst}
        print(f"[4] ray ({name}): {n} checked, {len(viols)} violations, "
              f"worst {worst[0] if worst else None}", flush=True)
    out["rays"] = res


def stage_dense(out):
    worst, viols, n = [], [], 0
    for s in range(2, 29):
        for a in range(1, s // 2 + 1):
            b = s - a
            for A in range(0, 25):
                C, h = s + A, A + 2
                kA = min(band_kA(C, max(h, 2)), 36)
                for k in range(2, kA + 1):
                    n += 1
                    bad, r = pair_check(a, b, A, k, max(A + 1, 1))
                    if r is not None:
                        topk_push(worst, [r, a, b, A, k])
                    if bad:
                        viols.append([r, a, b, A, k])
    out["dense"] = {"checked": n, "n_violations": len(viols),
                    "violations": viols[:50], "worst": worst}
    print(f"[5] dense (**): {n} checked, {len(viols)} violations, "
          f"worst {worst[0] if worst else None}", flush=True)


def stage_honest_ccmu(out):
    worst, viols, n = [], [], 0
    for cv in (4, 8, 16, 32):
        for m in (2, 3, 4):
            for u in range(1, 13):
                C, h = 2 * cv + u * m, u + 2
                kA = min(band_kA(C, h), KCAP)
                for k in range(2, kA + 1):
                    for (a, b, A) in ((cv, cv, u * m),
                                      (cv, m, cv + (u - 1) * m)):
                        n += 1
                        bad, r = pair_check(a, b, A, k, h - 1)
                        if r is not None:
                            topk_push(worst, [r, a, b, A, k, cv, m, u])
                        if bad:
                            viols.append([r, a, b, A, k, cv, m, u])
    out["honest_ccmu"] = {"checked": n, "n_violations": len(viols),
                          "violations": viols[:50], "worst": worst}
    print(f"[6] honest (c,c,m^u): {n} checked, {len(viols)} violations, "
          f"worst {worst[0] if worst else None}", flush=True)


def stage_A_limit(out):
    probes = {}
    for (a, b) in ((2, 2), (4, 4), (8, 8), (16, 16), (1, 8), (1, 32)):
        for k in (2, 3, 4, 6, 8, 12, 16, 24, 32, 48):
            seq = []
            for A in (64, 128, 256, 512, 1024, 2048, 4096):
                if k > band_kA(a + b + A, A + 2):
                    continue
                _, r = pair_check(a, b, A, k, A + 1)
                seq.append([A, r])
            probes[f"{a},{b},k={k}"] = seq
    out["A_limit"] = probes
    mx = max((r for seq in probes.values() for _, r in seq if r is not None),
             default=None)
    print(f"[7] A-limit probes: max ratio over all probes = {mx}", flush=True)


def aggregate_t0(types, k):
    """Aggregate DD at t=0 for the multiset given as [(c, mult)] with
    distinct c values: sum_{i != j}(G y_ij - x_i x_j) <= sum_i x_i^2."""
    C = sum(cv * m for cv, m in types)
    G = comb(C, k) << k
    x = {cv: f(cv, C - cv, k - 1) for cv, _ in types}
    lhs = 0
    for ci, mi in types:
        for cj, mj in types:
            cnt = mi * (mi - 1) if ci == cj else mi * mj
            if cnt == 0:
                continue
            y = f(ci + cj, C - ci - cj, k - 2)
            lhs += cnt * (G * y - x[ci] * x[cj])
    rhs = sum(m * x[cv] ** 2 for cv, m in types)
    if rhs == 0:
        return True, None
    return lhs <= rhs, float(Fraction(lhs, rhs))


def stage_aggregate(out):
    worst, viols, n = [], [], 0
    for cv in (2, 4, 8, 16, 32, 64):
        for A in (1, 2, 4, 8, 16, 32, 64, 128):
            C, h = 2 * cv + A, A + 2
            kA = min(band_kA(C, h), KCAP)
            for k in range(2, kA + 1):
                n += 1
                ok, r = aggregate_t0([(cv, 2), (1, A)], k)
                if r is not None:
                    topk_push(worst, [r, cv, A, k])
                if not ok:
                    viols.append([r, cv, A, k])
    out["aggregate_cc1A"] = {"checked": n, "n_violations": len(viols),
                             "violations": viols[:50], "worst": worst}
    print(f"[8] aggregate DD on (c,c,1^A): {n} checked, {len(viols)} "
          f"violations, worst {worst[0] if worst else None}", flush=True)


def stage_schur(out):
    bad_mono, bad_fact = [], []
    for s in range(2, 41):
        prev = None
        for a in range(1, s // 2 + 1):
            b = s - a
            S = [f(a, b, m) + f(b, a, m) for m in range(s + 2)]
            # factorization: S = (1+3x+2x^2)^a * T_{b-a},
            # T_d = (1+x)^d + (1+2x)^d
            d = b - a
            T = [comb(d, m) + (comb(d, m) << m) for m in range(d + 1)]
            Pq = [1]
            for _ in range(a):
                Pq = pmul(Pq, [1, 3, 2], s + 1)
            F = pmul(Pq, T, s + 1)
            if any(F[m] != S[m] for m in range(s + 1)):
                bad_fact.append([a, b])
            if prev is not None:
                # prev = S(a-1, b+1): claim prev >= S coefficientwise
                if any(prev[m] < S[m] for m in range(s + 1)):
                    bad_mono.append([a, b])
            prev = S
    out["schur_S"] = {"s_max": 40, "monotonicity_fails": bad_mono,
                      "factorization_fails": bad_fact}
    print(f"[9] Schur-S: monotonicity fails {len(bad_mono)}, "
          f"factorization fails {len(bad_fact)}", flush=True)


def stage_cores(out):
    # even-core regression (proved): C(s,k-2) 2^k C(s,k) <= 2 T_{k-1}^2
    worst_even, bad_even = [], []
    for s in range(2, 41, 2):
        m = s // 2
        kA = band_kA(s, 2)
        for k in range(2, kA + 1):
            lhs = comb(s, k - 2) * comb(s, k) << k
            rhs = 2 * f(m, m, k - 1) ** 2
            r = float(Fraction(lhs, rhs))
            topk_push(worst_even, [r, s, k])
            if lhs > rhs:
                bad_even.append([s, k])
    # odd-core candidate: 2 C(s,k-2) 2^k C(s,k) <= U_{k-1}^2,
    # U = coeffs of (1+3x+2x^2)^{(s-1)/2} (2+3x)
    worst_odd, bad_odd = [], []
    for s in range(3, 42, 2):
        m = (s - 1) // 2
        kA = band_kA(s, 2)
        for k in range(2, kA + 1):
            U = 2 * f(m, m, k - 1) + 3 * f(m, m, k - 2)
            lhs = 2 * comb(s, k - 2) * comb(s, k) << k
            rhs = U * U
            r = float(Fraction(lhs, rhs))
            topk_push(worst_odd, [r, s, k])
            if lhs > rhs:
                bad_odd.append([s, k])
    out["even_core_regression"] = {"fails": bad_even, "worst": worst_even}
    out["odd_core_candidate"] = {"fails": bad_odd, "worst": worst_odd}
    print(f"[10] even-core fails {len(bad_even)} (worst "
          f"{worst_even[0][0]:.4f}); odd-core fails {len(bad_odd)} (worst "
          f"{worst_odd[0][0]:.4f})", flush=True)


SAMPLES = [
    (1, 8, 1, 1), (4, 4, 1, 1), (2, 8, 3, 1), (1, 16, 1, 1, 1, 1),
    (8, 8, 1, 1, 1, 1), (1, 64, 1, 1, 1, 1, 1, 1), (3, 5, 2, 2, 1),
]


def pair_indices(cs):
    seen, pairs = set(), []
    for i in range(len(cs)):
        for j in range(i + 1, len(cs)):
            key = (cs[i], cs[j])
            if key not in seen:
                seen.add(key)
                pairs.append((i, j))
    return pairs[:3]


def stage_diag_profile(out):
    res, argmax_not0 = {}, []
    ts = [(0, 1), (1, 2), (1, 1), (3, 2), (2, 1)]
    for cs in SAMPLES:
        h, C = len(cs), sum(cs)
        kA = band_kA(C, h)
        kset = sorted({2, 3, 4, max(2, kA // 2), kA})
        kset = [k for k in kset if 2 <= k <= kA]
        for (i, j) in pair_indices(cs):
            bi, bj = poly_b(cs[i]), poly_b(cs[j])
            Ei, Ej = poly_E(cs[i]), poly_E(cs[j])
            bg = [cs[l] for l in range(h) if l not in (i, j)]
            for k in kset:
                prof = []
                for (p, q) in ts:
                    W = [slot_poly(cv, p, q) for cv in bg]
                    P = bracket([bi, bj] + W, k)
                    QE = bracket([Ei, Ej] + W, k)
                    X0 = bracket([bi, Ej] + W, k)
                    Y0 = bracket([bj, Ei] + W, k)
                    bud2 = X0 * X0 + Y0 * Y0
                    if bud2 == 0:
                        prof.append(None)
                        continue
                    lhs = (P * QE - X0 * Y0) * 2 * (h - 1)
                    prof.append(float(Fraction(lhs, bud2)))
                key = f"{cs}|pair({cs[i]},{cs[j]})|k={k}"
                res[key] = prof
                vals = [(v, idx) for idx, v in enumerate(prof) if v is not None]
                if vals and max(vals)[1] != 0:
                    argmax_not0.append(key)
    out["diag_profile"] = {"t_values": ["0", "1/2", "1", "3/2", "2"],
                           "profiles": res,
                           "argmax_not_at_t0": argmax_not0}
    print(f"[11] diagonal-t profiles: {len(res)} profiles, "
          f"{len(argmax_not0)} with max NOT at t=0", flush=True)


def stage_convexity(out):
    n, nonconvex = 0, []
    for cs in SAMPLES:
        h, C = len(cs), sum(cs)
        kA = band_kA(C, h)
        kset = [k for k in sorted({2, 3, 4, kA}) if 2 <= k <= kA]
        for (i, j) in pair_indices(cs):
            bg_idx = [l for l in range(h) if l not in (i, j)]
            if not bg_idx:
                continue
            bi, bj = poly_b(cs[i]), poly_b(cs[j])
            Ei, Ej = poly_E(cs[i]), poly_E(cs[j])
            seen_active = set()
            for act in bg_idx:
                if cs[act] in seen_active:
                    continue
                seen_active.add(cs[act])
                for tau in (0, 1, 2):
                    for k in kset:
                        vals = []
                        for t in (0, 1, 2):
                            W = [slot_poly(cs[l], t if l == act else tau, 1)
                                 for l in bg_idx]
                            P = bracket([bi, bj] + W, k)
                            QE = bracket([Ei, Ej] + W, k)
                            X0 = bracket([bi, Ej] + W, k)
                            Y0 = bracket([bj, Ei] + W, k)
                            vals.append((P * QE - X0 * Y0) * 2 * (h - 1)
                                        - (X0 * X0 + Y0 * Y0))
                        n += 1
                        if vals[0] - 2 * vals[1] + vals[2] < 0:
                            nonconvex.append(
                                [list(cs), cs[i], cs[j], cs[act], tau, k])
    out["convexity"] = {"checked": n, "nonconvex": nonconvex[:50],
                        "n_nonconvex": len(nonconvex)}
    print(f"[12] per-slot convexity: {n} checked, "
          f"{len(nonconvex)} non-convex", flush=True)


def main():
    out = {}
    stage_t_cancellation(out)
    stage_crosscheck(out)
    stage_danger_cc1A(out)
    stage_rays(out)
    stage_dense(out)
    stage_honest_ccmu(out)
    stage_A_limit(out)
    stage_aggregate(out)
    stage_schur(out)
    stage_cores(out)
    stage_diag_profile(out)
    stage_convexity(out)
    path = REPO / "logs" / "993_purepair_reduction.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"wrote {path}", flush=True)


if __name__ == "__main__":
    main()
