from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

import networkx as nx


Poly = tuple[int, ...]


@dataclass(frozen=True)
class IndependenceAnalysis:
    """Computed diagnostics for an independence polynomial."""

    coefficients: Poly
    unimodal: bool
    log_concave: bool
    modes: tuple[int, ...]
    log_concavity_failures: tuple[tuple[int, int, int, int], ...]
    worst_log_concavity_ratio: Fraction | None


def trim(poly: Sequence[int]) -> Poly:
    end = len(poly)
    while end > 1 and poly[end - 1] == 0:
        end -= 1
    return tuple(poly[:end])


def add(a: Sequence[int], b: Sequence[int]) -> Poly:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(out)


def mul(a: Sequence[int], b: Sequence[int]) -> Poly:
    if not a or not b:
        return (0,)
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj:
                out[i + j] += ai * bj
    return trim(out)


def x_mul(poly: Sequence[int]) -> Poly:
    return (0, *poly)


def independence_polynomial(graph: nx.Graph) -> Poly:
    """Return (i_0, i_1, ..., i_alpha) for a forest.

    The recurrence is rooted-tree DP. For a vertex v:
      included(v) = x * product excluded(child)
      excluded(v) = product total(child)

    For a forest, component polynomials multiply.
    """

    if graph.number_of_nodes() == 0:
        return (1,)
    if not nx.is_forest(graph):
        raise ValueError("independence_polynomial currently expects a forest")

    result: Poly = (1,)
    seen: set[object] = set()
    adjacency = graph.adj

    for root in graph.nodes:
        if root in seen:
            continue

        parent: dict[object, object | None] = {root: None}
        order: list[object] = []
        stack = [root]
        seen.add(root)
        while stack:
            node = stack.pop()
            order.append(node)
            for neighbor in adjacency[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                seen.add(neighbor)
                stack.append(neighbor)

        included: dict[object, Poly] = {}
        excluded: dict[object, Poly] = {}
        for node in reversed(order):
            inc: Poly = (0, 1)
            exc: Poly = (1,)
            for child in adjacency[node]:
                if parent.get(child) != node:
                    continue
                inc = mul(inc, excluded[child])
                exc = mul(exc, add(included[child], excluded[child]))
            included[node] = inc
            excluded[node] = exc

        result = mul(result, add(included[root], excluded[root]))

    return result


def is_unimodal(seq: Sequence[int]) -> bool:
    if len(seq) <= 2:
        return True

    i = 1
    while i < len(seq) and seq[i - 1] <= seq[i]:
        i += 1
    while i < len(seq) and seq[i - 1] >= seq[i]:
        i += 1
    return i == len(seq)


def modes(seq: Sequence[int]) -> tuple[int, ...]:
    if not seq:
        return ()
    maximum = max(seq)
    return tuple(i for i, value in enumerate(seq) if value == maximum)


def log_concavity_failures(seq: Sequence[int]) -> tuple[tuple[int, int, int, int], ...]:
    """Return failures as (k, i_k^2, i_{k-1}, i_{k+1})."""

    failures: list[tuple[int, int, int, int]] = []
    for k in range(1, len(seq) - 1):
        left = seq[k - 1]
        mid_sq = seq[k] * seq[k]
        right = seq[k + 1]
        if mid_sq < left * right:
            failures.append((k, mid_sq, left, right))
    return tuple(failures)


def is_log_concave(seq: Sequence[int]) -> bool:
    return not log_concavity_failures(seq)


def synchronization_margins(
    a: Sequence[int],
    b: Sequence[int],
    *,
    stop: int | None = None,
) -> tuple[tuple[int, int, int], ...]:
    """Return synchronization margins as (k, left_margin, right_margin).

    The two margins are
      a_k b_k - a_{k-1} b_{k+1}
      a_k b_k - a_{k+1} b_{k-1}.
    Nonnegative margins for all relevant k mean a and b are synchronized.
    """

    n = max(len(a), len(b))
    aa = [*a, *([0] * (n - len(a)))]
    bb = [*b, *([0] * (n - len(b)))]
    last = n - 2 if stop is None else min(stop, n - 2)

    margins: list[tuple[int, int, int]] = []
    for k in range(1, last + 1):
        lhs = aa[k] * bb[k]
        margins.append(
            (
                k,
                lhs - aa[k - 1] * bb[k + 1],
                lhs - aa[k + 1] * bb[k - 1],
            )
        )
    return tuple(margins)


def synchronization_failures(
    a: Sequence[int],
    b: Sequence[int],
    *,
    stop: int | None = None,
) -> tuple[tuple[int, str, int, int], ...]:
    """Return cross-inequality failures for log-concavity of a+b.

    If a and b are log-concave and these cross inequalities hold, then their
    pointwise sum is log-concave. The optional stop checks only k <= stop.
    """

    n = max(len(a), len(b))
    aa = [*a, *([0] * (n - len(a)))]
    bb = [*b, *([0] * (n - len(b)))]
    last = n - 2 if stop is None else min(stop, n - 2)

    failures: list[tuple[int, str, int, int]] = []
    for k in range(1, last + 1):
        lhs = aa[k] * bb[k]
        right = aa[k - 1] * bb[k + 1]
        if lhs < right:
            failures.append((k, "left", lhs, right))
        right = aa[k + 1] * bb[k - 1]
        if lhs < right:
            failures.append((k, "right", lhs, right))
    return tuple(failures)


def worst_log_concavity_ratio(seq: Sequence[int]) -> Fraction | None:
    ratios: list[Fraction] = []
    for k in range(1, len(seq) - 1):
        denom = seq[k - 1] * seq[k + 1]
        if denom:
            ratios.append(Fraction(seq[k] * seq[k], denom))
    return min(ratios) if ratios else None


def analyze(graph: nx.Graph) -> IndependenceAnalysis:
    coeffs = independence_polynomial(graph)
    failures = log_concavity_failures(coeffs)
    return IndependenceAnalysis(
        coefficients=coeffs,
        unimodal=is_unimodal(coeffs),
        log_concave=not failures,
        modes=modes(coeffs),
        log_concavity_failures=failures,
        worst_log_concavity_ratio=worst_log_concavity_ratio(coeffs),
    )


def subdivide_edge(tree: nx.Graph, edge: tuple[object, object]) -> nx.Graph:
    u, v = edge
    if not tree.has_edge(u, v):
        raise ValueError(f"edge {edge!r} is not present")
    out = tree.copy()
    new_node = max((x for x in out.nodes if isinstance(x, int)), default=-1) + 1
    while new_node in out:
        new_node += 1
    out.remove_edge(u, v)
    out.add_edge(u, new_node)
    out.add_edge(new_node, v)
    return out


def contract_edge(tree: nx.Graph, edge: tuple[object, object]) -> nx.Graph:
    u, v = edge
    if not tree.has_edge(u, v):
        raise ValueError(f"edge {edge!r} is not present")
    return nx.contracted_edge(tree, edge, self_loops=False)


def path(length: int) -> nx.Graph:
    """Path with length vertices."""

    if length < 0:
        raise ValueError("length must be nonnegative")
    return nx.path_graph(length)


def star(leaves: int) -> nx.Graph:
    if leaves < 0:
        raise ValueError("leaves must be nonnegative")
    return nx.star_graph(leaves)


def spider(arms: Iterable[int]) -> nx.Graph:
    """Build a spider from arm lengths measured in edges from the center."""

    graph = nx.Graph()
    graph.add_node(0)
    next_node = 1
    for arm_length in arms:
        if arm_length < 0:
            raise ValueError("arm lengths must be nonnegative")
        previous = 0
        for _ in range(arm_length):
            graph.add_edge(previous, next_node)
            previous = next_node
            next_node += 1
    return graph


def broom(handle_edges: int, leaves: int) -> nx.Graph:
    """Path with a star attached to one endpoint."""

    if handle_edges < 0 or leaves < 0:
        raise ValueError("handle_edges and leaves must be nonnegative")
    graph = nx.path_graph(handle_edges + 1)
    next_node = handle_edges + 1
    for _ in range(leaves):
        graph.add_edge(handle_edges, next_node)
        next_node += 1
    return graph
