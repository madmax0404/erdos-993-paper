"""Check the paper-facing reproducibility logs.

This script does not re-run the expensive searches.  It validates that the
committed logs and certificates contain the counts, zero-failure properties,
and selected extremal values quoted in the manuscript.
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


def require_exists(relative_path: str) -> None:
    require((ROOT / relative_path).exists(), f"missing {relative_path}")


def check_artifact_inventory() -> None:
    required = [
        "REPRODUCIBILITY.md",
        "FORMALIZATION.md",
        "lean-toolchain",
        "lakefile.lean",
        "formal/Erdos993Formal.lean",
        "formal/Erdos993Formal/Basic.lean",
        "scripts/check_formalization.py",
        "scripts/reproduce_all.py",
        "notes/993_audit_report.md",
        "notes/993-current-integration-audit.md",
        "notes/993-counterexample-hunt-design.md",
        "notes/993-counterexample-hunt-findings.md",
        "notes/993_factorial_ladder.md",
        "notes/993_purepair_reduction.md",
        "notes/monic-product-closure.md",
        "notes/certify_993_giant_polyc.py",
        "notes/certify_993_ladder_polyc.py",
        "notes/certify_starred_newton.py",
        "notes/probe_993_tree_lc_dip_atlas.py",
        "notes/scan_monic_products.py",
        "notes/search_993_forest_pair_products.py",
        "notes/search_993_junction_beam.py",
        "notes/verify_993_bandbottom.py",
        "notes/verify_993_bush_sweep.py",
        "notes/verify_993_exchange_census.py",
        "notes/verify_993_factorial_ladder.py",
        "notes/verify_993_first_product_concavity.py",
        "notes/verify_993_giant_vs_bal.py",
        "notes/verify_993_ladder_schur_step.py",
        "notes/verify_993_locmax_census.py",
        "notes/verify_993_maximizer_census.py",
        "notes/verify_993_mechanism_map.py",
        "notes/verify_993_tail_chain.py",
        "notes/verify_993_threshold_landscape.py",
        "notes/verify_993_window_box_design.py",
        "notes/verify_993_window_census.py",
        "notes/verify_993_window_form.py",
        "notes/verify_starred_newton.py",
        "logs/993_bandbottom.json",
        "logs/993_bush_sweep.json",
        "logs/993_cx_hunt_junction_beam11.json",
        "logs/993_cx_hunt_junction_beam11seed.json",
        "logs/993_cx_hunt_lc_dip_atlas.json",
        "logs/993_cx_hunt_pairscan_smoke3.json",
        "logs/993_exchange_census.json",
        "logs/993_factorial_ladder.json",
        "logs/993_first_product_concavity_certificate.log",
        "logs/993_giant_certification.json",
        "logs/993_giant_vs_bal.json",
        "logs/993_ladder_polyc_h3-10_k28.json",
        "logs/993_ladder_schur_step.json",
        "logs/993_locmax_census.json",
        "logs/993_maximizer_census.json",
        "logs/993_mechanism_map.json",
        "logs/993_tail_chain.json",
        "logs/993_threshold_landscape.json",
        "logs/993_window_box_design.json",
        "logs/993_window_census.json",
        "logs/993_window_form.json",
    ]
    for path in required:
        require_exists(path)
    cert = (LOGS / "993_first_product_concavity_certificate.log").read_text()
    require("Thus F is concave" in cert, "first-product certificate text mismatch")
    print(f"Artifact inventory: {len(required)} paper-facing files present")


def check_main_certificates() -> None:
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

    aggregate = load("993_aggregate_dd.json")
    require(aggregate["uniform_sanity"]["mismatches"] == [], "aggregate uniform mismatch")
    aggregate_total = sum(
        aggregate[name]["checked"]
        for name in ("cc1A", "ray1c2c", "perpair_witnesses", "random_mixed")
    )
    require(aggregate_total == 14410, "aggregate scan count mismatch")
    for name in ("cc1A", "ray1c2c", "perpair_witnesses", "random_mixed"):
        require(aggregate[name]["n_violations"] == 0, f"aggregate {name} violations")
    require(aggregate["smallest_perpair_witness"][:2] == [107, 1], "per-pair witness mismatch")
    print("Aggregate flow scans: evaluations=14410 violations=0")


def check_band_b() -> None:
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


def check_ladder_and_landscape() -> None:
    ladder = load("993_factorial_ladder.json")
    ladder_total = sum(
        ladder[name]["checked"] for name in ("uniform", "ab1A", "random_mixed")
    )
    require(ladder_total == 5298, "factorial ladder profile count mismatch")
    for name in ("uniform", "ab1A", "random_mixed"):
        require(ladder[name]["n_violations"] == 0, f"ladder {name} failures")
    require(ladder["consistency"]["n_mismatch"] == 0, "ladder consistency mismatch")
    print("Factorial ladder scan: profiles=5298 rung_failures=0")

    schur = load("993_ladder_schur_step.json")
    schur_steps = schur["exhaustive"]["steps_checked"] + schur["random"]["steps_checked"]
    schur_violations = schur["exhaustive"]["n_violations"] + schur["random"]["n_violations"]
    require(schur_steps == 49941, "Schur step count mismatch")
    require(schur_violations == 11278, "Schur violation count mismatch")
    require(schur["global_argmax"]["cases"] == 1082, "Schur argmax case mismatch")
    require(
        schur["global_argmax"]["argmax_not_balanced"] == 212,
        "Schur nonbalanced argmax count mismatch",
    )
    print("Schur landscape: steps=49941 violations=11278 nonbalanced_argmax=212/1082")

    adjacent = load("993_ladder_polyc_h3-10_k28.json")
    require(adjacent["range"] == [3, 10, 28], "adjacent-value certificate range mismatch")
    require(len(adjacent["certified"]) == 7866, "adjacent-value certificate count mismatch")
    require(adjacent["failed"] == [], "adjacent-value certificate failures present")
    require(
        adjacent["schur_datapoint"]["balanced_is_worse"] is True,
        "adjacent-value Schur datapoint mismatch",
    )
    print("Adjacent-two-value ladder certificates: certified=7866 failures=0")

    giant_cert = load("993_giant_certification.json")
    require(len(giant_cert["certified"]) == 1512, "giant certificate count mismatch")
    require(giant_cert["failed"] == [], "giant certificate failures present")
    giant_sweep = load("993_giant_vs_bal.json")
    require(giant_sweep["y_lc_extended"]["n_fails"] == 0, "giant y-LC failures")
    require(giant_sweep["sweep_rows"] == 4720, "giant sweep row mismatch")
    require(giant_sweep["unconditional"]["max_ratio_G"] < 1.0, "giant sweep violated ladder")
    require(
        giant_sweep["unconditional"]["argmax_G"][2:5] == [100, 6, 8],
        "giant sweep argmax mismatch",
    )
    print("Bulk-plus-giant sweep: rows=4720 max_ratio<1 certificates=1512")

    threshold_landscape = load("993_threshold_landscape.json")
    require(threshold_landscape["exhaustive"]["cases"] == 139537, "threshold case mismatch")
    require(
        threshold_landscape["exhaustive"]["high_ratio_all_bal_dominated"] is True,
        "threshold high-ratio domination mismatch",
    )
    require(threshold_landscape["large_h"]["n_high_not_dominated"] == 0, "large-h threshold failures")
    print("Threshold landscape: exhaustive_cases=139537 high_ratio_domination=True")

    w_schur = load("993_W_schur_dom.json")
    require(w_schur["w_schur_sanity"]["n_fails"] == 0, "W-Schur sanity failures")
    require(
        w_schur["dom_prime"]["by_threshold"]["0.7"]["exceedances"] == 0,
        "endpoint domination threshold 0.7 mismatch",
    )
    require(
        w_schur["large_h"]["max_bal_ratio_beaten"] < 0.66,
        "endpoint domination large-h bound mismatch",
    )
    print("Endpoint-domination probes: threshold_0.7_exceedances=0")

    bandbottom = load("993_bandbottom.json")
    require(bandbottom["sanity"]["n_fails"] == 0, "band-bottom sanity failures")
    require(bandbottom["rho_bar_map"]["k-s=1"]["n_above_1"] == 0, "band-bottom k-s=1 crosses 1")
    require(bandbottom["rho_bar_map"]["k-s=2"]["n_above_1"] == 0, "band-bottom k-s=2 crosses 1")
    require(bandbottom["rho_bar_map"]["k-s=3"]["n_above_1"] > 0, "band-bottom k-s=3 did not cross 1")
    require(bandbottom["rho_bar_map"]["k-s=1"]["max"][0] <= 0.546, "band-bottom k-s=1 max mismatch")
    require(bandbottom["rho_bar_map"]["k-s=2"]["max"][0] <= 0.897, "band-bottom k-s=2 max mismatch")
    print("Band-bottom maps: k-s=1,2 below 1; k-s=3 crosses 1")


def check_structural_searches() -> None:
    exchange = load("993_exchange_census.json")
    require(exchange["distinct_local_maxima"] == 76, "exchange local-max count mismatch")
    require(exchange["n_tight_OTHER"] == 0, "unclassified exchange local maxima")
    print("Exchange census: local_maxima=76 unclassified=0")

    for name in ("993_locmax_census.json", "993_maximizer_census.json"):
        census = load(name)
        if "n_tight_OTHER" in census:
            require(census["n_tight_OTHER"] == 0, f"{name} has unclassified tight maxima")

    mechanism = load("993_mechanism_map.json")
    require(mechanism["n_unclassified"] == 0, "mechanism map unclassified cases")
    require(mechanism["tight_configs"] == 697, "mechanism map tight-config count mismatch")

    tail_chain = load("993_tail_chain.json")
    require(tail_chain["sweep"]["n_uncovered"] == 0, "tail-chain uncovered cases")

    window_form = load("993_window_form.json")
    require(window_form["n_fails"] == 0, "window-form failures present")
    window_box = load("993_window_box_design.json")
    require(window_box["n_violations"] == 0, "window-box violations present")
    window_census = load("993_window_census.json")
    require("does NOT control" in window_census["verdict"], "window-census verdict mismatch")
    print("Structural shortcut probes: mechanism/window/tail checks present")

    atlas = load("993_cx_hunt_lc_dip_atlas.json")
    require(atlas["constructor_trees"] == 240602, "dip-atlas constructor count mismatch")
    require(atlas["non_lc_count"] == 1289, "dip-atlas non-LC count mismatch")
    require(atlas["non_unimodal"] == [], "dip-atlas non-unimodal trees present")
    require(atlas["max_offset_histogram"] == {"1": 1289}, "dip-atlas offset mismatch")
    require(atlas["non_monic_non_lc"] == 19, "dip-atlas non-monic count mismatch")

    bush = load("993_bush_sweep.json")
    require(bush["trees"] == 14767, "bush sweep tree count mismatch")
    require(bush["non_unimodal"] == 0, "bush sweep non-unimodal trees present")
    require(bush["offset_law_depth2"]["checked"] == 87, "bush offset-law count mismatch")
    require(bush["offset_law_depth2"]["violations"] == [], "bush offset-law violations")
    require(bush["best_balance"][2] == 46, "bush best-balance order mismatch")
    require(0.0439 < bush["best_balance"][0] < 0.0440, "bush best-balance value mismatch")

    beam = load("993_cx_hunt_junction_beam11seed.json")
    require(beam["gadget_count"] == 2975, "junction beam gadget count mismatch")
    require(beam["counterexamples"] == [], "junction beam counterexample candidates present")
    require(beam["history"][0]["n"] == 48, "junction beam seed order mismatch")
    require(
        0.04512 <= beam["history"][0]["best_balance"] <= 0.04513,
        "junction beam seed balance mismatch",
    )
    require(max(row["best_balance"] for row in beam["history"]) < 1.0, "junction beam found valley")

    pairscan = load("993_cx_hunt_pairscan_smoke3.json")
    require(pairscan["catalog_size"] == 35785, "pairscan catalog size mismatch")
    require(pairscan["counterexample_candidates"] == [], "pairscan counterexamples present")
    require(sum(row["pairs_scanned"] for row in pairscan["strategies"]) == 408910, "pairscan count mismatch")
    print("Extremal/search logs: atlas, bush, junction, and pairscan checks passed")


def check_auxiliary_presence() -> None:
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


def main() -> None:
    check_artifact_inventory()
    check_main_certificates()
    check_band_b()
    check_ladder_and_landscape()
    check_structural_searches()
    check_auxiliary_presence()


if __name__ == "__main__":
    main()
