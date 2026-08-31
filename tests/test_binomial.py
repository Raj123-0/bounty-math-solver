"""
Unit Tests for A306477 Binomial Sum Checker
Author: Raj123-0
"""

import unittest
from src.a306477_checker import decompose_n, count_representations, check_range, comb

class TestA306477Checker(unittest.TestCase):

    def test_base_case_n_equals_1(self):
        """Test base case n = 1: C(0+2,2) + C(0+3,4) + C(0+5,6) + C(0+7,8) = 1 + 0 + 0 + 0 = 1."""
        sol = decompose_n(1)
        self.assertIsNotNone(sol, "n=1 should have a representation")
        w, x, y, z = sol
        val = comb(w + 2, 2) + comb(x + 3, 4) + comb(y + 5, 6) + comb(z + 7, 8)
        self.assertEqual(val, 1)

    def test_base_case_n_equals_2(self):
        """Test base case n = 2: e.g. w=0, x=1, y=0, z=0 ==> 1 + 1 + 0 + 0 = 2."""
        sol = decompose_n(2)
        self.assertIsNotNone(sol, "n=2 should have a representation")
        w, x, y, z = sol
        val = comb(w + 2, 2) + comb(x + 3, 4) + comb(y + 5, 6) + comb(z + 7, 8)
        self.assertEqual(val, 2)

    def test_known_small_integers(self):
        """Test integers 1 through 50 for valid decomposition."""
        for n in range(1, 51):
            sol = decompose_n(n)
            self.assertIsNotNone(sol, f"n={n} should have a representation")
            w, x, y, z = sol
            self.assertGreaterEqual(w, 0)
            self.assertGreaterEqual(x, 0)
            self.assertGreaterEqual(y, 0)
            self.assertGreaterEqual(z, 0)
            val = comb(w + 2, 2) + comb(x + 3, 4) + comb(y + 5, 6) + comb(z + 7, 8)
            self.assertEqual(val, n)

    def test_range_verification(self):
        """Verify that check_range(500) reports zero uncovered integers."""
        res = check_range(500)
        self.assertTrue(res["is_conjecture_supported"])
        self.assertEqual(res["uncovered"], [])

if __name__ == '__main__':
    unittest.main()