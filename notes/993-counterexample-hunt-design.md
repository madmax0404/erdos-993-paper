# 993 Counterexample Hunt Design

Updated: 2026-06-10 KST.

This note opens a counterexample-facing branch: search for a tree or forest
whose independent-set sequence is not unimodal.  The problem statement (per
`notes/2026-05-08-erdos-993-start.md`, quoting erdosproblems.com/993) covers
trees and forests, so a non-unimodal forest falsifies the conjecture.

## Why forests first

- Local exhaustive coverage is tiny: trees are verified here through
  `n <= 18`, forest products only through total `n <= 20`.  The external
  Reynolds artifact claims trees through `n <= 29`.  Forests with two
  components of 20-32 vertices each are unexplored by anyone.
- The sequence-level mechanism already exists in this repo: the synthetic
  product `(1,15,107,38,32) x (1,171,109,104)` is non-unimodal although both
  factors are unimodal with decreasing tails.  The pattern is two separated
  humps, `spike x tail` and `tail x spike`, with an unfilled plateau between.
  Both factors have early sharp modes and heavy flat tails with large leading
  coefficients.  Tree polynomials have unbounded leading coefficients
  (`i_alpha` = number of maximum independent sets), so the monicity obstacle
  that protects the proved families does not protect general forests.
- Forest products are the cheapest objects to search: one exact integer
  convolution per candidate over a precomputed catalog, no isomorphism
  handling per test.

## Known constraint on valley location

Levit-Mandrescu (and the Basit-Galvin extension, arXiv:2006.12562) prove the
final third of the independence sequence of any König-Egerváry graph is
weakly decreasing.  Forests are bipartite, hence KE.  So any valley must sit
in the first two thirds of the product sequence.  This is a sanity filter,
not a search restriction: the valley scorer sees every index anyway.

## Search components

1. `notes/search_993_forest_pair_products.py` (this session)
   - Catalog: exhaustive non-isomorphic trees through a small bound, dedup by
     polynomial; structured families through `n ~ 64`: caterpillars with
     pendant-leaf patterns (coronas of paths included), spiders with arm
     lengths in `{1,2,3}`, multi-hub depth-2 spiders generalizing
     `T_{a,b,c}`, brooms with pendant-P2 banks, random trees.
   - Features per entry: `alpha`, mode index, mode fraction, leading
     coefficient, tail flatness `i_alpha / max`, spike sharpness.
   - Pair scan strategies: tail-heavy x tail-heavy, spike x tail-heavy,
     random coverage.  Exact `int64` convolution is safe through total
     `n <= 64` because every product coefficient is at most `C(64,32)`.
   - Valley score of a sequence: `max_b [min(prefix_max_before_b,
     suffix_max_after_b) - i_b]`.  Score `>= 1` is a counterexample.  Track
     top relative near-misses (score divided by the local hump height) since
     absolute scores are incomparable across magnitudes.
   - Any positive hit is re-verified by rebuilding the forest as a graph and
     recomputing with `src/erdos993/indpoly.py` before being believed.

2. Edge-join deepening (next, if near-misses appear): for the best pairs,
   scan all joins `I(T1) I(T2) - x^2 I(T1 - N[u]) I(T2 - N[v])` over root
   choices `u, v`.  The subtracted term is concentrated in middle degrees, so
   it can deepen a plateau into a valley, and a hit is a connected tree
   counterexample directly.

3. Annealing over tree space (later): local moves (subtree regraft, leaf
   moves) on `n = 20..120` optimizing the valley score, seeded by the most
   fragile shapes found by the product scan, parallel over 16 threads.

## Success and stop criteria

- Success: an exactly verified non-unimodal tree or forest polynomial with a
  reconstructed witness graph.
- Useful failure: near-miss landscape (best relative valley margins by
  family pair), which tells us whether the two-hump mechanism is being
  starved by realizability and where to push next.
