# Claim ledger for the interdisciplinary HMOS model

| Statement | Status | Reason |
|---|---|---|
| Finite truncation retains `N` coordinates | Lean-verified | `retained_card` |
| A declared threshold indicator matches `threshold <= value` | Lean-verified | finite decidable order |
| `S2 + epsilon > 0` for `epsilon > 0` | Lean-verified | square non-negativity |
| The affine clock is strictly monotone | Lean-verified | positive coefficient |
| Constant-forcing flow starts at `e0` | Lean-verified | closed-form substitution |
| Constant-forcing flow has negative asymptotic offset for `a,b>0` | Lean-verified boundary warning | shows need for barrier/projection |
| Finite eta evaluation detects exact zeros | Rejected | finite error interval is inconclusive near zero |
| `t_crit=2*pi*N/log N` is a universal Turing-Odlyzko theorem for eta truncation | Unsubstantiated | no cited theorem/error model establishing this formula |
| GUE spacing implies zeros lie on the critical line | Rejected | pair-correlation evidence does not prove RH |
| Truncating inputs makes `P=NP` | Rejected | every finite restriction is decidable; this says nothing about asymptotic classes |
| `P approximately NP` under `(epsilon,N)` | Definition only | hardware-specific cost relation, not class equality |
| Exponential search automatically becomes an `O(1)` response | Rejected | abort/lookup changes the task or assumes precomputation/storage |
| `Div=1` proves no reduction between Navier-Stokes and P/NP | Rejected | it is a chosen feature indicator |
| Eta residual generates Yang-Mills mass gap | Hypothesis/analogy | no derived map between the theories |
| All seven Millennium problems form one de Rham/sheaf geometry | Axiom proposal | no functors, objects, morphisms, equivalences or proof supplied |
| Finite eta numerator removes the pole of `eta_N/(1-2^(1-s))` | Rejected | denominator still vanishes at `s=1`; residue is `eta_N(1)/log 2` |
| `[Res,T]=-1` is a canonical operator commutator | Rejected as stated | residue and truncation act on different declared domains without a common operator algebra |
| `1/sqrt(N+1)` is the exact complex eta remainder | Rejected | it is not the general exact remainder; use a justified bound |
| `e'=-0.21774e-0.01` stays nonnegative and stabilizes at zero | Rejected | solution crosses zero and tends to a negative offset |
| `e'=-ae-b0*tanh(e)` preserves a nonnegative equilibrium | Model candidate | requires a separately verified ODE/invariance proof |
| Rijndael-512 provides a certified fallback | Rejected | not defined by FIPS 197 and not implemented |
| HMOS is CMI compliant | Rejected wording | CMI rules concern proposed solutions and qualifying publication, not framework certification |

The ledger is the authoritative boundary between checker-verified mathematics,
tested software, chosen definitions, hypotheses and rejected inferences.
