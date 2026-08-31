"""
A306477 Verification Module - 2-4-6-8 Binomial Coefficient Sums
Author: Raj123-0
Description: Independent computational verification tool for Zhi-Wei Sun's
             2-4-6-8 conjecture (OEIS A306477).

Conjecture (Zhi-Wei Sun, 2019):
Every positive integer n >= 1 can be represented as:
    n = C(w+2, 2) + C(x+3, 4) + C(y+5, 6) + C(z+7, 8)
where w, x, y, z are non-negative integers (w, x, y, z in {0, 1, 2, ...}).

Note: This module provides computational verification up to a specified bound N.
      The full theoretical proof for all n >= 1 remains an open problem.
"""

import math
from typing import Dict, List, Optional, Tuple

def comb(n: int, k: int) -> int:
    """Exact integer binomial coefficient C(n, k)."""
    return math.comb(n, k)

def decompose_n(n: int) -> Optional[Tuple[int, int, int, int]]:
    """
    Finds a valid non-negative integer quadruple (w, x, y, z) such that:
        n = C(w+2, 2) + C(x+3, 4) + C(y+5, 6) + C(z+7, 8)
    Returns the first found decomposition (w, x, y, z), or None if none exists.
    """
    if n < 1:
        return None
        
    z = 0
    while True:
        c8 = comb(z + 7, 8)
        if c8 > n:
            break
        rem_z = n - c8
        
        y = 0
        while True:
            c6 = comb(y + 5, 6)
            if c6 > rem_z:
                break
            rem_y = rem_z - c6
            
            x = 0
            while True:
                c4 = comb(x + 3, 4)
                if c4 > rem_y:
                    break
                rem_x = rem_y - c4
                
                # We need C(w+2, 2) = rem_x
                # (w+2)(w+1)/2 = rem_x  ==>  w^2 + 3w + (2 - 2*rem_x) = 0
                # Discriminant: 9 - 4(2 - 2*rem_x) = 1 + 8*rem_x
                disc = 1 + 8 * rem_x
                r = math.isqrt(disc)
                if r * r == disc and (r - 3) % 2 == 0:
                    w = (r - 3) // 2
                    if w >= 0 and comb(w + 2, 2) == rem_x:
                        return (w, x, y, z)
                x += 1
            y += 1
        z += 1
    return None

def count_representations(n: int) -> int:
    """
    Counts the total number of representations of n as:
        C(w+2, 2) + C(x+3, 4) + C(y+5, 6) + C(z+7, 8)
    """
    if n < 1:
        return 0
    count = 0
    z = 0
    while True:
        c8 = comb(z + 7, 8)
        if c8 > n:
            break
        rem_z = n - c8
        y = 0
        while True:
            c6 = comb(y + 5, 6)
            if c6 > rem_z:
                break
            rem_y = rem_z - c6
            x = 0
            while True:
                c4 = comb(x + 3, 4)
                if c4 > rem_y:
                    break
                rem_x = rem_y - c4
                disc = 1 + 8 * rem_x
                r = math.isqrt(disc)
                if r * r == disc and (r - 3) % 2 == 0:
                    w = (r - 3) // 2
                    if w >= 0 and comb(w + 2, 2) == rem_x:
                        count += 1
                x += 1
            y += 1
        z += 1
    return count

def check_range(max_n: int = 1000) -> Dict[str, any]:
    """
    Checks that every integer from 1 to max_n has at least one representation.
    Returns summary statistics and any uncovered integers.
    """
    uncovered = []
    sample_decompositions = {}
    
    for n in range(1, max_n + 1):
        sol = decompose_n(n)
        if sol is None:
            uncovered.append(n)
        elif n <= 10 or n in {50, 100, 500, 1000}:
            sample_decompositions[n] = sol
            
    return {
        "max_n": max_n,
        "verified_count": max_n - len(uncovered),
        "uncovered": uncovered,
        "is_conjecture_supported": len(uncovered) == 0,
        "samples": sample_decompositions
    }

if __name__ == "__main__":
    print("=== A306477 (2-4-6-8 Sum) Computational Verification ===")
    results = check_range(1000)
    print(f"Verified range: 1 .. {results['max_n']}")
    print(f"Represented numbers: {results['verified_count']}/{results['max_n']}")
    print(f"Uncovered numbers: {results['uncovered']}")
    print("\nSample Decompositions:")
    for n, (w, x, y, z) in sorted(results["samples"].items()):
        v2 = comb(w + 2, 2)
        v4 = comb(x + 3, 4)
        v6 = comb(y + 5, 6)
        v8 = comb(z + 7, 8)
        print(f"  n = {n:4d}: C({w+2},2)={v2} + C({x+3},4)={v4} + C({y+5},6)={v6} + C({z+7},8)={v8}  [Sum: {v2+v4+v6+v8}]")