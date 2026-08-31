"""
Comprehensive Test Suite for Bounty Math Solver Modules
Author: Raj123-0
"""

import unittest
from src.a306477_checker import decompose_n, check_range
from src.ternary_polygonal_solver import compute_polygonal_representations, get_representation
from src.quadratic_form_local_global import verify_local_congruences, solve_ternary_form
from src.rado_checker import verify_formula_for_c

class TestAllVerificationModules(unittest.TestCase):

    def test_a306477_checks(self):
        """Verify 2-4-6-8 sums up to 200."""
        res = check_range(200)
        self.assertEqual(res["uncovered"], [])
        self.assertTrue(res["is_conjecture_supported"])

    def test_ternary_polygonal_conjecture(self):
        """Verify OEIS A287616 up to 10,000."""
        counts, zeros, uniques, _ = compute_polygonal_representations(10000)
        self.assertEqual(zeros, [], "Zero representable numbers found in A287616!")
        self.assertEqual(uniques, [0, 1, 2, 4, 7, 9, 22], "Unique values mismatch in A287616!")

    def test_ternary_quadratic_form(self):
        """Verify 15u^2 + 5v^2 + 3w^2 = 120n + 23 representations for small n."""
        for n in range(25):
            self.assertTrue(verify_local_congruences(n))
            sols = solve_ternary_form(n)
            self.assertGreater(len(sols), 0, f"No quadratic form solution for n={n}")

    def test_rado_formula_c_zero_and_one(self):
        """Verify empirical Rado bounds for c = 0 and c = 1."""
        res0 = verify_formula_for_c(0)
        self.assertTrue(res0["formula_confirmed"])
        self.assertEqual(res0["predicted_rado_number"], 14)
        
        res1 = verify_formula_for_c(1)
        self.assertTrue(res1["formula_confirmed"])
        self.assertEqual(res1["predicted_rado_number"], 27)

if __name__ == '__main__':
    unittest.main()