# Erdős 993 Current Integration Audit

This is the current proof-state snapshot after the adaptive terminal-block
handoff work and the later `w=1` E4 residual closure.

## Closed Now

The hard near-terminal Lambda branch has a coherent proof package.

- `L>=0`: closed by the refined summed/run allocation in
  `notes/summed-jump-bound-lemma.md`.
- `L<0`: closed by the shifted piecewise allocation in
  `notes/piecewise-terminal-block-lemma.md`.
- The branch splice is stated in
  `notes/adaptive-terminal-block-handoff.md`.
- A clean theorem/proof draft is in
  `notes/adaptive-terminal-block-proof-draft.md`.

The old adaptive pointwise scalar target is false and is now marked as legacy
in `notes/verify_boundary_variation_generic_barrier.py`.  Future proof checks
for the hard terminal branch should use
`notes/verify_boundary_variation_terminal_handoff.py`.

The current repeatable checks are:

- `logs/993_boundary_variation_piecewise_terminal_block_algebra.log`;
- `logs/993_boundary_variation_handoff_identities.log`;
- `logs/993_boundary_variation_terminal_handoff_coefficients.log`;
- `logs/993_boundary_variation_terminal_handoff_coefficients_wide.log`.

The wide handoff verifier checked degrees `13..80`, `80` generated factors
per degree, plus frontier and explicit families, for `7,126` total factors.

The hard `w=1` E4 residual in the `m=2` append-adjacent lower-endpoint
reduction is now closed as a separate exact certificate package.  The compact
audit is in `notes/993-w-one-e4-cover-audit.md`, with the chronological log in
`notes/993-w-one-face-progress.md`.  The final cover uses:

- exact `N<0` infeasibility for `C >= 121/128`;
- exact `N<0` base-root and one-step `C` split covers reducing to 14 child
  collars;
- exact NH bridge certificates on `Z=[1/65536,1/32768]`;
- exact finite-`Z` quotient and `N<0` certificates on `Z=[0,1/65536]`.

The conclusion for that component is: the finite residual produced by the
`w=1` E4 analysis has no remaining open child boxes.

## How This Fits The Monic Product Program

The monic product program begins with factors

`P=(1,p_1,...,p_{m-1},1)`,

log-concave through the penultimate coefficient and with decreasing final
tail.  Product unimodality is reduced to the adjacent implication

`D_{k+1}>0 => D_k>=0`.

If the final monic endpoint were fully log-concave, this would follow from
the sliding lemma.  The only obstruction is the endpoint-defect case.  That
case is transformed into a local sign-change problem for

`theta_i=delta_{k+1-i}`.

The terminal-block handoff closes the stable near-terminal Lambda branch that
appears after the corrected-variation reductions.  It replaces the false
claim that every terminal index has a pointwise combined reserve by a global
branch reserve:

- for `L>=0`, prove `GN-yV>0`;
- for `L<0`, prove `CK>V`.

This is an actual proof upgrade, not just more evidence.

## Still Live

There are two different kinds of remaining work.

First, within the monic product closure program, the upstream endpoint-defect
proof is not yet a single finished theorem.  The note
`notes/monic-product-closure.md` contains many historical branches.  Some are
proved, some are superseded, and some remain live.  The most important live
thread appears to be the general early-plateau/lower-branch slope invariant,
recorded in the older notes as the endpoint-credit, S-bound, or power-curve
target.  In short, the terminal handoff closes the hard near-terminal block,
but the global proof still needs a clean dependency chain showing that every
endpoint-defect case reaches either:

- an already proved early-plateau branch;
- the general slope/endpoint-credit invariant;
- or the now-closed terminal handoff.

Second, even a finished monic product closure theorem would still not be the
full Erdős 993 result by itself.  The original note explicitly warns that
general tree independence polynomials need not be monic.  So after the monic
closure theorem is complete, there is still a separate bridge to the actual
problem statement unless the problem has been reduced to the monic class in a
different note.

## Recommended Next Step

The first dependency audit is now in
`notes/endpoint-credit-dependency-audit.md`.  It confirms that several
`m=2` endpoint-credit branches that still appear as "next targets" in the
chronological monic note were later closed by certificate scripts.  The
remaining useful task is no longer broad random search.  The current sharp
frontier inside the structured `m=2 -> m=3` append package is the upper cap
surface

`R=1/sqrt(rho_1^2 rho_2)`.

It is isolated in `notes/993-m2-append-cap-surface-progress.md`: direct
Bernstein fails, and low-degree LPs using the two cap feasibility slacks plus
the old S-bound slack improve but do not close.

There are now three focused proof-integration tasks:

1. Wrap the existing `m=2` adjacent-ratio endpoint-credit certificate forest
   into one callable theorem.
2. Close the `m=2 -> m=3` upper cap-surface endpoint.
3. Preferably, prove the structural prospective S-bound append lemma isolated
   in the audit:

   `(M,S,U) -> (R M-(R-1)G, R S+G, U+G)`.

This should tell us whether the monic product closure is close to a complete
proof, or whether the main remaining difficulty is still upstream of the
terminal block.
