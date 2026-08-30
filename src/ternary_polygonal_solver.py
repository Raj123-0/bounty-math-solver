"""
Ternary Polygonal Number Solver & Verifier
Addresses OEIS A287616 ($135 USD Bounty offered by Zhi-Wei Sun):
Every natural number n >= 0 can be written as:
    n = T_x + P_y + H_z
where:
    T_x = x(x + 1) / 2  (Triangular number, x >= 0)
    P_y = y(3y + 1) / 2 (Pentagonal number, y >= 0)
    H_z = z(5z + 1) / 2 (Heptagonal number, z >= 0)

And a(n) = 1 (unique representation) if and only if:
    n in {0, 1, 2, 4, 7, 9, 22}
"""

import numpy as np
import time

def compute_polygonal_representations(max_n=100000):
    """
    Computes the number of representations a(n) for all 0 <= n <= max_n.
    """
    t0 = time.time()
    
    x_max = int((2 * max_n)**0.5) + 2
    T = [x * (x + 1) // 2 for x in range(x_max) if x * (x + 1) // 2 <= max_n]
    
    y_max = int((2 * max_n / 3)**0.5) + 2
    P = [y * (3 * y + 1) // 2 for y in range(y_max) if y * (3 * y + 1) // 2 <= max_n]
    
    z_max = int((2 * max_n / 5)**0.5) + 2
    H = [z * (5 * z + 1) // 2 for z in range(z_max) if z * (5 * z + 1) // 2 <= max_n]
    
    counts = np.zeros(max_n + 1, dtype=np.int32)
    
    for p in P:
        for h in H:
            ph = p + h
            if ph <= max_n:
                for t in T:
                    s = ph + t
                    if s <= max_n:
                        counts[s] += 1
                    else:
                        break
                        
    zeros = np.where(counts == 0)[0].tolist()
    uniques = np.where(counts == 1)[0].tolist()
    t1 = time.time()
    
    return counts, zeros, uniques, t1 - t0

def find_specific_representation(n):
    """
    Finds all triples (x, y, z) >= 0 such that n = T_x + P_y + H_z.
    """
    solutions = []
    z_max = int((2 * n / 5)**0.5) + 2
    for z in range(z_max):
        h = z * (5 * z + 1) // 2
        if h > n:
            break
        rem1 = n - h
        y_max = int((2 * rem1 / 3)**0.5) + 2
        for y in range(y_max):
            p = y * (3 * y + 1) // 2
            if p > rem1:
                break
            rem2 = rem1 - p
            disc = 8 * rem2 + 1
            r = int(disc**0.5)
            if r * r == disc and r % 2 == 1:
                x = (r - 1) // 2
                solutions.append((x, y, z))
    return solutions

if __name__ == '__main__':
    print("Testing Triangular + Pentagonal + Heptagonal Solver...")
    counts, zeros, uniques, duration = compute_polygonal_representations(50000)
    print(f"Computed representations up to 50,000 in {duration:.3f}s.")
    print(f"Zeros found: {zeros}")
    print(f"Unique representation values (a(n)=1): {uniques}")
    assert zeros == [], "Found unrepresentable numbers!"
    assert uniques == [0, 1, 2, 4, 7, 9, 22], f"Unique values {uniques} do not match conjecture!"
    print("Verification SUCCESSFUL!")