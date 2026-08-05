# Chebyshev-tail diagnostics

This research module studies finite, reproducible diagnostics of the Chebyshev
tail `E(x) = psi(x) - x`, where `psi(x) = sum_{p^k <= x} log p`.  It is a
numerical exploration of the prime-zero explicit formula, not a proof or a
disproof of the Riemann Hypothesis (RH).

## What the module does

- computes `psi(x)` exactly from prime powers for a finite integer range;
- forms raw and windowed tail diagnostics;
- displays the generic fourfold symmetry orbit associated with a hypothetical
  off-critical zero;
- uses Fibonacci as a solved control example for a two-root linear recurrence;
- records every output as an experiment with finite scope.

## What it does not do

- infer the location of every zeta zero from five samples or five primes;
- use the Euler product in the critical strip as a convergent representation;
- infer prime gaps, Chebyshev bias, GUE statistics, or an RH conclusion from a
  tail plot;
- associate nontrivial zeros geometrically with trivial zeros `-2,-4,...`.

## Reproduce

```powershell
python simulations/chebyshev_tail.py --max-x 20000 --out research/chebyshev_tail
python -m pytest -q tests/test_chebyshev_tail.py
```

The generated report and figures label every computation as finite numerical
evidence.  See `docs/claim-boundary.md` and `paper/tail_diagnostics.tex`.
