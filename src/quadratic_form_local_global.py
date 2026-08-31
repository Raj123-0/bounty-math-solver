"""
Ternary Quadratic Form Congruence & Representation Explorer
Author: Raj123-0
Description: Analyzes the algebraic reduction:
    n = T_x + P_y + H_z  <===>  15 u^2 + 5 v^2 + 3 w^2 = 120 n + 23
where:
    u = 2x + 1  (u > 0, u = 1 mod 2)
    v = 6y + 1  (v > 0, v = 1 mod 6)
    w = 10z + 1 (w > 0, w = 1 mod 10)

Disclaimer:
    This file explores the local modular compatibility of the ternary form.
"""

from typing import List, Tuple

def verify_local_congruences(n: int) -> bool:
    """
    Checks congruence consistency modulo 3, 5, and 8 for target = 120n + 23.
    """
    target = 120 * n + 23
    
    # Modulo 3: 5*1^2 = 2 = 23 mod 3
    if target % 3 != (5 * (1**2)) % 3:
        return False
    # Modulo 5: 3*1^2 = 3 = 23 mod 5
    if target % 5 != (3 * (1**2)) % 5:
        return False
    # Modulo 8: 15(1) + 5(1) + 3(1) = 23 = 7 mod 8
    if target % 8 != (15 + 5 + 3) % 8:
        return False
        
    return True

def solve_ternary_form(n: int) -> List[Tuple[int, int, int]]:
    """
    Finds positive integer solutions (u, v, w) satisfying:
        15 u^2 + 5 v^2 + 3 w^2 = 120 n + 23
    with u = 1 mod 2, v = 1 mod 6, w = 1 mod 10.
    """
    target = 120 * n + 23
    solutions = []
    
    u_max = int((target / 15)**0.5) + 1
    for u in range(1, u_max + 1, 2):
        rem1 = target - 15 * u * u
        if rem1 < 8:
            continue
        v_max = int((rem1 / 5)**0.5) + 1
        for v in range(1, v_max + 1, 6):
            rem2 = rem1 - 5 * v * v
            if rem2 < 3:
                continue
            if rem2 % 3 == 0:
                w2 = rem2 // 3
                w = int(w2**0.5)
                if w * w == w2 and w % 10 == 1:
                    solutions.append((u, v, w))
    return solutions

if __name__ == '__main__':
    print("Testing modular compatibility and representation for n in 0..100...")
    for n in range(101):
        assert verify_local_congruences(n), f"Congruence failed at n={n}"
        sols = solve_ternary_form(n)
        assert len(sols) > 0, f"No solution found at n={n}"
    print("Local congruence checks and representations verified for 0..100.")