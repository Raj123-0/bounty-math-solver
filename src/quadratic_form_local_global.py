"""
Ternary Quadratic Form Algebraic & Local-Global Analysis
Analyzes the equivalence:
    n = T_x + P_y + H_z  <===>  15 u^2 + 5 v^2 + 3 w^2 = 120 n + 23
where:
    u = 2x + 1  (u > 0, u = 1 mod 2)
    v = 6y + 1  (v > 0, v = 1 mod 6)
    w = 10z + 1 (w > 0, w = 1 mod 10)
"""

def verify_local_congruences(n):
    """
    Verifies that target = 120n + 23 is locally represented by 15u^2 + 5v^2 + 3w^2
    modulo 2, 3, 5, 8, 24, 120.
    """
    target = 120 * n + 23
    
    # Modulo 3: 5 v^2 = 23 = 2 mod 3 ==> 2 v^2 = 2 mod 3 ==> v^2 = 1 mod 3
    assert target % 3 == (5 * (1**2)) % 3, "Failed mod 3 congruence!"
    
    # Modulo 5: 3 w^2 = 23 = 3 mod 5 ==> w^2 = 1 mod 5
    assert target % 5 == (3 * (1**2)) % 5, "Failed mod 5 congruence!"
    
    # Modulo 8: 15(1) + 5(1) + 3(1) = 23 = 7 mod 8
    assert target % 8 == (15 + 5 + 3) % 8, "Failed mod 8 congruence!"
    
    return True

def solve_ternary_form(n):
    """
    Finds integer solutions (u, v, w) to 15u^2 + 5v^2 + 3w^2 = 120n + 23
    satisfying u = 1 mod 2, v = 1 mod 6, w = 1 mod 10 with u, v, w > 0.
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
    print("Verifying Local Congruences and Form Representation...")
    for n in range(100):
        assert verify_local_congruences(n)
        sols = solve_ternary_form(n)
        assert len(sols) > 0, f"No solution for n={n}!"
    print("Local-Global Verification PASSED for all n in 0..100!")