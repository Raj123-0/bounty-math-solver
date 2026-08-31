# Mathematical Theory & Verification Notes

**Author**: Raj123-0  
**Repository**: `bounty-math-solver`

---

## 1. Mixed Polygonal Sum Representations (OEIS A287616)

### Attribution & Published Proof
- **Conjecture**: Zhi-Wei Sun (arXiv:1502.03056, 2015).
- **Proof**: Proved by Yichuan Cao, Dakai Guo, Ruichen Qiu, Ruyong Feng, and Xiao-Shan Gao (arXiv:2606.26035, June 2026).
- **Credit**: Credit for the original proof belongs entirely to Cao et al. (2026). This repository provides independent implementation and verification code.

### Statement
For any integer $n \ge 0$, there exist non-negative integers $x, y, z \in \mathbb{N}$ such that:
$$n = T_x + P_y + H_z$$
where:
$$T_x = \frac{x(x+1)}{2}, \quad P_y = \frac{y(3y+1)}{2}, \quad H_z = \frac{z(5z+1)}{2}$$
The representation is unique ($a(n)=1$) if and only if $n \in \{0, 1, 2, 4, 7, 9, 22\}$.

### Algebraic Transformation to Ternary Form
Multiplying by $\text{lcm}(8, 24, 40) = 120$:
$$15(2x+1)^2 + 5(6y+1)^2 + 3(10z+1)^2 = 120 n + 23$$
Setting $u = 2x+1, v = 6y+1, w = 10z+1$, this is equivalent to solving:
$$15 u^2 + 5 v^2 + 3 w^2 = 120 n + 23$$
subject to $u \equiv 1 \pmod 2, v \equiv 1 \pmod 6, w \equiv 1 \pmod{10}$.

---

## 2. 2-4-6-8 Binomial Sums (OEIS A306477)

### Attribution
Conjectured by **Prof. Zhi-Wei Sun** (2019).

### Statement
Every integer $n \ge 1$ can be expressed as:
$$n = \binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8} \quad (w, x, y, z \ge 0)$$

### Status
This repository provides computational checking tools verifying $n \le 100,000$. The full theoretical proof for all $n \ge 1$ remains an **open problem**.

---

## 3. Conjectured 3-Color Rado Numbers ($x + y + c = z$)

### Conjectured Formula
$$R_3(x + y + c = z) = 13c + 14$$

### Status
Computationally verified for small constants $c \in \{0, 1, 2, 3\}$ using SAT solvers. A general combinatorial proof for all $c \ge 0$ is currently an open conjecture.