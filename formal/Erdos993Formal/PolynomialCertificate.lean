import Mathlib.Tactic

namespace Erdos993
namespace PolynomialCertificate

/-!
A proof-carrying certificate checker for univariate integer-polynomial
nonnegativity on all integer inputs `n >= 1`.

The certificate pattern mirrors the Taylor-shift method used by the paper's
E-core, ladder, and bulk-plus-giant scripts:

* check all finite samples `P(1), ..., P(B)` exactly;
* prove every coefficient of `P(x + B)` is nonnegative;
* conclude `P(n) >= 0` for every integer `n >= 1`.

The theorem `certificate_sound` is the checker soundness statement.  Exported
certificate data can instantiate `PositivityCertificate` with exact sample and
tail proofs, and Lean then checks the conclusion without trusting Python.
-/

abbrev IntPoly := List Int

/-- Evaluate an integer polynomial stored as ascending coefficients. -/
def eval : IntPoly -> Int -> Int
  | [], _ => 0
  | a :: p, x => a + x * eval p x

def polyAdd : IntPoly -> IntPoly -> IntPoly
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: polyAdd p q

def polySMul (a : Int) : IntPoly -> IntPoly
  | [] => []
  | b :: p => (a * b) :: polySMul a p

def polyXMul (p : IntPoly) : IntPoly :=
  0 :: p

def mulXPlus (B : Int) (p : IntPoly) : IntPoly :=
  polyAdd (polySMul B p) (polyXMul p)

/-- Coefficients of `P(x + B)`, for `P` stored in ascending order. -/
def shift (p : IntPoly) (B : Int) : IntPoly :=
  match p with
  | [] => []
  | a :: q => polyAdd [a] (mulXPlus B (shift q B))

def CoeffsNonneg (p : IntPoly) : Prop :=
  ∀ a ∈ p, 0 ≤ a

def SamplesNonneg (p : IntPoly) (B : Nat) : Prop :=
  ∀ n : Nat, 1 ≤ n -> n ≤ B -> 0 ≤ eval p (Int.ofNat n)

structure PositivityCertificate (p : IntPoly) where
  bound : Nat
  samples : SamplesNonneg p bound
  tail : CoeffsNonneg (shift p (Int.ofNat bound))

theorem eval_polyAdd (p q : IntPoly) (x : Int) :
    eval (polyAdd p q) x = eval p x + eval q x := by
  induction p generalizing q with
  | nil => cases q <;> simp [polyAdd, eval]
  | cons a p ih =>
      cases q with
      | nil => simp [polyAdd, eval]
      | cons b q =>
          simp [polyAdd, eval, ih]
          ring

theorem eval_polySMul (a : Int) (p : IntPoly) (x : Int) :
    eval (polySMul a p) x = a * eval p x := by
  induction p with
  | nil => simp [polySMul, eval]
  | cons b p ih =>
      simp [polySMul, eval, ih]
      ring

theorem eval_polyXMul (p : IntPoly) (x : Int) :
    eval (polyXMul p) x = x * eval p x := by
  simp [polyXMul, eval]

theorem eval_mulXPlus (B : Int) (p : IntPoly) (x : Int) :
    eval (mulXPlus B p) x = (B + x) * eval p x := by
  simp [mulXPlus, eval_polyAdd, eval_polySMul, eval_polyXMul]
  ring

theorem eval_shift (p : IntPoly) (B x : Int) :
    eval (shift p B) x = eval p (B + x) := by
  induction p with
  | nil => simp [shift, eval]
  | cons a p ih =>
      simp [shift, eval, eval_polyAdd, eval_mulXPlus, ih]

theorem eval_nonneg_of_coeffsNonneg (p : IntPoly) {x : Int}
    (hp : CoeffsNonneg p) (hx : 0 ≤ x) :
    0 ≤ eval p x := by
  induction p with
  | nil => simp [eval]
  | cons a p ih =>
      have ha : 0 ≤ a := hp a (by simp)
      have hp' : CoeffsNonneg p := by
        intro b hb
        exact hp b (by simp [hb])
      have ht : 0 ≤ eval p x := ih hp'
      have hmul : 0 ≤ x * eval p x := mul_nonneg hx ht
      simpa [eval] using add_nonneg ha hmul

/--
Soundness of the Taylor-shift positivity certificate.

The proof splits an arbitrary `n >= 1` into either the finite checked window
`n <= B`, or the tail `n = B + m` with `m > 0`; the latter follows from the
nonnegative coefficients of `P(x+B)` evaluated at nonnegative `m`.
-/
theorem certificate_sound {p : IntPoly} (cert : PositivityCertificate p) :
    ∀ n : Nat, 1 ≤ n -> 0 ≤ eval p (Int.ofNat n) := by
  intro n hn
  by_cases hle : n ≤ cert.bound
  · exact cert.samples n hn hle
  · have hlt : cert.bound < n := Nat.lt_of_not_ge hle
    let m : Nat := n - cert.bound
    have hn_eq : n = cert.bound + m := by
      exact (Nat.add_sub_of_le (Nat.le_of_lt hlt)).symm
    have hm_nonneg : 0 ≤ (Int.ofNat m) := by
      exact Int.natCast_nonneg m
    have htail :=
      eval_nonneg_of_coeffsNonneg
        (shift p (Int.ofNat cert.bound))
        cert.tail
        hm_nonneg
    have hshift := eval_shift p (Int.ofNat cert.bound) (Int.ofNat m)
    rw [hshift] at htail
    have hcast : (Int.ofNat cert.bound + Int.ofNat m) = Int.ofNat n := by
      rw [hn_eq]
      exact (Int.natCast_add cert.bound m).symm
    rwa [hcast] at htail

end PolynomialCertificate
end Erdos993
