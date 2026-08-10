theory Renormalization
  imports Main
begin

definition cutoff :: "nat => nat => nat" where
  "cutoff N n = (if n < N then 1 else 0)"

lemma cutoff_idempotent:
  "cutoff N n * cutoff N n = cutoff N n"
  by (simp add: cutoff_def)

definition drift :: "real => real" where
  "drift e = -0.21774 * e - 0.01"

lemma drift_negative:
  assumes "0 <= e"
  shows "drift e < 0"
  using assms by (simp add: drift_def)

definition equilibrium :: real where
  "equilibrium = -0.01 / 0.21774"

lemma equilibrium_negative: "equilibrium < 0"
  by (simp add: equilibrium_def)

end
