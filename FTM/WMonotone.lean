import Std.Tactic.Omega

namespace FTM.WMonotone

def step (w score : Nat) : Nat :=
  w + (score * score + 1)

theorem step_strictly_grows (w score : Nat) :
    w < step w score := by
  unfold step
  omega

/-- This theorem has no claim about networks, availability, security, or DoS. -/
theorem positive_delta (w score : Nat) :
    0 < step w score - w := by
  unfold step
  omega

end FTM.WMonotone
