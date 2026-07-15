# Federated Trivalent Manifold

Programa de pesquisa para estruturas trivalentes locais, sua colagem em objetos globais e possíveis interfaces rigorosas com os Problemas do Milênio.

> **Estado científico:** este repositório não reivindica a solução de nenhum Problema do Milênio. Uma conexão só é matemática quando há definições, enunciado formal, redução e prova auditável; o restante é programa, conjectura ou analogia.

## Núcleo formal

- [Fundamentos](docs/fundamentos.md): objeto básico, morfismos, federação e consistência.
- [Matriz dos Problemas do Milênio](docs/matriz-milenio.md): visão comparativa.
- [Cadernos individuais](docs/problems/README.md): formalização problema por problema.
- [Molde de Poincaré](docs/poincare-method-template.md): fluxo, entropia, cirurgia, correções e ordem de desbloqueio.
- [Registro de afirmações](docs/claims-register.md): estados lógicos auditáveis.
- [Roadmap](docs/roadmap.md): resultados mínimos e critérios de falsificação.
- [Referências](docs/references.md): fontes primárias e política de citação.

## Lean 4

- [Metateorema fluxo–cirurgia](FTM/PoincareMethod.lean).
- [Adaptadores dos seis problemas abertos](FTM/MillenniumAdapters.lean).
- A integração contínua executa o build Lean em pushes e pull requests.

O metateorema é condicional. Todos os adaptadores permanecem bloqueados até que suas seis obrigações sejam provadas; nenhum axioma afirma uma solução.

## Cadernos

[Poincaré](docs/problems/poincare.md) ·
[Hodge](docs/problems/hodge.md) ·
[Yang–Mills](docs/problems/yang-mills.md) ·
[Navier–Stokes](docs/problems/navier-stokes.md) ·
[P versus NP](docs/problems/p-vs-np.md) ·
[Riemann](docs/problems/riemann.md) ·
[Birch–Swinnerton-Dyer](docs/problems/bsd.md)

As formulações oficiais são as do [Clay Mathematics Institute](https://www.claymath.org/millennium-problems/).
