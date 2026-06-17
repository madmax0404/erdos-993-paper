"""Beam search over root-gadget compositions for a junction-valley tree.

Any multiset of rooted gadgets R_1..R_m attached to a fresh root gives a tree
with independence polynomial

    P = prod_i F_i  +  x * prod_i G_i,

where F_i = I(R_i) and G_i = I(R_i - root_i).  All known non-log-concave
trees (T_{a,b,c}, T*, multi-hub spiders) are instances.  The dip lives at the
junction where the x*prod G hump ends; a counterexample needs the dip balance
min(left, right)/mid to exceed 1.  A Maclaurin-inequality heuristic says
balance is capped near 0.5 * sqrt(e_2) < 1 for arm-hub-type gadgets; this
search tries to break that cap with arbitrary mixed gadgets (every rooted
tree up to a size bound is available).

Exact integer arithmetic throughout.  Any state with balance > 1 or a
non-unimodal polynomial is a counterexample to Erdős 993; it would be
re-verified by rebuilding the tree from the gadget multiset.
"""

from __future__ import annotations

import argparse
import json
import sys
from multiprocessing import Pool
from pathlib import Path
from time import perf_counter

import networkx as nx

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from erdos993.indpoly import independence_polynomial, is_unimodal, mul  # noqa: E402


def np_binom_row(c: int, base: int) -> list[int]:
    """Coefficients of (1 + base*x)^c."""

    from math import comb

    return [comb(c, k) * base**k for k in range(c + 1)]


# ----------------------------------------------------------------------------
# Gadget enumeration: all rooted trees up to a size bound, dedup by (F, G).
# ----------------------------------------------------------------------------


def rooted_gadgets(max_size: int) -> list[dict]:
    seen: dict[tuple[tuple[int, ...], tuple[int, ...]], dict] = {}
    for n in range(1, max_size + 1):
        trees = [nx.path_graph(1)] if n == 1 else nx.nonisomorphic_trees(n)
        for index, tree in enumerate(trees):
            for root in tree.nodes:
                free = independence_polynomial(tree)
                killed_graph = tree.copy()
                killed_graph.remove_node(root)
                killed = independence_polynomial(killed_graph)
                key = (free, killed)
                if key not in seen:
                    seen[key] = {
                        "F": free,
                        "G": killed,
                        "n": n,
                        "label": f"g(n={n},t={index},r={root})",
                    }
    return list(seen.values())


# ----------------------------------------------------------------------------
# Junction scoring
# ----------------------------------------------------------------------------


def compose(F: tuple[int, ...], G: tuple[int, ...]) -> tuple[int, ...]:
    poly = list(F) + [0] * max(0, len(G) + 1 - len(F))
    for i, g in enumerate(G):
        poly[i + 1] += g
    return tuple(poly)


def score(poly: tuple[int, ...], junction: int) -> tuple[float, float, int, bool]:
    """Return (combined score, balance, dip index, unimodal).

    Stage 1 (no LC failure yet): combined = LC ratio left*right/mid^2
    maximized over the junction window only (k near 1 + deg(prod G), where
    the x*prod-G hump ends).  Maximizing the global LC ratio is deceptive:
    any big smooth polynomial has ratios -> 1 near its mode, so the beam
    drifts to a smooth attractor and never crosses.  Stage 2 (failure
    exists anywhere): combined = 1000 + best balance.  Balance > 1 is a
    counterexample.
    """

    d = len(poly) - 1
    best_balance, best_k = 0.0, -1
    for k in range(1, d):
        if poly[k] * poly[k] < poly[k - 1] * poly[k + 1]:
            balance = min(poly[k - 1], poly[k + 1]) / poly[k]
            if balance > best_balance:
                best_balance, best_k = balance, k
    if best_balance > 0.0:
        return 1000.0 + best_balance, best_balance, best_k, is_unimodal(poly)
    lc_max = 0.0
    for k in range(max(1, junction - 2), min(d, junction + 3)):
        mid2 = poly[k] * poly[k]
        cross = poly[k - 1] * poly[k + 1]
        if mid2 > 0 and cross > 0:
            lc_max = max(lc_max, cross / mid2)
    return min(lc_max, 1.0), 0.0, -1, True


GADGETS: list[dict] = []


def init_worker(gadgets: list[dict]) -> None:
    global GADGETS
    GADGETS = gadgets


