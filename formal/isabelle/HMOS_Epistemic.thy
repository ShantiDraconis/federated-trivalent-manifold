theory HMOS_Epistemic
  imports Complex_Main
begin

datatype epistemic_status =
    Proved | Refuted | Conditional | Bounded
  | SpecialCase | IndependentFrom | Empirical | Open

record evidence_record =
  claim :: string
  status :: epistemic_status
  assumptions :: "string list"
  certificate :: "string option"
  verifier :: "string option"

definition epsilon :: real where
  "epsilon = 1 / 1000000"

definition w_step :: "real ⇒ real ⇒ real" where
  "w_step w load = w + load + epsilon"

lemma epsilon_positive: "0 < epsilon"
  unfolding epsilon_def by simp

lemma w_step_strict:
  assumes "0 ≤ load"
  shows "w < w_step w load"
  using assms epsilon_positive unfolding w_step_def by linarith

lemma truth_has_no_half_state: "P ∨ ¬ P"
  by blast

lemma conditional_transport:
  assumes "H ⟹ P" and H
  shows P
  using assms by blast

text ‹RH, GUE e BSD permanecem premissas locais explicitamente declaradas.›

end

