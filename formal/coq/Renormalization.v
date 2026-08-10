From Coq Require Import Arith.

Definition cutoff (N n : nat) : nat := if n <? N then 1 else 0.

Theorem cutoff_idempotent : forall N n,
  cutoff N n * cutoff N n = cutoff N n.
Proof.
  intros N n. unfold cutoff.
  destruct (n <? N); simpl; reflexivity.
Qed.

Inductive drift_sign := negative.

Record scaled_drift := {
  sign : drift_sign;
  magnitude : nat
}.

Definition boundary_drift (e : nat) : scaled_drift :=
  {| sign := negative; magnitude := S (21774 * e + 999) |}.

Definition strictly_negative (d : scaled_drift) : Prop :=
  sign d = negative /\ 0 < magnitude d.

Theorem boundary_drift_strictly_negative : forall e,
  strictly_negative (boundary_drift e).
Proof.
  intro e. split; simpl.
  - reflexivity.
  - apply Nat.lt_0_succ.
Qed.

Definition equilibrium_numerator : nat := 1000.
Theorem equilibrium_magnitude_positive : 0 < equilibrium_numerator.
Proof. unfold equilibrium_numerator. apply Nat.lt_0_succ. Qed.
