# Formalização cruzada

| Sistema | Arquivo | Estado local |
|---|---|---|
| Lean 4 + Mathlib | `FederatedTrivalent/Epistemic.lean` | compilado por `lake env lean` |
| Coq | `formal/coq/HMOS_Epistemic.v` | fonte; requer Coq para verificação |
| Isabelle/HOL | `formal/isabelle/HMOS_Epistemic.thy` | fonte; requer Isabelle para verificação |

As traduções expressam deliberadamente um núcleo pequeno e comparável. RH, BSD
e GUE não são declaradas como axiomas globais. Uma teoria que precise delas deve
recebê-las como hipóteses locais, de modo que a dependência apareça no tipo do
teorema.

O resultado de liveness é discreto: uma carga não negativa somada a um regulador
estritamente positivo aumenta o contador. Isso não demonstra disponibilidade de
rede, segurança criptográfica, ausência de starvation do escalonador ou qualquer
conjectura matemática externa.
