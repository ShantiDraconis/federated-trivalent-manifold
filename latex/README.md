# LaTeX — Pacotes de Lacunas Formais

Este diretório contém os cadernos LaTeX para os seis Problemas do Milênio
abertos, elaborados no quadro do programa Federated Trivalent Manifold (FTM).

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `ftm.sty` | Estilo compartilhado: macros, ambientes, teoremas, status |
| `main.tex` | Documento mestre: introdução, metodologia, sumário dos 6 problemas |
| `riemann.tex` | Hipótese de Riemann — 5 programas, 4 obrigações, lacunas |
| `p-vs-np.tex` | P versus NP — barreiras, GCT, circuitos, linguagem FTM |
| `bsd.tex` | Birch–Swinnerton-Dyer — Gross-Zagier, Iwasawa, funtor Φ |
| `hodge.tex` | Conjectura de Hodge — abeliano, motivos, H-SURJ |
| `navier-stokes.tex` | Navier–Stokes — Prodi-Serrin, integração convexa, NS4 |
| `yang-mills.tex` | Yang–Mills e gap — Balaban, Wilson loop, YM1–YM5 |

## Como compilar

Cada arquivo é autônomo. Com uma instalação TeX Live ou MiKTeX:

```bash
# Documento mestre (recomendado para visão geral)
cd latex
pdflatex main.tex
pdflatex main.tex   # segunda passagem para referências cruzadas

# Cadernos individuais
pdflatex riemann.tex
pdflatex p-vs-np.tex
pdflatex bsd.tex
pdflatex hodge.tex
pdflatex navier-stokes.tex
pdflatex yang-mills.tex
```

No Overleaf: carregue todos os arquivos `.tex` e `.sty` juntos;
defina `main.tex` como documento raiz.

## Convenções de status

- `\OPEN` — lacuna não fechada, prova inexistente
- `\PROVED` — resultado demonstrado (usado em subresultados)
- `\CONDITIONAL` — válido sob hipótese explícita
- `\MATURITY{...}` — nível de maturidade M0–M3

## Estado científico

Nenhum documento constitui solução de nenhum Problema do Milênio.
As formulações oficiais são as do
[Clay Mathematics Institute](https://www.claymath.org/millennium-problems/).
