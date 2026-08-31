"""
Unit tests for p-adic local density calculator.
"""

import unittest
import numpy as np
from src.local_density_calculator import (
    compute_local_density_table,
    P2, P4, P6, P8
)

class TestLocalDensity(unittest.TestCase):
    def test_p2_equidistribution(self):
        t2 = compute_local_density_table(2, 2)
        self.assertTrue(np.allclose(t2, 1.0))
        
    def test_p3_positivity(self):
        t3 = compute_local_density_table(3, 2)
        self.assertGreater(np.min(t3), 0.70)
        self.assertAlmostEqual(np.mean(t3), 1.0, places=5)
        
    def test_p5_positivity(self):
        t5 = compute_local_density_table(5, 2)
        self.assertGreater(np.min(t5), 0.85)
        self.assertAlmostEqual(np.mean(t5), 1.0, places=5)
        
    def test_p7_positivity(self):
        t7 = compute_local_density_table(7, 2)
        self.assertGreater(np.min(t7), 0.88)
        self.assertAlmostEqual(np.mean(t7), 1.0, places=5)

if __name__ == "__main__":
    unittest.main()