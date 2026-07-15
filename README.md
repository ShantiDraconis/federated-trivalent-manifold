# Federated Trivalent Manifold

Programa de pesquisa para estruturas trivalentes locais, sua colagem em objetos globais e possíveis interfaces rigorosas com os Problemas do Milênio.

> **Estado científico:** este repositório não reivindica a solução de nenhum Problema do Milênio. Uma conexão só é tratada como matemática quando há definições, enunciado formal e prova auditável; o restante é rotulado como programa, conjectura ou analogia.

## Documentos

- [Fundamentos](docs/fundamentos.md): objeto básico, morfismos, federação e consistência.
- [Matriz dos Problemas do Milênio](docs/matriz-milenio.md): análise problema a problema e obrigações de prova.
- [Roadmap](docs/roadmap.md): resultados mínimos e critérios de falsificação.

O nome do projeto não determina uma teoria. A definição inicial é provisória e torna afirmações testáveis. As formulações oficiais são as do [Clay Mathematics Institute](https://www.claymath.org/millennium-problems/).

## Modelo computacional reproduzível

O repositório inclui agora uma camada experimental independente da documentação
conjectural:

- `gateway_model/`: equação `S = αt² - βe²` e funções puras;
- `gateway/main_v4.py`: controlador operacional com domínio validado;
- `FederatedTrivalent/FlowOperators.lean`: operadores e cirurgia construtiva;
- `GatewayModel/Classes.lean`: identidades exatas em números racionais;
- `tests/`: testes numéricos, de domínio e de integridade da formalização;
- `outputs/`: artigo, dados JSON e figuras reproduzíveis;
- `scripts/`: geração determinística dos resultados e do artigo.

### Resultados verificados

Com as latências informadas, `t_total = 3.155 s`, `S_eff = 0.9856042` e
`β_crit = 11.06002778`. Portanto, o exemplo `α=0.1, β=5` ainda é positivo:
`S_eff = 0.5454025`. A igualdade aproximada entre α e β não define equilíbrio,
porque os coeficientes multiplicam grandezas em escalas diferentes.

### Limite lógico

Este modelo prova apenas propriedades das definições declaradas. In particular,
it proves nothing about P vs NP, the Riemann hypothesis, or the Yang-Mills mass
gap. Os termos “zeta”, “gauge”, “Perelman” e “mass proxy” são analogias ou nomes
de parâmetros internos, salvo quando acompanhados de uma redução matemática
formal e auditável.

O fluxo dissipativo Lean recebe um `TimeStep` não negativo. Isso evita a falsa
afirmação de contração para tempos negativos. A cirurgia é construída com
`min e limiar`, reduzindo o êxodo sem postular que ele zera. O fluxo zeta não é
declarado como instância de preservação de energia, pois essa propriedade não
decorre de sua fórmula.

### Execução

```powershell
python -m unittest discover -s tests -v
python scripts/run_experiment.py
python scripts/build_article.py
lake update
lake build
uvicorn gateway.main_v4:app --reload
```

As figuras geradas são `outputs/action_regimes.png` e
`outputs/exodus_decay.png`; o artigo completo está em
`outputs/artigo_gateway.pdf`.

## Kubernetes e autocicatrização

`infrastructure/kubernetes/gateway.yaml` fornece três réplicas, rolling update
sem indisponibilidade, PodDisruptionBudget, probes distintas, HPA, recursos,
NetworkPolicy e execução sem privilégios. A readiness probe retira um pod em
estado de isolamento do balanceamento; a liveness probe reinicia somente um
processo realmente travado, evitando ciclos de reinício causados por carga.

O HPA usa `gateway_stress`, exposto em `/metrics`. Para funcionar no cluster,
essa métrica precisa ser registrada por Prometheus e mapeada pelo Prometheus
Adapter para `custom.metrics.k8s.io`. Sem o adapter, Kubernetes não consegue
escalar por uma métrica da aplicação; isso é uma dependência operacional, não
uma propriedade provada em Lean.

## Auditoria interdisciplinar e formalização cruzada

O núcleo epistemológico está em `FederatedTrivalent/Epistemic.lean`, com
traduções explícitas para Coq e Isabelle/HOL em `formal/`. A árvore que separa
teoremas, hipóteses abertas, evidência finita e analogias está em
`docs/EVIDENCIAS_INTERDISCIPLINARES.md`.

```powershell
python scripts/evidence_calculations.py
python -m unittest discover -s tests -v
```

O arquivo Lean é verificável pelo kernel Lean/Mathlib. As traduções Coq e
Isabelle somente podem ser marcadas como verificadas depois de compiladas nos
respectivos ambientes; a presença do texto-fonte não equivale a certificado.
