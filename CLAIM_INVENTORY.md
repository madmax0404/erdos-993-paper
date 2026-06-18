# Claim Inventory for Independent Mathematical Review

This inventory is a pre-submission review aid.  It is not an independent
mathematical endorsement of the manuscript.  Its purpose is to show a reviewer
which claims are theorem-prover checked, which are exact-script checked, which
are manuscript proofs, and which are conjectural or empirical.

## Status Legend

- `Lean-checked`: checked by Lean 4 with no `sorry`, `admit`, or `axiom`.
- `Exact-script checked`: checked by committed Python/SymPy/Fraction scripts and
  committed logs, but the checker is not fully formalized in Lean.
- `Manuscript proof`: proved in the paper text; not mechanically checked except
  where noted.
- `Evidence`: computational search or structural evidence, not used as an
  unconditional theorem unless explicitly stated.
- `Conjectural/open`: stated as a conjecture or open work item.

## Trust Boundaries

- Lean currently proves the generic Taylor-shift polynomial certificate
  soundness theorem and 996 generated vertex-background E-core
  integer-polynomial certificate instances.
- The generated E-core Lean file checks positivity of the exported scaled
  integer polynomials.  Lean does not yet independently derive those polynomial
  coefficients from the hub-spider bracket formulas; that extraction is still
  done by Python/SymPy.
- The T1/T2 master-inequality certificates, Band B verifier, ladder
  certificates, giant certificates, and search/audit logs are exact-script
  checked, but their checker soundness and enumeration completeness are not
  fully formalized in Lean.
- The manuscript's main theorem and reductions are not fully theorem-prover
  verified.

## Main Theorems

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| Hub-spider definition and root decomposition `I(S)=F+xg` | Definition 1.1, equation (1) | Manuscript definition/algebra | Medium |
| Unconditional scope: listed hub spiders have unimodal independence sequences | Theorem `thm:scope` | Assembly of manuscript lemmas plus exact-script checks; not fully Lean-checked | Critical |
| Reduction to flow concavity plus certificate inequalities | Theorem `thm:reduction` | Conditional manuscript proof using exact-script certificate claims | Critical |
| E-core at `h=2`, uniform arms | Theorem `thm:h2` | Manuscript proof; supporting algebraic style suitable for formalization, but not fully Lean-checked | High |
| Flow concavity at `h=2`, arbitrary arms | Theorem `thm:h2mixed` | Manuscript proof; `t`-cancellation algebra is Lean-checked in abstract form, but the full theorem is not | High |
| Limit calculus for uniform all-`E` background | Theorem `thm:limit` | Manuscript calculus/asymptotic proof; not Lean-checked | Medium |
| Finite certification for the uniform ladder and vertex-background E-core | Theorem `thm:cert` | Uniform ladder is exact-script checked via the `p=h` subfamily of the adjacent-two-value certificates; vertex-background E-core polynomial positivity instances are Lean-checked after export; bracket-to-polynomial extraction remains Python/SymPy trusted | Critical |

## Reduction and Assembly Claims

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| Seam lemma: early log-concavity plus later decreasing zone implies unimodality | Lemma `lem:seam` | Manuscript proof | Medium |
| Band B threshold and finite residual verification | Section `sec:bandB` | Mix of manuscript inequalities and exact-script finite checks | Critical |
| Assembly of Theorem `thm:reduction` | Section `sec:assembly` | Manuscript proof dependent on T1/T2, flow facts, Band B, and decreasing-zone literature | Critical |
| Assembly of Theorem `thm:scope` | Section `sec:assembly` | Manuscript proof dependent on Theorems `thm:h2`, `thm:h2mixed`, `thm:cert`, ladder certificates, and grid membership | Critical |

## Analytic and Algebraic Lemmas

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| A0: `E_c + t b_c` is log-concave for `t in [0,2]` | Lemma `lem:a0` | Manuscript binomial-algebra proof | High |
| A2: virtual ultra-log-concavity of `H_c` with degree `c+1+ceil(c/30)` | Theorem `thm:a2` | Manuscript proof plus stated finite exact verification for `c <= 3000`; not Lean-checked | Critical |
| Closure of positive log-concave convolution | Lemma `lem:a1` | Classical result cited; proof sketch only | Medium |
| `h=1` log-concavity | Lemma `lem:d1` | Manuscript binomial-algebra proof | High |
| Epsilon identity and master inequality reduction | Lemma `lem:epsid` | Manuscript algebra proof | Critical |
| Ratio sandwich for `(1+x)^a(1+2x)^(C-a)` | Lemma `lem:e1` | Manuscript proof using likelihood-ratio order and citation | Medium |
| Exact window means | Lemma `lem:means` | Manuscript coefficient proof | Medium |
| Jensen floor and ceiling growth bounds | Lemma `lem:jensen` | Manuscript proof | High |

