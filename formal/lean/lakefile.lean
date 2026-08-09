import Lake
open Lake DSL

package «federated-trivalent-manifold» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.8.0"

lean_lib Trivalent where
  srcDir := "."

lean_lib Model where
  srcDir := "."

lean_lib NavierStokesScaffold where
  srcDir := "."
