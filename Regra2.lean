-- Regra 2: Princípio da Cifração do Êxodo
-- Erro original: log em texto puro com scrcpy/ffmpeg
-- Lei gerada: "Todo êxodo imaginário i·e(t) deve ser cifrado antes de persistir"
-- Comportamento: e = dados sensíveis, se e ≠ "" então Encrypt(e) obrigatório

/-- Tipo opaco para chaves criptográficas (AES-GCM-256). -/
opaque Key : Type

/-- Tipo opaco para logs cifrados. -/
opaque EncryptedLog : Type

/-- Primitiva de cifração — AES-GCM-256 abstracta.
    A implementação concreta é opaca; as propriedades são garantidas pelos axiomas abaixo. -/
opaque aes_gcm_256 : Key → String → EncryptedLog

/-- Regra 2 — Cifração do Êxodo:
    Dado um log e uma chave, produz o log cifrado correspondente. -/
def Regra2_LogCifrado (log : String) (k : Key) : EncryptedLog :=
  aes_gcm_256 k log

/-- Predicado: um log é sensível quando não está vazio. -/
def isSensitive (log : String) : Prop := log ≠ ""

/-- Axioma de injetividade de chave:
    Chaves distintas produzem textos cifrados distintos para o mesmo log. -/
axiom aes_gcm_256_key_inj (log : String) (k1 k2 : Key) :
    k1 ≠ k2 → aes_gcm_256 k1 log ≠ aes_gcm_256 k2 log

/-- Regra 2 — Existência da cifração:
    Para qualquer log sensível, existe exatamente um EncryptedLog produzido pela
    função Regra2_LogCifrado com a chave k. -/
theorem Regra2_ExistenciaCifracao (log : String) (k : Key)
    (_ : isSensitive log) :
    ∃ e : EncryptedLog, e = Regra2_LogCifrado log k :=
  ⟨Regra2_LogCifrado log k, rfl⟩

/-- Princípio de obrigatoriedade: todo log sensível que persiste deve ser
    representável como a cifração de algum log em claro.
    Modelado como tipo-dependente: PersistidoSeguros carrega a prova de origem. -/
structure PersistidoSeguro where
  log_original : String
  chave        : Key
  encrypted    : EncryptedLog
  is_image     : encrypted = Regra2_LogCifrado log_original chave

/-- Construção canônica de um PersistidoSeguro. -/
def persistir_seguro (log : String) (k : Key) : PersistidoSeguro :=
  { log_original := log,
    chave        := k,
    encrypted    := Regra2_LogCifrado log k,
    is_image     := rfl }
