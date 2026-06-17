#!/usr/bin/env bash
set -euo pipefail

uv run pytest -q
uv run python notes/verify_993_band_B.py
uv run python notes/verify_993_band_B_threshold.py
uv run python scripts/check_reproducibility.py
if command -v lake >/dev/null 2>&1; then
  lake build
elif [ -x "$HOME/.elan/bin/lake" ]; then
  "$HOME/.elan/bin/lake" build
else
  echo "lake not found; install Lean via elan to run the formalization check" >&2
  exit 1
fi
uv run python scripts/check_formalization.py

if command -v tectonic >/dev/null 2>&1; then
  (cd paper && tectonic main.tex)
else
  echo "tectonic not found; skipping PDF rebuild" >&2
fi
