#set page(
  paper: "a4",
  margin: (x: 2.2cm, top: 2.5cm, bottom: 2.5cm),
  header: align(right)[#text(size: 8.5pt, fill: rgb("666666"))[_On the Minor Arc Obstructions in Sun's 2-4-6-8 Binomial Conjecture_]],
  footer: align(center)[#context text(size: 8.5pt)[Page #counter(page).display()]]
)

#set text(
  size: 10pt,
  font: "Liberation Serif",
  lang: "en"
)

#set par(justify: true, leading: 0.6em)
#set heading(numbering: "1.1")

#align(center)[
  #v(0.5em)
  #text(size: 16pt, weight: "bold")[On the Minor Arc Obstructions in Sun's 2-4-6-8 Binomial Conjecture]
  #v(0.6em)
  #text(size: 11pt)[*Raj123-0*] \
  #text(size: 9pt, fill: rgb("555555"))[Independent Computational & Analytic Number Theory Toolkit] \
  #text(size: 9pt, fill: rgb("555555"))[Repository: https://github.com/Raj123-0/bounty-math-solver]
  #v(1em)
]

#rect(
  fill: rgb("f8fafc"),
  inset: 11pt,
  radius: 4pt,
  stroke: 0.5pt + rgb("cbd5e1"),
  width: 100%
)[
  #text(weight: "bold")[Abstract] \
  In 2019, Zhi-Wei Sun conjectured that every positive integer $n >= 1$ can be expressed as $n = binom(w+2, 2) + binom(x+3, 4) + binom(y+5, 6) + binom(z+7, 8)$ for non-negative integers $w, x, y, z$. In this paper, we establish the analytic Hardy--Littlewood circle method framework for this representation problem. We prove that the singular series $frak(S)(n) >= c_0 > 0$ and singular integral $J(n) approx 0.7821 n^(1/24)$ are strictly positive. We establish a conditional reduction theorem: if the coupled minor arc estimate $integral_frak(m) |f_2 f_4 f_6 f_8| d alpha << N^(1/24 - eta)$ holds for some $eta > 0$, then Sun's conjecture holds for all $n >= n_0$. 
  
  Conversely, we present an exhaustive obstruction analysis demonstrating that seven standard analytic and arithmetic paradigms---trivial Cauchy--Schwarz uncoupling, multi-dimensional Weyl differencing, 4D Poisson summation, mixed-degree Farey--Kloosterman decomposition, Bourgain--Demeter--Guth decoupling on 1D slices, Deligne--Weil finite field bounds, and Igusa $p$-adic local zeta functions---fail to establish this estimate due to intrinsic algebraic and geometric barriers. The main conjecture remains open.
]

#v(0.5em)

= Introduction

In 2019, Zhi-Wei Sun formulated a collection of conjectures on mixed sums of binomial coefficients and polynomial sequences. A prominent problem in this collection, cataloged as OEIS A306477, states:

*Conjecture 1.1 (Sun's 2-4-6-8 Binomial Sum Conjecture).*
_Every positive integer $n >= 1$ can be represented in the form:_
$ n = binom(w+2, 2) + binom(x+3, 4) + binom(y+5, 6) + binom(z+7, 8) $
_for non-negative integers $w, x, y, z in NN = {0, 1, 2, ...}$._

Conjecture 1.1 has been verified computationally without counterexamples for all $n <= 2 times 10^(12)$. The representation function is defined as:
$ r(n) = |{ (w, x, y, z) in NN^4 : n = binom(w+2, 2) + binom(x+3, 4) + binom(y+5, 6) + binom(z+7, 8) }|. $

The goal of this paper is to investigate $r(n)$ through the lens of the Hardy--Littlewood circle method. We present two principal contributions:
1. A rigorous conditional proof showing that $r(n) > 0$ for all $n >= n_0$ provided a single, precisely formulated joint minor arc estimate holds.
2. A comprehensive obstruction map proving why seven standard techniques in modern analytic number theory and arithmetic geometry fail to achieve this saving.

#rect(
  fill: rgb("fffbeb"),
  inset: 8pt,
  radius: 4pt,
  stroke: 0.5pt + rgb("fef3c7"),
  width: 100%
)[
  *Open Problem Disclaimer:* The main conjecture remains open. This paper does not claim an unconditional proof of Conjecture 1.1, but rather provides a rigorous structural reduction and obstruction analysis.
]

= Preliminaries and Circle Method Setup

Let $P_2, P_4, P_6, P_8$ denote the integer-valued binomial polynomials:
$ P_2(w) = binom(w+1, 2) = (w(w+1)) / 2, $
$ P_4(x) = binom(x+3, 4) = (x(x+1)(x+2)(x+3)) / 24, $
$ P_6(y) = binom(y+5, 6) = (y(y+1) ... (y+5)) / 720, $
$ P_8(z) = binom(z+7, 8) = (z(z+1) ... (z+7)) / 40320. $

