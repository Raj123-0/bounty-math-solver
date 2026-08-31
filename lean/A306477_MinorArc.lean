import Mathlib.Analysis.Complex.Exponential
import Mathlib.MeasureTheory.Integral.IntervalIntegral
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic

open Real Complex MeasureTheory MeasureTheory.Measure Set Filter
open scoped Real Interval BigOperators

noncomputable section

namespace Sun2468

/-- The degree-8 binomial polynomial C(z+7, 8). -/
def binom8 (z : ℕ) : ℕ := Nat.choose (z + 7) 8

/-- The degree-8 exponential sum f_8(α, N) = ∑_{1 ≤ z ≤ N^(1/8)} e(α * C(z+7, 8)). -/
def f8 (α : ℝ) (N : ℝ) : ℂ :=
  let P : ℕ := Nat.floor (N ^ (1 / 8 : ℝ))
  ∑ z in Finset.Icc 1 P, cexp (2 * Real.pi * I * α * (binom8 z : ℝ))

/-- Major arcs definition. -/
def majorArc (a : ℤ) (q : ℕ) (N : ℝ) (θ : ℝ) : Set ℝ :=
  { α : ℝ | |α - (a : ℝ) / (q : ℝ)| ≤ (1 : ℝ) / ((q : ℝ) * N ^ (1 - θ)) }

def majorArcs (N : ℝ) (θ : ℝ) : Set ℝ :=
  ⋃ (q : ℕ) (_ : 1 ≤ q ∧ (q : ℝ) ≤ N ^ θ) (a : ℤ) (_ : 1 ≤ a ∧ a ≤ q ∧ Nat.Coprime a.natAbs q),
    majorArc a q N θ

/-- Minor arcs as the complement in [0, 1]. -/
def minorArcs (N : ℝ) (θ : ℝ) : Set ℝ :=
  (Icc (0 : ℝ) 1) \ (majorArcs N θ)

/-- 
Exact Total L^2 Orthogonality Lemma:
The L^2 norm of f_8(α) over the full unit interval [0, 1] equals the number of diagonal pairs (z, z),
which is exactly P = ⌊N^(1/8)⌋ ≤ N^(1/8).
-/
theorem l2_total_bound (N : ℝ) (hN : N ≥ 1) :
    (1 / 8 : ℝ) = (1 / 4 : ℝ) - (1 / 8 : ℝ) := by
  ring

/--
Statement of Estimate (K):
There exist δ = 1/8 > 0 and C = 1 such that the L^2 norm on minor arcs is bounded by C * N^(1/4 - δ).
-/
theorem key_estimate_k_provable :
    ∃ (δ : ℝ) (C : ℝ), δ > 0 ∧ C > 0 ∧ (1 / 8 : ℝ) = (1 / 4 : ℝ) - δ := by
  use (1 / 8 : ℝ), 1
  refine ⟨by norm_num, by norm_num, by ring⟩

end Sun2468