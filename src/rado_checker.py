"""
Rado Number Computational Checker (Non-Homogeneous 3-Coloring)
Author: Raj123-0
Description: Independent computational verification tool for exploring
             3-color Rado numbers of the non-homogeneous equation:
                 x + y + c = z

Conjecture under study:
    For any integer c >= 0, the 3-color Rado number R_3(x + y + c = z) appears
    to follow the linear pattern 13c + 14.

Disclaimer:
    Values for small c (e.g. c=0, 1, 2, 3) are verified via SAT-based exhaustive
    search. A full general mathematical proof for all c remains an open conjecture.
"""

from typing import List, Optional, Tuple
import time

import z3


def check_3color_sat(c_const: int, n: int) -> Tuple[bool, Optional[List[int]], float]:
    """
    Checks if {1, 2, ..., n} can be 3-colored without any monochromatic
    solution to x + y + c_const = z.
    
    Returns:
        (is_satisfiable, coloring_list, duration_seconds)
    """
    solver = z3.Solver()
    # b[i][c] is True iff integer i has color c (c in {0, 1, 2})
    b = [[z3.Bool(f"b_{i}_{col}") for col in range(3)] for i in range(n + 1)]
    
    # 1. Exactly one color per integer
    for i in range(1, n + 1):
        solver.add(z3.Or(b[i][0], b[i][1], b[i][2]))
        solver.add(z3.Not(z3.And(b[i][0], b[i][1])))
        solver.add(z3.Not(z3.And(b[i][0], b[i][2])))
        solver.add(z3.Not(z3.And(b[i][1], b[i][2])))
        
    # 2. Avoid monochromatic solutions in each color
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            z = x + y + c_const
            if 1 <= z <= n:
                for col in range(3):
                    solver.add(z3.Or(
                        z3.Not(b[x][col]),
                        z3.Not(b[y][col]),
                        z3.Not(b[z][col])
                    ))
                    
    # 3. Symmetry breaking: 1 is assigned color 0
    solver.add(b[1][0])
    for col in range(1, 3):
        for i in range(1, n + 1):
            if i == 1:
                solver.add(z3.Not(b[1][col]))
            else:
                solver.add(z3.Or(z3.Not(b[i][col]), z3.Or([b[j][col-1] for j in range(1, i)])))
                
    t0 = time.time()
    result = solver.check()
    duration = time.time() - t0
    
    if result == z3.sat:
        model = solver.model()
        coloring = []
        for i in range(1, n + 1):
            for col in range(3):
                if z3.is_true(model.eval(b[i][col])):
                    coloring.append(col)
                    break
        return True, coloring, duration
    return False, None, duration


def verify_formula_for_c(c_const: int) -> dict:
    """
    Tests whether the exact transition from SAT to UNSAT occurs at 13c + 14.
    """
    predicted_bound = 13 * c_const + 14
    sat_at_lower, col, t_sat = check_3color_sat(c_const, predicted_bound - 1)
    unsat_at_bound, _, t_unsat = check_3color_sat(c_const, predicted_bound)
    
    is_valid = sat_at_lower and (not unsat_at_bound)
    return {
        "c": c_const,
        "predicted_rado_number": predicted_bound,
        "sat_at_N_minus_1": sat_at_lower,
        "unsat_at_N": not unsat_at_bound,
        "formula_confirmed": is_valid,
        "timing_sat_sec": t_sat,
        "timing_unsat_sec": t_unsat
    }

if __name__ == "__main__":
    print("=== Rado Number Formula Computational Checks ===")
    for c in [0, 1, 2, 3]:
        res = verify_formula_for_c(c)
        status = "CONFIRMED" if res["formula_confirmed"] else "FAILED"
        print(f"c={c}: R_3(x+y+{c}=z) = {res['predicted_rado_number']} [{status}] (SAT in {res['timing_sat_sec']:.3f}s, UNSAT in {res['timing_unsat_sec']:.3f}s)")