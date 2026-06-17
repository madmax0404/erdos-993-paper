# The factorial ladder: a t-free route to the flow concavity

Part of `notes/993-hub-spider-unimodality-program.md` (session 15,
continued).  Script: `notes/verify_993_factorial_ladder.py`; log:
`logs/993_factorial_ladder.json`.

## Lemma FL (factorial criterion)

**Lemma.**  Let G(t) = sum_{s=0}^N W_s t^s with W_s >= 0 and
contiguous support.  If the factorial-weighted sequence (s! W_s) is
log-concave on the support, then G is log-concave on (0, infinity).

**Proof.**  Log-concavity of (s! W_s) says
rho_s := s W_s / W_{s-1} is nonincreasing on the support.  Under the
tilted law P_t(S = s) = W_s t^s / G(t),

    (ln G)'(t) = G'(t)/G(t)
               = sum_s (s+1) W_{s+1} t^s / G(t)
               = E_t[ rho_{S+1} ]

(with rho := 0 above the support).  For t' > t the likelihood ratio
P_{t'}(s)/P_t(s) prop. to (t'/t)^s is increasing in s, so P_{t'}
dominates P_t in the likelihood-ratio order, hence stochastically
[Shaked--Shanthikumar, Thm 1.C.1]; since rho_{S+1} is nonincreasing,
E_t[rho_{S+1}] is nonincreasing in t.  So (ln G)' is nonincreasing on
(0, infinity), i.e. G is log-concave there.  QED

## The ladder

Apply Lemma FL to the demotion flow G(t) = [prod_i(E_i + t b_i)]_k =
sum_s W_s(k) t^s, whose coefficients are the class masses

    W_s(k) = sum_{|S|=s} [ prod_{i in S} b_i prod_{i not in S} E_i ]_k

(contiguous support [0, min(h,k)] at band positions).  Hypothesis
(ii) (the flow concavity, for all t in [0,2]) FOLLOWS FROM the
t-free ladder

    (L_s)   s W_s(k)^2 >= (s+1) W_{s-1}(k) W_{s+1}(k),
            1 <= s <= min(h,k) - 1,

at every band position k.  Exact consistencies (all verified in the
script):

- Rung s = 1 reads W_1^2 >= 2 W_0 W_2, which is IDENTICALLY the
  aggregate (ii) at t = 0 (so the bottom rung loses nothing: it is
  necessary for (ii)).
- At h = 2 the ladder is the single rung W_1^2 >= 2 W_0 W_2 =
  (x_1+x_2)^2 >= 2 G y, which is the inequality proved in Theorem
  L3.  Lemma FL re-derives the L1-monotonicity step there: h = 2 is
  the one-rung case of the ladder, now PROVED for all arms.
- At uniform multisets W_s = C(h,s) u_s with u_s = [b^s E^{h-s}]_k,
  and (L_s) becomes

      u_s^2 >= u_{s-1} u_{s+1} (h-s)/(h-s+1),

  whose s = 1 case is the symmetric E-core h u_1^2 >= (h-1) u_0 u_2.
  The higher rungs are new inequalities of the same shape, with each
  bracket a polynomial in c at fixed (k,h,s) -- certifiable by the
  existing Taylor-shift method.

So the ladder simultaneously (a) eliminates the t-direction at zero
cost at its binding bottom rung, (b) reduces mixed multisets to a
finite family of class-mass inequalities of E-core shape, and (c)
explains the h = 2 theorem as its one-rung case.

## Scan verdicts (exact; logs/993_factorial_ladder.json)

- 5,298 profiles checked, ZERO rung failures:
  - uniform (c <= 12, h <= 12, band k <= 40): worst ratio 0.9172 at
    (12^12), k = 26, rung 1;
  - (a,b,1^A) closed-form families (all 200 per-pair violation
    witnesses + (c,c)/(1,c)/(2,c) grids, c <= 128, A <= 256): worst
    0.9711 at (128,128,1^256), k = 40, rung 1;
  - 60 random mixed (h <= 10, c_i <= 12): worst 0.8837, rung 1.
- The worst rung is ALWAYS s = 1 -- the rung that is necessary for
  (ii).  Higher rungs carry more slack.
- Schur probe (first pass, 15 worst-rung cases): balanced argmax in
  all 15.  CORRECTED by the wider per-rung scan (see "Ladder-Schur
  refuted as stated" below): balanced-argmax FAILS in 212/1082
  exhaustive (C,h,k,s) cases, but all such cases have ratio <= 0.544.
  The reduction to the two-adjacent-value families (a^p, (a+1)^q)
  must take a THRESHOLD form, not a Schur monotonicity.
- Consistency: 39/39 (rung-1 sign == aggregate-t0 sign on mixed
  samples; the h=2 rung margin == Theorem L3's margin identically).

## A rung-1 polynomial identity

With Phi_0 = prod E_l, Phi_1 = sum_i b_i prod_{l != i} E_l,
Phi_2 = sum_{i<j} b_i b_j prod_{l != i,j} E_l (so W_s = [Phi_s]_k):
since (prod_{l != i} E)(prod_{l != j} E) = (prod E)(prod_{l != i,j} E)
for i != j, the cross terms cancel exactly and

    Phi_1^2 - 2 Phi_0 Phi_2 = sum_i b_i^2 (prod_{l != i} E_l)^2,

which is coefficientwise nonnegative.  Rung 1 asks for the same
comparison at the (k,k)-diagonal product of coefficients,
[Phi_1]_k^2 >= 2[Phi_0]_k[Phi_2]_k -- i.e. rung 1 is a
diagonal-localization statement for an identity with explicit
coefficientwise slack sum_i [b_i^2 (prod_{l!=i} E)^2].  (At h = 2
this localization IS Theorem L3.)  Possible proof routes: Newton-type
localization using the real-rootedness of Phi_0, or the certified
near-uniform reduction above.

## Two-value certification (the Ladder-Schur reduction target)

notes/certify_993_ladder_polyc.py extends the Taylor-shift method to
the rungs on (a^p, (a+1)^q): at fixed (k, h, p, s) each class mass
is a polynomial in a of degree <= k-s, and the rung R(a) =
s W_s^2 - (s+1) W_{s-1} W_{s+1} is certified for ALL integers a >= 1
(positive leading coefficient + root bound + Taylor-shift positivity
+ exact evaluations).  RESULT
(logs/993_ladder_polyc_certification.json):

    915 instances -- h in [3,6], p in [1,h], k in [2,16], all rungs
    -- ALL CERTIFIED, zero failures, 55 seconds
    (logs/993_ladder_polyc_certification.json);

    FULL RANGE: 7,866 instances -- h in [3,10], p in [1,h],
    k in [2,28], all rungs -- ALL CERTIFIED, zero failures,
    32 minutes (logs/993_ladder_polyc_h3-10_k28.json).

So the ladder holds for EVERY two-adjacent-value multiset with
h <= 10 and k <= 28, all arm degrees; p = h includes the uniform
higher rungs.  This matches the reach of the uniform E-core grid
and is the certified half of the mixed endgame; the open half is
the threshold reduction below.

Schur consistency datapoint: the balanced partition (1^4, 2^254) of
(C, h) = (512, 258) at k = 40 has rung-1 ratio 0.972944, slightly
ABOVE the (128,128,1^256) value 0.971088 from the scan -- the
balanced partition is the worse one, exactly as Ladder-Schur
predicts.

## Ladder-Schur REFUTED as stated (same day, hours later)

Script notes/verify_993_ladder_schur_step.py, log
logs/993_ladder_schur_step.json, all exact:

- TRANSFER MONOTONICITY (the would-be proof route) is FALSE:
  11,278 of 49,941 Robin Hood steps toward balance DECREASE the
  rung ratio (margins to -0.23; violations at all rungs, mostly
  s >= 2 and small k, but rung 1 included).
- GLOBAL balanced-argmax is FALSE as stated: 212/1082 exhaustive
  (C,h,k,s) cases (h <= 5, C <= 20, every band k, every partition)
  have a non-balanced argmax -- typically lopsided shapes like
  (1,1,c) at small k.
- BUT: every argmax-not-balanced case has rung ratio <= 0.5437,
  far below 1.  Where ratios approach 1 (the large-h corners,
  e.g. 0.9729 at balanced (1^4,2^254) vs 0.9711 at lopsided
  (128,128,1^256), k=40), balanced dominates in every observation.

The usable reduction is therefore a THRESHOLD statement (to be
proved): ratio(any multiset) <= max(ratio(balanced two-value
companion), c0) for an absolute c0 < 1 (observed c0 ~ 0.55 on the
exhaustive range).  Lesson repeated: monotone-looking structure
must be scanned exhaustively before conjecturing -- this is the
fourth over-strong intermediate statement refuted by our own scans
(symmetric E-core, weighted per-pair, transfer monotonicity,
balanced argmax), while the underlying object (the ladder / the
aggregate) has never produced a violation.

## Lemma W-Schur (PROVED): class masses are Schur-convex

**Lemma.**  At fixed (C, h, k, s), the class mass

    W_s(c) = sum_{|S|=s} f(sigma_S, C - sigma_S, k - s),
    sigma_S = sum_{i in S} c_i,

is Schur-convex on multisets with fixed sum C and h parts: spreading
(moving away from balance in the majorization order) never decreases
any W_s.  In particular W_s(c) >= W_s(bal(C,h)) for every c.

**Proof.**  (a) A Robin Hood transfer toward balance on slots (i,j)
with c_i < c_j induces, on the multiset of s-subset sums, the
simultaneous transfers (sigma_{S+i}, sigma_{S+j}) ->
(sigma_{S+i}+1, sigma_{S+j}-1) over all (s-1)-subsets S avoiding i
and j -- each itself toward balance, since sigma_S + c_i <
sigma_S + c_j; subsets containing both or neither of i,j are
unchanged.  Hence the subset-sum multiset on the spread side
majorizes the one on the balanced side.  (b) The summand
u(sigma) = f(sigma, C - sigma, m), m = k - s, is convex in sigma:
Delta^2 u = f(sigma, C - sigma - 2, m - 2) >= 0 exactly (for
m >= 2; u is linear 2C - sigma at m = 1 and constant 1 at m = 0).
(c) Karamata's inequality.  QED

Consequences: BOTH sides of every rung grow away from balance
(numerator (s+1)W_{s-1}W_{s+1} and denominator s W_s^2), so DOM is
a relative-rate statement -- the numerator must not outgrow the
square of the denominator in the high regime.  It also yields the
cleaner conditioning DOM' below, whose hypothesis references only
the canonical balanced companion.

## The DOM lemma: the surviving formulation (end of session 15)

Three successive proof-route shortcuts were probed and refuted the
same day (scripts/logs: verify_993_ladder_schur_step.py,
verify_993_conditional_monotonicity.py, verify_993_window_census.py):

1. Schur walk (every balance-ward transfer increases the ratio):
   FALSE -- 11,278/49,941 violating steps.
2. Conditional walk (transfers are monotone when the ratio is
   high): FALSE -- theta* = 0.868: a violating step at ratio 0.868
   ((8,9,12,10,4,5,8,9,6), transfer (10,12)->(11,11), k=24, s=1).
3. Window lemma (wide value-window forces slack): FALSE -- one
   outlier in a large near-balanced bulk keeps the ratio high
   (window 7, ratio 0.944 at h=60).

What survives every probe (~25,000 exact checks: the threshold
landscape, 24,220 high-ratio cases, large-h stress to h=40), in its
final conditioning (on the CANONICAL balanced companion, not on c;
scripts verify_993_W_schur_dom.py, log 993_W_schur_dom.json):

    (DOM')  if ratio_s(bal(C,h), k) >= theta_0, then
            ratio_s(c, k) <= ratio_s(bal(C,h), k) for ALL multisets
            c with sum C and h parts.

Scan verdicts: over 2,331 exhaustive (C,h,k,s) cases (h <= 6,
C <= 24, every band k) the balanced companion is NEVER beaten once
its ratio is >= 0.6 (61 hairline beats below 0.585); in the large-h
families (h <= 40) never beaten above 0.658.  So theta_0 = 0.7
holds on all data with margin.  Bal-beating at LOW ratios is common
(13,715 instances) and spread across k-s in {1:7486, 2:4520,
3:1701, 4:8} -- so k-s does not classify the beats; the threshold
does.

BAND-BOTTOM TAMENESS (supporting structure): positions with
k - s <= 2 never get tight.  Census to h = 200: max observed ratio
0.6653.  Structurally, at k = s+1 the bracket levels degenerate
(m = k-s = 1: u(sigma) = 2C - sigma is LINEAR, so W_s is
partition-FREE; m = 0: W_{s+1} = C(h,s+1) partition-free), the
partition enters only through Q = sum c_i^2 in W_{s-1} (affine in
Q, nonneg coefficient), and the h -> infinity limit of the ratio is
1/2.  Hence the high regime lives entirely at k - s >= 3, and the
k - s <= 2 rungs reduce to an explicit rational inequality in
(C, h, s, Q), Q <= (h-1) + (C-h+1)^2 -- an elementary lemma target
("band-bottom lemma").

## The BB-reduction (PROVED) and the band-bottom map

**Lemma (BB-reduction).**  For every multiset c (sum C, h parts) and
every (k, s):

    rho_s(c,k) <= rho-bar(C,h,k,s)
               := (s+1) W_{s-1}(ext) W_{s+1}(ext) / (s W_s(bal)^2),

with ext = (1^{h-1}, C-h+1) and bal = bal(C,h).  Proof: ext
majorizes every multiset and every multiset majorizes bal, so by
Lemma W-Schur the two numerator masses are maximized at ext and the
denominator mass is minimized at bal.  QED  (At k-s = 1, W_s and
W_{s+1} are partition-free, so rho-bar = rho(ext) exactly.)

Map of rho-bar (exact; verify_993_bandbottom.py ->
logs/993_bandbottom.json; h <= 60, C <= 2000, in-band k):

    k-s = 1:  max 0.5452, tracking the exact large-C asymptote
              (2 - 1.5 lam)/(2 - lam)^2 <= 9/16  (lam = (s-1)/h)
              from below (agreement to 1e-3 at C = 2000);
    k-s = 2:  max 0.8962  -- still uniformly below 1;
    k-s = 3:  crosses 1 (max 1.49) -- the reduction's reach ends
              exactly where the high regime begins.

So the BAND-BOTTOM LEMMA takes the final form "rho-bar < 1 at
k-s <= 2": an explicit inequality between two canonical multisets,
polynomial in (C, h, s) at fixed k-s, with the asymptote derived.
What remains is uniform bookkeeping (explicit error terms beyond
the scanned range), not an idea.  Sanity: rho(c) <= rho-bar
verified at 1,200 random instances (zero failures, as the proof
requires).

ARCHITECTURE for hypothesis (ii), mixed h >= 3 (end of session 15):

    1. Lemma FL                       PROVED
    2. Lemma W-Schur                  PROVED
    3. BB-reduction                   PROVED (corollary of 2)
    4. band-bottom lemma (k-s <= 2)   = "rho-bar < 1": explicit
                                      canonical-pair inequality;
                                      mapped (max 0.896), asymptote
                                      derived; uniform bookkeeping
                                      remains
    5. DOM'/(T3) (k-s >= 3)           target, THE core open lemma
    6. two-value certificates         DONE h <= 10, k <= 28 (7,866)
    7. low regime (ratio < theta_0)   trivial (margin 1 - theta_0)
    ==> ladder ==> (ii) within caps; cap-lifting via M-k-style
    limit lemmas (separate target).

## Lemma y-LC (PROVED): the kernel's 1-d backbone

**Lemma.**  For fixed C >= 0 and j >= 0, the sequence
y(m) = [x^j](1+x)^m (1+2x)^{C-m}, m = 0..C, is log-concave in m.
(Equivalently the DOM' kernel K(s,t) = g y(s+t)/(x(s)x(t)) is
log-submodular.)

**Proof.**  Single out one slot and condition on it.  With
z_i(m) := [x^i](1+x)^m(1+2x)^{C-1-m}, splitting off one heavy
factor gives y(m) = 2 z_{j-1}(m) + z_j(m), and splitting off one
light factor gives y(m+1) = z_{j-1}(m) + z_j(m).  Hence

    y(m+1)/y(m) = 1 - 1/(2 + R(m)),   R(m) := z_j(m)/z_{j-1}(m),

and log-concavity of y is equivalent to R(m) nonincreasing in m.
Compare the coefficient rows at m and m+1 through the common base
B = (1+x)^m(1+2x)^{C-2-m}: z^{(m)}_i = B_i + 2B_{i-1} and
z^{(m+1)}_i = B_i + B_{i-1}, so

    z^{(m+1)}_i / z^{(m)}_i = (1 + t_i)/(1 + 2 t_i),
    t_i := B_{i-1}/B_i .

B is a product of log-concave polynomials, hence log-concave, so
t_i is nondecreasing in i, so the displayed ratio is nonincreasing
in i.  Applying this at i = j and i = j-1 gives exactly
z^{(m+1)}_j z^{(m)}_{j-1} <= z^{(m)}_j z^{(m+1)}_{j-1}, i.e.
R(m+1) <= R(m).  (Edge cases: j = 0 is constant; m = C-1 uses
B = (1+x)^{C-2} directly.)  QED

Verified exactly to C = 800 (see logs/993_giant_vs_bal.json,
stage 1).  In lr-order language: the row at m+1 is
likelihood-ratio smaller than the row at m, which is the monotone
structure behind both this lemma and Lemma FL.

## The DOM' campaign (opened same day): kernel view, two more dead
## shortcuts, and the variational program

KERNEL REFORMULATION (exact identity, verified 150/150;
verify_993_dom_kernel.py -> logs/993_dom_kernel.json): at rung 1,

    ratio_1(c,k) = sum_{i != j} w_i w_j K(c_i, c_j),
    w_i = x(c_i)/sum x,   K(s,t) = g y(s+t)/(x(s) x(t)),

where K depends only on (C,k) -- NOT on h.  Diagnostics: K is
maximized at the extreme corner (1, C-2) (values 1.6-1.7), is
Schur-CONVEX at fixed sum (lopsided pairs larger), and is perfectly
log-submodular (reverse-TP2, 800/800) -- equivalently y(m) is
log-concave in m (verified 555/555; MLR-provable like Lemma FL).
The mechanism of DOM' is weight-kernel ANTICORRELATION: spread
multisets are forced to put their weight on small-argument pairs.

TWO MORE SHORTCUTS REFUTED (the 4th and 5th):
4. the kernel-max chain ratio(c) <= (1 - 1/h) Kmax: closes only
   24/224 tight cases (Kmax lives at corners no multiset weights);
5. (PP-R), the R-conditioned weighted per-pair form
   g y(s+t) <= R[xy + (x^2+y^2)/(2(h-1))]: FALSE in the tight
   regime -- 187/207 failures, margins to 1.54, failing even at
   R = 0.988 (verify_993_ppr.py -> logs/993_ppr.json).  EVERY
   reduction that decouples a pair from the rest of the multiset
   dies; the weight coupling is the phenomenon.

THE VARIATIONAL PROGRAM (census verify_993_locmax_census.py ->
logs/993_locmax_census.json): over the transfer graph at fixed
(C,h,k), in every tight census case (h <= 5, C <= 24), the global
maximizer of ratio_1 is bal, and every local maximizer is either
adjacent-two-value or "bulk+giant" (a,...,a,M); multiplicity only
at the band top.

## DOM' REFUTED (the sixth refutation); the program reshaped

The Step-B sweep (verify_993_giant_vs_bal.py ->
logs/993_giant_vs_bal.json; 4,720 exact instances, h <= 100,
a <= 6, M to C = 1200, k - 1 >= 3) shows the bulk+giant family
BEATS bal deep in the tight regime: 376 exceedances with
ratio(bal) >= 0.7, up to ratio(bal) = 0.956 beaten (witness family
shape: small h, huge gap M - a in [28, 1066]; e.g. (1^5, 95),
k = 46: G = 0.778 > bal = 0.734).  The earlier ~25K-check evidence
for DOM' never swept bulk-a >= 2 giants at scale -- the same
corner-blindness as every previous refutation.  DOM' as stated is
FALSE; so is any inter-family domination route.

What survives, again, is the underlying object: the LADDER.  Max
ratio_G over the whole sweep is 0.98646 < 1, attained at the
MINIMAL giant (6^99, 8), k = 100 -- a gap-2 two-value multiset
tracking bal from just below (bal = 0.9864617 vs G = 0.9864591).
The beats at huge gaps cap out near 0.78 and are harmless.

RESHAPED ARCHITECTURE (cleaner -- domination was never needed):

  A (exchange lemma, THE core): every local maximizer of ratio_1
    with ratio >= theta_0 is adjacent-two-value or bulk+giant
    (a,...,a,M).  Then the global max over the connected transfer
    graph is attained at a classified shape, so the rung for ALL
    multisets follows from per-family bounds -- no comparison
    between families required.
  B' (giant certification): DONE within caps --
    certify_993_giant_polyc.py -> logs/993_giant_certification.json:
    1,512 instances (h in [3,10], d = M - a in [2,8], k in [2,28]),
    rung certified for ALL integers a >= 1, zero failures, 11 min.
    Remaining for the family: the large-d tail (observed cap ~0.78;
    an M -> infinity limit lemma) and the (h,k) cap-lifting shared
    with the whole program.
  Adjacent-two-value: already certified (7,866 instances).

Tools standing: W-Schur, y-LC (proved above), the exact transfer
calculus Delta x(v) = -f(v, C-v-1, k-2),
Delta y(m) = -f(m, C-m-1, k-3), second differences
Delta^2 f = f(., .-2, m-2).

SUB-LEMMA A.1 (multi-giant kill) -- PINNED, UNCONDITIONAL
(verify_993_A1_multigiant.py -> logs/993_A1_multigiant.json):
a two-value config (v^p, M^q) with gap M - v >= 2 and q >= 2 is
NEVER a local maximum: at all 3,522 scanned configs (no tightness
filter; h <= 40, v <= 6, gap <= 20, q <= 6, k <= 80) the
giant-spread T1 = (M,M)->(M-1,M+1) or the pair-balance
T2 = (v,M)->(v+1,M-1) strictly improves the ratio (T2: 1801,
both: 1206, T1: 257; closed-form deltas verified exactly).
Killing q >= 2 closes the ENTIRE two-value case of Lemma A
(q = 1 is bulk+giant, allowed).

Proof structure found: dividing the two stationarity conditions
cancels rho (hence unconditionality), leaving the CORE inequality

  [p D2y(v+M-1) + (q-2) D2y(2M-1)] * [A(v) - A(M-1)]
    > [(p-1)(dy(2v) - dy(v+M-1)) + (q-1)(dy(v+M) - dy(2M-1))]
      * [A(M-1) - A(M)]

(long-range A-drop against one-step A-drop).  CORE holds at all
3,522 configs but with minimum LHS/RHS = 1.0020 at
(v,M,p,q,k) = (6,8,34,6,4): essentially SHARP at small gap and
small k, so the proof must carry the quadratic correction terms
exactly there.  Plan: slack region (large gap or k) by telescoping
+ dy-log-concavity (Lemma y-LC at level k-3); thin region by
polynomial certification (CORE at fixed (gap,q,k) is polynomial in
(v,p) -- univariate certifications after one more parameter fix).
Remaining sub-case after A.1: A.2 (three-or-more values never a
local maximum), then Lemma A assembles.

SUB-LEMMA A.2 (three-value kill) -- PINNED, UNCONDITIONAL
(verify_993_A2_threevalue.py -> logs/993_A2_threevalue.json):
8,224 three-value configs (v1^p1, v2^p2, v3^p3), gaps to 12, six
multiplicity patterns + thirds, h <= 40, band k -- and EVERY one
has a strictly improving transfer (zero local maxima).  The drain
map: mid-give/bot-recv 6,358 (the middle value drains DOWNWARD --
the dominant mechanism), top-give/bot-recv 1,649 (outer balancing),
mid-give/top-recv 87, mid-self-spread 130.  A.2's proof shape: the
middle value is never stable, predominantly draining to the bottom.

TELESCOPED FORM OF CORE (the A.1 proof's engine): with
B(t) = f(t, C-t-2, k-3) = A(t) - A(t+1) and
E(m) = f(m, C-m-2, k-4) = dy(m) - dy(m+1), both positive,
decreasing, and LOG-CONCAVE (Lemma y-LC at totals C-1, C-2 one and
two levels down), CORE reads

  [p E(v+M-1) + (q-2) E(2M-1)] * sum_{t=v}^{M-2} B(t)
    > [(p-1) sum_{m=2v}^{v+M-2} E(m) + (q-1) sum_{m=v+M}^{2M-2} E(m)]
      * B(M-1).

At gap 2 (the sharp case, margin 1.002) the sums are single terms
and the inequality is a four-point E-comparison at interleaved
arguments {2v+1, 2M-1} vs {2v, v+M} with multiplier shifts
(p vs p-1, q-2 vs q-1) -- exactly balanced by E-log-concavity.
The proof plan: gap-2 by quantitative E-LC; larger gaps gain
telescoping slack; quadratic corrections carried exactly; thin
cases by univariate polynomial certification.

A.1 GAP-2 CASING (verify_993_A1_gap2.py -> logs/993_A1_gap2.json):
- k = 4: PROVED.  The E-level is k-4 = 0, so e_j = 1 and CORE
  collapses to (h-2) B(v) > (h-2) B(v+1), i.e. strict monotonicity
  of B, exact: B(t) - B(t+1) = f(t, C-t-3, 0) = 1.  The 1.0020
  "sharp minimum" of CORE was this benign case.
- k = 5: E is linear (e_j = 2C-4-2v-j); the CORE difference is a
  polynomial in v certified positive (leading coefficient + integer
  evaluations + Taylor shift) for 28 (h,q) grid families, zero
  failures.  Full-parameter symbolic treatment queued.
- k >= 6: exact min margins by stratum, CORE and quadratic-corrected,
  all > 1 but thin at scattered strata (1.0013 at k=6, 1.0014 at
  k=8, 1.0016 at k=12; mid-band 1.005, band-top 1.015) -- the same
  near-cancellation structure as k=4 one E-level up.  CONCLUSION:
  the general-k proof should find the POSITIVE EXPANSION of the
  CORE difference (the project's standard endgame: cf.
  Phi_1^2 - 2 Phi_0 Phi_2 = sum b_i^2 (prod E)^2), with the
  corrected version differing only by explicitly-bounded factors
  (corrected minima within 0.3% of CORE minima everywhere).

THE CORE REGROUPING (general gap; the proof frontier).  Exact
algebraic identity (verified at k=4 where it collapses correctly):

  LHS - RHS = p sum_t D_t + (q-2) sum_t D'_t
              + B(M-1) sum_j [E(2v+j) - E(v+M+j)],

over t in [v, M-2], j in [0, M-v-2], with the cross-level minors
D_t = E(v+M-1)B(t) - E(v+t)B(M-1),
D'_t = E(2M-1)B(t) - E(t+M)B(M-1).  The third term is ALWAYS
strictly positive (E decreasing).  Via the conditioning identity
(F_j(t) = 1 + 1/(1+R_j(t))), D_t >= 0 reduces to level-ratio
comparisons of the form R_{k-3}(t') <= R_{k-4}(m') with m' > t' --
where the two PROVED monotonicities (R decreasing in position, from
the y-LC proof; R decreasing in level, classical row-LC) pull in
OPPOSITE directions.  The E1 sandwich closes the comparison for
k <= 5 and in the bulk regime (positions far apart, level step
dominant); the remaining corner -- small h (position step v -> 2v
large relative to C) with large k -- can have D_t < 0 and must be
covered by the positive third term (CORE itself never failed
anywhere: margins >= 1.0013).

D-SIGN MAP AND COMPENSATION (verify_993_A1_dsign.py ->
logs/993_A1_dsign.json; 1,981 gap-2 configs, corner emphasis):
- second exact regrouping found and verified:
  (G2) LHS - RHS = (p-1) D1 + (q-1) D3 + (e1 - e3) B(v);
  both (G1) and (G2) identities exact at every config;
- D1 < 0 at 301 configs, D3 < 0 at 484, spread across all (p,q)
  patterns (the corner is wider than the R-sandwich suggested) --
  BUT the compensation is tiny: the worst ratio of the negative
  D-part to the positive term is 0.1331 (G1) / 0.1311 (G2), i.e.
  the always-positive term covers with a 7.5x margin everywhere;
- clean partial bounds: |D1|^- <= (e0 - e1) B(v+1),
  |D3|^- <= (e2 - e3) B(v+1) (one-line proofs), which already close
  (p,q) = (1,2) exactly.
REMAINING for CORE(gap 2): the compensation bound
p |D1|^- + (q-2) |D3|^- <= (e0 - e2) B(v+1) with 7.5x empirical
slack.  Reduced under the conditioning forms (divide by e0; F =
B(v)/B(v+1) = 1 + 1/(1+R3), R3 = R_{k-3}(v); s_j = e_{j+1}/e_j =
(1+R4^j)/(2+R4^j), R4^j = R_{k-4}(2v+j); all R at total C-3) to:

    p (1 - s0 F)^+ + (q-2) s0 s1 (1 - s2 F)^+  <=  1 - s0 s1,

where D1 < 0 iff R3 > 1 + R4^0 -- and to leading order the needed
input is an upper bound on the level-step-at-doubled-position
R_{k-3}(v) - R_{k-4}(2v) against 2(1+R3)/p.  RESOLVED by the window-mean
attack (verify_993_compensation_lemma.py ->
logs/993_compensation_lemma.json):

1. EXACT window-mean identity: R_j(t) = (2C3 - t - mu_{j-1}(t))/j,
   mu in [j-1, 2(j-1)] trivially (verified 120/120).
2. EXACT collapse: 1 - s0 F = (R3 - R4^0)/((2+R4^0)(1+R3)) and
   1 - s0 s1 = (3 + R4^0 + R4^1)/((2+R4^0)(2+R4^1)); the
   compensation lemma is EQUIVALENT to the rational inequality (*)
   in (R3, R4^0, R4^1, R4^2; p, q) (verified 80/80).
3. mu-COUPLING: mu4^j <= mu3 - 1 (level step adds weight in [1,2];
   position-monotonicity mu_j(t) nonincreasing in t, verified
   200/200) -- tightens the critical numerator of R3 - R4^0 from
   ~k^2 to v(k-2) - 2C3 + (k-5).
4. (*) is piecewise-linear in each R, each R affine in its mu ==>
   the coupled-box CORNERS decide.
5. COUPLED-BOX CERTIFICATE: 1,662/1,662 (v,p,q,k) grid cases
   certified, ZERO residuals (the crude uncoupled box managed only
   59.9%).

THE TWO MU MINI-LEMMAS -- PROVED (2026-06-13;
verify_993_mu_minilemmas.py -> logs/993_mu_minilemmas.json: every
proof step verified exactly, 16,000+ checks, zero failures).

**Lemma ML1 (level step).**  For the two-base row z_j(t) =
f(t, N-t, j), the window mean mu_j(t) = 2N - t - (j+1) R_{j+1}(t)
satisfies mu_j - mu_{j-1} in [1, 2].

Proof.  mu_j = j + E[H_j], H_j the heavy count under the
2^H-weighted hypergeometric row P(H_j = i) prop. to
C(N-t, i) C(t, j-i) 2^i.  LOWER: consecutive rows are lr-ordered
(the ratio C(t, j-i)/C(t, j-1-i) is increasing in i), so
H_j >=_st H_{j-1} and E[H_j] >= E[H_{j-1}].  UPPER: sample S_j from
the j-measure and drop a uniformly chosen element; the resulting
(j-1)-marginal is the TRUE (j-1)-measure tilted by (W - w(S')),
where W is the total ground weight.  Since w = (j-1) + H on
(j-1)-subsets, Cov(H, W - w) = -Var(H) <= 0, so the tilt only
lowers the mean: E_true[H_{j-1}] >= E_tilted[H_{j-1}]
= E[H_j] - P(dropped element heavy) >= E[H_j] - 1.  QED

**Lemma ML2 (position step).**  j [R_j(t) - R_j(t+1)] in [0, 1];
equivalently mu_{j-1}(t) is nonincreasing in t.

Proof.  Common-base decomposition (base row b = the coefficients at
total N-1): z_j(t) = b_j + 2 b_{j-1}, z_j(t+1) = b_j + b_{j-1},
giving the EXACT step

    R_j(t) - R_j(t+1) = beta2 (beta2 - beta1)
                        / ((beta2 + 1)(beta2 + 2)),

beta1 = b_j/b_{j-1} <= beta2 = b_{j-1}/b_{j-2} (base LC) -- hence
>= 0.  For the upper half, the window identity on the base row plus
ML1 (applied to the base) bound the ratio gap:

    beta2 - beta1 = [(2(N-1) - t) + (j-1)(mu-step) - mu_{j-2}]
                    / (j (j-1))
                 <= (2(N-1) - t + j) / (j (j-1)),

and beta2 >= (2(N-1) - t - 2(j-2))/(j-1), so

    j beta2 (beta2 - beta1) <= beta2 (2(N-1) - t + j)/(j-1)
      <= beta2^2 + 3 beta2  <= (beta2+1)(beta2+2),

where the middle step reduces, after clearing (j-1), to the
comparison 2(N-1) - t + j <= [2(N-1) - t - 2j + 4] + 3(j - 1),
i.e. j <= j + 1.  QED

## General gap: probe verdict and the corrected strategy

(verify_993_A1_generalgap.py -> logs/993_A1_generalgap.json + the
large-d trend probe.)  The general-gap regrouped expansion holds as
an identity and CORE never fails (4,628 configs, zero), BUT the
gap-2 proof's aggregation -- bounding the deficit tail against the
always-positive THIRD term -- fails at scale: the ratio
(negative D-parts)/(third term) grows with the gap, crossing 1 at
d = 32 (k large) and reaching 4.3 by d = 192.  The SEVENTH refuted
intermediate device.  Diagnosis: at large gaps the deficit tail
[t*, M-2] must be covered by the positive HEAD of the D-sum itself
(early-t minors are large and positive; the suffix-interval
structure holds at 4,622/4,628 configs, 6 boundary exceptions to
classify); the third term is asymptotically irrelevant.  Corrected
strategy for the next session: head-vs-tail pairing INSIDE
sum_t D_t -- equivalently, prove
sum_t [prod_{s in [t,M-2]} F_B(s) - prod F_E(s+v)] >= (deficit
terms) by the per-factor window-mean comparison with the
arithmetic of the t*-interval; the gap-2 machinery applies
per-factor, the new content is the summation geometry.

HEAD-TAIL PROBE (verify_993_headtail.py -> logs/993_headtail.json;
1,729 configs, d to 192, k to 400):
- the simple split S1 = sum D_t >= 0, S2 = sum D'_t >= 0 is FALSE
  (the eighth refuted simple form): S1 < 0 at 550 configs, S2 < 0
  at 1,406; CORE lives in the weighted combination only.  The
  coverage-0 witness (h=4, q=2, v=10, d=4, k=16) has NO positive
  head at all -- the all-deficit regime exists and is exactly the
  small-d corner where the THIRD term carries (old aggregation
  ratio <= 0.59 there).
- the REFLECTION PAIRING never fails (0/1,729): where a head
  exists, head term i >= deficit term i, with the cumulative
  fallback also never failing.
PROOF ARCHITECTURE (general gap, three layers):
  (i)   near tail: reflection pairing (verified mechanism);
  (ii)  far tail beyond the head length (the smallest deficits):
        against the third term;
  (iii) all-deficit regime (small d): against the third term (the
        gap-2-style aggregation, valid in this regime).
Plus the (q-2)-weighted S2 handled alongside (small weight).  Next:
classify the regime boundary (head exists <=> N(v) <= 0, an
explicit parameter inequality) and prove layers (ii)/(iii) with the
third-term arithmetic.

## THE NINTH AND TENTH REFUTATIONS (session 16, late): the
## two-shape classification is FALSE at extreme parameters

Corner-stressing the all-deficit region (large v, d, k -- beyond
every earlier census cap) found GENUINE TIGHT LOCAL MAXIMA outside
both families:
- two-value multi-giant: (16^10, 48^2), k = 132, ratio 0.8596;
  (16^22, 144^2), k = 329, ratio 0.9375; (10-bulk variants to
  0.9534) -- so sub-lemma A.1's "multi-giant is never a local max"
  is FALSE at scale (it is TRUE in the ranges where it was proved,
  including all of CORE(gap 2)'s domain, but those parameters do
  not exhaust the band);
- three-value bulk + two NEAR-EQUAL giants: (16^10, 47, 48) at
  0.8593, (16^22, 143, 144) at 0.9374 (38 instances found) -- so
  the A.2 drain claim also fails at scale.

CORRECTED CONJECTURE (two-cluster classification): every tight
local maximizer is a TWO-CLUSTER multiset -- values within
{a, a+1} union {b, b+1} (bulk cluster + giant cluster).  All
observed maxima to date fit it (adjacent two-value = one cluster;
bulk+giant; multi-giant; bulk + near-equal giant pair).

THE COLLAPSE LEMMA (PROVED -- three lines from the definitions;
verified 15,992/15,992, verify_993_collapse_lemma.py).  For any
transfer (u -> u-1, w -> w+1), u != w:

  d2(u,w) = sum_{v != u,w} m_v [dy(v+u-1) - dy(v+w)]
            + (m_u-1)[dy(2u-1) - dy(u+w)]
            + (m_w-1)[dy(u+w-1) - dy(2w)],

(self-move: background sum + (m_u-2)[dy(2u-1) - dy(2u)]) -- the
four raw corrections absorb into multiplicity-reduced self-terms;
every bracket telescopes into E-sums.  All stationarity analyses
are henceforth correction-free.

THE WINDOW FORM (corollary of the collapse lemma; verified
7,835/7,835, verify_993_window_form.py): every transfer delta is a
uniform-length window sum -- spreads: d2 = sum_v m-hat_v
Win_E(v+u-1, w-u+1), d1 = Win_B(u-1, w-u+1); balances: the mirrored
forms at start v+w, length u-w-1, with m-hat the moved-slot-reduced
multiplicities.  The general M1 leading form is a window-sum-product
comparison; per-window factors are governed by the cross-level
R-comparison and the mu-coupled compensation -- the expansion phase
of the M1 grind is COMPLETE.

THE M1-TRIPLE KEYSTONE (verified 121/121,
verify_993_m1_triple.py).  At the thin spot (a^p, a+1, a+2):
d2_s = p[E(2a) + E(2a+1)] (the spread sees only the bulk), and

  lead_o = [E0 B0 - E1 B1] + (p-1)[E1 B0 - E0 B1]

-- a positive step-product plus (p-1) times the gap-2 cross-level
minor with the same R_{k-3}(a) vs R_{k-4}(2a) comparison and
mu-coupled compensation: the CORE(gap 2) proof transfers verbatim
to M1's hardest case.  M1 leading-form margins
(verify_993_m1_leading.py): failures only inside the geometric
corner (0 outside, 697 configs); min M1 margin 0.0044 at the
consecutive triple, structurally near-degenerate as expected.

THE MINOR EXPANSION (verified 179/179,
verify_993_minor_expansion.py): the M1 leading form is exactly a
positive-weighted double sum of the elementary cross-level minors
E(v+y-1+i)B(x+j) - E(v+x+j)B(y-1+i) over the window offsets, plus
multiplicity-diagonal terms that are single pairs of the same
family.  Every minor's sign is the factorwise
R_{k-3}(s) <= R_{k-4}(s+v) comparison with the mu-coupled
compensation already proved in CORE(gap 2).  M1's remaining content
is the summation arithmetic where minors invert -- the head-tail
geometry at minor granularity with explicit weights.

THE WINDOW-LEVEL COUPLED BOX (the M1 final-pass design;
structural facts verified, verify_993_window_box_design.py):
1. ANCHORING: lead_o is degree-2 homogeneous in the (dy, A)
   ladders (scale-free), so all values express through F-ratio
   products from per-chain anchors.
2. ML2-TUBES: along every consecutive position chain, each step's
   R-drop satisfies j*dR in [0,1] (verified: max usage 0.827,
   zero violations) -- chains are confined to tubes around their
   anchors, reducing the mu-box dimension from ~2h to the number
   of chain anchors (~4 for three-value shapes).
3. CORNER CERTIFICATION: lead_o, as a multi-affine-fractional
   function of the anchor R's (each entering through its own
   window-mean mu), is monotone in each parameter; the coupled
   corners decide, per stratum, exactly as in CORE(gap 2).
Execution order for the next session: implement the tube-interval
corner certificate on the three-value strata; measure coverage;
stratum-tail certification; then the corner drag (M2/M3, 14
configs) and Lemma A' assembly.

THE M1 REGROUPING (verified 223/223,
verify_993_m1_regrouping.py; supersedes the failed v1/v2
certificates): with N_v = Ws_v WinB(x,G) - Wo_v WinB(y-1,L),

  (R1) lead_o = sum_v mhat_o_v N_v
                + [WinE(x+y-1,L) - WinE(2y-1,L)] WinB(x,G),
  (R2) lead_o = sum_v mhat_s_v N_v
                + [WinE(2x,G) - WinE(x+y,G)] WinB(y-1,L),

both remainders strictly positive.  Measured compensation
(best-of-two): worst 0.882, zero over-1 -- the remainder always
covers the negative matched minors.  The M1 quantitative pass is
the gap-2 pipeline at window level: per-minor coupled boxes +
compensation arithmetic (12% worst slack) + stratum certification.

THE BLOCK-MINOR MECHANISM (verified 534/534 identity,
186/186 mechanism, verify_993_block_minors.py): each matched minor
splits exactly as N_v = M_PQ + M_eQ + M_eP over the three aligned
blocks (Q = [x,y-1), P = [y-1,z-1), e = {z-1}; E-side shifted by
v).  Factorwise favorability F_B(s) >= F_E(s+v) across the span
makes the per-position E/B ratio increasing, hence the B-weighted
block averages ordered, hence all three minors nonnegative -- the
favorable half of M1 is proved modulo a four-line weighted-mean
write-up, with the remainder positive unconditionally.  The corner
half: mu-coupled boxes bound the ratio inversions against the
measured 0.882 compensation.  (Alignment guard: e_v = E(v+z-1),
NOT E(v+z) -- the misaligned split fails the mechanism at 100%.)

GRANULARITY FINDING (verify_993_minor_compensation.py): termwise
minor accounting cancels catastrophically (neg/pos to 9,338 at
corner shapes) -- the same failure mode as the uncoupled mu-box.
The M1 summation lemma must run at the WINDOW level: the mu-coupled
box applied to the full window-form lead_o (window-R's in place of
single R's), i.e. the gap-2 pipeline one level up.  The minor
expansion stands as the structural map, not the quantitative
granularity.

THE WEIGHTED-MEAN LEMMA (PROVED -- the favorable half of M1).
Let r(s) = E(s+v)/B(s) on [x, z-1].  If F_B(s) >= F_E(s+v) for all
s in [x, z-2], then r(s+1)/r(s) = F_B(s)/F_E(s+v) >= 1, so r is
nondecreasing; the block ratios lambda_i (B-weighted averages of r
over the ordered blocks Q = [x,y-1), P = [y-1,z-1), e = {z-1})
satisfy lambda_Q <= lambda_P <= lambda_e; and the three block
minors are positive multiples of their differences
(M_PQ = QB*PB*(lambda_P - lambda_Q), etc.), hence all nonnegative,
hence N_v >= 0.  QED  With the strictly positive remainder, lead_o
> 0 outright wherever every (v, span) is factorwise favorable.

THE ENVELOPE BOUND (corner half; form verified 209/209 with min
slack 3.16x, verify_993_envelope_bound.py): where minors go
negative, |N_v|^- <= Phi_v * lambda_max * (QB(PB+eB) + PB*eB) with
Phi_v the summed mu-box fall envelope -- the crude version already
over-covers 3x; the coupled boxes and suffix restriction tighten
further.  Against the remainder (measured compensation <= 0.882)
the stratum certification has compounded headroom.  M1 STATUS: the
favorable half proved; the corner half verified in form at every
joint, awaiting the constants write-up and stratum certification.

THE CORNER FALL BOUND (verified 2,772/2,772 both stages,
verify_993_corner_fall.py): per-step inversions obey the exact
gap-2 collapse 1 - F_B(s)/F_E(s+v) = (R3-R4)/((1+R3)(2+R4)) and sit
inside the mu-box envelope; the coupled (ML1/ML2) boxes bound them
tighter.  Corner-half assembly: summed envelopes -> block-minor
negativity bound (weighted-mean reversed) -> vs the remainder's
measured 12% slack -> stratum certification.

THE DRAG MARGINS (verify_993_drag_margins.py): all 64 tight
geometric-corner configs escape the pinch (M2: 56 below, M3: 8
above, zero inside; min escape margin 0.63%).  The drag proof
operates in the wide-separation regime (explicit kernel/pair-class
comparisons), with one thin stratum requiring exact terms.  With
this, EVERY mechanism of the four-condition inconsistency is
verified with measured budgets: M1 favorable (proved), M1 corner
(3.16x envelope slack), M2/M3 drag (escape uniform).

THE MECHANISM MAP (verify_993_mechanism_map.py ->
logs/993_mechanism_map.json): the four-condition inconsistency
splits into exactly three mechanisms, all 697 tight
not-two-cluster configs classified, zero exceptions:
  M1 (683 = 98%): the x-balances undercut the spread bound --
      S > min(B_b, B_o), the rho-interval is empty.  This is a
      division-CORE comparison in the window-mean variables; the
      CORE(gap 2) machinery (collapse to rational R-forms,
      mu-coupled boxes, quadrant Taylor-shift certification)
      applies pattern-for-pattern.
  M2 (6): rho-hat < S (drag below the pair-local level);
  M3 (8): rho-hat > B_om (drag above) -- both confined to the
      geometric-spacing corners ((a, ~3a, ~6a)-type shapes); the
      drag estimate compares the global ratio (kernel form, the
      x-bulk's low-K pairs) against the (y,z)-pair-local
      stationary level.
LEMMA A' PROOF PLAN, FINAL: prove M1's inequality on a region
covering all but an explicit corner (the CORE-pattern grind), and
the drag estimate on the corner.  Then Lemma A' + the three
certified families (27,492 instances) close rung 1 for all mixed
multisets within caps.

THE FOUR-MOVE DICHOTOMY -- FINAL FORM (verify_993_fourmove.py ->
logs/993_fourmove.json; supersedes the three-move version below):
at every tight NOT-two-cluster config (772 at extreme parameters,
zero failures), one of the four position moves improves:

    T_b = mid->bot, T_s = mid->top, T_o = top->bot, T_om = top->mid
    (carry: 413 / 198 / 150 / 11),

equivalently (linearized): the actual ratio never lies in the
stationarity interval [S, min(B_b, B_o, B_om)] formed by the one
spread lower-bound and three balance upper-bounds.  The three-move
set provably misses a corner ((16^14,48,96), k=189: rho = 0.8997
INSIDE [0.8855, 0.9163]; the improver is top->mid).  The division-
pair probe (verify_993_division_pair.py -> 993_division_pair.json)
showed INEQ1 OR INEQ2 carries 486/496 with the geometric-spacing
shapes needing the fourth bound.  PROOF OBLIGATION (the final
analytic core of Lemma A'): the four exact stationarity conditions
are jointly inconsistent at tight not-two-cluster configs --
i.e. rho outside the four-bound interval -- with the window-mean
machinery (ML1/ML2, coupling, coupled boxes) on the four bounds.

THE MIDDLE/OUTER DICHOTOMY (verify_993_middle_dichotomy.py ->
logs/993_middle_dichotomy.json): at 434 tight NOT-two-cluster
configs at extreme parameters (consecutive/spread/wide triples,
four-value shapes, h <= 40, C <= 700, k to 350), EVERY one admits
an improving transfer (zero local maxima -- Lemma A' holds at this
scale), and the drain map is: the middle pair T_b = (mid -> bot),
T_s = (mid -> top) covers 310/434; the remaining 124 are carried by
the OUTER balance T_o = (top -> bot) (all mapped failures are
top-gives/bot-recv).  Lemma A' proof obligation, pinned: the
THREE-MOVE dichotomy -- not T_b, not T_s, not T_o jointly
contradictory -- via two rho-cancelling stationarity divisions
(middle pair and outer pair), each a CORE-analog in the
window-mean variables; the A.1 toolkit applies to both.

EXTREME-PARAMETER CENSUS (verify_993_maximizer_census.py ->
logs/993_maximizer_census.json): exact hill-climbing at C <= 720,
k <= 400 (the ranges that broke the old classification), seeds
covering every shape that has ever appeared as a maximum plus
random: 255 distinct local maxima, ALL classified -- 63 one-cluster
+ 192 two-cluster, ZERO others (all tight).  Lemma A' is
census-hardened at scale.  Proof program: cluster-level drain
analysis (three clusters or an intra-cluster spread > 1 always
admits an improving transfer) + two-cluster family certification
(at fixed (k, h, p, q): bivariate in the two cluster values; or
univariate slices) + the now-load-bearing limit lemmas.

Two-value ceiling trend: worst rung-1 ratio on (v^p, M^q) climbs
with h (0.9535 / 0.9774 / 0.9887 at h = 24/48/96, at
(p,q,v,d) = (h-2, 2, 4, 128)) -- approaching 1 from below; the
ladder holds everywhere but per-family certification at scale
hinges on M-k-style limit lemmas (now load-bearing).

CONSEQUENCE FOR CORE(gap 2) (next section): it remains a TRUE,
fully-proved theorem on its domain, and its machinery (window-mean
identity, mu-coupling, coupled-box corners, quadrant Taylor-shift
certification) is THE established toolkit -- but it is no longer
on the critical path, since multi-giant configs need not be
excluded (they are certifiable shapes).  The critical path now
runs: systematic maximizer census -> two-cluster classification
proof (drain analysis at cluster level) -> two-cluster family
certification + limit lemmas.

## CORE(gap 2): PROVED (2026-06-13, end of session 16)

Assembly, every link proved or symbolically certified:
1. regrouping identity (G1)                       [exact algebra]
2. collapse to the rational form (*)              [exact; 80/80]
   -- including the (*) => CHAIN reduction step, which uses ML2
   twice (R4^0 - R4^2 <= 2/(k-4) <= 1 gives 1+R4^0 <= 2+R4^2) and
   the RHS drop (3+R4^0+R4^1) >= (2+R4^1) with slack factor >= 3/2;
3. window-mean identity + mu boxes                [proved; 120/120]
4. ML1, ML2                                       [PROVED above]
5. coupling mu4 <= mu3 - 1                        [ML1 + ML2]
6. piecewise-linearity => coupled-box corners     [structural]
7. branch X < 0 <= X + 2(k-3)                     [hand, via
   RHS_chain >= (k-4)(v(h-1) + 2q)]
8. branch X >= 0 = G >= 0:
   - Tail 1 (k > 12h): hand (v_band >= (3k-6h)/2h >= (k+3h)/h >= v_G)
   - five quadrant branches B1a/B1b/B2/B3a/B3b: ALL certified by
     multivariate Taylor-shift coefficient-nonnegativity with base
     shift h >= 3 (certify_993_G_tails.py ->
     logs/993_G_tails_certification.json) -- the symbolic
     certificates cover ALL parameters; the 33,245,001-case
     exhaustive sweep (verify_993_G_closure.py, h <= 200, zero
     failures) stands as independent cross-validation.

QUADRATIC CORRECTIONS (CORE => the exact A.1 dichotomy at gap 2):
the exact non-improvement conditions need CORE with multiplicative
margin (2W1 + B(M-1))/(2W1 - S_B); since S_B, B(M-1) <= A(v) <=
x(v)/2 (conditioning) and x(v+2) >= x(v)/4 (F <= 2), one gets
3 S_B + 2 B <= 2 W1 for all p >= 1, q >= 2, so the needed margin is
<= 3/2 -- exactly covered by the RHS-drop slack in step 2.  One
careful write-out pass threads the two 3/2's through matching
normalizations; every constant is in hand.

THE CHAIN (the uniform corner bound;
verify_993_tail_chain.py -> logs/993_tail_chain.json).  Dropping
two factors <= 1 from (*) and applying the coupled numerators plus
the worst-corner bound 1 + R3 >= (2C3 - v - k + 5)/(k - 3) yields
the single elementary inequality

  (CHAIN)  p X^+ + (q-2)(X + 2(k-3))^+
              <= (k-4)(v(2h-1) - k + 4q - 1),
           X := v(k-2-2h) + k + 1 - 4q .

Verified: CHAIN holds at ALL 3,024 in-band gap-2 multi-giant cases
(h <= 64, v <= 40, k <= 120) -- it is the uniform bound, not just
the tail -- and never disagrees with the exact corner check (zero
chain-but-not-corner, zero uncovered).  Hand proof status: the
in-band RHS positivity is closed (k <= kA <= C-1 <= v(2h-1)+4q-1);
the X >= 0 branch reduces to

  G := v[h(k+2h-10) + k] - (k+1-4q)(k+h-6) - 2(q-2)(k-3) >= 0

with h(k+2h-10)+k > 0 always, and the k+1-4q <= 0 sub-branch
contributing positively; the remaining sign bookkeeping (one
careful pass, possibly sympy-assisted over the constraint polytope)
is the LAST step before CORE(gap 2) is declared proved.

CORE(gap 2) ASSEMBLY: regrouping identity [proved] + collapse to
(*) [proved] + ML1, ML2 [PROVED] + coupling and corner reduction
[proved] + CHAIN [verified at every in-band case; hand pass
pending].  One bookkeeping pass from a theorem.

LEMMA A STATUS: both sub-cases pinned unconditionally at ~11,700
exact configs total, zero counterexamples, proof tools identified
(B/E log-concavity, telescoping, the exact stationarity system).
Gap-2 k=4 is PROVED, k=5 grid-certified; the general-k frontier is
the CORE regrouping above (one corner of D-sign analysis left).
The grind is bookkeeping-shaped, not idea-shaped.

EXCHANGE CENSUS AT SCALE (verify_993_exchange_census.py ->
logs/993_exchange_census.json): exact first-improvement
hill-climbing over single transfers, 43 (C,h,k) combos with h up to
24, C up to 128, k up to 64, ~18 starts each (bal, the spread
extreme, every giant seed, 12 random).  RESULT: 76 distinct local
maxima found, EVERY one classified -- 43 adjacent-two-value, 33
bulk+giant, ZERO others (in particular zero tight others).  Notable
negative: no mixed-bulk giant (a, a+1, ..., M) maximum ever appears
-- three-value configurations always drain.  The Lemma A statement
is census-hardened at the scale that killed DOM'.

Structural note for the Lemma A proof (next session): the giant's
stability is COLLECTIVE -- the pair (a, M) inside (a^{h-1}, M) is
an interior maximum of its pair-split path only because the bulk
holds the background fixed; single-pair split analysis cannot see
this, so the proof must work with the stationarity system of all
transfers at once (the exact conditions
(W2 + dW2) W1^2 <= W2 (W1 + dW1)^2 with the Delta-calculus above).

THE EXACT STATIONARITY SYSTEM (the Lemma A launch point; probe
verify_993_phi_field.py -> logs/993_phi_field.json).  For a unit
transfer from a slot at value u to a slot at value v, with
A(t) = f(t, C-t-1, k-2), dy(m) = f(m, C-m-1, k-3),
S_y(t) = sum_l dy(c_l + t):

    dW1 = A(u-1) - A(v),
    dW2 = [S_y(u-1) - S_y(v)]
          - dy(2u-1) - dy(u+v-1) + dy(u+v) + dy(2v),

and the local-max condition is dW2 W1^2 <= W2 (2 W1 dW1 + dW1^2),
exactly.  The naive first-order field PHI(t) = S_y(t) -
(2W2/W1) A(t) with the order condition PHI(u-1) <= PHI(v) is
directionally right (predicts an exact improving transfer at 81/107
probed non-maximal configs) but NOT sufficient: the four dy
exclusion corrections are large at small values (22/25 exact maxima
violate the uncorrected order condition; 27/132 PHI rows are
multi-valley).  The corrected analysis must carry the pair terms
-dy(2u-1) - dy(u+v-1) + dy(u+v) + dy(2v), whose signs and
monotonicity are governed by dy log-concavity = Lemma y-LC one
level down (k-3).  This exact system, plus y-LC and W-Schur, is the
full toolkit for the classification proof.

## Status

Lemma FL: PROVED (above).  The ladder (L_s): verified at 5,298
profiles (zero failures everywhere, including all 212 odd-argmax
cases) and CERTIFIED for all two-value multisets (h <= 10, k <= 28,
all a; 7,866 instances); binding rung s = 1.  Open: the DOM lemma
(above) and the cap-lifting limit lemmas.  The logical chain:

    DOM + two-value certificates  ==>  ladder (L_s)
    ==>  hypothesis (ii)  ==>  (with (i)) unimodality,

with rung 1 necessary for (ii): the ladder is tight at its base.

## The Newton tail machine (2026-06-13): infinite a-tails for
## gap-scaling strata, and the affine-direction cap-lifting pattern

The gap-scaling caveat is gone.  Yesterday's drag-strata run
closed (h, c2, c3, k) windows exactly but capped tails at 40 deep
because window LENGTHS grow with a ("not a single polynomial").
The length-uniform reformulation overturns that:

LEMMA (gap-scaling polynomiality; proof in 993_m1_proof.md Sec.
6.1).  comb(x, u) agrees at every integer x >= 0 with its
degree-u falling-factorial polynomial, so on {alpha, beta >= 0}
the kernel f agrees with a bivariate polynomial of total degree
m; all f-arguments in the window form stay in that region for
a >= 1; window sums over affine-in-a ranges are polynomial by
Faulhaber.  Hence lead_o(a) is ONE polynomial of degree
<= 2(k-1) for all a >= 1.

NEWTON CRITERION.  deg g <= N, D^i g(b) >= 0 (i <= N), g(b) > 0
==> g(b+t) = sum C(t,i) D^i g(b) > 0 for ALL integers t >= 0.

RUN (certify_993_drag_tails_poly.py ->
logs/993_drag_tails_poly.json): 18/18 strata closed for ALL
in-band a.  Stronger than asked: base b = a_min everywhere,
residues EMPTY -- at fixed k the gap-scaling strata are purely
M1 (drag binds only when k scales with kA(C(a))).  The exact
triangles show actual degree 2k-5 in all 18 (the collapse degree
drop, visible in data); every difference of order > 2(k-1)
vanishes exactly (machine confirmation of the degree bound,
3+XTRA zero rows per stratum).

PATTERN (cap lifting).  h enters lead_o affinely (C and
multiplicities affine, window positions h-free): lead_o(h) at
fixed (a, gaps, k) is a polynomial of degree <= 2k-6 -- the
identical triangle certifies h-tails, no Faulhaber needed.
Same for the gap direction d.  EVERY affine parameter direction
admits exact Newton tails; only the k-direction needs genuine
limit analysis.

h-TAILS RUN (same day; certify_993_h_tails.py ->
logs/993_h_tails.json): 39/39 lines closed for ALL h --
gap-scaling (a in {1,2}) and fixed-gap (a in {1,2,4}, gaps
(1,1)/(2,2)/(4,8)), k in {14,22,30}.  Base = h_min everywhere,
residues EMPTY (every in-band h is M1), actual degree exactly
2k-7 in all 39.  The fixed-gap h <= 16 cap is lifted along
these lines.  Tally: 57/57 one-parameter Newton lines (a- and
h-directions) had all differences nonnegative at their first
in-band point.

2D QUADRANT RUN (same day; certify_993_quadrant2d.py ->
logs/993_quadrant2d.json): 15/15 (line, k)-slabs closed on their
FULL 2D (a, h) in-band regions -- five value-lines x k in
{14,22,30}.  Every staircase corner certified at its own
position (zero shifts), zero residue anywhere: ALL mixed
differences D_a^p D_h^q lead are nonnegative at every in-band
corner, bivariate degree bounds confirmed by exact vanishing.
On these slabs the dichotomy is pure M1 at every in-band (a, h).

VERTEX REDUCTION (same day; PROVED -- 993_m1_proof.md Sec. 6.2).
lead_o is LINEAR in the multiplicity vector at fixed
(C, h, k, x, y, z): the B-windows D1O, D1S are multiset-free and
D2S, D2O are affine in m.  Hence over the transportation
polytope of backgrounds the minimum sits at a vertex = support
<= 2.  General multisets reduce EXACTLY to two-background-value
shapes (x, y, z, u^alpha, w^beta) -- no Schur step, no
approximation.  Machine checks
(verify_993_vertex_reduction.py): linearity 332/332 exact;
vertex-min 12/12 fully-enumerated polytopes; semantics 57/57
(lead_o > 0 ==> T_s or T_o strictly improves -- the division
calculus re-anchored).  The former beyond-grid compensation
obligation collapses to: certify the VERTEX family (all
parameter directions affine -> the Newton/quadrant machine
applies coordinate-wise), then the k-direction limit lemma as
the single analytic remainder of the M1 program.
