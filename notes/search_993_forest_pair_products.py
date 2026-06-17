"""Counterexample hunt for Erdős 993: pair products of tree polynomials.

Build a catalog of exact tree independence polynomials (exhaustive small
trees, heavy-tail structured families, random trees), then scan products of
two catalog entries for unimodality failures.  A forest counterexample
falsifies the conjecture as stated (trees or forests).

Exactness: every catalog polynomial comes from the verified integer DP in
src/erdos993/indpoly.py (or the regression-checked closed forms in
families.py).  Pair products use numpy int64 convolution, which is exact
because every product coefficient is at most C(64, 32) < 2^63 when the total
vertex count is at most 64.  Any candidate hit is re-verified by rebuilding
the forest as a graph and recomputing from scratch.

Usage:
  uv run python notes/search_993_forest_pair_products.py \
      --exhaustive-max 17 --tag main \
      --top-pool 2500 --random-pairs 2000000
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from dataclasses import dataclass
from math import comb
from multiprocessing import Pool
from pathlib import Path
from time import perf_counter

import networkx as nx
import numpy as np
from networkx.generators.nonisomorphic_trees import nonisomorphic_trees

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from erdos993.families import t_3_m_n_polynomial, t_star_3_m_n_polynomial  # noqa: E402
from erdos993.indpoly import independence_polynomial, is_unimodal  # noqa: E402

MAX_TOTAL_N = 64  # int64-exact bound: product coefficients <= C(64,32) < 2^63


# ----------------------------------------------------------------------------
# Catalog construction
# ----------------------------------------------------------------------------


@dataclass
class Entry:
    label: str
    n: int
    poly: tuple[int, ...]
    graph6: str | None  # present when we built an explicit graph


def graph_to_graph6(graph: nx.Graph) -> str:
    canonical = nx.convert_node_labels_to_integers(graph)
    return nx.to_graph6_bytes(canonical, header=False).decode("ascii").strip()


def caterpillar(spine: int, legs: tuple[int, ...]) -> nx.Graph:
    """Spine path with a pendant path of length legs[i] at spine vertex i."""

    graph = nx.path_graph(spine)
    nxt = spine
    for i, leg in enumerate(legs):
        prev = i
        for _ in range(leg):
            graph.add_edge(prev, nxt)
            prev = nxt
            nxt += 1
    return graph


def spider(arms: tuple[int, ...]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_node(0)
    nxt = 1
    for arm in arms:
        prev = 0
        for _ in range(arm):
            graph.add_edge(prev, nxt)
            prev = nxt
            nxt += 1
    return graph


def hub_spider(counts: tuple[int, ...], root_leaves: int = 0) -> nx.Graph:
    """Root with one hub per entry; hub i carries counts[i] length-2 arms.

    Generalizes the T_{a,b,c} construction to any number of hubs.  Optional
    pendant leaves at the root add a binomial spike to the same tree, so this
    family carries both counterexample ingredients (sharp spike, deep
    log-convex tail dip) in a single connected graph.
    """

    graph = nx.Graph()
    graph.add_node(0)
    nxt = 1
    for count in counts:
        hub = nxt
        graph.add_edge(0, hub)
        nxt += 1
        for _ in range(count):
            mid, leaf = nxt, nxt + 1
            graph.add_edge(hub, mid)
            graph.add_edge(mid, leaf)
            nxt += 2
    for _ in range(root_leaves):
        graph.add_edge(0, nxt)
        nxt += 1
    return graph


def corona(base: nx.Graph) -> nx.Graph:
    """Attach one pendant leaf to every vertex of base."""

    graph = nx.convert_node_labels_to_integers(base)
    n = graph.number_of_nodes()
    for v in range(n):
        graph.add_edge(v, n + v)
    return graph


def pendant_p2_everywhere(base: nx.Graph) -> nx.Graph:
    """Attach one pendant length-2 path to every vertex of base."""

    graph = nx.convert_node_labels_to_integers(base)
    n = graph.number_of_nodes()
    for v in range(n):
        graph.add_edge(v, n + 2 * v)
        graph.add_edge(n + 2 * v, n + 2 * v + 1)
    return graph


def leg_patterns(spine: int, rng: random.Random, random_per_spine: int) -> list[tuple[int, ...]]:
    patterns: set[tuple[int, ...]] = set()
    patterns.add(tuple([1] * spine))  # corona of path
    patterns.add(tuple([2] * spine))
    for period in ((0, 1), (0, 2), (1, 2), (0, 1, 2), (2, 1), (2, 0), (1, 0)):
        patterns.add(tuple(period[i % len(period)] for i in range(spine)))
    for split in range(1, spine):
        patterns.add(tuple([1] * split + [2] * (spine - split)))
        patterns.add(tuple([0] * split + [2] * (spine - split)))
    for _ in range(random_per_spine):
        patterns.add(tuple(rng.choice((0, 1, 2)) for _ in range(spine)))
    return sorted(patterns)


def build_graph_jobs(args: argparse.Namespace) -> list[tuple[str, nx.Graph]]:
    rng = random.Random(args.seed)
    jobs: list[tuple[str, nx.Graph]] = []

    for spine in range(2, args.spine_max + 1):
        for legs in leg_patterns(spine, rng, args.random_leg_patterns):
            graph = caterpillar(spine, legs)
            if graph.number_of_nodes() <= MAX_TOTAL_N:
                jobs.append((f"caterpillar(spine={spine},legs={''.join(map(str, legs))})", graph))

    for a in range(0, 33):
        for b in range(0, 29):
            for c in range(0, 17):
                n = 1 + a + 2 * b + 3 * c
                if 4 <= n <= MAX_TOTAL_N and a + b + c >= 3:
                    jobs.append((f"spider(1^{a},2^{b},3^{c})", spider(tuple([1] * a + [2] * b + [3] * c))))

    def hub_count_lists(parts: int, total_max: int) -> list[tuple[int, ...]]:
        out: list[tuple[int, ...]] = []

        def rec(prefix: list[int], remaining: int, minimum: int) -> None:
            if prefix:
                out.append(tuple(prefix))
            if len(prefix) == parts:
                return
            for value in range(minimum, remaining + 1):
                rec([*prefix, value], remaining - value, value)

        rec([], total_max, 1)
        return out

    seen_hub: set[tuple[int, ...]] = set()
    for counts in hub_count_lists(parts=7, total_max=30):
        if counts in seen_hub:
            continue
        seen_hub.add(counts)
        n = 1 + len(counts) + 2 * sum(counts)
        if 7 <= n <= MAX_TOTAL_N and len(counts) >= 2:
            jobs.append((f"hubspider{counts}", hub_spider(counts)))
        if len(counts) >= 2:
            for root_leaves in (4, 8, 12, 16, 20, 24, 28):
                rooted_n = n + root_leaves
                if rooted_n <= MAX_TOTAL_N:
                    jobs.append(
                        (f"hubspider{counts}+r{root_leaves}", hub_spider(counts, root_leaves))
                    )

    base_trees: list[tuple[str, nx.Graph]] = []
    for n in range(2, args.corona_base_max + 1):
        for index, tree in enumerate(nonisomorphic_trees(n)):
            base_trees.append((f"n{n}i{index}", tree))
    for name, tree in base_trees:
        big = corona(tree)
        if big.number_of_nodes() <= MAX_TOTAL_N:
            jobs.append((f"corona({name})", big))
        bigger = pendant_p2_everywhere(tree)
        if bigger.number_of_nodes() <= MAX_TOTAL_N:
            jobs.append((f"p2corona({name})", bigger))

    for n in range(18, MAX_TOTAL_N + 1, 2):
        for repeat in range(args.random_trees_per_n):
            seed = rng.randrange(2**31)
            tree = nx.random_labeled_tree(n, seed=seed)
            jobs.append((f"random(n={n},seed={seed})", tree))

    return jobs


def poly_job(item: tuple[str, nx.Graph]) -> Entry:
    label, graph = item
    poly = independence_polynomial(graph)
    return Entry(label=label, n=graph.number_of_nodes(), poly=poly, graph6=graph_to_graph6(graph))


def exhaustive_job(n: int) -> list[Entry]:
    out: list[Entry] = []
    for index, tree in enumerate(nonisomorphic_trees(n)):
        poly = independence_polynomial(tree)
        out.append(
            Entry(
                label=f"tree(n={n},idx={index})",
                n=n,
                poly=poly,
                graph6=graph_to_graph6(tree),
            )
        )
    return out


def build_catalog(args: argparse.Namespace, pool: Pool) -> list[Entry]:
    started = perf_counter()
    entries: list[Entry] = []

    exhaustive_ns = list(range(2, args.exhaustive_max + 1))
    for chunk in pool.imap_unordered(exhaustive_job, exhaustive_ns):
        entries.extend(chunk)
    print(f"[catalog] exhaustive n<={args.exhaustive_max}: {len(entries)} trees "
          f"({perf_counter() - started:.1f}s)", flush=True)

    jobs = build_graph_jobs(args)
    family_started = perf_counter()
    for entry in pool.imap_unordered(poly_job, jobs, chunksize=64):
        entries.append(entry)
    print(f"[catalog] families+random: {len(jobs)} graphs "
          f"({perf_counter() - family_started:.1f}s)", flush=True)

    for m in range(1, 27):
        for n in range(m, 27):
            if 10 + 2 * m + 2 * n <= MAX_TOTAL_N:
                entries.append(Entry(f"T(3,{m},{n})", 10 + 2 * m + 2 * n, t_3_m_n_polynomial(m, n), None))
            if 12 + 2 * m + 2 * n <= MAX_TOTAL_N:
                entries.append(Entry(f"T*(3,{m},{n})", 12 + 2 * m + 2 * n, t_star_3_m_n_polynomial(m, n), None))

    unique: dict[tuple[int, ...], Entry] = {}
    for entry in entries:
        known = unique.get(entry.poly)
        if known is None or entry.n < known.n:
            unique[entry.poly] = entry
    catalog = sorted(unique.values(), key=lambda e: (e.n, e.label))
    print(f"[catalog] total {len(entries)} entries, {len(catalog)} distinct polynomials "
          f"({perf_counter() - started:.1f}s)", flush=True)
    return catalog


# ----------------------------------------------------------------------------
# Valley scoring and pair scanning
# ----------------------------------------------------------------------------

POLYS: list[np.ndarray] = []
SIZES: np.ndarray | None = None


def init_worker(polys: list[np.ndarray], sizes: np.ndarray) -> None:
    global POLYS, SIZES
    POLYS = polys
    SIZES = sizes


def valley_metrics(conv: np.ndarray) -> tuple[int, float, int, int]:
    """Return (abs_margin, dip_ratio, dip_index, lc_fail_count).

    abs_margin >= 1 anywhere means the sequence is NOT unimodal (exact int64
    prefix/suffix maxima test).  The near-miss score is LC-dip based: a valley
    bottom is always a log-concavity failure point, so we look at interior LC
    failures in the first two thirds (valleys cannot live in the last third
    for KE graphs by Levit-Mandrescu) and report the best ratio
    min(left, right) / mid there.  Ratio > 1 is a strict valley; close to 1
    from below is a genuine budding dip.  A smooth single-peak shoulder is
    log-concave, so it cannot score at all - this metric is immune to the
    near-mode flatness artifact.
    """

    pmax = np.maximum.accumulate(conv)
    smax = np.maximum.accumulate(conv[::-1])[::-1]
    hump = np.minimum(pmax[:-2], smax[2:])
    abs_margin = int((hump - conv[1:-1]).max())

    f = conv.astype(np.float64)
    left, mid, right = f[:-2], f[1:-1], f[2:]
    lc_fail = mid * mid < left * right
    cut = max(1, (2 * (conv.size - 1)) // 3)
    lc_fail[cut:] = False
    count = int(lc_fail.sum())
    if not count:
        return abs_margin, 0.0, -1, 0
    ratio = np.minimum(left, right)[lc_fail] / mid[lc_fail]
    pick = int(np.argmax(ratio))
    dip_index = int(np.nonzero(lc_fail)[0][pick]) + 1
    return abs_margin, float(ratio[pick]), dip_index, count


def scan_chunk(pairs: np.ndarray) -> tuple[list, list, int]:
    """Score pairs; return (top near-misses by dip ratio, detections, count)."""

    results: list[tuple[float, int, int, int, int, int]] = []
    detections: list[tuple[int, int, int]] = []
    for i, j in pairs:
        conv = np.convolve(POLYS[i], POLYS[j])
        abs_margin, dip_ratio, b, count = valley_metrics(conv)
        if abs_margin >= 1:
            detections.append((abs_margin, i, j))
        results.append((dip_ratio, abs_margin, b, count, i, j))
    results.sort(reverse=True)
    return results[:60], detections, len(pairs)


def run_strategy(
    name: str,
    pairs: np.ndarray,
    pool: Pool,
    keep: int,
) -> tuple[dict, list[tuple[int, int, int]]]:
    started = perf_counter()
    top: list[tuple[float, int, int, int, int, int]] = []
    detections: list[tuple[int, int, int]] = []
    scanned = 0
    chunks = np.array_split(pairs, max(1, len(pairs) // 20000))
    for chunk_top, chunk_detections, count in pool.imap_unordered(scan_chunk, chunks):
        scanned += count
        detections.extend(chunk_detections)
        top.extend(chunk_top)
        top.sort(reverse=True)
        del top[keep:]
    elapsed = perf_counter() - started
    print(f"[scan:{name}] {scanned} pairs in {elapsed:.1f}s, "
          f"best dip ratio {top[0][0]:.6f}, best abs margin {max(t[1] for t in top)}, "
          f"detections {len(detections)}", flush=True)
    result = {
        "strategy": name,
        "pairs_scanned": scanned,
        "elapsed_seconds": round(elapsed, 2),
        "top": top,
    }
    return result, detections


def admissible_pairs_among(indices: np.ndarray, sizes: np.ndarray) -> np.ndarray:
    ii, jj = np.meshgrid(indices, indices, indexing="ij")
    mask = (ii <= jj) & (sizes[ii] + sizes[jj] <= MAX_TOTAL_N)
    return np.stack([ii[mask], jj[mask]], axis=1)


def cross_pairs(a: np.ndarray, b: np.ndarray, sizes: np.ndarray) -> np.ndarray:
    ii, jj = np.meshgrid(a, b, indexing="ij")
    mask = sizes[ii] + sizes[jj] <= MAX_TOTAL_N
    pairs = np.stack([ii[mask], jj[mask]], axis=1)
    pairs.sort(axis=1)
    return np.unique(pairs, axis=0)


# ----------------------------------------------------------------------------
# Verification
# ----------------------------------------------------------------------------


def exact_product(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return tuple(out)


def verify_candidate(e1: Entry, e2: Entry) -> dict:
    """Re-verify a candidate hit from scratch with arbitrary precision."""

    product = exact_product(e1.poly, e2.poly)
    payload: dict = {
        "factor_labels": [e1.label, e2.label],
        "factor_ns": [e1.n, e2.n],
        "factor_polys": [list(e1.poly), list(e2.poly)],
        "product": [str(c) for c in product],
        "product_unimodal_exact": is_unimodal(product),
    }
    if e1.graph6 and e2.graph6:
        g1 = nx.from_graph6_bytes(e1.graph6.encode("ascii"))
        g2 = nx.from_graph6_bytes(e2.graph6.encode("ascii"))
        forest = nx.disjoint_union(g1, g2)
        recomputed = independence_polynomial(forest)
        payload["graph6"] = [e1.graph6, e2.graph6]
        payload["recomputed_matches"] = tuple(recomputed) == product
        payload["forest_unimodal_recomputed"] = is_unimodal(recomputed)
    return payload


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exhaustive-max", type=int, default=17)
    parser.add_argument("--corona-base-max", type=int, default=13)
    parser.add_argument("--spine-max", type=int, default=21)
    parser.add_argument("--random-leg-patterns", type=int, default=40)
    parser.add_argument("--random-trees-per-n", type=int, default=60)
    parser.add_argument("--top-pool", type=int, default=2500)
    parser.add_argument("--random-pairs", type=int, default=2_000_000)
    parser.add_argument("--keep", type=int, default=60)
    parser.add_argument("--workers", type=int, default=14)
    parser.add_argument("--seed", type=int, default=993)
    parser.add_argument("--tag", type=str, default="smoke")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    started = perf_counter()

    with Pool(args.workers) as pool:
        catalog = build_catalog(args, pool)

    polys = [np.array(e.poly, dtype=np.int64) for e in catalog]
    for entry in catalog:
        if max(entry.poly) > comb(entry.n, entry.n // 2):
            raise AssertionError(f"coefficient bound violated for {entry.label}")
    sizes = np.array([e.n for e in catalog], dtype=np.int64)
    alphas = np.array([len(e.poly) - 1 for e in catalog], dtype=np.float64)
    leads = np.array([float(e.poly[-1]) for e in catalog])
    maxes = np.array([float(max(e.poly)) for e in catalog])
    tail_ratios = leads / maxes
    spike_fracs = maxes / np.array([float(sum(e.poly)) for e in catalog])

    def own_dip(poly: np.ndarray) -> float:
        """Worst own log-concavity ratio (1.0 when log-concave)."""

        if poly.size < 3:
            return 1.0
        f = poly.astype(np.float64)
        with np.errstate(divide="ignore", invalid="ignore"):
            ratios = (f[1:-1] * f[1:-1]) / (f[:-2] * f[2:])
        ratios = ratios[np.isfinite(ratios)]
        return float(min(1.0, ratios.min())) if ratios.size else 1.0

    own_dips = np.array([own_dip(p) for p in polys])

    def top_by(score: np.ndarray, mask: np.ndarray, count: int) -> np.ndarray:
        indices = np.nonzero(mask)[0]
        order = indices[np.argsort(-score[indices], kind="stable")]
        return order[:count]

    # Size-banded pools so the n1+n2 <= 64 filter does not starve any strategy.
    dip_pool = top_by(-own_dips, (own_dips < 1.0) & (sizes <= 50), args.top_pool)
    spike_pool = top_by(spike_fracs, sizes <= 24, args.top_pool)
    tail_small = top_by(tail_ratios, sizes <= 32, args.top_pool)
    tail_tiny = top_by(tail_ratios, sizes <= 18, args.top_pool)

    strategies: list[tuple[str, np.ndarray]] = [
        ("dip_x_spike", cross_pairs(dip_pool, spike_pool, sizes)),
        ("dip_x_dip", admissible_pairs_among(top_by(-own_dips, (own_dips < 1.0) & (sizes <= 32), args.top_pool), sizes)),
        ("tail32_x_tail32", admissible_pairs_among(tail_small, sizes)),
        ("tail46_x_tail18", cross_pairs(top_by(tail_ratios, (sizes > 32) & (sizes <= 46), args.top_pool), tail_tiny, sizes)),
    ]

    n_catalog = len(catalog)
    random_pairs: list[np.ndarray] = []
    random_count = 0
    while random_count < args.random_pairs:
        raw = rng.integers(0, n_catalog, size=(args.random_pairs, 2))
        mask = sizes[raw[:, 0]] + sizes[raw[:, 1]] <= MAX_TOTAL_N
        kept = raw[mask]
        random_pairs.append(kept)
        random_count += len(kept)
        if not len(kept):
            break
    strategies.append(("random", np.concatenate(random_pairs)[: args.random_pairs]))

    all_results = []
    hits: list[dict] = []
    with Pool(args.workers, initializer=init_worker, initargs=(polys, sizes)) as pool:
        for name, pairs in strategies:
            if not len(pairs):
                continue
            result, detections = run_strategy(name, pairs, pool, args.keep)
            for abs_margin, i, j in detections:
                hits.append(verify_candidate(catalog[i], catalog[j]))
            result["top"] = [
                {
                    "dip_ratio": dip_ratio,
                    "abs_margin": margin,
                    "dip_index": b,
                    "lc_fails": count,
                    "labels": [catalog[i].label, catalog[j].label],
                    "ns": [int(sizes[i]), int(sizes[j])],
                }
                for dip_ratio, margin, b, count, i, j in result["top"]
            ]
            all_results.append(result)

    payload = {
        "tag": args.tag,
        "catalog_size": len(catalog),
        "catalog_args": {
            "exhaustive_max": args.exhaustive_max,
            "corona_base_max": args.corona_base_max,
            "spine_max": args.spine_max,
            "random_leg_patterns": args.random_leg_patterns,
            "random_trees_per_n": args.random_trees_per_n,
            "seed": args.seed,
        },
        "elapsed_seconds": round(perf_counter() - started, 2),
        "strategies": all_results,
        "counterexample_candidates": hits,
    }
    out_path = REPO / "logs" / f"993_cx_hunt_pairscan_{args.tag}.json"
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"[done] wrote {out_path} ({perf_counter() - started:.1f}s total)", flush=True)
    if hits:
        print("!!! COUNTEREXAMPLE CANDIDATES FOUND - see JSON for exact verification !!!", flush=True)
    else:
        print("[done] no unimodality failure; nearest relative margins above", flush=True)


if __name__ == "__main__":
    main()
