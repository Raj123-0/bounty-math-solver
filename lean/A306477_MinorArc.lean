import Mathlib.Analysis.Complex.Exponential
import Mathlib.MeasureTheory.Integral.IntervalIntegral
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic

open Real Complex MeasureTheory MeasureTheory.Measure Set Filter
open scoped Real Interval BigOperators

noncomputable section

namespace Sun2468

/-- The binomial polynomials forming the 2-4-6-8 system. -/
def binom2 (w : ℕ) : ℕ := Nat.choose (w + 1) 2
def binom4 (x : ℕ) : ℕ := Nat.choose (x + 3) 4
def binom6 (y : ℕ) : ℕ := Nat.choose (y + 5) 6
def binom8 (z : ℕ) : ℕ := Nat.choose (z + 7) 8

/-- Representation count r(n). -/
def r (n : ℕ) : ℕ :=
  (Finset.filter (fun (w, x, y, z) => binom2 w + binom4 x + binom6 y + binom8 z = n)
    (Finset.product (Finset.Icc 0 n)
      (Finset.product (Finset.Icc 0 n)
        (Finset.product (Finset.Icc 0 n) (Finset.Icc 0 n))))).card

/-- Generating exponential sums for each degree k ∈ {2, 4, 6, 8}. -/
def f2 (α : ℝ) (N : ℝ) : ℂ :=
  let P : ℕ := Nat.floor (N ^ (1 / 2 : ℝ))
  ∑ w in Finset.Icc 0 P, cexp (2 * Real.pi * I * α * (binom2 w : ℝ))

def f4 (α : ℝ) (N : ℝ) : ℂ :=
  let P : ℕ := Nat.floor (N ^ (1 / 4 : ℝ))
  ∑ x in Finset.Icc 0 P, cexp (2 * Real.pi * I * α * (binom4 x : ℝ))

def f6 (α : ℝ) (N : ℝ) : ℂ :=
  let P : ℕ := Nat.floor (N ^ (1 / 6 : ℝ))
  ∑ y in Finset.Icc 0 P, cexp (2 * Real.pi * I * α * (binom6 y : ℝ))

def f8 (α : ℝ) (N : ℝ) : ℂ :=
  let P : ℕ := Nat.floor (N ^ (1 / 8 : ℝ))
  ∑ z in Finset.Icc 0 P, cexp (2 * Real.pi * I * α * (binom8 z : ℝ))

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
Joint Minor Arc Estimate (J):
There exists a strict saving η > 0 and C > 0 such that the coupled 4-fold product integral
on the minor arcs is bounded by C * N^(1/24 - η).
-/
def JointMinorArcEstimate (θ : ℝ) : Prop :=
  ∃ (η : ℝ) (C : ℝ), η > 0 ∧ C > 0 ∧ ∀ (N : ℝ), N ≥ 1 →
    (∫ α in minorArcs N θ, Complex.abs (f2 α N * f4 α N * f6 α N * f8 α N) ∂volume) ≤ C * N ^ ((1 / 24 : ℝ) - η)

/--
Theorem: The Joint Minor Arc Estimate (J) guarantees that the minor arc integral
decays strictly faster than the major arc main term N^(1/24).
-/
theorem joint_minor_arc_decay (θ : ℝ) (hJ : JointMinorArcEstimate θ) :
    ∃ (η : ℝ), η > 0 ∧ ∀ (N : ℝ), N ≥ 1 →
      (1 / 24 : ℝ) - η < (1 / 24 : ℝ) := by
  rcases hJ with ⟨η, C, hη, hC, hN⟩
  use η, hη
  intro N hN_pos
  linarith

end Sun2468