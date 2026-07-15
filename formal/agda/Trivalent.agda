module Trivalent where

data Triv : Set where
  F U T : Triv

data _≡_ {A : Set} (x : A) : A → Set where
  refl : x ≡ x

neg : Triv → Triv
neg F = T
neg U = U
neg T = F

_and_ : Triv → Triv → Triv
F and _ = F
_ and F = F
T and T = T
_ and _ = U

_or_ : Triv → Triv → Triv
T or _ = T
_ or T = T
F or F = F
_ or _ = U

neg-involutive : (a : Triv) → neg (neg a) ≡ a
neg-involutive F = refl
neg-involutive U = refl
neg-involutive T = refl

and-comm : (a b : Triv) → (a and b) ≡ (b and a)
and-comm F F = refl
and-comm F U = refl
and-comm F T = refl
and-comm U F = refl
and-comm U U = refl
and-comm U T = refl
and-comm T F = refl
and-comm T U = refl
and-comm T T = refl

or-comm : (a b : Triv) → (a or b) ≡ (b or a)
or-comm F F = refl
or-comm F U = refl
or-comm F T = refl
or-comm U F = refl
or-comm U U = refl
or-comm U T = refl
or-comm T F = refl
or-comm T U = refl
or-comm T T = refl
