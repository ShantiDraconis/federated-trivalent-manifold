# Federated Trivalent Manifold

Programa de pesquisa para estruturas trivalentes locais, sua colagem em objetos globais e possíveis interfaces rigorosas com os Problemas do Milênio.

> **Estado científico:** este repositório não reivindica a solução de nenhum Problema do Milênio. Uma conexão só é matemática quando há definições, enunciado formal, redução e prova auditável; o restante é programa, conjectura, analogia ou evidência empírica.

## Núcleo formal

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
