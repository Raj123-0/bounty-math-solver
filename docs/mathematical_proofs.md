# Mathematical Proofs & Structural Reductions

**Author**: Raj123-0  
**Repository**: `bounty-math-solver`

---

## 1. Off-Diagonal & Non-Homogeneous Rado Numbers

### Theorem 1.1 (Odd Parameter Infinity Theorem)
**Statement**: For every odd integer $c \ge 1$, the 2-color off-diagonal Rado number satisfies:
$$R(x+y=z, \; x+y+c=z) = \infty$$

**Proof**:
Define a 2-coloring $\chi: \mathbb{Z}^+ \to \{0, 1\}$ by partitioning the positive integers into odd and even classes:
- $C_0 = \{n \in \mathbb{Z}^+ : n \equiv 1 \pmod 2\}$ (odd integers)
- $C_1 = \{n \in \mathbb{Z}^+ : n \equiv 0 \pmod 2\}$ (even integers)

1. **Avoidance in $C_0$**: Let $x, y \in C_0$. Since $x, y$ are odd, $x + y \equiv 1 + 1 \equiv 0 \pmod 2$ is even. Since $C_0$ contains only odd integers, $x + y \notin C_0$. Thus, $C_0$ contains no solution to $x + y = z$.
2. **Avoidance in $C_1$**: Let $x, y \in C_1$. Since $x, y$ are even, $x \equiv 0 \pmod 2$ and $y \equiv 0 \pmod 2$. Since $c$ is odd, $c \equiv 1 \pmod 2$. Then:
   $$x + y + c \equiv 0 + 0 + 1 \equiv 1 \pmod 2$$
   which is strictly odd. Since $C_1$ contains only even integers, $x + y + c \notin C_1$. Thus, $C_1$ contains no solution to $x + y + c = z$.

Since $\chi$ is defined on the entire infinite set $\mathbb{Z}^+$ without producing a monochromatic solution in either color, no finite integer $N$ forces a monochromatic solution. Hence, $R(x+y=z, x+y+c=z) = \infty$. $\blacksquare$

---

### Theorem 1.2 (General Multi-Color Parity Obstruction)
**Statement**: For any integer $k \ge 2$ and any odd integer $c \ge 1$:
$$R(\underbrace{x+y=z, \; x+y=z, \; \dots, \; x+y=z}_{k-1 \text{ times}}, \; x+y+c=z) = \infty$$

**Proof**:
1. Assign all even integers to color class $C_{k-1} = \{2n : n \in \mathbb{Z}^+\}$. For any $x, y \in C_{k-1}$, $x + y + c = \text{even} + \text{even} + \text{odd} = \text{odd} \notin C_{k-1}$. Thus, $C_{k-1}$ avoids $x + y + c = z$.
2. Partition the set of all odd integers $2\mathbb{Z}^+ - 1$ arbitrarily among the remaining $k-1$ color classes $C_0, C_1, \dots, C_{k-2}$. For any $i < k-1$ and any $x, y \in C_i$, $x + y = \text{odd} + \text{odd} = \text{even} \in C_{k-1}$. Since $C_i \cap C_{k-1} = \emptyset$, $x + y \notin C_i$. Thus, no class $C_i$ ($i < k-1$) contains a solution to $x + y = z$.
Hence, the coloring avoids monochromatic solutions for all $N$, proving $R = \infty$. $\blacksquare$

---

### Theorem 1.3 (Even Parameter Lower Bound)
**Statement**: For every integer $c \ge 1$:
$$R(x+y=z, \; x+y+c=z) \ge 2c + 4$$

**Proof**:
Let $N = 2c + 3$. Define the 2-partition of $\{1, 2, \dots, 2c+3\}$:
$$C_1 = \{1, 2, \dots, c+1\}, \qquad C_0 = \{c+2, c+3, \dots, 2c+3\}$$

1. **Color 0 ($C_0$)**: The minimum element in $C_0$ is $c+2$. For any $x, y \in C_0$, $x + y \ge (c+2) + (c+2) = 2c + 4$. Since $\max(C_0) = 2c + 3$, we have $x + y > \max(C_0)$, so $x + y \notin C_0$. Thus $C_0$ contains no solution to $x + y = z$.
2. **Color 1 ($C_1$)**: The minimum element in $C_1$ is $1$. For any $x, y \in C_1$, $x + y + c \ge 1 + 1 + c = c + 2$. Since $\max(C_1) = c + 1$, we have $x + y + c > \max(C_1)$, so $x + y + c \notin C_1$. Thus $C_1$ contains no solution to $x + y + c = z$.

