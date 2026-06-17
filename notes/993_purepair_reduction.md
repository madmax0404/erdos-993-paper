# Pure-pair reduction of the weighted E-core, and mixed h=2

Part of `notes/993-hub-spider-unimodality-program.md` (session 15).
Companion script: `notes/verify_993_purepair_reduction.py`, log:
`logs/993_purepair_reduction.json`.

HEADLINE: the weighted per-pair E-core (the session-14 reform) is
REFUTED below by honest in-band instances; the correct and final form
of the hypothesis is the AGGREGATE flow concavity (ii-agg), which
passes every scan with margin and coincides with the certified
symmetric form at uniform multisets.  Lemmas L1/L2 and Theorem L3 are
proved and survive; with the odd core (proved at the end of this
note) L3 covers ALL h = 2 arms, closing hypothesis (ii) at h = 2
completely and extending the unconditional scope to 66 families
beyond h = 1 (the eleven mixed h=2 grid members join).

Throughout, slots i != j carry b_i = x(1+x)^{c_i}, E_i = (1+2x)^{c_i},
A_i = E_i + t b_i, and W is the background (the product of the other
h-2 slot polynomials, arbitrary unless stated).  All brackets [.]_k
are coefficient extractions at x^k.  The weighted E-core (paper
hypothesis (ii), as of session 14) is

    (ii)  [b_i b_j W]_k [A_i A_j W]_k
            <= X Y + (X^2 + Y^2) / (2(h-1)),
          X = [b_i A_j W]_k,  Y = [b_j A_i W]_k,

needed for k in band A, on the diagonal A_l = E_l + t b_l, t in [0,2].

## Lemma L1 (t-cancellation: the pair-slot parameter is removable)

**Lemma.**  Fix ANY background W (any polynomial; in particular any
mixed per-slot diagonal values).  Write

    P = [b_i b_j W]_k,   Q0 = [E_i E_j W]_k,
    X0 = [b_i E_j W]_k,  Y0 = [b_j E_i W]_k.

Then for every t,

    [b_i b_j W]_k [A_i A_j W]_k - [b_i A_j W]_k [b_j A_i W]_k
        = P Q0 - X0 Y0,

independent of t.

**Proof.**  Brackets are linear in each slot polynomial, so

    [A_i A_j W] = Q0 + t (X0 + Y0) + t^2 P,
    [b_i A_j W] = X0 + t P,   [b_j A_i W] = Y0 + t P.

Expanding, P[A_iA_jW] - [b_iA_jW][b_jA_iW]
= P Q0 + tP(X0+Y0) + t^2 P^2 - (X0Y0 + tP(X0+Y0) + t^2 P^2)
= P Q0 - X0 Y0.  Equivalently, the 2x2 matrix
M(t) = [[P, Y], [X, Q]] satisfies M(t) = (I + t e2 e1^T) M(0)
(I + t e1 e2^T), a unipotent congruence, which preserves the
determinant.  QED.

