# Formal artefacts

This directory contains two deliberately different kinds of material. They
must not be conflated.

1. **Verified finite core.** Elementary finite/algebraic lemmas are listed in
   [`VERIFIED_CORE.md`](VERIFIED_CORE.md). Those files contain no `sorry`,
   `admit`, `Axiom`, or `postulate` declaration.
2. **Conditional and exploratory models.** Other files introduce assumptions,
   open placeholders, or experimental encodings. They are not proof artefacts
   for a Millennium Prize Problem. Their exact status is in
   [`OPEN_OBLIGATIONS.md`](OPEN_OBLIGATIONS.md).

| Prover | Checked finite core | Local status recorded here |
|---|---|---|
| `lean/` | Lean 4.8 / Mathlib | `RadialGeometry.lean`, `FiniteEvidence.lean`, `NavierStokesScaffold.lean` |
| `coq/` | Coq | `WMonotone.v`, `Renormalization.v` |
| `isabelle/` | Isabelle/HOL | `WMonotone.thy`, `Renormalization.thy` |
| `agda/` | Agda | `WMonotone.agda` |

No finite computation, diagram, truncation rule, eclipse datum, or cross-domain
analogy in this repository proves or refutes RH, P versus NP, Navier--Stokes,
Yang--Mills, Hodge, or BSD. A declared assumption remains an assumption; a
machine checker only establishes the conclusion relative to that assumption.

The Lean file `lean/NavierStokesScaffold.lean` adds a conservative scaffold for
kinetic-energy monotonicity: it formalizes what follows from an externally
provided antitone energy witness, but it does not claim a proof of global
regularity, Beale-Kato-Majda, or any Clay Millennium result.
