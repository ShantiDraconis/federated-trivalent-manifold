theory WMonotone
  imports Main
begin

definition step :: "nat => nat => nat" where
  "step w score = w + (score * score + 1)"

theorem step_strictly_grows:
  "w < step w score"
  unfolding step_def by simp

text "This arithmetic theorem has no network or security conclusion."

end
