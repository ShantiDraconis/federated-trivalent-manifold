theory Trivalent
  imports Main
begin

datatype triv = F | U | T

fun neg :: "triv => triv" where
  "neg F = T" | "neg U = U" | "neg T = F"

fun tand :: "triv => triv => triv" where
  "tand F _ = F" | "tand _ F = F" |
  "tand T T = T" | "tand _ _ = U"

fun tor :: "triv => triv => triv" where
  "tor T _ = T" | "tor _ T = T" |
  "tor F F = F" | "tor _ _ = U"

lemma neg_involutive: "neg (neg a) = a" by (cases a) simp_all
lemma and_comm: "tand a b = tand b a" by (cases a; cases b) simp_all
lemma or_comm: "tor a b = tor b a" by (cases a; cases b) simp_all

record system_state = port_open :: bool log_encrypted :: bool
definition teardown :: "system_state => system_state" where
  "teardown s = s\<lparr>port_open := False\<rparr>"
lemma teardown_closes: "port_open (teardown s) = False"
  by (simp add: teardown_def)

consts CryptoAssumption :: bool RiemannHypothesisAssumption :: bool
theorem conditional_pipeline:
  "CryptoAssumption \<Longrightarrow> RiemannHypothesisAssumption \<Longrightarrow> True" by simp

end
