"""Atlas of log-concavity failures across structured tree families.

Motivation: a forest counterexample to Erdős 993 needs at least one non-LC
tree factor (products of log-concave sequences are log-concave, hence
unimodal).  Every known non-LC tree fails only at offset 1-2 below the top
degree, with a monic cliff (right neighbor 1), and width-1 cliffs are erased
by the >= sqrt(n) spread of any partner polynomial.  This probe maps, over a
rich constructor space:

  - the maximum failure offset from the top degree;
  - the maximum "balance" min(left, right)/mid at a failure (close to 1
    means a genuine valley seed, > 1 would be a non-unimodal tree);
  - whether any non-monic tree (lead >= 2, multiple maximum independent
    sets) has an LC failure at all.

Families: spine trees with per-vertex (leaf, P2-arm, P3-arm) attachments
(generalizing stars, brooms, spiders, T_{a,b,c}, multi-hub spiders with
mixed arms), depth-3 hub spiders, and corona-with-gadget grafts.
"""

from __future__ import annotations

import argparse
import json
import sys
from itertools import product
from multiprocessing import Pool
from pathlib import Path
from time import perf_counter

import networkx as nx

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from erdos993.indpoly import independence_polynomial, is_unimodal  # noqa: E402

MAX_N = 36


# ----------------------------------------------------------------------------
# Constructors
# ----------------------------------------------------------------------------


def attach(graph: nx.Graph, site: int, leaves: int, p2: int, p3: int, nxt: int) -> int:
    for _ in range(leaves):
        graph.add_edge(site, nxt)
        nxt += 1
    for _ in range(p2):
        graph.add_edge(site, nxt)
        graph.add_edge(nxt, nxt + 1)
        nxt += 2
    for _ in range(p3):
        graph.add_edge(site, nxt)
        graph.add_edge(nxt, nxt + 1)
        graph.add_edge(nxt + 1, nxt + 2)
        nxt += 3
    return nxt


def spine_tree(specs: tuple[tuple[int, int, int], ...]) -> nx.Graph:
    spine = len(specs)
    graph = nx.path_graph(spine)
    nxt = spine
    for site, (leaves, p2, p3) in enumerate(specs):
        nxt = attach(graph, site, leaves, p2, p3, nxt)
    return graph


def depth3_spider(hubs: tuple[tuple[int, int, int], ...]) -> nx.Graph:
    """Root with hubs; hub i has (subhubs, arms_per_subhub, direct_p2) structure."""

    graph = nx.Graph()
    graph.add_node(0)
    nxt = 1
    for subhubs, arms_each, direct_p2 in hubs:
        hub = nxt
        graph.add_edge(0, hub)
        nxt += 1
        for _ in range(subhubs):
            sub = nxt
            graph.add_edge(hub, sub)
            nxt += 1
            for _ in range(arms_each):
                graph.add_edge(sub, nxt)
                graph.add_edge(nxt, nxt + 1)
                nxt += 2
        for _ in range(direct_p2):
            graph.add_edge(hub, nxt)
            graph.add_edge(nxt, nxt + 1)
            nxt += 2
    return graph


def corona_path_with_gadget(k: int, leaves: int, p2: int, p3: int) -> nx.Graph:
    """Corona of P_k (flat heavy tail) with a gadget grafted at one end."""

    graph = nx.path_graph(k)
    for v in range(k):
        graph.add_edge(v, k + v)
    nxt = 2 * k
    attach(graph, 0, leaves, p2, p3, nxt)
    return graph


