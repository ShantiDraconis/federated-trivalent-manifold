# Independent numerical and logical audit of v4.1

## Reproduced

- `Seff²(0,10)=118.526769`.
- The constant-`e` integral is `0.605003007857`; adding `e(T)=0.3`
  gives `0.905003007857`.
- For `e(t)=0.3 exp(-0.2t)`, the integral is `0.617104804182`; adding
  the endpoint gives `0.776722646806`.
- The supplied divergence matrix is symmetric, has zero diagonal, lies in
  `[0,1]`, and has off-diagonal mean `0.6751333`.

## Corrected

- At `(t,e)=(3.15,0.3)`, `Seff²=0.965211342833`, not `0.9714`.
- The full matrix mean is `0.5786857`; `0.6751` excludes the diagonal.
- A quadrature with `n` samples is `O(n)`. Only one integrand evaluation is
  `O(1)` with respect to `n`.
- A microbenchmark does not establish zero end-to-end latency.
- Standard AES has 128-bit blocks and 128/192/256-bit keys; “AES-512” was
  removed.
- A monotone accumulator does not demonstrate DoS immunity, non-collapse, or
  a theorem of geometric analysis.
- `Div=1` means disjointness under the declared feature encoding, not a
  mathematical refutation or impossibility of a reduction.

## Publication status

The work is suitable as an experimental specification-calculator/software
paper after scope, provenance of the divergence matrix, benchmarks and formal
toolchain checks are completed. It is not currently evidence for a Millennium
Problem result.

## Remaining-behavior audit

- The positive-branch solution of `q(t,e)^2=1` is
  `sqrt((1+beta*e^2)/alpha)`: approximately `3.16245` for `e=0.1` and
  `3.22368` for `e=0.6`. This is a threshold of the definition, not a measured
  Quest buffer.
- The zeta alignment force is zero at `sigma=0.5` by construction. It does not
  move or constrain actual zeta zeros.
- The gauge- and complexity-inspired curves are declared decay functions and
  do not transport theorems between their source domains.
- Monotone constant, exponential and oscillating `W` profiles follow from a
  non-negative defined integrand.
- The seven reported eigenvalues cannot be independently reproduced until the
  complete source matrix is versioned. They do not match the matrix obtained as
  `1-Div` from the existing divergence table.
- The eight supplied imaginary parts have mean `30.665`, median `31.675`,
  population standard deviation about `9.4639`, sample standard deviation about
  `10.1174`, mean spacing `4.17`, and spacing coefficient of variation about
  `0.3886`.

## Anomaly-kernel boundary audit

- `1_{zeta(s)=0}` is a definition, not a computable detector. Finite evaluation
  returns certified nonzero or inconclusive.
- Eta and zeta share zeros only with the critical-strip restriction stated.
- `partial_e S2=-4*beta*e*(alpha*t^2-beta*e^2)`; the proposed e-flow is not
  globally damping.
- `S2+10^-6*t+e` vanishes at the origin. The positive-rate theorem instead uses
  `S2+epsilon`, with `epsilon>0`.
- Affine-clock monotonicity does not establish operational liveness.
- FIPS 197 does not define AES with 512-bit keys or blocks. No Rijndael-512 or
  quantum implementation is included.
