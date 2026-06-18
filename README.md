# Erdős 993 Hub-Spider Paper

This repository contains the public paper and reproducibility package for
`Unimodality of independence polynomials of hub spiders`.

## Contents

- `paper/main.tex`: manuscript source.
- `paper/main.pdf`: compiled manuscript.
- `src/erdos993/`: small independence-polynomial library used by the checks.
- `tests/`: unit tests for the polynomial/tree utilities.
- `notes/`: curated exact-arithmetic verification scripts used for the paper.
- `logs/`: paper-facing JSON certificate and audit outputs.
- `REPRODUCIBILITY.md`: claim-to-artifact map for the manuscript.
- `FORMALIZATION.md`: Lean formalization status and build instructions.
- `CLAIM_INVENTORY.md`: pre-submission map from paper claims to verification
  status and trust boundaries.
- `EXPERT_REVIEW_BRIEF.md`: short brief for independent mathematical review.
- `formal/`: Lean 4 sources for the checked formal surface.
- `scripts/check_reproducibility.py`: validates the committed logs against the
  headline counts used in the manuscript.
- `scripts/reproduce_all.py`: regenerates paper-facing artifacts in a temporary
  copy and compares them with the committed outputs.
- `scripts/export_ecore_poly_certificate.py`: exports exact polynomial
  certificate data for the Lean Taylor-shift checker.
- `scripts/generate_ecore_lean_certificates.py`: regenerates the Lean theorem
  instances for the 996 committed E-core polynomial certificates.
- `scripts/reproduce.sh`: runs the fast reproducibility checks and rebuilds the
  PDF when `tectonic` is installed.

## Quick Reproduction

Install dependencies with `uv`, then run:

```bash
uv sync --dev
bash scripts/reproduce.sh
```

The fast path now also builds the Lean project. Install Lean with `elan` first
if `lake` is not already available; Lake will fetch the pinned Mathlib
dependency from `lake-manifest.json`.

The script runs:

```bash
uv run pytest -q
uv run python notes/verify_993_band_B.py
uv run python notes/verify_993_band_B_threshold.py
uv run python scripts/check_reproducibility.py
lake build
uv run python scripts/check_formalization.py
```

If `tectonic` is available, it also rebuilds `paper/main.pdf` with a fixed
`SOURCE_DATE_EPOCH` unless that variable is already set.

For a section-by-section map from manuscript claims to scripts and committed
logs, see `REPRODUCIBILITY.md`.

## Full Regeneration

The complete regeneration harness copies the repository to a temporary
worktree, reruns the paper-facing generators, and compares regenerated outputs
to the committed logs after normalizing timing fields:

```bash
uv run python scripts/reproduce_all.py --list
uv run python scripts/reproduce_all.py
```

The full run includes exact symbolic certificates and structural searches, so
it is substantially slower than `scripts/reproduce.sh`.

The generated Lean E-core certificate file can also be refreshed directly:

```bash
uv run python scripts/generate_ecore_lean_certificates.py --jobs 16
```

## Longer Certificate Scripts

The repository also includes scripts for the larger exact certificates and
structural scans, for example:

```bash
uv run python notes/extract_993_M_dual_certificates.py
uv run python notes/extract_993_M_dual_certificates.py --ext
uv run python notes/certify_993_ecore_polyc.py
uv run python notes/certify_993_ecore_polyc.py --h-min 8 --h-max 10 --k-min 2 --k-max 20 --out 993_ecore_polyc_ext.json
uv run python notes/certify_993_ecore_polyc.py --topup
uv run python notes/verify_993_h2mixed_scope.py
uv run python notes/verify_993_oddcore.py
uv run python notes/verify_993_aggregate_dd.py
uv run python notes/verify_993_purepair_reduction.py
uv run python notes/verify_993_factorial_ladder.py
uv run python notes/verify_993_ladder_schur_step.py
uv run python notes/certify_993_ladder_polyc.py 3 10 28 993_ladder_polyc_h3-10_k28.json
uv run python notes/certify_993_giant_polyc.py
uv run python notes/verify_993_giant_vs_bal.py
uv run python notes/verify_993_exchange_census.py
uv run python notes/verify_993_bush_sweep.py
uv run python notes/search_993_junction_beam.py --gadget-max 11 --beam 200 --max-n 170 --tag beam11 --no-hub-seed
uv run python notes/search_993_junction_beam.py --gadget-max 11 --beam 200 --max-n 170 --tag beam11seed
uv run python notes/search_993_forest_pair_products.py --exhaustive-max 10 --corona-base-max 7 --spine-max 8 --random-leg-patterns 4 --random-trees-per-n 5 --top-pool 400 --random-pairs 100000 --tag smoke3
```

Some of these are slower than the quick reproduction path.  The committed
`logs/` files are the paper-facing outputs used by the manuscript.

## AI-Use Declaration

The manuscript includes an AI-use declaration.  AI tools, including Claude
(Anthropic) and ChatGPT/Codex (OpenAI), assisted with proof exploration,
drafting, code development, and audit, but are not listed as authors.  This
draft is being prepared for independent mathematical review; for any submitted
version, the human author is responsible for the manuscript, proofs,
verification code and data, and final approval.
