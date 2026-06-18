import Mathlib.Tactic

namespace Erdos993

/-!
Algebraic identities used by the certificate reductions.

These statements are deliberately abstract: the paper applies them after each
symbol is instantiated as an exact coefficient bracket.  Keeping the
coefficient extraction out of the statements makes the algebraic load-bearing
step small enough to kernel-check directly.
-/

/-- The determinant-like pair defect used in the pair-slot reductions. -/
def pairDefect {R : Type} [Sub R] [Mul R] (P Q X Y : R) : R :=
  P * Q - X * Y

/--
The algebraic core of Lemma `t`-cancellation: after replacing
`X,Y,Q` by the two-slot flow expressions, the pair defect is independent of
the common flow parameter `t`.
-/
theorem tCancellation {R : Type} [CommRing R] (P Q X Y t : R) :
    pairDefect P (Q + t * (X + Y) + t * t * P) (X + t * P) (Y + t * P)
      = pairDefect P Q X Y := by
  simp [pairDefect]
  ring

/--
Subtraction-free form of `tCancellation`, useful when the bracket values live
in a semiring before being embedded in an ordered ring.
-/
theorem tCancellationSemiring {R : Type} [CommSemiring R] (P Q X Y t : R) :
    P * (Q + t * (X + Y) + t * t * P) + X * Y
      = P * Q + (X + t * P) * (Y + t * P) := by
  ring

/--
If the bracket `P` and flow parameter `t` are nonnegative, then each cross
bracket `X + tP`, `Y + tP` dominates its value at `t = 0`.
-/
theorem crossBracket_le_flow {R : Type} [CommSemiring R] [LinearOrder R]
    [IsStrictOrderedRing R] {P X t : R} (hP : 0 ≤ P) (ht : 0 ≤ t) :
    X ≤ X + t * P := by
  exact le_add_of_nonneg_right (mul_nonneg ht hP)

/--
The product of the two cross brackets is nondecreasing in the common
nonnegative flow parameter.  This is the ordered part of the consequence used
after `tCancellation`.
-/
theorem crossBracketProduct_le_flow {R : Type} [CommSemiring R] [LinearOrder R]
    [IsStrictOrderedRing R] {P X Y t : R} (hP : 0 ≤ P) (hX : 0 ≤ X)
    (hY : 0 ≤ Y) (ht : 0 ≤ t) :
    X * Y ≤ (X + t * P) * (Y + t * P) := by
  have htp : 0 ≤ t * P := mul_nonneg ht hP
  have hXp : 0 ≤ X + t * P := add_nonneg hX htp
  exact mul_le_mul
    (le_add_of_nonneg_right htp)
    (le_add_of_nonneg_right htp)
    hY
    hXp

end Erdos993
