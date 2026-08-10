import Lake
open Lake DSL

package «federated-trivalent-manifold» where

lean_lib Trivalent where
  srcDir := "."

lean_lib Model where
  srcDir := "."

lean_lib AnaliseTanhParaH1 where
  srcDir := "../../ANALISE_TANH_PARA_H1"