## Flow, Ladder, and Schur Claims

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| Flow facts from `phi'' <= 0` | Proposition `prop:flow` | Manuscript calculus/probability proof | High |
| Diagonal dominance identity and symmetric implication | Proposition `prop:dd` | Manuscript algebra proof; related cross-bracket inequalities partially Lean-checked | High |
| Pairwise split failures | Remark `rem:nopairwise` | Exact-script evidence and logged witnesses | Medium |
| Factorial criterion for flow log-concavity from ladder inequalities | Proposition `prop:ladder` | Manuscript proof using likelihood-ratio order | High |
| Schur-convexity of class masses | Proposition `prop:wschur` | Manuscript majorization/Karamata proof; mainly supports open-program discussion | Medium |

## E-Core and Two-Hub Lemmas

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| Slot expansion reducing pair-slot `E`/`E+2b` cases to the core case | Lemma `lem:slot` | Manuscript coefficientwise expansion proof | High |
| `t`-cancellation determinant identity | Lemma `lem:tcancel` | Manuscript proof; core algebra is Lean-checked in `CertificateAlgebra.lean` | High |
| Schur minimality of balanced split | Lemma `lem:schurS` | Manuscript coefficientwise proof | High |
| Odd core inequality | Lemma `lem:oddcore` | Manuscript proof plus exact finite verification statement; not Lean-checked | High |

## Certificate and Reproducibility Claims

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| T1/T2 master-inequality certificates over grid `G` | Section `sec:verification` | Exact-script checked; checker soundness not Lean-checked | Critical |
| E-core Taylor-shift certificate method | Section `sec:polyc` | Generic positivity checker Lean-checked; 996 generated vertex-background E-core integer-polynomial instances Lean-checked | Critical |
| Uniform factorial-ladder certificates | Section `sec:verification`, Theorem `thm:cert` | Exact-script checked; the `p=h` subfamily covers all uniform rungs for `3 <= h <= 10`, `k <= 28` | Critical |
| Audit report found and repaired two implementation flaws with unchanged headline figures | Section `sec:audit`, notes | Exact-script/audit documentation | Medium |
| Ladder scans: 5,298 profiles, zero rung failures | Section `sec:audit` | Exact-script evidence | Medium |
| Adjacent-two-value ladder certificates: 7,866 instances | Section `sec:audit` | Exact-script checked; not Lean-checked | High |
| Bulk-plus-giant certificates: 1,512 instances | Section `sec:open` and logs | Exact-script checked; not Lean-checked | Medium |

## Extremal and Search Claims

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| Balance definition and relation to width-one valleys | Definition `def:balance` | Manuscript definition/observation | Low |
| Offset law for uniform hub spiders in searched range | Section `sec:extremal` | Search evidence, not a theorem for all parameters | Medium |
| High-fragility 48-vertex witness and beam-search claims | Section `sec:extremal` | Search evidence with committed logs | Medium |
| Decreasing-zone protection and mechanism discussion | Section `sec:extremal` | Manuscript heuristic/structural explanation plus inequalities | Medium |
| Forest product scans through total size 64 | Section `sec:extremal` | Search evidence | Low |

## Conjectures and Open Work

| Claim | Location | Current status | Review priority |
| --- | --- | --- | --- |
| Flow concavity for all hub spiders | Conjecture `conj:ecore` | Conjectural/open | Critical if reviewer evaluates the broader program |
| T1/T2 certificates for all parameters | Conjecture `conj:g2` | Conjectural/open | Critical if reviewer evaluates the broader program |
| Gadget dichotomy and broader tree extensions | Open question | Open | Low for current unconditional scope |
| Exchange lemma / domination program for all hub spiders | Section `sec:open` | Open program supported by exact probes | Medium |

## Suggested Expert Review Order

1. Check whether Theorem `thm:scope` really follows from Theorem
   `thm:reduction` plus the stated grid/certificate coverage.
2. Check the reduction proof: Lemma `lem:epsid`, the charge decomposition,
   Proposition `prop:flow`, and the T1/T2 certificate interface.
3. Check Theorem `thm:a2`, since it supplies the quantitative margin used
   throughout.
4. Check the repaired uniform-scope chain: the `p=h` ladder certificates,
   Proposition `prop:ladder`, and Theorem `thm:cert`.
5. Check the `h=2` arbitrary-arm proof, especially the use of
   `t`-cancellation, Schur minimality, and the odd core.
6. Check the E-core vertex-background certificates and whether the Python/SymPy
   coefficient extraction matches the bracket formulas.
7. Treat the extremal/search section as supporting context unless the reviewer
   wants to audit the broader open program.
