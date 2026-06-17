from __future__ import annotations

import networkx as nx

from .indpoly import Poly, add, mul, x_mul


def t_3_m_n(m: int, n: int) -> nx.Graph:
    """Return the tree T_{3,m,n} from the non-log-concave family.

    The tree has root v0 with three children v1, v2, v3. The three hubs have
    3, m, and n length-2 arms respectively.
    """

    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")
    return t_a_b_c(3, m, n)


def t_a_b_c(a: int, b: int, c: int) -> nx.Graph:
    """Return the ordinary three-hub tree with a, b, and c length-2 arms."""

    _validate_arm_counts((a, b, c))
    return _three_hub_tree((a, b, c), star_arm=False)


def t_star_3_m_n(m: int, n: int) -> nx.Graph:
    """Return the tree T^*_{3,m,n}.

    This is T_{3,m,n} with one of the fixed three arms extended so that the
    corresponding hub sees a path on four vertices.
    """

    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")
    return _three_hub_tree((3, m, n), star_arm=True)


def t_3_m_n_polynomial(m: int, n: int) -> Poly:
    """Closed-form independence polynomial of T_{3,m,n}."""

    root_excluded, root_included = t_3_m_n_parts(m, n)
    return add(root_excluded, root_included)


def t_3_m_n_parts(m: int, n: int) -> tuple[Poly, Poly]:
    """Return the root-excluded and root-included summands for T_{3,m,n}."""

    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")
    return t_a_b_c_parts(3, m, n)


def t_a_b_c_polynomial(a: int, b: int, c: int) -> Poly:
    """Closed-form independence polynomial of T_{a,b,c}."""

    root_excluded, root_included = t_a_b_c_parts(a, b, c)
    return add(root_excluded, root_included)


def t_a_b_c_parts(a: int, b: int, c: int) -> tuple[Poly, Poly]:
    """Return the root-excluded and root-included summands for T_{a,b,c}."""

    _validate_arm_counts((a, b, c))
    ha, hb, hc = (_hub_total(arms) for arms in (a, b, c))
    ea, eb, ec = (_hub_excluded(arms) for arms in (a, b, c))
    root_excluded = mul(mul(ha, hb), hc)
    root_included = x_mul(mul(mul(ea, eb), ec))
    return root_excluded, root_included


def t_star_3_m_n_polynomial(m: int, n: int) -> Poly:
    """Closed-form independence polynomial of T^*_{3,m,n}."""

    root_excluded, root_included = t_star_3_m_n_parts(m, n)
    return add(root_excluded, root_included)


def t_star_3_m_n_parts(m: int, n: int) -> tuple[Poly, Poly]:
    """Return the root-excluded and root-included summands for T^*_{3,m,n}."""

    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")
    hstar, hm, hn = _star_hub_total(), _hub_total(m), _hub_total(n)
    estar, em, en = _star_hub_excluded(), _hub_excluded(m), _hub_excluded(n)
    root_excluded = mul(mul(hstar, hm), hn)
    root_included = x_mul(mul(mul(estar, em), en))
    return root_excluded, root_included


def t_3_m_n_penultimate_margin(m: int, n: int) -> int:
    """Return i_{d-2} i_d - i_{d-1}^2 for T_{3,m,n}.

    Positive means log-concavity fails at the penultimate coefficient.
    """

    return t_a_b_c_penultimate_margin(3, m, n)


def t_a_b_c_penultimate_margin(a: int, b: int, c: int) -> int:
    """Return i_{d-2} i_d - i_{d-1}^2 for T_{a,b,c}."""

    i_d_minus_2, i_d_minus_1, i_d = t_a_b_c_tail_coefficients(a, b, c)
    return i_d_minus_2 * i_d - i_d_minus_1 * i_d_minus_1


def t_star_3_m_n_penultimate_margin(m: int, n: int) -> int:
    """Return i_{d-2} i_d - i_{d-1}^2 for T^*_{3,m,n}."""

    i_d_minus_2, i_d_minus_1, i_d = t_star_3_m_n_tail_coefficients(m, n)
    return i_d_minus_2 * i_d - i_d_minus_1 * i_d_minus_1


def t_3_m_n_tail_coefficients(m: int, n: int) -> tuple[int, int, int]:
    """Return (i_{d-2}, i_{d-1}, i_d) for T_{3,m,n}."""

    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")

    return t_a_b_c_tail_coefficients(3, m, n)


