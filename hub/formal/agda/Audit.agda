module Audit where

open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.List using (List; []; _∷_)

data Status : Set where
  proved finite-certificate conditional equivalent conjectural refuted open : Status

automatic : Status → Bool
automatic proved = true
automatic conditional = true
automatic finite-certificate = false
automatic equivalent = false
automatic conjectural = false
automatic refuted = false
automatic open = false

finite-not-automatic : automatic finite-certificate ≡ false
finite-not-automatic = refl

open-not-automatic : automatic open ≡ false
open-not-automatic = refl

data AllProved : List Status → Set where
  all[] : AllProved []
  all∷ : ∀ {tail} → AllProved tail → AllProved (proved ∷ tail)

record Node : Set where
  constructor node
  field
    status : Status
    dependencies : List Status

safeBase : Node
safeBase = node proved []
