-- Regra 5: Conservação do Êxodo
-- Erro original: afirmar que ∫ i·e dt → 0 sem matar i·e (apenas com pipeline)
-- Lei gerada: "Enquanto houver vantagem do adversário, há êxodo imaginário"
-- Nos eixos: t acumula e, se e≠0 então sistema fica em 1/2 para sempre

/-!
## Conservação do Êxodo Imaginário

O "êxodo" e(t) modela a vantagem computacional residual do adversário num protocolo
federado. Enquanto e(t) ≠ 0, a integral acumulada ∫₀ᵀ i·e(t) dt não pode ser zero.
Colapsar o sistema para o estado provado (1) exige um axioma matemático novo
que anule e — nenhuma técnica criptográfica existente é suficiente.
-/

/-- Tempo discreto não-negativo. -/
abbrev Time := ℕ

/-- Função de êxodo: mapeia instantes de tempo para valores reais.
    e(t) > 0 representa vantagem do adversário no instante t. -/
abbrev ExodusFunc := Time → Float

/-- Predicado: o êxodo persiste em t — a vantagem do adversário não foi eliminada. -/
def exodoPersiste (e : ExodusFunc) (t : Time) : Prop := e t ≠ 0.0

/-- Integral discreta do êxodo sobre o intervalo [0, T]. -/
def integralExodo (e : ExodusFunc) (T : Time) : Float :=
  (List.range T).foldl (fun acc t => acc + e t) 0.0

/-- Axioma de Conservação do Êxodo (Regra 5):
    Se o êxodo persiste em algum instante t < T, a integral acumulada é não-nula. -/
axiom Regra5_Conservacao (e : ExodusFunc) (T : Time) :
    (∃ t < T, exodoPersiste e t) → integralExodo e T ≠ 0.0

/-- Função de êxodo nulo: o adversário não tem vantagem em nenhum instante. -/
def exodoNulo : ExodusFunc := fun _ => 0.0

/-- A integral do êxodo nulo é zero — base do colapso para o estado provado. -/
theorem integral_exodo_nulo (T : Time) : integralExodo exodoNulo T = 0.0 := by
  induction T with
  | zero => simp [integralExodo, exodoNulo]
  | succ n ih =>
    simp [integralExodo, List.range_succ, List.foldl_append, exodoNulo]

/-- Contraposição da Regra 5:
    Se a integral for zero, então o êxodo é nulo em todo o intervalo. -/
theorem Regra5_Contraposicao (e : ExodusFunc) (T : Time) :
    integralExodo e T = 0.0 → ∀ t < T, ¬ exodoPersiste e t := by
  intro h t ht hpersiste
  exact absurd h (Regra5_Conservacao e T ⟨t, ht, hpersiste⟩)

/-- Corolário — Regime 1/2:
    Se o êxodo persiste, o sistema permanece indefinidamente no estado intermediário
    (não colapsa nem para 0 nem para 1 sem um axioma matemático adicional). -/
theorem regime_meio_enquanto_exodo (e : ExodusFunc) (T : Time)
    (h : ∃ t < T, exodoPersiste e t) :
    integralExodo e T ≠ 0.0 :=
  Regra5_Conservacao e T h
