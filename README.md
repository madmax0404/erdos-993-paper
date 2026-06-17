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
- `scripts/check_reproducibility.py`: validates the committed logs against the
  headline counts used in the manuscript.
- `scripts/reproduce.sh`: runs the fast reproducibility checks and rebuilds the
  PDF when `tectonic` is installed.

## Quick Reproduction

Install dependencies with `uv`, then run:

```bash
uv sync --dev
bash scripts/reproduce.sh
```

The script runs:

```bash
uv run pytest -q
uv run python notes/verify_993_band_B.py
uv run python notes/verify_993_band_B_threshold.py
uv run python scripts/check_reproducibility.py
```

If `tectonic` is available, it also rebuilds `paper/main.pdf`.

For a section-by-section map from manuscript claims to scripts and committed
logs, see `REPRODUCIBILITY.md`.

## Longer Certificate Scripts

The repository also includes scripts for the larger exact certificates and
structural scans, for example:

```bash
uv run python notes/extract_993_M_dual_certificates.py
uv run python notes/certify_993_ecore_polyc.py
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
```

Some of these are slower than the quick reproduction path.  The committed
`logs/` files are the paper-facing outputs used by the manuscript.

## AI-Use Declaration

The manuscript includes an AI-use declaration.  AI tools, including Claude
(Anthropic), assisted with proof exploration, drafting, code development, and
audit, but are not listed as authors.  The human author takes responsibility for
the manuscript, proofs, verification code and data, and final approval.
