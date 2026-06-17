from __future__ import annotations

import sys
from pathlib import Path
from unittest import TestCase, main

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from erdos993.indpoly import (  # noqa: E402
    add,
    contract_edge,
    independence_polynomial,
    is_log_concave,
    is_unimodal,
    log_concavity_failures,
    mul,
    path,
    spider,
    star,
    subdivide_edge,
    synchronization_failures,
    synchronization_margins,
    x_mul,
)
from erdos993.families import (  # noqa: E402
    t_3_m_n,
    t_3_m_n_penultimate_margin,
    t_3_m_n_parts,
    t_3_m_n_polynomial,
    t_3_m_n_tail_coefficients,
    t_a_b_c,
    t_a_b_c_penultimate_margin,
    t_a_b_c_parts,
    t_a_b_c_polynomial,
    t_a_b_c_tail_coefficients,
    t_star_3_m_n,
    t_star_3_m_n_penultimate_margin,
    t_star_3_m_n_parts,
    t_star_3_m_n_polynomial,
    t_star_3_m_n_tail_coefficients,
)


class IndependencePolynomialTests(TestCase):
    def test_basic_polynomial_arithmetic(self) -> None:
        self.assertEqual(add((1, 2), (3, 4, 5)), (4, 6, 5))
        self.assertEqual(mul((1, 1), (1, 2)), (1, 3, 2))
        self.assertEqual(x_mul((1, 2, 3)), (0, 1, 2, 3))

    def test_small_tree_polynomials(self) -> None:
        self.assertEqual(independence_polynomial(path(0)), (1,))
        self.assertEqual(independence_polynomial(path(1)), (1, 1))
        self.assertEqual(independence_polynomial(path(3)), (1, 3, 1))
        self.assertEqual(independence_polynomial(star(3)), (1, 4, 3, 1))
        self.assertEqual(independence_polynomial(spider([1, 2])), (1, 4, 3))

    def test_forest_polynomial_is_component_product(self) -> None:
        graph = nx.Graph()
        graph.add_nodes_from([0, 1])
        self.assertEqual(independence_polynomial(graph), (1, 2, 1))

    def test_sequence_predicates(self) -> None:
        self.assertTrue(is_unimodal((1, 3, 3, 2)))
        self.assertFalse(is_unimodal((1, 4, 3, 5)))
        self.assertTrue(is_log_concave((1, 4, 3)))
        self.assertFalse(is_log_concave((1, 2, 5)))
        self.assertEqual(synchronization_failures((1, 2, 1), (1, 2, 1)), ())
        self.assertEqual(synchronization_margins((1, 2, 1), (1, 2, 1)), ((1, 3, 3),))

    def test_subdivision_contraction_identity(self) -> None:
        tree = nx.path_graph(5)
        edge = (1, 2)
        lhs = independence_polynomial(subdivide_edge(tree, edge))
        rhs = add(independence_polynomial(tree), x_mul(independence_polynomial(contract_edge(tree, edge))))
        self.assertEqual(lhs, rhs)

    def test_published_non_log_concave_examples(self) -> None:
        t1 = t_3_m_n(4, 4)
        self.assertEqual(t1.number_of_nodes(), 26)
        self.assertEqual(
            independence_polynomial(t1),
            (
                1,
                26,
                300,
                2040,
                9142,
                28551,
                63933,
                103736,
                121376,
                100144,
                55499,
                18683,
                2979,
                51,
                1,
            ),
        )
        self.assertEqual(t_3_m_n_polynomial(4, 4), independence_polynomial(t1))

        t2 = t_star_3_m_n(3, 4)
        self.assertEqual(t2.number_of_nodes(), 26)
        self.assertEqual(
            independence_polynomial(t2),
            (
                1,
                26,
                300,
                2037,
                9089,
                28147,
                62183,
                98968,
                112870,
                90178,
                48086,
                15498,
                2372,
                48,
                1,
            ),
        )
        self.assertEqual(t_star_3_m_n_polynomial(3, 4), independence_polynomial(t2))

    def test_known_family_penultimate_margins(self) -> None:
        t_root_excluded, t_root_included = t_3_m_n_parts(4, 4)
        self.assertEqual(add(t_root_excluded, t_root_included), t_3_m_n_polynomial(4, 4))
        self.assertTrue(
            all(
                left >= 0 and right >= 0
                for _, left, right in synchronization_margins(
                    t_root_excluded,
                    t_root_included,
                    stop=12,
                )
            )
        )
        self.assertEqual(t_3_m_n_tail_coefficients(4, 4), t_3_m_n_polynomial(4, 4)[-3:])
        self.assertEqual(t_3_m_n_penultimate_margin(4, 4), 2979 - 51**2)
        self.assertGreater(t_3_m_n_penultimate_margin(4, 6), 0)
        self.assertLess(t_3_m_n_penultimate_margin(4, 7), 0)

        star_root_excluded, star_root_included = t_star_3_m_n_parts(3, 4)
        self.assertEqual(
            add(star_root_excluded, star_root_included),
            t_star_3_m_n_polynomial(3, 4),
        )
        self.assertTrue(
            all(
                left >= 0 and right >= 0
                for _, left, right in synchronization_margins(
                    star_root_excluded,
                    star_root_included,
                    stop=12,
                )
            )
        )
        self.assertEqual(
            t_star_3_m_n_tail_coefficients(3, 4),
            t_star_3_m_n_polynomial(3, 4)[-3:],
        )
        self.assertEqual(t_star_3_m_n_penultimate_margin(3, 4), 2372 - 48**2)
        self.assertGreater(t_star_3_m_n_penultimate_margin(4, 7), 0)
        self.assertLess(t_star_3_m_n_penultimate_margin(4, 8), 0)

    def test_ordinary_three_hub_family(self) -> None:
        tree = t_a_b_c(2, 6, 6)
        self.assertEqual(tree.number_of_nodes(), 32)
        self.assertEqual(t_a_b_c_polynomial(2, 6, 6), independence_polynomial(tree))
        self.assertEqual(t_a_b_c_polynomial(2, 6, 6), t_a_b_c_polynomial(6, 2, 6))

        root_excluded, root_included = t_a_b_c_parts(2, 6, 6)
        polynomial = add(root_excluded, root_included)
        self.assertTrue(is_unimodal(polynomial))
        self.assertEqual(log_concavity_failures(polynomial), ((16, 21316, 22543, 1),))
        self.assertEqual(t_a_b_c_tail_coefficients(2, 6, 6), polynomial[-3:])
        self.assertEqual(t_a_b_c_penultimate_margin(2, 6, 6), 22543 - 146**2)


if __name__ == "__main__":
    main()
