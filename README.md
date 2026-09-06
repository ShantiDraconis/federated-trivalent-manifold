# Federated Trivalent Manifold

> **Rigor boundary:** classical hypothesis-management and specification
> experiment; not a Millennium Problem solution, a quantum computer, or a
> CMI-certified system. See [`docs/rigor-boundary.md`](docs/rigor-boundary.md).

> **Estado científico:** este repositório não reivindica a solução de nenhum Problema do Milênio. Uma conexão só é matemática quando há definições, enunciado formal, redução e prova auditável; o restante é programa, conjectura, analogia ou evidência empírica.

## Núcleo formal

Calculadora de especificações condicionais para modelos trivalentes sobre o
espaço de estados `(x, y, z, t, e)`. O projeto separa rigorosamente:

- **axioma**: hipótese declarada pelo utilizador;
- **definição**: construção introduzida pelo modelo;
- **lei derivada**: consequência que requer uma derivação válida;
- **obrigação de prova**: proposição ainda não verificada;
- **teorema verificado**: resultado aceite por um proof assistant.

O projeto não prova P vs NP, a Hipótese de Riemann nem qualquer outro problema
do milénio. O valor `half` significa **indeterminado/condicional no modelo**;
não significa simultaneamente verdadeiro e falso.

- [Fundamentos](docs/fundamentos.md): objeto básico, morfismos, federação e consistência.
- [Matriz dos Problemas do Milênio](docs/matriz-milenio.md): visão comparativa.
- [Cadernos individuais](docs/problems/README.md): formalização problema por problema.
- [Molde de Poincaré](docs/poincare-method-template.md): fluxo, entropia, cirurgia, correções e ordem de desbloqueio.
- [Registro de afirmações](docs/claims-register.md): estados lógicos auditáveis.
- [Roadmap](docs/roadmap.md): resultados mínimos e critérios de falsificação.
- [Referências](docs/references.md): fontes primárias e política de citação.
- [Dados científicos e evidência](docs/scientific-data-evidence.md): taxonomias atômica, cosmológica e bioquímica, estados e operadores.
- [Esquema de observação](data/scientific-observation.schema.json): proveniência, unidade, incerteza e auditoria da ponte.

## Auditoria v4.1

- [Auditoria das alegações](AUDITORIA_v4_1.md): separa teorema, hipótese, simulação e não-alegação.
- [Fronteiras numéricas do HMOS](docs/hmos-numerical-boundaries.md): eta truncada, polo de zeta, parâmetros e pontes epistemológicas.
- AES permanece AES-256; não existe alegação de “AES-512”.
- Monotonicidade do regulador prova somente crescimento/liveness do estado interno.
- Testes são evidência de implementação, não prova de segurança ou dos Problemas do Milênio.
- A matriz `Div` é tratada como parametrização até existir uma métrica derivada e validada.

## Formalizações verificáveis

- [Lean 4](FTM/WMonotone.lean): crescimento estrito do passo discreto.
- [Coq](formal/coq/WMonotone.v): certificado equivalente.
- [Agda](formal/agda/WMonotone.agda): testemunha construtiva de crescimento.
- [Isabelle/HOL](formal/isabelle/WMonotone.thy): teoria fornecida; execução requer uma distribuição Isabelle.
- [Metateorema fluxo–cirurgia](FTM/PoincareMethod.lean) e [adaptadores](FTM/MillenniumAdapters.lean).

O metateorema é condicional. Os adaptadores permanecem bloqueados até que suas obrigações sejam provadas; nenhum axioma afirma uma solução.

## Aplicação e runtime experimental

- [Gateway FastAPI v4.1](gateway/main_v4_1_corrigido.py): regulador com limites explícitos e política AES-256.
- [Testes Python](tests/test_w_monotone.py): liveness e ausência de alegações indevidas.
- [Runtime C++](runtime/ftm_runtime.cpp): simulador de runtime em espaço de usuário; **não é um sistema operacional nem kernel**.
- [Aplicação HTML](app/index.html): painel local do modelo.
- [Dockerfile](Dockerfile): inicializa o gateway corrigido.
- [CI multilíngue](.github/workflows/multilang.yml): executa Python, C++, HTML, Coq e Agda; o workflow Lean executa `lake build`.

## Paper

- [Paper condicional](output/pdf/paper_conditional.pdf): *A Conditional Security Framework Inspired by L-function Structures (Assuming RH)*.
- [Paper de auditoria anterior](output/pdf/paper_final_v4_1.pdf).

