# Adversarial audit of the hub-spider theorem chain (2026-06-12)

Scope: every link of notes/993_hub_spider_theorem.md - logical
composition, load-bearing identities, verification code, and
certification logic.  Conducted with fresh re-derivations and
independently-written check code.

## Findings

**F1 (flaw, repaired): the strategy-B dev bound used the wrong slot.**
In both cap implementations (certify_993_M_lp_toolbox.py,
extract_993_M_dual_certificates.py), dev = max(ceilA - 1, 1 - floor)
used the k+1-level ceiling ceilA to majorize |g0 - 1| where g0 is the
growth at level k.  The sub-bound |g0-1| <= dev failed in 592 of
10,751 exact class-instances (worst gap 3.0): the WRITTEN DERIVATION
of cap_B was invalid, although the final cap inequality
(contribution <= cap_B) happened to hold everywhere checked - slack
elsewhere masked the broken step, which is precisely the
shared-blind-spot failure mode this audit targeted.
Repair: dev := max(ceil0 - 1, 1 - floor) with the k-level ceiling.

**F2 (flaw, repaired): the no-bound sentinel acted as a false bound.**
ceiling_v2 returned BIG = 10 (Fraction) / 10.0 (float) where the
reverse-Jensen formula provides no valid ceiling (class-birth
positions, exhausted v-support).  At [2^12], k=13, class (12,24): true
g0 = 13 > min(QB, BIG) = 10 - a genuinely false constraint.
Repair: return None; callers fall back to the Q-ceiling alone.

**F3 (positive): k = 1 log-concavity closes gap G3 in one line.**
P_0 = 1, P_1 = n (vertices), P_2 = C(n,2) - (n-1) (tree edges), and
n^2 >= n(n-1)/2 - (n-1) is n^2 + 3n - 2 >= 0.  G3 resolved.

## Post-repair verification (all exact)

- Sub-bound audit, 10,751 class-instances: g+ <= ceilA, floor <= g0
  <= ceil0, |g0-1| <= dev, contribution <= cap_A, contribution <=
  cap_B - ZERO violations on all six.
- T1/T2 certificates: original grid 238/238 (worst 0.4352 unchanged),
  extended grid 212/212 (worst 0.4352).
- LP certification: worst 0.7403 / margin 25.97% unchanged (the
  repaired instances were never binding).
- End-to-end: all 68 trees in the claimed unconditional scope are
  unimodal by direct DP (independent of all lemma machinery).
- Bracket construction (certify_993_ecore_polyc.brackets) crosschecked
  against independent numeric products at 120 random points: exact
  match.  (The E-core certification is unaffected by F1/F2: it uses
  only the bracket polynomials, not the caps.)

## Re-derivations checked clean (by hand, this session)

The eps-identity; the (M) -> band-A-LC reduction (the step
g_k g_{k-1} rho_k m (1+eps)^2 = m F_k^2 is exact); T1's chain
(A0-only dependence confirmed); the charge decomposition and the
validity of the per-class min of strategies A and B (both bound the
SAME per-class contribution; verified including the g0 < 1 equality
case); the DD step and P6's exact role at position k (no cross-k
dependence); the flow facts at fixed k (phi'(1), both envelope
directions, m1, m2); the exact-mean identities and both Jensen
directions; the slot expansion (any W, any constant >= 1); the seam
composition (prefix-LC through kdec - 1 suffices); Liggett padding.

## Conclusion

Two implementation-level flaws found and repaired, one gap closed; no
mathematical link of the chain was broken.  All headline numbers are
unchanged after repair.  The certified scope stands.
