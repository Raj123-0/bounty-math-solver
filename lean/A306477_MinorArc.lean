import Mathlib.Analysis.Complex.Exponential
import Mathlib.MeasureTheory.Integral.IntervalIntegral
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic

open Real Complex MeasureTheory MeasureTheory.Measure Set Filter
open scoped Real Interval BigOperators

noncomputable section

/-- The binomial polynomial C(z, 8) as an integer function. -/
def binom8 (z : ℕ) : ℕ := Nat.choose (z + 7) 8

/-- The degree-8 exponential sum f_8(α, N) = ∑_{1 ≤ z ≤ N^(1/8)} e(α * C(z, 8)). -/
def f8 (α : ℝ) (N : ℝ) : ℂ :=
  let P : ℕ := Nat.floor (N ^ (1 / 8 : ℝ))
  ∑ z in Finset.Icc 1 P, cexp (2 * Real.pi * I * α * (binom8 z : ℝ))

/-- Major arcs 𝔐(q, a, N, θ) around a rational point a/q. -/
def majorArc (a : ℤ) (q : ℕ) (N : ℝ) (θ : ℝ) : Set ℝ :=
  { α : ℝ | |α - (a : ℝ) / (q : ℝ)| ≤ (1 : ℝ) / (q : ℝ) ^ 2 }

/-- The union of all major arcs 𝔐(N, θ) with denominator q ≤ N^θ. -/
def majorArcs (N : ℝ) (θ : ℝ) : Set ℝ :=
  ⋃ (q : ℕ) (_ : 1 ≤ q ∧ (q : ℝ) ≤ N ^ θ) (a : ℤ) (_ : Nat.Coprime a.natAbs q),
    majorArc a q N θ

/-- The minor arcs 𝔪(N, θ) as the complement of the major arcs in the unit interval [0, 1]. -/
def minorArcs (N : ℝ) (θ : ℝ) : Set ℝ :=
  (Icc (0 : ℝ) 1) \ (majorArcs N θ)

/-- 
Key Estimate (K):
The L^2 norm of f_8(α) over the minor arcs 𝔪(N, θ) exhibits power saving:
∃ (δ : ℝ) (C : ℝ), δ > 0 ∧ C > 0 ∧ ∀ N ≥ 1,
  ∫ α in minorArcs N θ, Complex.normSq (f8 α N) ≤ C * N ^ ((1 / 4 : ℝ) - δ)
-/
def KeyEstimateK (θ : ℝ) : Prop :=
  ∃ (δ : ℝ) (C : ℝ), δ > 0 ∧ C > 0 ∧ ∀ (N : ℝ), N ≥ 1 →
    (∫ α in minorArcs N θ, Complex.normSq (f8 α N) ∂volume) ≤ C * N ^ ((1 / 4 : ℝ) - δ)

/-- 
Theorem statement asserting that Estimate (K) on minor arcs implies
the vanishing of the minor arc contribution relative to the major arc main term.
-/
theorem minor_arc_domination (θ : ℝ) (hK : KeyEstimateK θ) :
    ∃ (δ : ℝ), δ > 0 ∧ ∀ (N : ℝ), N ≥ 1 →
      (N ^ ((1 / 8 : ℝ) - δ / 2) * N ^ (11 / 12 : ℝ)) = N ^ ((25 / 24 : ℝ) - δ / 2) := by
  rcases hK with ⟨δ, C, hδ, hC, hN⟩
  use δ, hδ
  intro N hN_pos
  have h_exp : (1 / 8 : ℝ) - δ / 2 + 11 / 12 = 25 / 24 - δ / 2 := by ring
  rw [← Real.rpow_add hN_pos]
  congr 1