# Formal artefacts

The files prove only finite truth-table properties and the abstract state update
for teardown. They deliberately do not formalize the deep mathematics required
by the Millennium problems.

| Directory | Intended checker | Unproved assumptions |
|---|---|---|
| `lean/` | Lean 4.8 | Crypto and RH propositions |
| `coq/` | Coq | Crypto and RH propositions |
| `isabelle/` | Isabelle/HOL | Uninterpreted Boolean assumptions |
| `agda/` | Agda | None in the K3 truth-table module |

An assumption is not a `sorry`: it is part of the theory's trusted input. This
does not make the assumed proposition a theorem of ordinary mathematics.
