#!/usr/bin/env bash
set -euo pipefail

uv run pytest -q
uv run python notes/verify_993_band_B.py
uv run python notes/verify_993_band_B_threshold.py
uv run python scripts/check_reproducibility.py

if command -v tectonic >/dev/null 2>&1; then
  (cd paper && tectonic main.tex)
else
  echo "tectonic not found; skipping PDF rebuild" >&2
fi
