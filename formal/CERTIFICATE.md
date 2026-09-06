# Scoped formal build record

This record is a reproducibility note, not a certificate for a Millennium Prize
Problem. It supersedes the earlier repository-wide wording: the repository now
contains exploratory files with explicit axioms and `sorry` placeholders, so a
claim that all Lean sources are hole-free would be false.

## Locally checked finite Lean core

- Date: 2026-08-10 (Europe/Warsaw)
- Lean: 4.8.0 / Mathlib v4.8.0
- Command: `lake build` from `formal/lean`
- Scope: `RadialGeometry.lean`, `FiniteEvidence.lean`, and the package targets
  configured by Lake
- Result: successful local build before the remote integration; re-run required
  after any source or dependency change
- Placeholder scan for the declared core: no `sorry`, `admit`, `Axiom`, or
  `postulate`

The source list and checker boundary are maintained in
[`VERIFIED_CORE.md`](VERIFIED_CORE.md). The excluded sources and their precise
unclosed obligations are maintained in
[`OPEN_OBLIGATIONS.md`](OPEN_OBLIGATIONS.md).

## Excluded claims

This record does not prove or refute the Riemann hypothesis, P versus NP,
Navier--Stokes existence and smoothness, Yang--Mills mass gap, Hodge, BSD,
cryptographic security, network availability, or any claimed unification of
those subjects. A plot, finite scan, numerical truncation, or natural-event
timestamp is not proof evidence for such a claim.
