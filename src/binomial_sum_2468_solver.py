"""
2-4-6-8 Binomial Coefficient Representation Solver
Addresses OEIS A306477 ($2,468 USD Bounty / 2,468 RMB Counterexample Bounty):
Every integer n >= 1 can be written as:
    n = C(w+2, 2) + C(x+3, 4) + C(y+5, 6) + C(z+7, 8)
where w, x, y, z >= 0.
"""

import numpy as np
import math

def binom(n, k):
    return math.comb(n, k)

def verify_2468_conjecture(max_n=100000):
    """
    Verifies that every 1 <= n <= max_n has at least one 2-4-6-8 representation.
    """
    # Generate binomial values <= max_n
    B2 = [binom(w + 2, 2) for w in range(int((2 * max_n)**0.5) + 3) if binom(w + 2, 2) <= max_n]
    B4 = [binom(x + 3, 4) for x in range(int((24 * max_n)**0.25) + 3) if binom(x + 3, 4) <= max_n]
    B6 = [binom(y + 5, 6) for y in range(int((720 * max_n)**(1/6)) + 3) if binom(y + 5, 6) <= max_n]
    B8 = [binom(z + 7, 8) for z in range(int((40320 * max_n)**0.125) + 3) if binom(z + 7, 8) <= max_n]
    
    represented = np.zeros(max_n + 1, dtype=bool)
    
    for b8 in B8:
        for b6 in B6:
            s86 = b8 + b6
            if s86 > max_n:
                break
            for b4 in B4:
                s864 = s86 + b4
                if s864 > max_n:
                    break
                for b2 in B2:
                    total = s864 + b2
                    if total <= max_n:
                        represented[total] = True
                    else:
                        break
                        
    uncovered = np.where(~represented[1:max_n + 1])[0] + 1
    return uncovered.tolist()

if __name__ == '__main__':
    print("Checking 2-4-6-8 Binomial Sums up to 50,000...")
    uncovered = verify_2468_conjecture(50000)
    print(f"Uncovered numbers: {uncovered}")
    assert len(uncovered) == 0, f"Counterexamples found: {uncovered}"
    print("Verification SUCCESSFUL: All n in 1..50,000 are representable!")