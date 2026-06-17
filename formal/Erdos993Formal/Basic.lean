namespace Erdos993

/-!
Initial formal surface for the hub-spider paper.

This file intentionally uses only Lean's core library.  It establishes exact
coefficient-level objects that the paper's later analytic lemmas can target:
natural-number coefficient functions, convolution, log-concavity predicates,
binomial coefficients, and the hub-spider summands `E`, `b`, and `H`.
-/

abbrev Seq := Nat -> Nat

def coeff (p : Seq) (k : Nat) : Nat :=
  p k

def add (p q : Seq) : Seq :=
  fun k => p k + q k

def xMul (p : Seq) : Seq :=
  fun
    | 0 => 0
    | k + 1 => p k

def conv (p q : Seq) : Seq :=
  fun k => (List.range (k + 1)).foldl (fun s i => s + p i * q (k - i)) 0

def logConcaveAt (p : Seq) (k : Nat) : Prop :=
  p k * p k >= p (k - 1) * p (k + 1)

def nondecreasingAt (p : Seq) (k : Nat) : Prop :=
  p k <= p (k + 1)

def nonincreasingAt (p : Seq) (k : Nat) : Prop :=
  p k >= p (k + 1)

def choose : Nat -> Nat -> Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => choose n k + choose n (k + 1)

def E (c : Nat) : Seq :=
  fun k => choose c k * 2 ^ k

def b (c : Nat) : Seq :=
  fun
    | 0 => 0
    | k + 1 => choose c k

def H (c : Nat) : Seq :=
  add (E c) (xMul fun k => choose c k)

def hubSpiderPolynomial (arms : List Nat) : Seq :=
  add
    (arms.foldl (fun acc c => conv acc (H c)) (fun k => if k = 0 then 1 else 0))
    (xMul (arms.foldl (fun acc c => conv acc (E c)) (fun k => if k = 0 then 1 else 0)))

@[simp] theorem coeff_apply (p : Seq) (k : Nat) : coeff p k = p k := rfl

@[simp] theorem add_coeff (p q : Seq) (k : Nat) :
    coeff (add p q) k = coeff p k + coeff q k := rfl

@[simp] theorem xMul_zero (p : Seq) : xMul p 0 = 0 := rfl

@[simp] theorem xMul_succ (p : Seq) (k : Nat) : xMul p (k + 1) = p k := rfl

@[simp] theorem choose_zero_right (n : Nat) : choose n 0 = 1 := by
  cases n <;> rfl

@[simp] theorem choose_zero_succ (k : Nat) : choose 0 (k + 1) = 0 := rfl

@[simp] theorem choose_succ_succ (n k : Nat) :
    choose (n + 1) (k + 1) = choose n k + choose n (k + 1) := rfl

@[simp] theorem E_zero (c : Nat) : E c 0 = 1 := by
  simp [E]

@[simp] theorem b_zero (c : Nat) : b c 0 = 0 := rfl

@[simp] theorem b_succ (c k : Nat) : b c (k + 1) = choose c k := rfl

@[simp] theorem H_coeff (c k : Nat) :
    H c k = E c k + xMul (fun j => choose c j) k := rfl

theorem logConcaveAt_unfold (p : Seq) (k : Nat) :
    logConcaveAt p k = (p k * p k >= p (k - 1) * p (k + 1)) := rfl

end Erdos993
