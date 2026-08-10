module WMonotone where

open import Agda.Builtin.Equality
open import Agda.Builtin.Nat

record Grows (old new : Nat) : Set where
  constructor growth
  field
    delta : Nat
    equation : new ≡ suc (old + delta)

step : Nat → Nat → Nat
step w score = suc (w + (score * score))

step-grows : (w score : Nat) → Grows w (step w score)
step-grows w score = growth (score * score) refl