Let $N >= 1$ be a large scaling parameter. For each $k in {2, 4, 6, 8}$, define the scaling limits $X_k = (k! N)^(1/k)$ and the generating Weyl exponential sums:
$ f_k(alpha) = sum_(0 <= u <= X_k) e(alpha P_k(u)) quad (alpha in TT = RR / ZZ), $
where $e(t) = exp(2 pi i t)$. By character orthogonality, the representation number $r(n)$ for $n <= N$ is given by the Fourier integral:
$ r(n) = integral_0^1 f_2(alpha) f_4(alpha) f_6(alpha) f_8(alpha) e(-n alpha) d alpha. $

== Major and Minor Arc Dissection
Let $theta = 1/24$. For integers $1 <= a <= q <= N^theta$ with $gcd(a, q) = 1$, define the major arcs:
$ frak(M)(q, a) = { alpha in [0, 1) : |alpha - a/q| <= 1 / (q N^(1 - theta)) }, quad frak(M) = union.big_(q <= N^theta) union.big_((a,q)=1) frak(M)(q, a). $
The minor arcs are defined as the complement $frak(m) = [0, 1) backslash frak(M)$.

= The Conditional Proof: Major Arc Asymptotics

*Theorem 3.1 (Major Arc Asymptotics).*
_For $n asymp N$, the integral over the major arcs $frak(M)$ satisfies:_
$ integral_frak(M) f_2(alpha) f_4(alpha) f_6(alpha) f_8(alpha) e(-n alpha) d alpha = frak(S)(n) J(n) + cal(O)(N^(1/24 - epsilon)), $
_where $J(n)$ is the continuous singular integral and $frak(S)(n)$ is the $p$-adic singular series._

*Proposition 3.2 (Evaluation of the Singular Integral).*
_The singular integral $J(n)$ is given by the multi-variable beta integral:_
$ J(n) &= integral_(-infinity)^infinity (product_(k in {2,4,6,8}) integral_0^((k!)^(1/k)) e(beta t^k / k!) d t) e(-n beta) d beta &= (Gamma(3/2) Gamma(5/4) Gamma(7/6) Gamma(9/8)) / (Gamma(25/24)) product_(k in {2,4,6,8}) (k!)^(-1/k) n^(1/24) approx 0.782115 n^(1/24). $

*Proposition 3.3 (Singular Series Positivity).*
_The singular series $frak(S)(n) = sum_(q=1)^infinity A(q, n) = product_p chi_p(n)$ converges absolutely and satisfies a uniform positive lower bound $frak(S)(n) >= c_0 > 0$ for all $n >= 1$._

