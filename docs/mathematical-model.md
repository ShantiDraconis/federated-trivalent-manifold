# Mathematical model and epistemic boundary

## State space

The calculator uses the real coordinate tuple `p=(x,y,z,t,e)`. The notation
`x,y,z,t,i e` means that only the accumulated action's exodus contribution is
imaginary; it does not turn the base space into a proven five-dimensional
manifold in the differential-geometric sense.

For an explicitly selected differentiable path `gamma`, the illustrative action
is

`S[gamma] = integral L(gamma(t), gamma'(t)) dt + i integral e(t) dt`.

The default numerical example chooses

`L(t) = 1 + alpha t^2 - beta e(t)^2` and
`e(t) = A sin(pi t/T)`.

These are definitions of a toy model. Euler-Lagrange equations become relevant
only after a suitable function space, boundary conditions and differentiability
assumptions have been stated. A derivative is not generally "equal to an
integral"; the fundamental theorem of calculus relates them under hypotheses.

## Truth status

Strong Kleene K3 is used as an information algebra:

- `F`: refuted in the selected theory;
- `U`: not decided in the selected theory;
- `T`: proved in the selected theory.

The law of excluded middle need not evaluate to `T` for `U`. This is a semantic
choice for the calculator, not a replacement for classical mathematics.

## Comparison

Connection scores are Jaccard similarities of declared feature sets. They are
auditable metadata, not discovered reductions between Millennium problems.
A mathematical reduction requires explicit maps and proofs preserving the
relevant structures.
