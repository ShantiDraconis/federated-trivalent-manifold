From Coq Require Import Reals Lra Classical_Prop String List.
Open Scope R_scope.

Inductive EpistemicStatus : Type :=
| Proved | Refuted | Conditional | Bounded
| SpecialCase | IndependentFrom | Empirical | Open.

Record EvidenceRecord : Type := mkEvidence {
  claim : string;
  status : EpistemicStatus;
  assumptions : list string;
  certificate : option string;
  verifier : option string
}.

Definition epsilon : R := / 1000000.
Definition w_step (w load : R) : R := w + load + epsilon.

Theorem epsilon_positive : 0 < epsilon.
Proof. unfold epsilon; apply Rinv_0_lt_compat; lra. Qed.

Theorem w_step_strict : forall w load : R,
  0 <= load -> w < w_step w load.
Proof. intros w load Hload; unfold w_step; unfold epsilon; lra. Qed.

Theorem truth_has_no_half_state : forall P : Prop, P \/ ~ P.
Proof. apply classic. Qed.

Theorem conditional_transport : forall H P : Prop,
  (H -> P) -> H -> P.
Proof. intros H P HP HH; exact (HP HH). Qed.

(* RH, GUE e BSD devem entrar como hipóteses de seções específicas, nunca como
   axiomas globais ocultos. Este arquivo não declara nenhuma delas. *)