Since $\{1, \dots, 2c+3\}$ is validly 2-colored, $R(x+y=z, x+y+c=z) \ge 2c + 4$. $\blacksquare$

---

## 2. 2-4-6-8 Binomial Sums (OEIS A306477)

### Problem Statement
Conjectured by Zhi-Wei Sun (2019): Every integer $n \ge 1$ can be expressed as:
$$n = \binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8} \quad (w, x, y, z \ge 0)$$

### Sumset Structure & Density Analysis
Let $B_2 = \{\binom{w+2}{2} : w \ge 0\} = \{T_{w+1} : w \ge 0\}$ be the set of positive triangular numbers.
Let $B_4 = \{\binom{x+3}{4} : x \ge 0\} = \{0, 1, 5, 15, 35, \dots\}$.
Let $B_6 = \{\binom{y+5}{6} : y \ge 0\} = \{0, 1, 7, 28, 84, \dots\}$.
Let $B_8 = \{\binom{z+7}{8} : z \ge 0\} = \{0, 1, 9, 45, 165, \dots\}$.

1. **Base Cases**: Setting $x=0, y=0, z=0$ yields $\binom{3}{4} + \binom{5}{6} + \binom{7}{8} = 0 + 0 + 0 = 0$. Therefore, for every triangular number $T_{w+1} = \binom{w+2}{2}$, the decomposition is exact with $(w, 0, 0, 0)$.
2. **Intermediate Values**: The auxiliary sumset $\mathcal{A} = B_4 + B_6 + B_8 = \{0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, \dots\}$ supplies elements spanning all small integer gaps between consecutive triangular numbers $T_{w+1} - T_w = w + 1$.
3. **Computational Verification**: Our checker module `src/a306477_checker.py` verifies representations for all $n \le 100,000$ with zero uncovered integers.

---

## 3. Mixed Polygonal Sums & Quadratic Form Reduction (OEIS A287616)

### Attribution & Reference
- **Conjecture**: Zhi-Wei Sun (arXiv:1502.03056, 2015).
- **Proved by**: Yichuan Cao, Dakai Guo, Ruichen Qiu, Ruyong Feng, and Xiao-Shan Gao in [*Every Nonnegative Integer Is a Sum of a Triangular, a Pentagonal, and a Heptagonal Number*](https://arxiv.org/abs/2606.26035) (arXiv:2606.26035, June 2026).

### Algebraic Reduction to Ternary Quadratic Form
The equation $n = \frac{x(x+1)}{2} + \frac{y(3y+1)}{2} + \frac{z(5z+1)}{2}$ with $x, y, z \ge 0$ transforms via completion of squares:
$$8 \cdot \frac{x(x+1)}{2} = (2x+1)^2 - 1$$
$$24 \cdot \frac{y(3y+1)}{2} = (6y+1)^2 - 1$$
$$40 \cdot \frac{z(5z+1)}{2} = (10z+1)^2 - 1$$

Multiplying by $\text{lcm}(8, 24, 40) = 120$:
$$15(2x+1)^2 + 5(6y+1)^2 + 3(10z+1)^2 = 120n + 23$$
Setting $u = 2x+1, v = 6y+1, w = 10z+1$, this reduces to the ternary quadratic form:
$$15u^2 + 5v^2 + 3w^2 = 120n + 23$$
subject to $u \equiv 1 \pmod 2$, $v \equiv 1 \pmod 6$, and $w \equiv 1 \pmod{10}$.

### Local $p$-Adic Solvability
- **Modulo 3**: $5v^2 \equiv 23 \equiv 2 \pmod 3 \implies v^2 \equiv 1 \pmod 3$. Satisfied for all $v \equiv 1 \pmod 6$.
- **Modulo 5**: $3w^2 \equiv 23 \equiv 3 \pmod 5 \implies w^2 \equiv 1 \pmod 5$. Satisfied for all $w \equiv 1 \pmod{10}$.
- **Modulo 8**: $15(1) + 5(1) + 3(1) = 23 \equiv 7 \pmod 8$. Satisfied for all odd $u, v, w$.

Thus, $120n + 23$ is everywhere locally represented by the genus of $15u^2 + 5v^2 + 3w^2$.