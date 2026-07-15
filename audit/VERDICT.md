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