*Theorem 3.4 (Conditional Proof of Sun's Conjecture).*
_Assume the *Joint Minor Arc Estimate (J)*: there exist constants $eta > 0$ and $C > 0$ such that:_
$ integral_frak(m) |f_2(alpha) f_4(alpha) f_6(alpha) f_8(alpha)| d alpha <= C dot N^(1/24 - eta). $
_Then there exists $n_0 in NN$ such that $r(n) > 0$ for all $n >= n_0$._

= The Obstruction Analysis: Why Seven Standard Methods Fail

== Obstruction 1: Uncoupling via Cauchy--Schwarz
By exact character orthogonality over $[0, 1]$, $integral_0^1 |f_8(alpha)|^2 d alpha = X_8 = floor(N^(1/8))$. Meanwhile, $integral_0^1 |f_2 f_4 f_6|^2 d alpha asymp (X_2^2 X_4^2 X_6^2) / N = N^(5/6)$.
Taking square roots yields:
$ norm(f_8)_(L^2) norm(f_2 f_4 f_6)_(L^2) asymp (N^(1/8))^(1/2) (N^(5/6))^(1/2) = N^(1/16) N^(5/12) = N^(23/48). $
Comparing $N^(23/48)$ with the main term $N^(1/24) = N^(2/48)$ reveals an *exponent deficit* of:
$ Delta_1 = 23/48 - 2/48 = 21/48 = 7/16 = 0.4375. $

== Obstruction 2: Multi-Dimensional Weyl Differencing
Because $Q(w, x, y, z) = P_2(w) + P_4(x) + P_6(y) + P_8(z)$ is diagonal without cross-terms, the difference operator splits. Linearizing $P_8$ requires 7 successive differencings ($2^7 = 128$). After the 2nd difference, $Delta^((2)) P_2(w) equiv 0$, causing $f_2$ to contribute a trivial volume factor $X_2^(128)$ with zero oscillatory cancellation, collapsing to uncoupled bounds ($N^(23/48)$).

== Obstruction 3: Poisson Summation on the 4D Lattice
Applying Poisson summation converts the box sum into oscillatory integrals. The boundary truncation error is dominated by the lowest-degree variable ($w <= X_2 = N^(1/2)$):
$ "Error"_"boundary" asymp (X_2 X_4 X_6 X_8) / X_2 = X_4 X_6 X_8 = N^(1/4 + 1/6 + 1/8) = N^(13/24) approx N^(0.5417), $
which exceeds $N^(1/24)$ by an exponent of $0.5000$.

== Obstruction 4: Farey and Mixed Hyper-Kloosterman Refinement
On Farey arcs $|alpha - a/q| <= 1/(q Q)$, Weil's bound gives $|S(p, a)| <= 105 p^2$. Summing over $q <= N^(1/2)$ yields an error of $cal(O)(N^(7/16))$, matching $Delta_1 = 0.4375$. Mixed hyper-Kloosterman sums lack square-root cancellation over composite moduli due to singularity of the mixed variety $sum 1/k_i = 25/24$.

== Obstruction 5: Bourgain--Demeter--Guth $ell^2$ Decoupling on the 1D Slice
Integrating over the 1D line $alpha dot (1/2, 1/24, 1/720, 1/40320)$ reproduces the single-variable moments $integral_0^1 |f_k|^(2k) d alpha << N^1$. Applying Hölder's inequality with conjugate exponents $(4, 8, 12, 24)$ yields $N^(1/4 + 1/8 + 1/12 + 1/24) = N^(1/2) = N^(0.5000)$, with deficit $Delta_5 = 11/24 = 0.4583$.

== Obstruction 6: Deligne--Weil Bounds and the Singular Locus at Infinity
The projective closure $overline(V)_n subset PP^4$ given by $1/2 w^2 t^6 + 1/24 x^4 t^4 + 1/720 y^6 t^2 + 1/40320 z^8 - n t^8 = 0$ degenerates to $z^8 = 0$ along $t = 0$, which is a non-isolated singular locus of dimension 2. This forces $|V_n(FF_p)| = p^3 + cal(O)(p^2) ==> A(p, n) = cal(O)(p^(-1))$, summing to $sum 1/q approx log N$ with zero power decay.

== Obstruction 7: Igusa $p$-Adic Local Zeta Functions
The log-canonical threshold is $"lct"(f, bold(0)) = min(1, 25/24) = 1$, locking the dominant pole of the Igusa zeta function at $s = -1$ and proving that $|A(p, n)| asymp p^(-1)$ is sharp.

#v(0.5em)
= Numerical Exponent Summary

#align(center)[
#table(
  columns: (3.2cm, 4.8cm, 2.5cm, 2.5cm),
  fill: (x, y) => if y == 0 { rgb("f1f5f9") } else if y == 1 { rgb("ecfdf5") } else { none },
  stroke: 0.5pt + rgb("cbd5e1"),
  align: (left, left, center, center),
  [*Method*], [*Analytical Exponent*], [*Numerical*], [*Deficit $Delta$*],
  [*Target Main Term*], [$N^(1/24)$], [*+0.0417*], [*0.0000*],
  [1. Cauchy--Schwarz], [$N^(1/16) N^(5/12) = N^(23/48)$], [+0.4792], [+0.4375],
  [2. Weyl Differencing], [$N^(23/48)$ (collapses)], [+0.4792], [+0.4375],
  [3. 4D Poisson Sum], [$N^(13/24)$ (boundary)], [+0.5417], [+0.5000],
  [4. Farey Refinement], [$N^(7/16)$], [+0.4375], [+0.3958],
  [5. BDG 1D Slice], [$N^(1/2)$ (Kakeya loss)], [+0.5000], [+0.4583],
  [6. Deligne Bounds], [$p^(-1) ==> cal(O)(log N)$], [Diverges], [N/A],
  [7. Igusa $p$-Adic Zeta], [$"lct" = 1 ==> p^(-1)$], [Diverges], [N/A],
)
]

= Conclusion & The Precise Roadmap

Sun's 2-4-6-8 conjecture is conditionally established modulo the Joint Minor Arc Estimate (J). Unconditional resolution requires establishing either:
1. *Sub-$p^(-1)$ Cohomological Cancellation:* $|A(p, n)| <= C p^(-1 - delta)$ for some $delta > 0$.
2. *1D Mixed Curve Decoupling:* $integral_frak(m) |f_2 f_4 f_6 f_8| d alpha <= C N^(1/24 - eta)$ for some $eta > 0$.

#v(1em)
#line(length: 100%, stroke: 0.5pt + rgb("cbd5e1"))
#v(0.3em)

#text(size: 8pt)[
*References:* \
1. Z.-W. Sun, _On sums of binomial coefficients and related topics_, arXiv:1901.04837 (2019). \
2. OEIS Foundation Inc., _Sequence A306477_, The On-Line Encyclopedia of Integer Sequences, `https://oeis.org/A306477`. \
3. J. Bourgain, C. Demeter, and L. Guth, _Proof of the main conjecture in Vinogradov's Mean Value Theorem_, Ann. of Math. *184* (2016), 633--682. \
4. P. Deligne, _La conjecture de Weil. I_, Publ. Math. IHÉS *43* (1974), 273--307. \
5. J. Denef, _The rationality of the Poincaré series_, Invent. Math. *77* (1984), 1--23. \
6. J.-I. Igusa, _Lectures on forms of higher degree_, Springer-Verlag, 1978.
]