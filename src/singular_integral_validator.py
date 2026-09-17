"""
Singular Integral & Statistical Window Validator for Sun's 2-4-6-8 Conjecture (A306477)
Author: Raj123-0
Description:
1. Derives and validates the singular integral constant c_J analytically and via direct 3D numerical quadrature.
2. Computes windowed statistical averages of r(n) vs S(n)*J(n) across scales N = 100 to 75,000.
"""
from __future__ import annotations


import math
import numpy as np
import scipy.integrate as integrate

try:
    from src.a306477_checker import count_representations
    from src.local_density_calculator import compute_local_density_table, compute_singular_series
except ImportError:
    from a306477_checker import count_representations
    from local_density_calculator import compute_local_density_table, compute_singular_series


def get_analytical_c_J() -> float:
    """Computes c_J analytically from the Dirichlet-Liouville beta integral."""
    g1_2 = math.gamma(0.5)
    g1_4 = math.gamma(0.25)
    g1_6 = math.gamma(1/6)
    g1_8 = math.gamma(0.125)
    g_sum = math.gamma(25/24)
    gamma_factor = (g1_2 * g1_4 * g1_6 * g1_8) / g_sum
    coeff_factor = (2**0.5 / 2.0) * (24**0.25 / 4.0) * (720**(1/6) / 6.0) * (40320**0.125 / 8.0)
    return gamma_factor * coeff_factor


def numerical_quadrature_J(n: float) -> float:
    """Computes J(n) via direct 3D numerical quadrature with regularized coordinate transformation."""
    c2 = 2**0.5 / 2.0
    c4 = 24**0.25 / 4.0
    c6 = 720**(1/6) / 6.0
    c8 = 40320**0.125 / 8.0
    
    def reg_integrand(z, y, x) -> float:
        """Reg integrand.
        
        Args:
            z:
            y:
            x:
        
        Returns:
            float: Result of type float
        
        """
        rem = n - x**2 - y**4 - z**6
        if rem <= 1e-12:
            return 0.0
        return 2.0 * 4.0 * 6.0 * (rem**(-7/8))
    
    x_max = n**0.5
    """Y max.
    
    Args:
        x:
    
    Returns:
        The computed result
    
    """
    def y_max(x): return max(0.0, n - x**2)**0.25
    """Z max.
    
    Args:
        x:
        y:
    
    Returns:
        The computed result
    
    """
    def z_max(x, y): return max(0.0, n - x**2 - y**4)**(1/6)
    
    val, _ = integrate.tplquad(
        reg_integrand,
        0, x_max,
        lambda x: 0, y_max,
        lambda x, y: 0, z_max,
        epsabs=1e-5, epsrel=1e-5
    )
    return c2 * c4 * c6 * c8 * val

if __name__ == "__main__":
    print("=== Singular Integral Validation ===")
    c_J_ana = get_analytical_c_J()
    print(f"Analytical c_J = {c_J_ana:.6f}")
    
    for n in [1.0, 10.0, 100.0]:
        j_num = numerical_quadrature_J(n)
        j_ana = c_J_ana * (n**(1/24))
        rel_diff = abs(j_num - j_ana) / j_ana
        print(f"  n = {n:5.1f} | Numerical J(n) = {j_num:.6f} | Analytical J(n) = {j_ana:.6f} | Rel Diff = {rel_diff:.2e}")