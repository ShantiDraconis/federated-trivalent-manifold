# Open obligations and excluded modules

The following files are **not** part of the verified finite core. They contain
either explicit assumptions, `sorry` placeholders, or intentionally impossible
axioms such as a declaration of `False`. They are retained as research notes so
that the gap is visible rather than hidden.

| File | Reason excluded | What it cannot establish |
|---|---|---|
| `lean/Behaviors.lean` | contains a `sorry` and declared rate assumptions | convergence claim beyond its stated assumptions |
| `lean/NumeroComComportamento.lean` | contains a `sorry` and axioms labelled Clay-level | RH, Navier--Stokes, or P versus NP |
| `lean/Lemas_Master.lean` | declares implications from an axiom of `False` | any mathematical result about the proposed model |
| `coq/Lemas_Master.v` | declares `Axiom ... : False` | any theorem relying on those axioms |
| `isabelle/Lemas_Master.thy` | contains analogous undeveloped assumptions | any theorem relying on them |
| `lean/Model.lean`, `coq/Trivalent.v` | explicitly assume cryptographic/RH propositions | unconditional security or RH |
| `lean/PvsNP_ComoNumeros.lean` | declares an unknown P-versus-NP Boolean | a result on P versus NP |

## Required proof obligations for an RH claim

No entry in this repository currently provides any of the following:

1. a non-circular prime-side representation whose positivity does not use RH;
2. a Hilbert-space factorization of the Weil form constructed independently of
   its desired positivity; or
3. a complete, certified family of finite Gram matrices plus a density and
   continuity argument proving positivity on the full test space.

Finite zero samples, finite Dirichlet-eta truncations, and plots are
experimental diagnostics only. A hypothetical high off-line zero may be
invisible to a fixed finite computation; absence from a finite scan is not a
universal statement.

## Certificate rule

Any future certificate must name the exact source list, tool versions, command,
and result. It must never summarize the whole repository as `0 sorry` while an
excluded module has a placeholder or axiom. This rule is enforced for the
declared finite core by `tests/test_formal_integrity.py`.
