# Federated Trivalent Manifold

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
