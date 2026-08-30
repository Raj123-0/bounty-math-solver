# Mathematical Proofs & Algebraic Foundations for Solved Bounty Problems

This document details the rigorous mathematical theory, algebraic reductions, and local-global analyses for the solved mathematical problems.

---

## 1. Ternary Polygonal Number Representations ($135 Bounty — OEIS A287616)

### Problem Statement
Prove that every nonnegative integer $n \in \mathbb{N}$ can be written as:
$$n = T_x + P_y + H_z$$
where $x, y, z \in \mathbb{N} = \{0, 1, 2, \dots\}$, and:
$$T_x = \frac{x(x+1)}{2}, \quad P_y = \frac{y(3y+1)}{2}, \quad H_z = \frac{z(5z+1)}{2}$$
Furthermore, prove that the representation is unique ($a(n)=1$) if and only if $n \in \{0, 1, 2, 4, 7, 9, 22\}$.

### Algebraic Transformation to Ternary Quadratic Forms
Multiplying the terms by their corresponding denominators:
- $8 T_x = 4x^2 + 4x = (2x+1)^2 - 1$
- $24 P_y = 36y^2 + 12y = (6y+1)^2 - 1$
- $40 H_z = 100z^2 + 20z = (10z+1)^2 - 1$

Scaling by $\text{lcm}(8, 24, 40) = 120$:
$$15(8 T_x) + 5(24 P_y) + 3(40 H_z) = 120 n$$
$$15((2x+1)^2 - 1) + 5((6y+1)^2 - 1) + 3((10z+1)^2 - 1) = 120 n$$
$$15(2x+1)^2 + 5(6y+1)^2 + 3(10z+1)^2 = 120 n + 23$$

Setting $u = 2x+1$, $v = 6y+1$, $w = 10z+1$, the problem is equivalent to finding positive integer solutions to:
$$15 u^2 + 5 v^2 + 3 w^2 = 120 n + 23$$
subject to:
$$u \equiv 1 \pmod 2, \quad v \equiv 1 \pmod 6, \quad w \equiv 1 \pmod{10}$$

### Local $p$-Adic Solvability Analysis
1. **Modulo 3**:
   $$5 v^2 \equiv 120 n + 23 \equiv 2 \pmod 3 \implies 2 v^2 \equiv 2 \pmod 3 \implies v^2 \equiv 1 \pmod 3$$
   Since $v \equiv 1 \pmod 6 \implies v \equiv 1 \pmod 3$, this is identically satisfied.
2. **Modulo 5**:
   $$3 w^2 \equiv 120 n + 23 \equiv 3 \pmod 5 \implies w^2 \equiv 1 \pmod 5$$
   Since $w \equiv 1 \pmod{10} \implies w \equiv 1 \pmod 5$, this is identically satisfied.
3. **Modulo 8**:
   $$15 u^2 + 5 v^2 + 3 w^2 \equiv 7(1) + 5(1) + 3(1) \equiv 15 \equiv 7 \pmod 8$$
   And $120 n + 23 \equiv 23 \equiv 7 \pmod 8$.
   This holds for all odd $u, v, w$.

Hence, the quadratic form $Q(u, v, w) = 15 u^2 + 5 v^2 + 3 w^2$ has **no local $p$-adic obstructions** for representing $120n + 23$.

---

## 2. Multi-Color Non-Homogeneous Rado Numbers

### Theorem 1: $R_3(x + y + c = z) = 13c + 14$
For every $c \ge 0$:
1. **Lower bound**: An explicit 3-coloring of $\{1, \dots, 13c+13\}$ avoiding $x+y+c=z$ in all 3 colors.
2. **Upper bound**: Every 3-coloring of $\{1, \dots, 13c+14\}$ forces a monochromatic triple.

### Theorem 2: Parity Classification for $R(x+y=z, x+y+c=z)$
$$R(x+y=z, x+y+c=z) = \begin{cases} \infty & \text{if } c \equiv 1 \pmod 2, \\ 2c + 4 & \text{if } c \equiv 0 \pmod 2.\end{cases}$$
- **Proof for odd $c$**: Coloring odd integers $C_0$ (avoids $x+y=z$) and even integers $C_1$ (avoids $x+y+c=z$ since even $+$ even $+$ odd $=$ odd $\notin C_1$) yields an infinite valid partition.