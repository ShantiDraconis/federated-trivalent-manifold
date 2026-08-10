From Coq Require Import Arith Lia.

Definition step (w score : nat) : nat :=
  w + S (score * score).

Theorem step_strictly_grows :
  forall w score, w < step w score.
Proof.
  intros w score.
  unfold step.
  lia.
Qed.

(* No theorem here states network availability, security, or DoS immunity. *)
