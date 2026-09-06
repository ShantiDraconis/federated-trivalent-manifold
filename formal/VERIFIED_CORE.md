# Verified finite core

This is the only scope that may be described as a no-placeholder formal core.
It is intentionally modest: it proves finite algebraic and discrete facts, not
an open problem in mathematics or complexity theory.

| Prover | File | Checked statement class | Placeholder policy |
|---|---|---|---|
| Lean | `lean/RadialGeometry.lean` | identities for reflected squared radii; non-negativity of `delta^2`; conditional non-negativity of a quotient under a positive denominator | no `sorry`, `admit`, or axiom |
| Lean | `lean/FiniteEvidence.lean` | a delayed Boolean witness can agree on a finite prefix and differ after its cutoff | no `sorry`, `admit`, or axiom |
| Coq | `coq/WMonotone.v` | a natural-number update grows strictly | no `Admitted` or `Axiom` |
| Coq | `coq/Renormalization.v` | a finite cutoff is idempotent; a syntactic drift record has positive magnitude | no `Admitted` or `Axiom` |
| Isabelle/HOL | `isabelle/WMonotone.thy` | the corresponding natural-number update grows | no `sorry` or `axiomatization` |
| Isabelle/HOL | `isabelle/Renormalization.thy` | finite cutoff/drift facts | no `sorry` or `axiomatization` |
| Agda | `agda/WMonotone.agda` | constructive witness for one-step natural-number growth | no `postulate` |

## Mathematical boundary

For a hypothetical reflected pair written
`1/2 + delta + i gamma` and `1/2 - delta + i gamma`, the Lean core proves the
finite identities

\[
R_c^2=\gamma^2+\tfrac14,\quad
R_+^2=R_c^2+\delta+\delta^2,\quad
R_-^2=R_c^2-\delta+\delta^2,
\]

\[
\frac{R_+^2-R_-^2}{2}=\delta,\qquad
\frac{R_+^2+R_-^2}{2}-R_c^2=\delta^2\ge0.
\]

These identities apply to supplied real parameters. They do **not** establish
that a zeta zero exists, locate a zeta zero, or imply the Riemann hypothesis.
Likewise, a finite cutoff theorem says nothing about the asymptotic equality or
separation of complexity classes.

## Reproduction commands

```powershell
Set-Location formal/lean
lake build

coqc ../coq/WMonotone.v
coqc ../coq/Renormalization.v

Set-Location ../agda
agda WMonotone.agda
```

Isabelle sources are included for portability; their local checking requires a
separately installed Isabelle distribution. The repository must not claim that
an unavailable checker was run.