def build_jobs(args: argparse.Namespace) -> list[tuple[str, nx.Graph]]:
    jobs: list[tuple[str, nx.Graph]] = []

    def site_options(budget: int, step: int = 1) -> list[tuple[int, int, int]]:
        out = []
        for a in range(0, min(16, budget) + 1, step):
            for b in range(0, (budget - a) // 2 + 1, step):
                for c in range(0, (budget - a - 2 * b) // 3 + 1, step):
                    out.append((a, b, c))
        return out

    # Single-site: generalized mixed-arm spiders.
    for spec in site_options(MAX_N - 1):
        a, b, c = spec
        if a + b + c >= 3:
            jobs.append((f"spine1[{spec}]", spine_tree((spec,))))

    # Two-site spine trees.
    options2 = site_options(MAX_N - 2)
    for s1 in options2:
        n1 = s1[0] + 2 * s1[1] + 3 * s1[2]
        if n1 > MAX_N - 2:
            continue
        for s2 in options2:
            if s2 < s1:
                continue
            n2 = s2[0] + 2 * s2[1] + 3 * s2[2]
            if 2 + n1 + n2 <= MAX_N and (n1 and n2):
                jobs.append((f"spine2[{s1},{s2}]", spine_tree((s1, s2))))

    # Three-site spine trees, coarser grid.
    options3 = site_options(MAX_N - 3, step=2)
    for s1 in options3:
        n1 = s1[0] + 2 * s1[1] + 3 * s1[2]
        for s2 in options3:
            n2 = s2[0] + 2 * s2[1] + 3 * s2[2]
            if 3 + n1 + n2 > MAX_N:
                continue
            for s3 in options3:
                if s3 < s1:
                    continue
                n3 = s3[0] + 2 * s3[1] + 3 * s3[2]
                if 3 + n1 + n2 + n3 <= MAX_N:
                    jobs.append((f"spine3[{s1},{s2},{s3}]", spine_tree((s1, s2, s3))))

    # Depth-3 spiders.
    hub_opts = [
        (s, ae, d)
        for s in range(0, 5)
        for ae in range(0, 5)
        for d in range(0, 7)
        if (s and ae) or d
    ]
    for h1 in hub_opts:
        for h2 in hub_opts:
            if h2 < h1:
                continue
            graph = depth3_spider((h1, h2))
            if graph.number_of_nodes() <= MAX_N:
                jobs.append((f"depth3[{h1},{h2}]", graph))
    for h1 in hub_opts:
        for h2 in hub_opts:
            if h2 < h1:
                continue
            for h3 in hub_opts:
                if h3 < h2:
                    continue
                size = 1 + sum(1 + s * (1 + 2 * ae) + 2 * d for s, ae, d in (h1, h2, h3))
                if size <= MAX_N:
                    jobs.append((f"depth3[{h1},{h2},{h3}]", depth3_spider((h1, h2, h3))))

    # Corona of P_k with a gadget at one end.
    for k in range(2, 13):
        for a in range(0, 13):
            for b in range(0, 9):
                for c in range(0, 5):
                    n = 2 * k + a + 2 * b + 3 * c
                    if n <= MAX_N and (a or b or c):
                        jobs.append(
                            (f"corona(P{k})+[{a},{b},{c}]", corona_path_with_gadget(k, a, b, c))
                        )

    return jobs


# ----------------------------------------------------------------------------
# Scoring
# ----------------------------------------------------------------------------


def analyze_job(item: tuple[str, nx.Graph]) -> dict | None:
    label, graph = item
    poly = independence_polynomial(graph)
    d = len(poly) - 1
    failures = []
    for k in range(1, d):
        if poly[k] * poly[k] < poly[k - 1] * poly[k + 1]:
            balance = min(poly[k - 1], poly[k + 1]) / poly[k]
            lc_ratio = (poly[k] * poly[k]) / (poly[k - 1] * poly[k + 1])
            failures.append(
                {
                    "k": k,
                    "offset": d - k,
                    "balance": balance,
                    "lc_ratio": lc_ratio,
                }
            )
    if not failures:
        return None
    return {
        "label": label,
        "n": graph.number_of_nodes(),
        "alpha": d,
        "lead": poly[-1],
        "monic": poly[-1] == 1,
        "unimodal": is_unimodal(poly),
        "tail": list(poly[-6:]),
        "failures": failures,
        "max_offset": max(f["offset"] for f in failures),
        "max_balance": max(f["balance"] for f in failures),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=14)
    parser.add_argument("--tag", type=str, default="atlas")
    args = parser.parse_args()

    started = perf_counter()
    jobs = build_jobs(args)
    print(f"[atlas] {len(jobs)} constructor trees (n <= {MAX_N})", flush=True)

    non_lc: list[dict] = []
    non_unimodal: list[dict] = []
    with Pool(args.workers) as pool:
        for result in pool.imap_unordered(analyze_job, jobs, chunksize=256):
            if result is None:
                continue
            non_lc.append(result)
            if not result["unimodal"]:
                non_unimodal.append(result)
                print(f"!!! NON-UNIMODAL TREE: {result['label']}", flush=True)

    non_lc.sort(key=lambda r: -r["max_balance"])
    by_offset: dict[int, int] = {}
    nonmonic = [r for r in non_lc if not r["monic"]]
    for r in non_lc:
        by_offset[r["max_offset"]] = by_offset.get(r["max_offset"], 0) + 1

    print(f"[atlas] non-LC trees: {len(non_lc)} / {len(jobs)}", flush=True)
    print(f"[atlas] max-offset histogram: {dict(sorted(by_offset.items()))}", flush=True)
    print(f"[atlas] non-monic non-LC trees: {len(nonmonic)}", flush=True)
    print("[atlas] top balance champions:", flush=True)
    for r in non_lc[:12]:
        print(f"   balance {r['max_balance']:.4f} offset {r['max_offset']} lead {r['lead']} "
              f"n={r['n']} tail {r['tail']} {r['label']}", flush=True)
    if nonmonic:
        nonmonic.sort(key=lambda r: -r["max_balance"])
        print("[atlas] top non-monic champions:", flush=True)
        for r in nonmonic[:12]:
            print(f"   balance {r['max_balance']:.4f} offset {r['max_offset']} lead {r['lead']} "
                  f"n={r['n']} tail {r['tail']} {r['label']}", flush=True)

    payload = {
        "constructor_trees": len(jobs),
        "non_lc_count": len(non_lc),
        "non_unimodal": non_unimodal,
        "max_offset_histogram": dict(sorted(by_offset.items())),
        "non_monic_non_lc": len(nonmonic),
        "top_balance": non_lc[:200],
        "top_non_monic": nonmonic[:200],
        "elapsed_seconds": round(perf_counter() - started, 2),
    }
    out = REPO / "logs" / f"993_cx_hunt_lc_dip_{args.tag}.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"[done] wrote {out} ({perf_counter() - started:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