def t_a_b_c_tail_coefficients(a: int, b: int, c: int) -> tuple[int, int, int]:
    """Return (i_{d-2}, i_{d-1}, i_d) for T_{a,b,c}."""

    _validate_arm_counts((a, b, c))

    top_minus_1 = [_h_one_below_top(arms) for arms in (a, b, c)]
    top_minus_2 = [_h_two_below_top(arms) for arms in (a, b, c)]
    root_included_top = 2 ** (a + b + c)
    i_d_minus_2 = (
        sum(top_minus_2)
        + top_minus_1[0] * top_minus_1[1]
        + top_minus_1[0] * top_minus_1[2]
        + top_minus_1[1] * top_minus_1[2]
        + root_included_top
    )
    i_d_minus_1 = sum(top_minus_1)
    return i_d_minus_2, i_d_minus_1, 1


def t_star_3_m_n_tail_coefficients(m: int, n: int) -> tuple[int, int, int]:
    """Return (i_{d-2}, i_{d-1}, i_d) for T^*_{3,m,n}."""

    if m < 0 or n < 0:
        raise ValueError("m and n must be nonnegative")

    am, an = (_h_one_below_top(a) for a in (m, n))
    bm, bn = (_h_two_below_top(a) for a in (m, n))
    star_one_below_top = 17
    star_two_below_top = 36
    root_included_top = 12 * 2 ** (m + n)
    i_d_minus_2 = (
        star_two_below_top
        + bm
        + bn
        + star_one_below_top * am
        + star_one_below_top * an
        + am * an
        + root_included_top
    )
    i_d_minus_1 = star_one_below_top + am + an
    return i_d_minus_2, i_d_minus_1, 1


def _three_hub_tree(arm_counts: tuple[int, int, int], *, star_arm: bool) -> nx.Graph:
    graph = nx.Graph()
    root = _add_node(graph)
    hubs = [_add_node(graph) for _ in arm_counts]
    for hub in hubs:
        graph.add_edge(root, hub)

    for hub_index, (hub, arm_count) in enumerate(zip(hubs, arm_counts, strict=True)):
        for arm_index in range(arm_count):
            middle = _add_node(graph)
            leaf = _add_node(graph)
            graph.add_edge(hub, middle)
            graph.add_edge(middle, leaf)

            if star_arm and hub_index == 0 and arm_index == arm_count - 1:
                # Replace one K2 pendant arm by the P4 arm v13-v13'-x-y.
                x = _add_node(graph)
                y = _add_node(graph)
                graph.add_edge(leaf, x)
                graph.add_edge(x, y)

    return graph


def _validate_arm_counts(arm_counts: tuple[int, int, int]) -> None:
    if any(arms < 0 for arms in arm_counts):
        raise ValueError("arm counts must be nonnegative")


def _add_node(graph: nx.Graph) -> int:
    node = graph.number_of_nodes()
    graph.add_node(node)
    return node


def _hub_excluded(arms: int) -> Poly:
    return _pow((1, 2), arms)


def _hub_total(arms: int) -> Poly:
    return add(_hub_excluded(arms), x_mul(_pow((1, 1), arms)))


def _h_one_below_top(arms: int) -> int:
    """Coefficient one below the leading term of H_a."""

    return 2**arms + arms


def _h_two_below_top(arms: int) -> int:
    """Coefficient two below the leading term of H_a."""

    if arms == 0:
        return 0
    return arms * 2 ** (arms - 1) + arms * (arms - 1) // 2


def _star_hub_excluded() -> Poly:
    # Two K2 arms plus one P4 arm away from the hub.
    return mul(_pow((1, 2), 2), (1, 4, 3))


def _star_hub_total() -> Poly:
    # If the hub is included, the two K2 arms leave optional leaves and the
    # extended arm leaves a P3.
    included = x_mul(mul(_pow((1, 1), 2), (1, 3, 1)))
    return add(_star_hub_excluded(), included)


def _pow(poly: Poly, exponent: int) -> Poly:
    result: Poly = (1,)
    base = poly
    n = exponent
    while n:
        if n & 1:
            result = mul(result, base)
        base = mul(base, base)
        n >>= 1
    return result
