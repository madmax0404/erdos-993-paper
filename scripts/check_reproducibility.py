"""Check the paper-facing reproducibility logs.

This script does not re-run the expensive searches.  It validates that
the committed JSON logs contain the counts and zero-failure properties
quoted in the manuscript.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "logs"


def load(name: str):
    return json.loads((LOGS / name).read_text())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    m = load("993_M_dual_certificates.json")
    require(m["cases"] == 238, "unexpected M-dual case count")
    require(len(m["failures"]) == 0, "M-dual failures present")
    print(f"M dual: cases={m['cases']} failures=0 worst_ratio={m['worst_ratio']:.6f}")

    ecore_logs = [
        "993_ecore_polyc_certification.json",
        "993_ecore_polyc_ext.json",
        "993_ecore_polyc_topup.json",
    ]
    ecore_total = 0
    for name in ecore_logs:
        data = load(name)
        require(not data.get("failed"), f"{name} has failed instances")
        count = len(data["certified"])
        ecore_total += count
        print(f"{name}: certified={count}")
    require(ecore_total == 996, "E-core certified total mismatch")
    print(f"E-core certified total={ecore_total}")

    for name in ("993_h2mixed_scope.json", "993_oddcore.json"):
        data = load(name)
        require(data.get("all_checks_pass") is True, f"{name} did not pass")
        print(f"{name}: all_checks_pass=True")

    band_b = load("993_band_B_verification.json")
    require(band_b["lcP_failures"] == 0, "Band B LC failures present")
    require(band_b["W1_lower_bound_violations"] == 0, "Band B W1 violations present")
    print(
        "Band B verifier: "
        f"multisets={band_b['cases_with_band_B']} "
        "LC_failures=0 W1_violations=0"
    )

    threshold = load("993_band_B_threshold.json")
    require(threshold["small_exact_cases"] == 24394, "Band B small case mismatch")
    require(threshold["small_exact_band_rows"] == 54049, "Band B row mismatch")
    require(threshold["small_exact_failures"] == [], "Band B small failures present")
    require(threshold["large_bound_failure_count"] == 0, "Band B large failures present")
    print(
        "Band B threshold: small_cases=24394 rows=54049 "
        f"large_pairs={threshold['large_bound_pairs_checked']} failures=0"
    )

    for name in (
        "993_A0prime_P6ext.json",
        "993_A1_dsign.json",
        "993_A1_gap2.json",
        "993_A1_generalgap.json",
        "993_A1_multigiant.json",
        "993_A2_threevalue.json",
        "993_G_tails_certification.json",
        "993_N_convexity.json",
        "993_W_schur_dom.json",
        "993_aggregate_dd.json",
        "993_kl_scope.json",
        "993_p6_h2_proof_check.json",
        "993_purepair_reduction.json",
    ):
        require((LOGS / name).exists(), f"missing {name}")
    print("Auxiliary paper-facing logs: present")


if __name__ == "__main__":
    main()