def expand_state(payload: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...], int]) -> list:
    """Try every gadget extension of one beam state; return scored children."""

    F, G, multiset, max_n = payload
    out = []
    base_n = 1 + sum(GADGETS[g]["n"] for g in multiset)
    for gi, gadget in enumerate(GADGETS):
        if base_n + gadget["n"] > max_n:
            continue
        if multiset and gi < multiset[-1]:
            continue  # canonical nondecreasing order kills duplicate multisets
        F2 = mul(F, gadget["F"])
        G2 = mul(G, gadget["G"])
        combined, balance, k, unimodal = score(compose(F2, G2), len(G2))
        out.append((combined, balance, k, unimodal, gi, multiset))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gadget-max", type=int, default=9)
    parser.add_argument("--beam", type=int, default=240)
    parser.add_argument("--max-n", type=int, default=200)
    parser.add_argument("--workers", type=int, default=14)
    parser.add_argument("--tag", type=str, default="beam")
    parser.add_argument(
        "--no-hub-seed",
        action="store_true",
        help="run the original unseeded stage-1 beam search",
    )
    args = parser.parse_args()

    started = perf_counter()
    gadgets = rooted_gadgets(args.gadget_max)
    print(f"[beam] {len(gadgets)} distinct (F, G) gadgets from rooted trees "
          f"n <= {args.gadget_max} ({perf_counter() - started:.1f}s)", flush=True)

    # Beam state: (F, G, multiset of gadget indices, n)
    beam: list[tuple[float, tuple, tuple, tuple]] = []
    for gi, gadget in enumerate(gadgets):
        beam.append((0.0, gadget["F"], gadget["G"], (gi,)))

    if not args.no_hub_seed:
        # Seed with uniform hub-spider multisets H_c^h, the known stage-2
        # states: the balance gradient is only informative once an LC failure
        # exists, and greedy stage-1 search drifts to a smooth attractor.
        hub_index: dict[int, int] = {}
        for gi, gadget in enumerate(gadgets):
            for c in range(1, 6):
                H = tuple(
                    a + b
                    for a, b in zip(
                        [int(x) for x in np_binom_row(c, 2)] + [0],
                        [0] + [int(x) for x in np_binom_row(c, 1)],
                        strict=True,
                    )
                )
                E = tuple(int(x) for x in np_binom_row(c, 2))
                if gadget["F"] == H and gadget["G"] == E:
                    hub_index[c] = gi
        for c, gi in sorted(hub_index.items()):
            gadget = gadgets[gi]
            for h in range(3, 20):
                if 1 + h * gadget["n"] > args.max_n:
                    break
                F, G = gadget["F"], gadget["G"]
                for _ in range(h - 1):
                    F = mul(F, gadget["F"])
                    G = mul(G, gadget["G"])
                combined, _, _, _ = score(compose(F, G), len(G))
                beam.append((combined, F, G, tuple([gi] * h)))
        print(f"[beam] seeded hub multisets for c in {sorted(hub_index)}", flush=True)
    else:
        print("[beam] hub seeding disabled", flush=True)

    best_overall: list[dict] = []
    counterexamples: list[dict] = []
    history = []

    with Pool(args.workers, initializer=init_worker, initargs=(gadgets,)) as pool:
        for depth in range(1, 40):
            payloads = [(F, G, multiset, args.max_n) for _, F, G, multiset in beam]
            children: list[tuple[float, int, bool, int, tuple]] = []
            for chunk in pool.imap_unordered(expand_state, payloads, chunksize=8):
                children.extend(chunk)
            if not children:
                break
            children.sort(key=lambda c: -c[0])
            # Diversity guard: cap near-identical scores so one attractor
            # cannot flood the beam.
            filtered: list = []
            score_counts: dict[float, int] = {}
            for child in children:
                key = round(child[0], 5)
                if score_counts.get(key, 0) >= 4:
                    continue
                score_counts[key] = score_counts.get(key, 0) + 1
                filtered.append(child)
                if len(filtered) >= args.beam:
                    break
            next_beam = []
            for combined, balance, k, unimodal, gi, multiset in filtered:
                new_multiset = (*multiset, gi)
                F = gadgets[new_multiset[0]]["F"]
                G = gadgets[new_multiset[0]]["G"]
                for g in new_multiset[1:]:
                    F = mul(F, gadgets[g]["F"])
                    G = mul(G, gadgets[g]["G"])
                next_beam.append((combined, F, G, new_multiset))
                if not unimodal or balance > 1.0:
                    counterexamples.append(
                        {
                            "multiset": [gadgets[g]["label"] for g in new_multiset],
                            "balance": balance,
                            "unimodal": unimodal,
                        }
                    )
                    print(f"!!! BREAKTHROUGH: balance {balance:.4f} unimodal={unimodal} "
                          f"multiset {new_multiset}", flush=True)
            beam = next_beam
            top = beam[0]
            n_top = 1 + sum(gadgets[g]["n"] for g in top[3])
            best_balance = max(0.0, top[0] - 1000.0)
            history.append({"depth": depth, "score": top[0], "best_balance": best_balance, "n": n_top})
            print(f"[beam] depth {depth}: score {top[0]:.5f} balance {best_balance:.5f} "
                  f"(n={n_top}, gadgets={len(top[3])}) beam {len(beam)}", flush=True)
            best_overall = [
                {
                    "score": s,
                    "n": 1 + sum(gadgets[g]["n"] for g in ms),
                    "multiset": [gadgets[g]["label"] for g in ms],
                }
                for s, _, _, ms in beam[:12]
            ]

    payload = {
        "gadget_max": args.gadget_max,
        "gadget_count": len(gadgets),
        "beam": args.beam,
        "max_n": args.max_n,
        "history": history,
        "best": best_overall,
        "counterexamples": counterexamples,
        "elapsed_seconds": round(perf_counter() - started, 2),
    }
    out = REPO / "logs" / f"993_cx_hunt_junction_{args.tag}.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"[done] wrote {out} ({perf_counter() - started:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
