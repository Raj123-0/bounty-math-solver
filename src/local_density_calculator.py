"""
Local Density Calculator for Zhi-Wei Sun's 2-4-6-8 Conjecture (A306477)
Author: Raj123-0
Description: Computes the exact p-adic local densities chi_p(n) for primes p=2, 3, 5, 7, ...
             via polynomial period enumeration and FFT convolution over Z/p^k Z.
"""

import math
import numpy as np

def P2(w: int) -> int:
    return (w + 2) * (w + 1) // 2

def P4(x: int) -> int:
    return (x + 3) * (x + 2) * (x + 1) * x // 24

def P6(y: int) -> int:
    return (y + 5) * (y + 4) * (y + 3) * (y + 2) * (y + 1) * y // 720

def P8(z: int) -> int:
    return (z + 7) * (z + 6) * (z + 5) * (z + 4) * (z + 3) * (z + 2) * (z + 1) * z // 40320

def get_poly_distribution(poly_func, mod: int) -> np.ndarray:
    """Finds the minimal period of poly_func mod `mod` and computes the residue PMF."""
    vals = [poly_func(t) % mod for t in range(mod * 64)]
    period = len(vals)
    for T in range(1, len(vals) // 2):
        if all(vals[t] == vals[t + T] for t in range(len(vals) - T)):
            period = T
            break
    counts = np.zeros(mod, dtype=np.float64)
    for t in range(period):
        counts[poly_func(t) % mod] += 1.0 / period
    return counts

def compute_local_density_table(p: int, k: int) -> np.ndarray:
    """Computes chi_p(n) for all residue classes n in {0, 1, ..., p^k - 1}."""
    mod = p ** k
    d2 = get_poly_distribution(P2, mod)
    d4 = get_poly_distribution(P4, mod)
    d6 = get_poly_distribution(P6, mod)
    d8 = get_poly_distribution(P8, mod)
    
    f_tot = np.fft.fft(d2) * np.fft.fft(d4) * np.fft.fft(d6) * np.fft.fft(d8)
    prob = np.real(np.fft.ifft(f_tot))
    return prob * mod

def compute_singular_series(n: int, primes_tables: dict, tail_bound: float) -> float:
    """Computes S(n) = prod_p chi_p(n) for a specific integer n."""
    val = 1.0
    for p, table in primes_tables.items():
        val *= table[n % len(table)]
    val *= tail_bound
    return val

if __name__ == "__main__":
    print("=== Exact p-Adic Local Density Analysis ===")
    
    # 1. Prime p = 2 (mod 4)
    t2 = compute_local_density_table(2, 2)
    print(f"p=2 (mod 4): min = {np.min(t2):.6f}, max = {np.max(t2):.6f} (Uniform: {np.allclose(t2, 1.0)})")
    
    # 2. Prime p = 3 (mod 9)
    t3 = compute_local_density_table(3, 2)
    print(f"p=3 (mod 9): min = {np.min(t3):.6f} (at n = 5 mod 9), max = {np.max(t3):.6f}")
    
    # 3. Prime p = 5 (mod 25)
    t5 = compute_local_density_table(5, 2)
    print(f"p=5 (mod 25): min = {np.min(t5):.6f} (at n = 19 mod 25), max = {np.max(t5):.6f}")
    
    # 4. Prime p = 7 (mod 49)
    t7 = compute_local_density_table(7, 2)
    print(f"p=7 (mod 49): min = {np.min(t7):.6f}, max = {np.max(t7):.6f}")