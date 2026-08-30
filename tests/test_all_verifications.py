"""
Comprehensive Automated Test Suite for Bounty Solvers and Mathematical Proofs
"""

import unittest
from src.ternary_polygonal_solver import compute_polygonal_representations, find_specific_representation
from src.quadratic_form_local_global import verify_local_congruences, solve_ternary_form
from src.binomial_sum_2468_solver import verify_2468_conjecture
from src.rado_ramsey_solver import get_exact_3color_rado

class TestBountyMathematicalSolvers(unittest.TestCase):

    def test_ternary_polygonal_conjecture(self):
        """Verify OEIS A287616 ($135 Bounty) up to 20,000."""
        counts, zeros, uniques, dur = compute_polygonal_representations(20000)
        self.assertEqual(zeros, [], "Zero representable numbers found in A287616!")
        self.assertEqual(uniques, [0, 1, 2, 4, 7, 9, 22], "Unique values mismatch in A287616!")

    def test_ternary_quadratic_form(self):
        """Verify 15u^2 + 5v^2 + 3w^2 = 120n + 23 representations."""
        for n in range(50):
            self.assertTrue(verify_local_congruences(n))
            sols = solve_ternary_form(n)
            self.assertGreater(len(sols), 0, f"No quadratic form solution for n={n}")

    def test_2468_binomial_conjecture(self):
        """Verify OEIS A306477 ($2,468 Bounty) up to 10,000."""
        uncovered = verify_2468_conjecture(10000)
        self.assertEqual(uncovered, [], "Counterexamples found in 2-4-6-8 conjecture!")

    def test_rado_theorem_values(self):
        """Verify Theorem 1: R_3(x + y + c = z) = 13c + 14 for c = 0, 1, 2."""
        for c in [0, 1, 2]:
            val, col = get_exact_3color_rado(c)
            self.assertEqual(val, 13 * c + 14)

if __name__ == '__main__':
    unittest.main()