**Corollary (pure-pair form).**  Since X = X0 + tP >= X0 and
Y = Y0 + tP >= Y0 (all brackets nonnegative), the right side of (ii)
is nondecreasing in the pair-slot t while the left-minus-XY defect is
constant.  Hence (ii) at slot-t = 0,

    (ii')  P Q0 - X0 Y0 <= (X0^2 + Y0^2) / (2(h-1)),

with the SAME background W, implies (ii) for all slot-t >= 0.
Conversely (ii') is the slot-t = 0 instance of (ii).  So hypothesis
(ii) on the diagonal is equivalent to the one-parameter family

    { (ii') with W = prod_{l != i,j} (E_l + t b_l) : t in [0, 2] },

and the pair slots can always be taken PURE (b's against E's).  This
also explains why the verification sweeps always found their worst
ratios at t = 0: in the slot direction the defect is flat and the
budget grows.

## The all-E normal form (**)

At t = 0 the background is degree-blind: W = (1+2x)^A with
A = sum of the background degrees.  Every bracket is then a
coefficient of a two-base product; with
f_{alpha,beta}(m) = [x^m](1+x)^alpha (1+2x)^beta and s = c_i + c_j:

    P  = f_{s, A}(k-2),        Q0 = 2^k C(s+A, k),
    X0 = f_{c_i, c_j+A}(k-1),  Y0 = f_{c_j, c_i+A}(k-1).

Since the budget denominator 2(h-1) is worst when h is largest, and
h-2 <= A (background slots have degree >= 1, with equality iff the
background is all-ones), the t = 0 case of (ii) for ALL multisets
reduces to the four-integer-parameter family

    (**)  f_{s,A}(k-2) 2^k C(s+A,k) - f_{c_i,c_j+A}(k-1) f_{c_j,c_i+A}(k-1)
            <= [ f_{c_i,c_j+A}(k-1)^2 + f_{c_j,c_i+A}(k-1)^2 ] / (2(A+1)).

(** ) at denominator A+1 is an honest instance of (ii) -- the multiset
(c_i, c_j, 1^A) -- not a strengthening, and it implies every smaller-h
instance with the same A.  Note (1+x)^alpha (1+2x)^beta is real-rooted,
so every bracket in (**) sits in an ultra-log-concave row.

## Lemma L2 (Schur-S: balanced split is the coefficientwise minimum)

For a + b = s let S(a,b) = (1+x)^a (1+2x)^b + (1+x)^b (1+2x)^a.

**Lemma.**  For a < b (so a+1 <= b-1 makes sense when b-a >= 2),

    S(a, b) - S(a+1, b-1) = x [(1+x)(1+2x)]^a
                              [ (1+2x)^{b-a-1} - (1+x)^{b-a-1} ]  >= 0

coefficientwise.  Hence the coefficients of S are minimized over the
splits of s at the balanced one: (s/2, s/2) for even s, and
((s-1)/2, (s+1)/2) for odd s.

**Proof.**  With d = b - a, S(a,b) = [(1+x)(1+2x)]^a T_d where
T_d = (1+x)^d + (1+2x)^d, so

    S(a,b) - S(a+1,b-1) = [(1+x)(1+2x)]^a [ T_d - (1+x)(1+2x) T_{d-2} ],

and T_d - (1+x)(1+2x)T_{d-2}
= (1+x)^{d-1}[(1+x)-(1+2x)] + (1+2x)^{d-1}[(1+2x)-(1+x)]
= x[(1+2x)^{d-1} - (1+x)^{d-1}], which has nonnegative coefficients
because (1+2x)^{d-1} dominates (1+x)^{d-1} coefficientwise.  QED.

## Theorem L3 (mixed h=2 weighted E-core, even total degree)

**Theorem.**  Let h = 2 with arms (c_1, c_2), s = c_1 + c_2 EVEN.
Then for all k >= 2,

    [b_1 b_2]_k [A_1 A_2]_k <= X Y + (X^2 + Y^2)/2,

i.e. (ii-agg) holds at h = 2 (the aggregate IS the single-pair
inequality there); equivalently the flow-box concavity phi'' <= 0
(the only DD input the h = 2 pipeline uses) holds for S(c_1, c_2)
along the whole demotion flow.

**Proof.**  At h = 2 there is no background, so W = 1 is t-free and
Lemma L1 reduces to slot-t = 0:

    2 [b_1 b_2]_k [E_1 E_2]_k <= (X0 + Y0)^2

(the right side because XY + (X^2+Y^2)/2 = (X+Y)^2/2).  Here
[b_1 b_2]_k = C(s, k-2), [E_1 E_2]_k = 2^k C(s, k), and

    X0 + Y0 = [x S(c_1, c_2)]_k = [x^{k-1}] S(c_1, c_2)
            >= [x^{k-1}] S(s/2, s/2) = 2 [x^{k-1}] (1+3x+2x^2)^{s/2}

by Lemma L2.  The uniform core (notes/993_p6_h2_proof.md, proved for
all c, k) states exactly

    C(2c, k-2) 2^k C(2c, k) <= 2 ( [x^{k-1}] (1+3x+2x^2)^c )^2

with c = s/2, i.e. 2 C(s,k-2) 2^k C(s,k) <= (2 [x^{k-1}](1+3x+2x^2)^{s/2})^2.
Chaining the two displays gives the claim.  QED.

**Odd s: the odd core, PROVED (2026-06-12, later the same day).**
The same chain needs the "odd core"

    2 C(s, k-2) 2^k C(s, k) <= U^2,
    U = U_{k-1} = 2 T_{k-1} + 3 T_{k-2},
    T_n = [x^n](1+3x+2x^2)^m,  m = (s-1)/2,

since the balanced split for odd s is ((s-1)/2, (s+1)/2) and
S((s-1)/2, (s+1)/2) = (1+3x+2x^2)^{(s-1)/2} (2+3x).

**Proof.**  For k > s the left side vanishes; let 2 <= k <= s and put
a = C(2m, k-2) >= 1, b = C(2m, k-1) >= 1.

1. Pascal + log-concavity of the row C(2m, .):
   C(s,k-2) = a + C(2m,k-3) <= a(1 + a/b)  [C(2m,k-3)/a <= a/b], and
   C(s,k)   = b + C(2m,k)   <= b(1 + b/a)  [C(2m,k)/b <= b/a], so

       C(s,k-2) C(s,k) <= a(a+b)/b * b(a+b)/a = (a+b)^2.

2. The even-core bound (AM-GM + Vandermonde, already proved):
   T_n >= 2^{n/2} C(2m, n); hence

       U >= 2 * 2^{(k-1)/2} b + 3 * 2^{(k-2)/2} a
         = 2^{k/2} ( sqrt2 * b + (3/2) a )
         >= 2^{k/2} * sqrt2 * (a + b),       because 3/2 > sqrt2.

3. Squaring, U^2 >= 2^{k+1} (a+b)^2 >= 2^{k+1} C(s,k-2) C(s,k).  QED

The constant 3 from T_1 = 2 + 3x is exactly what makes step 2 work:
3/2 = 1.5 > sqrt2 = 1.414...; a balanced split with cross term 2.8x
instead of 3x would fail.  All k >= 2, no band restriction, like the
even case.  Every step verified exactly for m <= 80 (s <= 161), all
k: notes/verify_993_oddcore.py, logs/993_oddcore.json (zero
failures).

**Theorem L3 (final form).**  For h = 2 and ALL arms (c_1, c_2), the
flow concavity phi'' <= 0 holds on the whole flow box at every
position k.  (Even s: the chain above with the even core; odd s: with
the odd core.)

## REFUTATION: the weighted per-pair E-core is FALSE

The danger scans found honest, in-band violations of (ii)/(**)
(exact arithmetic; logs/993_purepair_reduction.json):

- Smallest witness: the 107-vertex spider S(1, 27, 1^16) (h = 18,
  C = 44), k = 5, t = 0: defect/budget = 1.0110.  Violations appear
  throughout the dense range (84 in s <= 28, A <= 24; all have
  a <= 3, A >= 16, k in {5,6,7}; worst 1.177 at (1,27,1^24), k=6).
- (c,c,1^A): 62 violations (c >= 64, A >= 20, k in [4,10]),
  worst 2.530 at (128,128,1^192), k = 7.
- Rays: worst 7.509 at (1,128,1^256), k = 10.
- (c,c,m^u) with m >= 2: ZERO violations in the scanned range -- the
  failure mode needs many DEGREE-1 background slots (h large at fixed
  background degree A; the uniform 1/(h-1) budget then starves the
  heavy pair while the (1,1)-pairs massively underdraw).
- The original reform sweep missed this because it capped h at 8
  (A <= 6); the violations start around A ~ 16.

Both pairwise budget choices are now refuted (symmetric: session 14;
weighted (x_i^2+x_j^2)/(2(h-1)): here).  The per-pair decomposition
itself is the wrong device at 1-heavy backgrounds.

## REFORM: aggregate flow concavity (what DD actually needs)

The pipeline only ever uses phi''(t) <= 0, i.e. the AGGREGATE

    (ii-agg)   (G')^2 - G G'' >= 0,  G(t) = [prod_i (E_i + t b_i)]_k
    <=>  sum_{i!=j} (G y_ij - x_i x_j) <= sum_i x_i^2,

for k in band A, t in [0,2].  The per-pair forms were sufficient
devices for (ii-agg); (ii-agg) itself survives everything
(logs/993_aggregate_dd.json, all exact, t in {0,1/2,1,3/2,2}):

- All 200 per-pair violation witnesses: aggregate PASSES at every t;
  worst margin ratio -2.55 (defect strongly negative).
- (c,c,1^A) grid (c <= 128, A <= 256): 0 violations, worst +0.0847.
- Rays (1,c,1^A), (2,c,1^A) (c <= 128, A <= 256): 0 violations,
  worst -0.0094.
- 40 random mixed multisets (h <= 10, c_i <= 12): 0 violations,
  worst +0.0461.
- A -> infinity probes (A <= 1024): ratio decreases to ~ -5.31; the
  aggregate margin GROWS where the per-pair split dies.
- Uniform sanity: at (c^h) the aggregate ratio EQUALS the symmetric
  per-pair ratio (split exact by symmetry) -- 0 mismatches.  Hence
  the 996 polynomial-in-c certified instances, the h = 2 theorem, and
  the limit lemma are already proofs of (ii-agg) at uniform multisets.

(ii-agg) is the new hypothesis (ii) normal form.  At h = 2 it IS the
single-pair inequality, so Theorem L3 below is an unconditional
instance (mixed arms, even total degree).

## Scope consequence of Theorem L3

The certificate grid contains eleven mixed h=2 multisets: four of
even total degree -- (2,4), (6,8), (6,12), (10,12) -- and seven of
odd total degree -- (1,8), (3,4), (4,7), (4,9), (4,11), (7,8),
(11,12).  For all eleven, hypothesis (i) is grid-verified (max
certificate ratio 0.194), hypothesis (ii) is Theorem L3 (final form,
both parities), and band B is empty at h = 2
(k_dec <= ceil((2C+3)/3) <= C for C >= 3), so the reduction theorem
applies unconditionally: the eleven mixed spiders (n from 15 to 49)
are the first mixed-arm members of the certified scope; the count
beyond h=1 goes 55 -> 66.  End-to-end checks (grid membership +
ratios + band-B emptiness + brute-force unimodality):
notes/verify_993_h2mixed_scope.py -> logs/993_h2mixed_scope.json
(even four); notes/verify_993_oddcore.py -> logs/993_oddcore.json
(odd seven + the proof steps).

## Other scan verdicts

- t-cancellation (L1): 200 random instances (mixed per-slot
  backgrounds, rational slot-t), zero failures.
- Cross-check: (1,64,1^6), k = 4 reproduces the reformed-sweep worst
  ratio 0.7870.
- Schur-S monotonicity and factorization: zero failures (s <= 40).
- Even-core regression: zero failures (worst 0.5218; proved).
- Odd-core candidate: ZERO failures, worst 0.5217 at the same
  strength as the even core (and PROVED later the same day; see the
  L3 section above).
- Diagonal-t profiles: 28/99 per-pair profiles peak at t > 0 (so the
  old "t = 0 worst" heuristic was a small-h artifact; moot for the
  aggregate, whose scans cover the t-grid).
- Per-slot convexity probe: 408/408 instances CONCAVE in each
  background slot's t (box-vertex reduction is NOT available for the
  per-pair form; also moot now).