As formulações oficiais dos Problemas do Milênio são as do [Clay Mathematics Institute](https://www.claymath.org/millennium-problems/).
- [Auditoria estrutural da RH](docs/problems/riemann-audit/README.md): PDFs,
  fontes LaTeX e visualizações do detector radial e das lacunas lógicas.
- [Árvore formal de lemas](docs/formal/lemma-tree.md): dependências, barreiras de
  circularidade e obrigações para os sete programas.
- [FTM Observatory](app/index.html): aplicativo web progressivo para explorar a
  árvore e simular comportamentos sem promover evidência a prova.

## Aplicativo

O diretório [`app/`](app/) contém uma aplicação estática, responsiva e
instalável. O workflow de GitHub Pages publica a interface automaticamente a
partir da branch `main`.

## Programa formal preexistente

Esta camada computável complementa, sem substituir, os documentos já mantidos
no repositório:

- [`docs/fundamentos.md`](docs/fundamentos.md): célula trivalente decorada,
  atlas federado, descida e teorema de colagem T0;
- [`docs/matriz-milenio.md`](docs/matriz-milenio.md): classificação auditável
  das interfaces com os sete problemas;
- [`docs/roadmap.md`](docs/roadmap.md): fases de pesquisa e falsificadores;
- [`docs/millennium/`](docs/millennium/): cadernos individuais e obrigações
  formais para Poincaré, Hodge, Yang–Mills, Navier–Stokes, P versus NP,
  Riemann e BSD.

## Calculadora web

Abra `app/index.html` num navegador. Escolha um problema, o regime trivalente,
os parâmetros da trajetória e as hipóteses aceites. A interface calcula uma
aproximação discreta da ação

```text
S[γ] = ∫ L(γ(t), γ̇(t)) dt + i ∫ e(t) dt
```

e exporta uma especificação para Lean 4, Coq, Isabelle/HOL, Agda e LaTeX.
Exportar texto não equivale a verificá-lo no respetivo provador.

## Quest e OBS

O guia em `docs/quest-obs.md` distingue captura do ecrã, casting oficial,
Passthrough Camera API e ingestão de rede. O teardown do ADB é uma propriedade
operacional testável; não é consequência de um axioma matemático.

## Estado de verificação

Os exportadores são determinísticos e evitam `sorry`, `Admitted`, `sorry` de
Agda e equivalentes. As proposições que não têm prova são emitidas como axiomas
ou obrigações claramente rotuladas. Cada saída precisa ser compilada na versão
do provador indicada pelo utilizador antes de receber o estado `verified`.

## Licença

MIT.

## Estrutura

```text
app/          interface estática e exportadores interativos
model/        lógica K3, catálogo, ação numérica e comparação
gateway/      derivação HKDF e teardown ADB sem shell
formal/       Lean, Coq, Isabelle/HOL e Agda
simulations/  gerador único das oito figuras
figures/      PNGs reproduzíveis a 200 DPI
paper/        manuscrito LaTeX
docs/         modelo matemático, segurança e Quest/OBS
tests/        invariantes do modelo e do gateway
```

## Reproduzir

```sh
python -m pip install -e ".[dev,figures,crypto]"
pytest -q
ruff check model gateway tests simulations
python simulations/generate_figures.py
```

Para Lean:

```sh
cd formal/lean
lake build
```

Coq, Isabelle e Agda devem ser executados nos seus toolchains oficiais. O CI
inclui Python e Lean; os restantes poderão ser adicionados com imagens
versionadas quando as versões de referência forem fixadas.

## Figuras

1. projeção de uma trajetória do modelo 5D;
2. zeros conhecidos amostrados sobre a reta crítica, apenas como ilustração;
3. mapa `alpha-beta`, explicitamente não tratado como fronteira de decidibilidade;
4. `e(t)` e a sua integral acumulada;
5. matriz de Jaccard das características declaradas;
6. tabelas `AND` e `OR` da lógica K3;
7. máquina operacional de teardown;
8. separação entre axioma, derivação e conclusão condicional.

## Limites científicos

- Os cinco eixos são uma parametrização proposta, não uma equivalência
  estabelecida entre áreas matemáticas.
- A matriz de conexão não demonstra reduções entre problemas.
- A ação não é um funcional canónico dos problemas do milénio.
- Resultados de ponto flutuante não são certificados formais.
- O teorema abstrato de teardown não prova o estado físico do headset.
- Assumir RH permite conclusões condicionais; não constitui prova de RH.

## Disclaimer científico v4.1

- Todos os coeficientes de conexão são parâmetros hipotéticos de simulação;
  não são derivados de RH, BSD, P versus NP ou Yang-Mills.
- A matriz espectral citada nos materiais de origem não está reproduzível no
  repositório porque seus 21 coeficientes independentes não foram fornecidos.
  Os autovalores `0.014487,...,4.180106`, o condicionamento `288.54` e o posto
  efetivo `3.44` permanecem resultados reportados, não verificados.
- A matriz `C = 1 - Div` que pode ser construída a partir da tabela `Div`
  versionada não é a matriz espectral reportada e possui autovalor negativo;
  portanto não deve ser chamada de matriz de correlação positiva definida.
- Os oito pontos `0.5 + i gamma` estão na reta crítica por construção. As
  estatísticas dos espaçamentos descrevem apenas essa pequena amostra.
- `W` é um acumulador definido pelo software. Sua monotonicidade sob tempo
  não regressivo não estabelece entropia geométrica, não-colapso ou segurança.
- Uma avaliação da integral em um ponto é constante; uma quadratura com `n`
  pontos é `O(n)`. Não há alegação de latência zero.
- O dashboard auditado está em [`app/dashboard_v4_1.html`](app/dashboard_v4_1.html).
## Research Hub

O diretório [`hub/`](hub/) contém a base JSON, o motor Python, testes e os
núcleos Lean 4 e Agda. A metodologia e o estudo físico do eclipse estão em
[`docs/articles/`](docs/articles/). O workflow `formal.yml` executa os três
ambientes sem aceitar `sorry`, `postulate` ou promoção automática de evidência
finita para prova.

A [árvore canônica do repositório](docs/architecture/repository-tree.md)
documenta responsabilidades, fluxo de dados e a fonte de verdade de cada
camada.

Os [geradores de artefatos](tools/artifact-builders/), o
[teste end-to-end](tests/e2e/) e o
[pacote integral original](releases/) também estão versionados para preservar
todo o material produzido durante a construção do projeto.

O nome do projeto não determina uma teoria. A definição inicial é provisória e torna afirmações testáveis. As formulações oficiais são as do [Clay Mathematics Institute](https://www.claymath.org/millennium-problems/).
