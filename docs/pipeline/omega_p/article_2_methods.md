# Article 2 — Computational Methods and Reporting Rules

## Scope
Companion note for `docs/pipeline/omega_p/article_2_finite_confinement.tex`.
It defines operational numerical procedures and mandatory reporting for constants in Article 2.

## Constants and status

| Constant | Definition status | In Article 2 |
|---|---|---|
| `C_avg` | closed form `1/2 + 1/pi` | proved |
| `C1` | root of `f1(x)-f1'(x)=0` | proved existence/uniqueness + approximated |
| `C3` | root of `f2(x)-f2'(x)=0` | proved existence/uniqueness + approximated |
| `C5` | root of `favg(x)-favg'(x)=0` | proved existence/uniqueness + approximated |
| `C2, C4, C6` | defining equations deferred | not proved |

## Deterministic numerical protocol

1. Choose a closed interval `[a,b]` such that `h(a)*h(b) < 0`.
2. Run bisection until the half-interval width `(b-a)/2` is below tolerance `tol`.
3. Return midpoint as approximation and report:
   - interval used,
   - tolerance,
   - iteration count,
   - absolute residual `|h(x*)|`.

### Minimal reference implementation (Python standard library)

```python
import math

def bisect(fn, a, b, tol=1e-12, it=200):
    fa, fb = fn(a), fn(b)
    if fa * fb >= 0:
        raise ValueError("interval does not bracket a root")
    for _ in range(it):
        m = (a + b) / 2.0
        fm = fn(m)
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
        if (b - a) / 2.0 < tol:
            break
    return (a + b) / 2.0
```

## Reporting requirements

Every manuscript version must include:

- exact analytic equation being solved;
- proof obligation status (proved / conditional / conjectural);
- interval and algorithm parameters;
- precision and error metric;
- whether the value is theorem-level or only numerical evidence.

## Non-negotiable boundary

Numerical approximation is **not** a proof of broader claims (e.g., RH or universal residue principles).
Any bridge to those claims requires independent formal theorems.
