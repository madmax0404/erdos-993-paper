from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from fractions import Fraction
from time import perf_counter
from typing import Any

import networkx as nx
from networkx.generators.nonisomorphic_trees import nonisomorphic_trees

from .families import t_3_m_n, t_3_m_n_polynomial, t_star_3_m_n, t_star_3_m_n_polynomial
from .indpoly import analyze, broom, independence_polynomial, is_log_concave, is_unimodal, log_concavity_failures, modes, mul, spider, worst_log_concavity_ratio


def fraction_payload(value: Fraction | None) -> dict[str, int] | None:
    if value is None:
        return None
    return {"numerator": value.numerator, "denominator": value.denominator}


def graph_payload(graph: nx.Graph, *, include_graph6: bool = False) -> dict[str, Any]:
    degree_counts: dict[int, int] = {}
    for _, degree in graph.degree():
        degree_counts[degree] = degree_counts.get(degree, 0) + 1
    payload: dict[str, Any] = {
        "n": graph.number_of_nodes(),
        "degree_counts": dict(sorted(degree_counts.items())),
    }
    if include_graph6:
        payload["graph6"] = nx.to_graph6_bytes(graph, header=False).decode("ascii").strip()
    return payload


def polynomial_payload(poly: tuple[int, ...]) -> dict[str, Any]:
    if len(poly) <= 24:
        return {"degree": len(poly) - 1, "coefficients": poly}
    return {
        "degree": len(poly) - 1,
        "head": poly[:10],
        "tail": poly[-10:],
    }


def scan(max_n: int, top_near: int) -> dict[str, Any]:
    per_n: list[dict[str, Any]] = []
    near_misses: list[dict[str, Any]] = []
    started = perf_counter()

    for n in range(1, max_n + 1):
        count = 0
        lc_failures = 0
        unimodality_failures = []
        n_started = perf_counter()

        for tree in nonisomorphic_trees(n):
            count += 1
            analysis = analyze(tree)
            if not analysis.unimodal:
                unimodality_failures.append(
                    {
                        "analysis": serialize_analysis(analysis),
                        "graph": graph_payload(tree, include_graph6=True),
                    }
                )
            if not analysis.log_concave:
                lc_failures += 1
            if analysis.worst_log_concavity_ratio is not None:
                near_misses.append(
                    {
                        "n": n,
                        "ratio": analysis.worst_log_concavity_ratio,
                        "polynomial": polynomial_payload(analysis.coefficients),
                        "modes": analysis.modes,
                        "graph": graph_payload(tree),
                    }
                )

        near_misses.sort(key=lambda item: item["ratio"])
        del near_misses[top_near:]

        per_n.append(
            {
                "n": n,
                "trees": count,
                "log_concavity_failures": lc_failures,
                "unimodality_failures": len(unimodality_failures),
                "elapsed_seconds": round(perf_counter() - n_started, 3),
                "first_unimodality_failures": unimodality_failures[:3],
            }
        )

    return {
        "max_n": max_n,
        "elapsed_seconds": round(perf_counter() - started, 3),
        "per_n": per_n,
        "near_misses": [
            {
                **item,
                "ratio": fraction_payload(item["ratio"]),
            }
            for item in near_misses
        ],
    }


def family_scan(max_n: int, top_near: int) -> dict[str, Any]:
    cases: list[tuple[str, nx.Graph]] = []

    for n in range(1, max_n + 1):
        for handle_edges in range(n):
            leaves = n - handle_edges - 1
            cases.append((f"broom(handle_edges={handle_edges}, leaves={leaves})", broom(handle_edges, leaves)))

        # Balanced and nearly balanced spiders with 3 to 8 arms.
        for arm_count in range(3, min(9, n + 1)):
            remaining_edges = n - 1
            base, extra = divmod(remaining_edges, arm_count)
            arms = [base + (1 if i < extra else 0) for i in range(arm_count)]
            if all(arm > 0 for arm in arms):
                cases.append((f"balanced_spider(arms={arms})", spider(arms)))

    near: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for name, tree in cases:
        analysis = analyze(tree)
        if not analysis.unimodal:
            failures.append(
                {
                    "name": name,
                    "analysis": serialize_analysis(analysis),
                    "graph": graph_payload(tree, include_graph6=True),
                }
            )
        if analysis.worst_log_concavity_ratio is not None:
            near.append(
                {
                    "name": name,
                    "n": tree.number_of_nodes(),
                    "ratio": analysis.worst_log_concavity_ratio,
                    "polynomial": polynomial_payload(analysis.coefficients),
                    "modes": analysis.modes,
                    "graph": graph_payload(tree),
                }
            )

    near.sort(key=lambda item: item["ratio"])
    return {
        "max_n": max_n,
        "cases": len(cases),
        "unimodality_failures": failures,
        "near_misses": [
            {
                **item,
                "ratio": fraction_payload(item["ratio"]),
            }
            for item in near[:top_near]
        ],
    }


