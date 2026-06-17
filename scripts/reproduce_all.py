"""Regenerate and compare every paper-facing reproducibility artifact.

The fast `scripts/reproduce.sh` validates committed artifacts.  This script is
the heavier path: it copies the repository to a temporary worktree, reruns the
generators, and compares generated artifacts back to the committed files.
Timing fields are normalized away before comparison.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

IGNORE_NAMES = {
    ".git",
    ".lake",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "__pycache__",
    ".venv",
    "venv",
}

JSON_DROP_KEYS = {"elapsed_seconds"}

COMMANDS: list[tuple[str, list[str], list[str]]] = [
    ("unit tests", ["uv", "run", "pytest", "-q"], []),
    ("M dual certificates", ["uv", "run", "python", "notes/extract_993_M_dual_certificates.py"], ["logs/993_M_dual_certificates.json"]),
    ("M dual certificates extended", ["uv", "run", "python", "notes/extract_993_M_dual_certificates.py", "--ext"], ["logs/993_M_dual_certificates_ext.json"]),
    ("E-core certificates", ["uv", "run", "python", "notes/certify_993_ecore_polyc.py"], ["logs/993_ecore_polyc_certification.json"]),
    (
        "E-core extended certificates",
        [
            "uv",
            "run",
            "python",
            "notes/certify_993_ecore_polyc.py",
            "--h-min",
            "8",
            "--h-max",
            "10",
            "--k-min",
            "2",
            "--k-max",
            "20",
            "--out",
            "993_ecore_polyc_ext.json",
        ],
        ["logs/993_ecore_polyc_ext.json"],
    ),
    ("E-core top-up certificates", ["uv", "run", "python", "notes/certify_993_ecore_polyc.py", "--topup"], ["logs/993_ecore_polyc_topup.json"]),
    ("Band B verifier", ["uv", "run", "python", "notes/verify_993_band_B.py"], ["logs/993_band_B_verification.json"]),
    ("Band B threshold verifier", ["uv", "run", "python", "notes/verify_993_band_B_threshold.py"], ["logs/993_band_B_threshold.json"]),
    ("A0 prime/P6 extension", ["uv", "run", "python", "notes/verify_993_A0prime_P6ext.py"], ["logs/993_A0prime_P6ext.json"]),
    ("A1 d-sign", ["uv", "run", "python", "notes/verify_993_A1_dsign.py"], ["logs/993_A1_dsign.json"]),
    ("A1 gap-2", ["uv", "run", "python", "notes/verify_993_A1_gap2.py"], ["logs/993_A1_gap2.json"]),
    ("A1 general gap", ["uv", "run", "python", "notes/verify_993_A1_generalgap.py"], ["logs/993_A1_generalgap.json"]),
    ("A1 multigiant", ["uv", "run", "python", "notes/verify_993_A1_multigiant.py"], ["logs/993_A1_multigiant.json"]),
    ("A2 three-value", ["uv", "run", "python", "notes/verify_993_A2_threevalue.py"], ["logs/993_A2_threevalue.json"]),
    ("G tails", ["uv", "run", "python", "notes/certify_993_G_tails.py"], ["logs/993_G_tails_certification.json"]),
    ("N convexity", ["uv", "run", "python", "notes/verify_993_N_convexity.py"], ["logs/993_N_convexity.json"]),
    ("W Schur domination", ["uv", "run", "python", "notes/verify_993_W_schur_dom.py"], ["logs/993_W_schur_dom.json"]),
    ("pure-pair reduction", ["uv", "run", "python", "notes/verify_993_purepair_reduction.py"], ["logs/993_purepair_reduction.json"]),
    ("h=2 mixed scope", ["uv", "run", "python", "notes/verify_993_h2mixed_scope.py"], ["logs/993_h2mixed_scope.json"]),
    ("odd core", ["uv", "run", "python", "notes/verify_993_oddcore.py"], ["logs/993_oddcore.json"]),
    ("KL scope", ["uv", "run", "python", "notes/verify_993_kl_scope.py"], ["logs/993_kl_scope.json"]),
    ("aggregate flow scans", ["uv", "run", "python", "notes/verify_993_aggregate_dd.py"], ["logs/993_aggregate_dd.json"]),
    ("factorial ladder", ["uv", "run", "python", "notes/verify_993_factorial_ladder.py"], ["logs/993_factorial_ladder.json"]),
    ("ladder Schur step", ["uv", "run", "python", "notes/verify_993_ladder_schur_step.py"], ["logs/993_ladder_schur_step.json"]),
    (
        "adjacent-value ladder certificates",
        ["uv", "run", "python", "notes/certify_993_ladder_polyc.py", "3", "10", "28", "993_ladder_polyc_h3-10_k28.json"],
        ["logs/993_ladder_polyc_h3-10_k28.json"],
    ),
    ("giant certificates", ["uv", "run", "python", "notes/certify_993_giant_polyc.py"], ["logs/993_giant_certification.json"]),
    ("giant vs balanced", ["uv", "run", "python", "notes/verify_993_giant_vs_bal.py"], ["logs/993_giant_vs_bal.json"]),
    ("threshold landscape", ["uv", "run", "python", "notes/verify_993_threshold_landscape.py"], ["logs/993_threshold_landscape.json"]),
    ("band-bottom maps", ["uv", "run", "python", "notes/verify_993_bandbottom.py"], ["logs/993_bandbottom.json"]),
    ("exchange census", ["uv", "run", "python", "notes/verify_993_exchange_census.py"], ["logs/993_exchange_census.json"]),
    ("local maxima census", ["uv", "run", "python", "notes/verify_993_locmax_census.py"], ["logs/993_locmax_census.json"]),
    ("maximizer census", ["uv", "run", "python", "notes/verify_993_maximizer_census.py"], ["logs/993_maximizer_census.json"]),
    ("mechanism map", ["uv", "run", "python", "notes/verify_993_mechanism_map.py"], ["logs/993_mechanism_map.json"]),
    ("tail chain", ["uv", "run", "python", "notes/verify_993_tail_chain.py"], ["logs/993_tail_chain.json"]),
    ("window form", ["uv", "run", "python", "notes/verify_993_window_form.py"], ["logs/993_window_form.json"]),
    ("window box design", ["uv", "run", "python", "notes/verify_993_window_box_design.py"], ["logs/993_window_box_design.json"]),
    ("window census", ["uv", "run", "python", "notes/verify_993_window_census.py"], ["logs/993_window_census.json"]),
    ("P6 h=2", ["uv", "run", "python", "notes/verify_993_p6_h2.py"], ["logs/993_p6_h2_proof_check.json"]),
    (
        "first-product concavity certificate",
        ["bash", "-lc", "uv run python notes/verify_993_first_product_concavity.py > logs/993_first_product_concavity_certificate.log"],
        ["logs/993_first_product_concavity_certificate.log"],
    ),
    ("bush sweep", ["uv", "run", "python", "notes/verify_993_bush_sweep.py"], ["logs/993_bush_sweep.json"]),
    ("LC dip atlas", ["uv", "run", "python", "notes/probe_993_tree_lc_dip_atlas.py", "--workers", "14", "--tag", "atlas"], ["logs/993_cx_hunt_lc_dip_atlas.json"]),
    (
        "junction beam unseeded",
        ["uv", "run", "python", "notes/search_993_junction_beam.py", "--gadget-max", "11", "--beam", "200", "--max-n", "170", "--workers", "14", "--tag", "beam11", "--no-hub-seed"],
        ["logs/993_cx_hunt_junction_beam11.json"],
    ),
    (
        "junction beam seeded",
        ["uv", "run", "python", "notes/search_993_junction_beam.py", "--gadget-max", "11", "--beam", "200", "--max-n", "170", "--workers", "14", "--tag", "beam11seed"],
        ["logs/993_cx_hunt_junction_beam11seed.json"],
    ),
    (
        "forest pair scan",
        [
            "uv",
            "run",
            "python",
            "notes/search_993_forest_pair_products.py",
            "--exhaustive-max",
            "10",
            "--corona-base-max",
            "7",
            "--spine-max",
            "8",
            "--random-leg-patterns",
            "4",
            "--random-trees-per-n",
            "5",
            "--top-pool",
            "400",
            "--random-pairs",
            "100000",
            "--workers",
            "14",
            "--seed",
            "993",
            "--tag",
            "smoke3",
        ],
        ["logs/993_cx_hunt_pairscan_smoke3.json"],
    ),
    ("Lean formal surface", ["bash", "-lc", "command -v lake >/dev/null 2>&1 && lake build || \"$HOME/.elan/bin/lake\" build"], []),
    ("formalization guard", ["uv", "run", "python", "scripts/check_formalization.py"], []),
    ("fast validator", ["uv", "run", "python", "scripts/check_reproducibility.py"], []),
]


def ignore(dir_path: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORE_NAMES}


def normalize_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: normalize_json(child)
            for key, child in value.items()
            if key not in JSON_DROP_KEYS
        }
    if isinstance(value, list):
        return [normalize_json(child) for child in value]
    return value


def normalized_text(path: Path) -> str:
    if path.suffix == ".json":
        return json.dumps(normalize_json(json.loads(path.read_text())), sort_keys=True, indent=2)
    return path.read_text().strip()


def compare_artifacts(generated_root: Path, outputs: list[str]) -> None:
    for relative in outputs:
        generated = generated_root / relative
        committed = ROOT / relative
        if not generated.exists():
            raise SystemExit(f"{relative}: generator did not create output")
        if normalized_text(generated) != normalized_text(committed):
            raise SystemExit(f"{relative}: regenerated artifact differs from committed artifact")


def run_command(worktree: Path, label: str, cmd: list[str], *, verbose: bool) -> None:
    print(f"[reproduce-all] {label}", flush=True)
    if verbose:
        subprocess.run(cmd, cwd=worktree, check=True)
    else:
        result = subprocess.run(cmd, cwd=worktree, check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if result.returncode != 0:
            print(result.stdout)
            raise SystemExit(result.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="list regeneration steps and exit")
    parser.add_argument("--start-at", type=str, default=None, help="substring of first step to run")
    parser.add_argument("--stop-after", type=str, default=None, help="substring of final step to run")
    parser.add_argument("--keep-worktree", action="store_true", help="print and retain the temporary worktree")
    parser.add_argument("--verbose", action="store_true", help="stream subprocess output")
    args = parser.parse_args()

    selected = COMMANDS
    if args.start_at:
        index = next((i for i, row in enumerate(selected) if args.start_at in row[0]), None)
        if index is None:
            raise SystemExit(f"unknown --start-at step: {args.start_at}")
        selected = selected[index:]
    if args.stop_after:
        index = next((i for i, row in enumerate(selected) if args.stop_after in row[0]), None)
        if index is None:
            raise SystemExit(f"unknown --stop-after step: {args.stop_after}")
        selected = selected[: index + 1]
    if args.list:
        for label, cmd, outputs in selected:
            print(f"{label}: {' '.join(cmd)}")
            for output in outputs:
                print(f"  -> {output}")
        return

    temp = None
    if args.keep_worktree:
        temp_root = Path(tempfile.mkdtemp(prefix="erdos993-reproduce-"))
    else:
        temp = tempfile.TemporaryDirectory(prefix="erdos993-reproduce-")
        temp_root = Path(temp.name)
    worktree = temp_root / "repo"
    shutil.copytree(ROOT, worktree, ignore=ignore)
    if args.keep_worktree:
        print(f"[reproduce-all] keeping worktree at {worktree}", flush=True)

    os.makedirs(worktree / "logs", exist_ok=True)
    for label, cmd, outputs in selected:
        run_command(worktree, label, cmd, verbose=args.verbose)
        compare_artifacts(worktree, outputs)

    print("[reproduce-all] all selected artifacts regenerated and matched", flush=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
