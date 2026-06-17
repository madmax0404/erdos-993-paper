# Reproducibility Manifest

This repository is the public reproducibility package for the paper. It is
curated rather than a mirror of the private research workspace: it keeps the
paper source, the small reusable polynomial library, the scripts that generated
paper-facing computations, and the committed logs/certificates cited by the
manuscript.

Run the fast package check with:

```bash
uv sync --dev
bash scripts/reproduce.sh
```

`scripts/reproduce.sh` runs the unit tests, two direct Band B verifiers, the
log/certificate validator, and rebuilds `paper/main.pdf` when `tectonic` is
installed. Larger certification/search scripts are committed so the logs can be
regenerated, but they are intentionally outside the fast path.

## Claim-to-Artifact Map

| Paper claim or section | Primary script(s) | Committed output(s) |
| --- | --- | --- |
| Polynomial/tree utility correctness and known non-LC examples | `tests/`, `src/erdos993/` | `uv run pytest -q` |
| T1/T2 certificate grid: 238 cases, no failures, worst ratio 0.4352 | `notes/extract_993_M_dual_certificates.py` | `logs/993_M_dual_certificates.json`, `logs/993_M_dual_certificates_ext.json` |
| E-core polynomial certification: 996 instances, no failures | `notes/certify_993_ecore_polyc.py` | `logs/993_ecore_polyc_certification.json`, `logs/993_ecore_polyc_ext.json`, `logs/993_ecore_polyc_topup.json` |
| Band B residual: 24,394 multisets, 54,049 rows, no failures; large threshold from C=55 | `notes/verify_993_band_B.py`, `notes/verify_993_band_B_threshold.py` | `logs/993_band_B_verification.json`, `logs/993_band_B_threshold.json` |
| Scope theorem auxiliary checks for h=1, h=2, adjacent-three-hub families, odd cases, and pure-pair reduction | `notes/verify_993_h2mixed_scope.py`, `notes/verify_993_oddcore.py`, `notes/verify_993_kl_scope.py`, `notes/verify_993_purepair_reduction.py` | `logs/993_h2mixed_scope.json`, `logs/993_oddcore.json`, `logs/993_kl_scope.json`, `logs/993_purepair_reduction.json` |
| A0/A1/A2/G/N/W auxiliary proof obligations | `notes/verify_993_A0prime_P6ext.py`, `notes/verify_993_A1_*.py`, `notes/verify_993_A2_threevalue.py`, `notes/certify_993_G_tails.py`, `notes/verify_993_N_convexity.py`, `notes/verify_993_W_schur_dom.py` | matching `logs/993_A0prime_P6ext.json`, `logs/993_A1_*.json`, `logs/993_A2_threevalue.json`, `logs/993_G_tails_certification.json`, `logs/993_N_convexity.json`, `logs/993_W_schur_dom.json` |
| Audit report and audit-facing notes | audit notes and verification scripts in `notes/` | `notes/993_audit_report.md`, `notes/993-current-integration-audit.md` |
| Aggregate flow-concavity scans: 14,410 evaluations, zero violations, smallest per-pair witness | `notes/verify_993_aggregate_dd.py` | `logs/993_aggregate_dd.json` |
| Factorial ladder scan: 5,298 profiles, zero rung failures | `notes/verify_993_factorial_ladder.py` | `logs/993_factorial_ladder.json`, `notes/993_factorial_ladder.md` |
| Schur/Robin-Hood landscape: 49,941 steps, 11,278 monotonicity violations, 212 nonbalanced maximizers among 1,082 cases | `notes/verify_993_ladder_schur_step.py` | `logs/993_ladder_schur_step.json` |
| Two-adjacent-value ladder certificates: 7,866 instances, zero failures | `notes/certify_993_ladder_polyc.py 3 10 28 993_ladder_polyc_h3-10_k28.json` | `logs/993_ladder_polyc_h3-10_k28.json` |
| Bulk-plus-giant ladder certificates and sweep: 1,512 certified instances, 4,720 sweep rows, max ratio below 1 | `notes/certify_993_giant_polyc.py`, `notes/verify_993_giant_vs_bal.py` | `logs/993_giant_certification.json`, `logs/993_giant_vs_bal.json` |
| Threshold landscape, endpoint-domination probes, band-bottom maps, and failed shortcut catalog | `notes/verify_993_threshold_landscape.py`, `notes/verify_993_W_schur_dom.py`, `notes/verify_993_bandbottom.py`, `notes/verify_993_window_*.py`, `notes/verify_993_tail_chain.py` | `logs/993_threshold_landscape.json`, `logs/993_W_schur_dom.json`, `logs/993_bandbottom.json`, `logs/993_window_*.json`, `logs/993_tail_chain.json` |
| Local-maximizer and exchange-lemma evidence: 76 local maximizers, all classified | `notes/verify_993_exchange_census.py`, `notes/verify_993_locmax_census.py`, `notes/verify_993_maximizer_census.py` | `logs/993_exchange_census.json`, `logs/993_locmax_census.json`, `logs/993_maximizer_census.json` |
| Uniform/mixed-depth offset-law checks and extremal balance around `S(4^5)` | `notes/verify_993_bush_sweep.py`, `notes/probe_993_tree_lc_dip_atlas.py` | `logs/993_bush_sweep.json`, `logs/993_cx_hunt_lc_dip_atlas.json`, `notes/993-counterexample-hunt-findings.md` |
| Junction-tree beam search over 2,975 rooted gadgets and the 48-vertex high-fragility seed | `notes/search_993_junction_beam.py --gadget-max 11 --beam 200 --max-n 170 --tag beam11seed` | `logs/993_cx_hunt_junction_beam11seed.json`, `logs/993_cx_hunt_junction_beam11.json` |
| Forest product scans through the `n <= 64` exact-convolution regime | `notes/search_993_forest_pair_products.py` | `logs/993_cx_hunt_pairscan_smoke3.json`, `notes/993-counterexample-hunt-design.md` |
| Previous-record `T^*` symbolic/Newton checks used as regression context | `notes/verify_starred_newton.py`, `notes/certify_starred_newton.py` | unit-test and symbolic-check outputs |
| Monic product closure branch and first-product concavity certificate | `notes/scan_monic_products.py`, `notes/verify_993_first_product_concavity.py` | `notes/monic-product-closure.md`, `logs/993_first_product_concavity_certificate.log` |

## Fast Validator

`scripts/check_reproducibility.py` validates the headline counts, zero-failure
properties, and selected extremal/search values in the table above. It does not
rerun the expensive searches; it checks that the committed artifacts are the
ones cited by the paper.

## Larger Regeneration Commands

Examples:

```bash
uv run python notes/extract_993_M_dual_certificates.py
uv run python notes/certify_993_ecore_polyc.py
uv run python notes/verify_993_factorial_ladder.py
uv run python notes/verify_993_ladder_schur_step.py
uv run python notes/certify_993_ladder_polyc.py 3 10 28 993_ladder_polyc_h3-10_k28.json
uv run python notes/certify_993_giant_polyc.py
uv run python notes/verify_993_giant_vs_bal.py
uv run python notes/verify_993_exchange_census.py
uv run python notes/verify_993_bush_sweep.py
uv run python notes/search_993_junction_beam.py --gadget-max 11 --beam 200 --max-n 170 --tag beam11seed
```

Some of these are CPU-heavy or exploratory. The committed JSON files are the
paper-facing outputs used for publication.
