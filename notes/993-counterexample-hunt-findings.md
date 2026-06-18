# 993 Counterexample Hunt: Findings

Updated: 2026-06-10 KST.  Companion to `notes/993-counterexample-hunt-design.md`.

## Summary

No counterexample found, and the negative is structured: every mechanism that
produces non-log-concave trees at accessible sizes is provably-or-empirically
capped far below the threshold a unimodality failure needs.  The hunt produced
several new structural facts along the way, including high-fragility junction
trees and an observed offset law over the searched uniform range, and it
converts cleanly into proof-side material.

Balance language: at an interior index `k`, define
`balance(k) = min(i_{k-1}, i_{k+1}) / i_k`.  A strict valley at `k` means
`balance(k) > 1`, and every valley bottom is a log-concavity failure point.
So the counterexample hunt is exactly the problem "maximize balance over
reachable trees/forests", and unimodality of a class is the statement
"balance <= 1 across it".

## Fact 1: products need a non-LC factor

Convolution preserves log-concavity for positive sequences, so a non-unimodal
forest must contain a non-LC tree component.  This focuses the entire forest
route on the structure of non-LC trees.

## Fact 2: the dip atlas (240,602 trees, n <= 36)

`notes/probe_993_tree_lc_dip_atlas.py`, log
`logs/993_cx_hunt_lc_dip_atlas.json`.  Constructor space: spine trees with
per-vertex (leaf, P2, P3) attachments, depth-3 spiders, corona-with-gadget
grafts; generalizes stars, brooms, spiders, T_{a,b,c}, T*, multi-hub spiders.

- 1,289 non-LC trees; every single failure at offset 1 from the top degree.
- Max balance in this space: 0.0196 (= 1/51, the T_{3,4,4} tail).
- 19 non-monic non-LC trees (leads 2..8) - new; the literature families are
  all monic - but balance stays ~0.018.
- T and T* through parameter 40 (n up to ~170): offset 1 only, balance
  <= 0.0208.

## Fact 3: the hub offset law

Uniform hub spiders hub(c^h) (root, h hubs, c pendant P2-arms per hub) have
closed form

    I = H_c^h + x E_c^h,   H_c = (1+2x)^c + x(1+x)^c,  E_c = (1+2x)^c.

Sweep h <= 25, c <= 12, n up to 256: the unique LC failure sits at offset
exactly `h - 2` for c >= 4 (c >= 5 extends further), width always 1.  The dip
is the junction where the fat `x E^h` hump ends and the thin `H^h` tail
continues alone.  Balance peaks at 0.0439 for hub(4^5) (n = 46) and decays in
both directions; it never trends toward 1.

## Fact 4: junction calculus and the Maclaurin cap

Any tree is root + rooted gadgets R_1..R_m with

    P = prod F_i + x prod G_i,   F_i = I(R_i),  G_i = I(R_i - r_i).

A junction valley at index E+1 (E = 1 + deg prod G) requires simultaneously

  (a) prod F still rising past E+1 (its mode above the junction), and
  (b) top(prod G) larger than the local increment of prod F there.

Near the junction the coefficients of prod F organize as elementary symmetric
functions e_j of per-gadget weights (t_i ~ 2^{-c_i} for arm-hub gadgets): dip
existence needs roughly e_2 < 1 while balance ~ e_3/e_2.  Newton/Maclaurin
gives e_3/e_2 <~ 0.5 sqrt(e_2), so balance stays below ~0.5 even at a
perfectly tuned multiset, and the binomial corrections push the achievable
value to ~0.05.  The same log-concavity machinery the conjecture asserts is
what protects the junction: the mechanism is self-defending.

Empirical confirmation: beam search over all 2,975 distinct gadget types from
rooted trees with <= 11 vertices (`notes/search_993_junction_beam.py`, logs
`logs/993_cx_hunt_junction_beam11seed.json`):

- Unseeded beams are doubly deceptive (smooth attractors); seeded from the
  known non-LC hub multisets, the best reachable balance is 0.04554 (n = 59)
  and every further gadget extension strictly degrades it until the dip dies.
- Record verified tree: n = 48, alpha = 26, root + 4 H_4 hub gadgets + one
  11-vertex gadget with F = (1,11,45,88,84,33,2), G = (1,10,39,74,68,24);
  single LC failure at offset 3, balance 0.04512, lead 2 (non-monic), window
  (..., 3870613, 173488, 7828, 193, 2).  graph6:
  `ohOI?D??K??@?@?A??G?O??C?G???K?????@???G??A???@???O????_??G????@_????????G????G????O????@????A??????_???@??????@??????O?????G?????A??????O??????_?????@??????@???????O??????@???????C???????G`
  This more than doubles the literature's fragility record (T*(3,3,4) at
  0.0208).

## Fact 5: depth-3 nesting erases the dip

Using whole dipped trees (e.g. hub(4^5)) as gadgets under a new root removes
all LC failures: every nested composite tested (n up to 185, pure copies,
mixed with H_4 gadgets, mixed with root leaves) is fully log-concave.  The
second-level `F + xG` smoothing wipes the inner junction.  Even one pendant
leaf at the root of hub(4^5) removes its failure.

## Fact 6: products smooth the cliffs away

`notes/search_993_forest_pair_products.py` catalog scans (exhaustive trees,
caterpillars, mixed spiders, multi-hub spiders, coronas, pendant-P2 coronas,
T-families, random trees; int64-exact convolutions through total n = 64) plus
targeted exact probes: every product checked is not just unimodal but
log-concave.  Width-1 tail cliffs cannot survive convolution against any tree
partner, whose coefficient spread is on the order sqrt(n); making the partner
big enough to drag the dip image into the legal first two thirds
(Levit-Mandrescu: the last third of any KE-graph sequence decreases, and
forests are KE) makes the smoothing strictly worse.  The flat-heavy-tail
ingredient of the synthetic non-unimodal products
((1,15,107,38,32) x (1,171,109,104)) does not occur in real tree
polynomials: flat tails (coronas, i_{d-1}/i_d ~ 1.3) come only with full
log-concavity, while dips come only with steep monic-side cliffs
(i_{d-1}/i_d >= ~50).  The two ingredients refuse to coexist.

## Honest caveats

- Beam/greedy searches are incomplete; two deceptive attractors were already
  demonstrated, so "beam found nothing" is weak evidence by itself.  The
  strength of the negative comes from the structural caps (Facts 3-5), the
  exhaustive small spaces, and the closed forms.
- Gadget basis capped at 11 vertices and depth 2; products capped at total 64
  for the wide scans.  The Maclaurin cap is a heuristic sketch, not a
  theorem; the binomial corrections are unproven.
- Tree counterexamples at n >> 200 with wide log-convex windows are not ruled
  out, but no generator for width >= 2 windows is known: every observed
  failure has width exactly 1.

## Where this leaves the hunt

The expected-value of further small-scale counterexample search is now low:
the only dip mechanism available is capped at balance ~0.05 against a
requirement of > 1.  The productive continuations are:

1. Prove the cap: "every depth-2 junction tree has balance <= C < 1 at every
   LC failure" via the e_2/e_3 Newton tension.  This would subsume and extend
   all published family unimodality results (T_{3,m,n}, T*, Galvin-Hilyard
   families are all depth-2 junction trees), with a clean new mechanism.
2. Classify where LC failures can live at all (offset law for general
   gadget multisets; the h-2 law suggests offset = #(delta=1 gadgets) - 2).
3. Look for width->2 LC-failure generators as the remaining counterexample
   hope; if a parity/structure argument rules them out, the forest route
   closes entirely.
