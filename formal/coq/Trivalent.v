Inductive Triv : Type := F | U | T.

Definition neg (a : Triv) : Triv :=
  match a with F => T | U => U | T => F end.

Definition tand (a b : Triv) : Triv :=
  match a, b with
  | F, _ | _, F => F
  | T, T => T
  | _, _ => U
  end.

Definition tor (a b : Triv) : Triv :=
  match a, b with
  | T, _ | _, T => T
  | F, F => F
  | _, _ => U
  end.

Theorem neg_involutive : forall a, neg (neg a) = a.
Proof. destruct a; reflexivity. Qed.

Theorem and_comm : forall a b, tand a b = tand b a.
Proof. destruct a, b; reflexivity. Qed.

Theorem or_comm : forall a b, tor a b = tor b a.
Proof. destruct a, b; reflexivity. Qed.

Record SystemState := { port_open : bool; log_encrypted : bool }.
Definition teardown (s : SystemState) : SystemState :=
  {| port_open := false; log_encrypted := log_encrypted s |}.
Theorem teardown_closes : forall s, port_open (teardown s) = false.
Proof. intros; reflexivity. Qed.

Axiom CryptoAssumption : Prop.
Axiom RiemannHypothesisAssumption : Prop.
Theorem conditional_pipeline : CryptoAssumption -> RiemannHypothesisAssumption -> True.
Proof. intros; exact I. Qed.
