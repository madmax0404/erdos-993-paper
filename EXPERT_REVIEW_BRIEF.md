# Expert Review Brief

This is a pre-submission mathematical review request for the draft
`Unimodality of independence polynomials of hub spiders`.

## What I Need Reviewed

Please look for a fatal flaw in the main theorem proof, the reduction to the
flow concavity inequality, and the computational certificate interface.  The
most useful review is not copyediting; it is an attempt to break the proof.

The project was AI-assisted.  The public repository contains the paper source,
exact-arithmetic scripts, committed logs, reproducibility harnesses, and a
partial Lean formalization.  The author does not want to submit the paper
unless the core mathematics survives independent human review.

## Main Claim

The paper claims unconditional unimodality of the independence polynomials of a
listed finite/infinite scope of hub spiders:

- `h=1`, all arms;
- specified uniform families `S(c^h)`;
- eleven mixed two-hub spiders;
- sixteen three-hub adjacent-two-value spiders, including the first published
  non-log-concave trees `T_{3,4,4}` and `T_{3,3,4}`.

The broader all-parameter hub-spider statement is not claimed as proved.  It is
presented as conjectural/open.

## What Is Mechanically Checked

- `bash scripts/reproduce.sh` runs unit tests, selected exact verifiers, the
  log/certificate validator, `lake build`, the no-placeholder Lean guard, and
  the PDF rebuild when `tectonic` is available.
- `scripts/reproduce_all.py` regenerates paper-facing artifacts in a temporary
  worktree and compares them to committed outputs.
- Lean 4 checks:
  - coefficient-level formalization scaffolding;
  - algebraic certificate identities, including the `t`-cancellation pattern;
  - a generic Taylor-shift positivity checker for univariate integer
    polynomials;
  - 996 generated vertex-background E-core integer-polynomial positivity
    instances.

Important boundary: Lean checks the exported integer-polynomial certificates.
It does not yet independently derive those polynomials from the paper's bracket
formulas; that extraction is done by Python/SymPy.

## What Is Not Fully Theorem-Prover Verified

- The main theorem and reduction theorem.
- The T1/T2 certificate checker soundness.
- Enumeration completeness for every finite grid.
- The Band B threshold proof and finite residual interface.
- The ladder and bulk-plus-giant certificate families.
- The manuscript proofs of A0, A2, the epsilon calculus, the flow facts, and
  the two-hub mixed-arm theorem.

These are either manuscript proofs, exact-script checks, or both.  They need
human mathematical review.

## Suggested Review Path

1. Read the statement and proof of Theorem `thm:scope`.
2. Check the proof of Theorem `thm:reduction`, especially how the T1/T2
   certificates imply the master inequality.
3. Check Theorem `thm:a2`, the virtual ultra-log-concavity margin.
4. Check Lemma `lem:epsid`, the per-class growth bounds, and Proposition
   `prop:flow`.
5. Check the repaired uniform-scope route: the `p=h` factorial-ladder
   certificates, Proposition `prop:ladder`, and Theorem `thm:cert`.
6. Check the E-core vertex-background pipeline: Lemma `lem:slot`, the
   polynomial certification method, and the Python/SymPy bracket extraction.
7. Check Theorem `thm:h2mixed`, especially `t`-cancellation, Schur minimality,
   and the odd core.

The detailed inventory is in `CLAIM_INVENTORY.md`.

## Reproduction Commands

Fast check:

```bash
uv sync --dev
bash scripts/reproduce.sh
```

Full regeneration list:

```bash
uv run python scripts/reproduce_all.py --list
```

Full regeneration:

```bash
uv run python scripts/reproduce_all.py
```

Lean-only check:

```bash
lake build
uv run python scripts/check_formalization.py
```

Regenerate the Lean vertex-background E-core theorem instances:

```bash
uv run python scripts/generate_ecore_lean_certificates.py --jobs 16 --check
```

## Specific Questions for the Reviewer

1. Does Theorem `thm:reduction` have any hidden assumption or invalid use of
   the flow facts/certificate rows?
2. Does Theorem `thm:scope` actually cover exactly the families it claims?
3. Is Theorem `thm:a2` correct, including the virtual-degree bound and the
   absorption inequalities?
4. Does the factorial-ladder route prove the listed uniform cases without any
   hidden background-vertex assumption?
5. Is the E-core polynomial `R(c)` exactly the vertex-background bracket
   inequality stated in the paper for each generated instance?
6. Are the T1/T2 certificates sufficient to prove the master inequality in the
   way the manuscript states?
7. Are any empirical/search claims accidentally used as theorem inputs?

## Non-Goals

The review does not need to certify the open conjectures in Section `sec:open`
or endorse the broader all-hub-spider program.  The first goal is to determine
whether the current unconditional theorem claims are mathematically sound.
