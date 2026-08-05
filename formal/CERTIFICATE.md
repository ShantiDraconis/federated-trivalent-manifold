# Formal build certificate

Certificate scope: checker acceptance of the versioned Lean modules only.
This is not a proof certificate for any Millennium Prize Problem, physical
theory, cryptographic security property, or operational availability claim.

## Successful local verification

- Date: 2026-07-15 (America/Sao_Paulo)
- Lean: 4.8.0, commit `df668f00e6c0`
- Lake: 5.0.0-df668f0
- Mathlib: tag `v4.8.0`, commit `b5eba595428809e96f3ed113bc7ba776c5f801ac`
- Command: `lake build`
- Result: `Build completed successfully.`
- Python: 18 tests passed
- Ruff: all checks passed
- `sorry`/`admit` in Lean sources: none
- Explicit assumptions: `CryptoAssumption`, `RiemannHypothesisAssumption`

## Verified theorem boundary

The checker accepts finite K3 truth-table laws, coordinate preservation and
non-increase under explicit domains, non-decrease of a defined accumulator,
positivity of the defined regulated scalar rate, an algebraic derivative
identity, strict monotonicity of an affine clock, cardinality of a finite
truncation projector, correctness of a Boolean threshold indicator, and two
elementary properties of a declared linear-flow closed form.

It does not accept or contain proofs of RH, P versus NP, Navier-Stokes,
Yang-Mills mass gap, Hodge, BSD, black-hole information preservation, a
unification of the seven problems, or empirical performance/security.

## SHA-256 source ledger

```text
AnomalyKernel.lean 992051247A42043CDA00441ADC8609D3CEF4B7C79BB9BCA3063D8D38225B18BF
FiniteScale.lean D35A40814362BF0876BF9C662B031894B8337CF49F7950178115218C2E35D1F2
FlowOperators.lean 4DA242B57D3EF986C90AA8330356AC5EAF20B7C351306F2AE5881E5745E9A686
Model.lean 94A2CB3BB1013322C29344270A46CE230A076E0CB22F77C7D574F896E4ED5B58
Trivalent.lean 7DAAFE3684215486696F44C90F6960793D75456061CB43B0ADE0A43DB509D4B0
lakefile.lean FF77B7F26E779E828E9C23AA4BC26BEC7BD656C944395786A9E7D031BD35FE8F
lean-toolchain 0DF6875BFD9A61FC67FB394183802C10D10D54E5D0B3FFCB4804055CB2E76BC3
lake-manifest.json AF69E9ADE9AF90C3B2FC784F9E4D91572D9CB92504725FCED44396F8A23BBC06
```

The GitHub workflow repeats the Lean build on every push and pull request.
