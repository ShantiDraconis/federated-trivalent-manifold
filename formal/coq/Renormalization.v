From Coq Require Import Arith Lia ZArith.

Definition cutoff (N n : nat) : nat := if n <? N then 1 else 0.

Theorem cutoff_idempotent : forall N n,
  (cutoff N n * cutoff N n = cutoff N n)%nat.
Proof.
  intros N n. unfold cutoff.
  destruct (n <? N); simpl; reflexivity.
Qed.

Definition drift_scaled (e : nat) : Z :=
  - Z.of_nat (21774 * e + 1000).

Theorem drift_scaled_negative : forall e, (drift_scaled e < 0)%Z.
Proof.
  intros e. unfold drift_scaled.
  assert (H : (0 < Z.of_nat (21774 * e + 1000))%Z).
  { rewrite Nat2Z.inj_add. simpl. lia. }
  lia.
Qed.

Definition equilibrium_numerator : Z := -1000.

Theorem equilibrium_numerator_negative : (equilibrium_numerator < 0)%Z.
Proof. unfold equilibrium_numerator. lia. Qed.

(* The exact rational equilibrium is -1000/21774 in the common scaled units. *)
