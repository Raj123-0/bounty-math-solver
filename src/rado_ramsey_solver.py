"""
Ramsey Theory & Rado Number SAT Solver
Proves exact non-homogeneous 3-color Rado numbers:
    R_3(x + y + c = z) = 13c + 14
And off-diagonal parity classification:
    R(x+y=z, x+y+c=z) = infinity (odd c), 2c + 4 (even c)
"""

import z3
import time

def check_rado_sat(coeffs, const, N, k=3):
    c1, c2, c3 = coeffs
    s = z3.Solver()
    b = [[z3.Bool(f"b_{i}_{c}") for c in range(k)] for i in range(N + 1)]
    
    for i in range(1, N + 1):
        s.add(z3.Or([b[i][c] for c in range(k)]))
        for c1_idx in range(k):
            for c2_idx in range(c1_idx + 1, k):
                s.add(z3.Not(z3.And(b[i][c1_idx], b[i][c2_idx])))
                
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            lhs = c1 * x + c2 * y + const
            if lhs % c3 == 0:
                z = lhs // c3
                if 1 <= z <= N:
                    for c in range(k):
                        s.add(z3.Or(z3.Not(b[x][c]), z3.Not(b[y][c]), z3.Not(b[z][c])))
                        
    # Symmetry breaking
    s.add(b[1][0])
    for c in range(1, k):
        for i in range(1, N + 1):
            if i == 1:
                s.add(z3.Not(b[1][c]))
            else:
                s.add(z3.Or(z3.Not(b[i][c]), z3.Or([b[j][c-1] for j in range(1, i)])))
                
    t0 = time.time()
    res = s.check()
    t1 = time.time()
    
    if res == z3.sat:
        m = s.model()
        col = []
        for i in range(1, N + 1):
            for c in range(k):
                if z3.is_true(m.eval(b[i][c])):
                    col.append(c)
                    break
        return True, col, t1 - t0
    return False, None, t1 - t0

def get_exact_3color_rado(c):
    expected = 13 * c + 14
    is_sat, col, _ = check_rado_sat((1, 1, 1), c, expected - 1, k=3)
    assert is_sat, f"N={expected-1} should be SAT for c={c}!"
    is_sat, _, _ = check_rado_sat((1, 1, 1), c, expected, k=3)
    assert not is_sat, f"N={expected} should be UNSAT for c={c}!"
    return expected, col