def forest_scan(max_n: int) -> dict[str, Any]:
    """Search products of tree independence polynomials up to max_n vertices.

    This collapses forests with the same independence polynomial. That is enough
    for counterexample search, while keeping the state space much smaller than
    enumerating unlabeled forests directly.
    """

    started = perf_counter()
    component_types: list[dict[str, Any]] = []
    for n in range(1, max_n + 1):
        unique_for_n: dict[tuple[int, ...], dict[str, Any]] = {}
        for tree in nonisomorphic_trees(n):
            poly = independence_polynomial(tree)
            unique_for_n.setdefault(poly, graph_payload(tree, include_graph6=True))
        for poly, graph in unique_for_n.items():
            component_types.append({"n": n, "poly": poly, "graph": graph})

    states: list[dict[tuple[int, ...], list[int]]] = [dict() for _ in range(max_n + 1)]
    states[0][(1,)] = []
    first_failure: dict[str, Any] | None = None

    for type_index, component in enumerate(component_types):
        size = component["n"]
        poly = component["poly"]
        for total in range(size, max_n + 1):
            previous_items = list(states[total - size].items())
            for old_poly, old_witness in previous_items:
                new_poly = mul(old_poly, poly)
                if new_poly in states[total]:
                    continue
                witness = [*old_witness, type_index]
                states[total][new_poly] = witness
                if first_failure is None and not is_unimodal(new_poly):
                    first_failure = {
                        "n": total,
                        "polynomial": polynomial_payload(new_poly),
                        "components": [
                            {
                                "n": component_types[i]["n"],
                                "polynomial": polynomial_payload(component_types[i]["poly"]),
                                "graph": component_types[i]["graph"],
                            }
                            for i in witness
                        ],
                    }

    return {
        "max_n": max_n,
        "elapsed_seconds": round(perf_counter() - started, 3),
        "component_types": len(component_types),
        "unique_forest_polynomials_by_n": [
            {"n": n, "count": len(states[n])} for n in range(1, max_n + 1)
        ],
        "first_unimodality_failure": first_failure,
    }


def known_family_scan(max_parameter: int) -> dict[str, Any]:
    cases: list[tuple[str, int, tuple[int, ...]]] = []
    for m in range(1, max_parameter + 1):
        for n in range(1, max_parameter + 1):
            cases.append((f"T_{{3,{m},{n}}}", 10 + 2 * m + 2 * n, t_3_m_n_polynomial(m, n)))
            cases.append((f"T*_{{3,{m},{n}}}", 12 + 2 * m + 2 * n, t_star_3_m_n_polynomial(m, n)))

    failures: list[dict[str, Any]] = []
    lc_failure_payloads: list[dict[str, Any]] = []
    for name, order, poly in cases:
        payload = {
            "name": name,
            "n": order,
            "modes": modes(poly),
            "polynomial": polynomial_payload(poly),
        }
        if not is_unimodal(poly):
            failures.append(payload)
        if not is_log_concave(poly):
            lc_failure_payloads.append(
                {
                    **payload,
                    "log_concavity_failures": log_concavity_failures(poly),
                    "worst_ratio": fraction_payload(worst_log_concavity_ratio(poly)),
                }
            )

    return {
        "max_parameter": max_parameter,
        "cases": len(cases),
        "unimodality_failures": failures,
        "log_concavity_failure_count": len(lc_failure_payloads),
        "first_log_concavity_failures": lc_failure_payloads[:20],
    }


def serialize_analysis(analysis: Any) -> dict[str, Any]:
    payload = asdict(analysis)
    payload["worst_log_concavity_ratio"] = fraction_payload(analysis.worst_log_concavity_ratio)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description="Explore Erdős Problem #993.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="scan non-isomorphic trees")
    scan_parser.add_argument("--max-n", type=int, default=14)
    scan_parser.add_argument("--top-near", type=int, default=10)

    family_parser = subparsers.add_parser("families", help="scan simple structured tree families")
    family_parser.add_argument("--max-n", type=int, default=100)
    family_parser.add_argument("--top-near", type=int, default=10)

    forest_parser = subparsers.add_parser("forests", help="scan products of small-tree polynomials")
    forest_parser.add_argument("--max-n", type=int, default=16)

    known_parser = subparsers.add_parser("known-families", help="scan T_{3,m,n} and T*_{3,m,n}")
    known_parser.add_argument("--max-parameter", type=int, default=12)

    args = parser.parse_args()
    if args.command == "scan":
        payload = scan(args.max_n, args.top_near)
    elif args.command == "families":
        payload = family_scan(args.max_n, args.top_near)
    elif args.command == "forests":
        payload = forest_scan(args.max_n)
    elif args.command == "known-families":
        payload = known_family_scan(args.max_parameter)
    else:
        raise AssertionError(f"unknown command {args.command}")

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
