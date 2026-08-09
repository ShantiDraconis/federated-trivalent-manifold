# Formal boundary for the anomaly kernel

This repository is a classical hypothesis-management and specification
experiment. It is not a proposed Riemann-hypothesis solution, a quantum
computer, or a CMI-certified system. CMI does not certify such frameworks or
accept direct submissions; its prize rules concern qualifying publication,
elapsed time, and general acceptance of a proposed solution.

## Exact mathematics versus computation

For `Re(s)>0`, `eta(s)=sum_(n>=1) (-1)^(n-1)n^(-s)`. In the open critical strip
`0<Re(s)<1`, `1-2^(1-s)` is nonzero, so eta and zeta have the same zeros. The
domain restriction matters because the prefactor has zeros on `Re(s)=1`.

The exact observable `delta(s)=|Re(s)-1/2| 1_{zeta(s)=0}` is not a computable
detector as written: its indicator requires an exact zero witness. The finite
implementation returns `CERTIFIED_NONZERO` when `|eta_N(s)|` exceeds the bound

```text
|eta(s)-eta_N(s)| <= (N+1)^(-sigma) * (1 + |s|/sigma), sigma=Re(s)>0,
```

and `INCONCLUSIVE` otherwise. It never promotes a small finite sum to a zero.
The bound follows from summation by parts and the unit bound on partial sums of
the alternating signs.

## Corrected differential model

For `q=alpha*t^2-beta*e^2` and `S2=q^2`,

```text
partial S2 / partial e = -4*beta*e*(alpha*t^2-beta*e^2),
de/dt = 4*Gamma*beta*e*(alpha*t^2-beta*e^2) - chi*delta.
```

This is not globally damping: at `delta=0`, its sign changes with `q`. Stability
needs a separate Lyapunov argument and a specified parameter domain.

The verified positive model rate is `dW/dt=S2+epsilon`, `epsilon>0`. The
alternative `S2+10^-6*t+e` is zero at the origin, so it is not unconditionally
strictly positive. Lean proves a scalar rate property and affine-clock lemma,
not scheduling, availability, bounded latency or DoS resistance.

## Operational boundary

`INCONCLUSIVE` is never evidence of an off-line zero. Isolation may be driven
by ordinary telemetry thresholds, but that is policy, not a refutation. FIPS
197 specifies AES-128, AES-192 and AES-256 with 128-bit blocks. No Rijndael-512
or quantum implementation is included. Reproducible records need inputs,
precision, term count, error bound, status, software version and source digest.
