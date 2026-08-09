# Pipeline de 24 Artigos Auditáveis + 7 Alvos Clay

> **Fronteira de rigor:** nenhum dos 24 artigos desta esteira reivindica
> solução de Problema do Milênio. Cada artigo é classificado explicitamente
> como **Evidência numérica**, **Teorema condicional** ou
> **Teorema publicado**. Os 7 alvos Clay (`F1–F7`) são esboços futuros
> separados, com `TODO` explícito onde a prova analítica ainda falta.

---

## Estrutura hierárquica

### PARTE A — Fundamentos (3 artigos)

| ID  | Título provisório                             | Status estimado |
|-----|-----------------------------------------------|-----------------|
| A1  | Célula trivalente decorada e atlas federado   | 99 % aceite     |
| A2  | Morfismos, colagem e teorema T0               | 99 % aceite     |
| A3  | Lemas compartilhados e componentes reutilizáveis | 95 % aceite  |

### PARTE B — 7 Problemas × 3 artigos (21 artigos)

Para cada problema P ∈ {RH, PvsNP, NS, YM, Hodge, BSD, Poincaré}:

| Sufixo | Conteúdo                                 | Aceite estimado |
|--------|------------------------------------------|-----------------|
| .A     | Fundamentação — só literatura            | 99 %            |
| .B     | Modelo — evidências, figuras fig1–fig6   | 80 %            |
| .C     | Validação — falsificação Popper          | 85 %            |

**Lista completa (IDs 4–24):**

```
RH.A   RH.B   RH.C
PvsNP.A  PvsNP.B  PvsNP.C
NS.A   NS.B   NS.C
YM.A   YM.B   YM.C
Hodge.A  Hodge.B  Hodge.C
BSD.A  BSD.B  BSD.C
Poincaré.A  Poincaré.B  Poincaré.C  ← Teorema publicado (Perelman 2003)
```

### Alvos Clay futuros (após os 24)

| ID | Problema          | Chance est. | Buraco principal                        |
|----|-------------------|-------------|-----------------------------------------|
| F1 | Riemann           | 0,5 %       | `TODO: E_Res(ω)=0` analítico           |
| F2 | P vs NP           | 0,1 %       | `TODO: N_max→∞` sem hardware            |
| F3 | Navier-Stokes     | 1 %         | `TODO: e_linear(ω)≥0` sem tanh         |
| F4 | Yang-Mills        | 0,1 %       | `TODO: mass gap` analítico             |
| F5 | Hodge             | 0,1 %       | `TODO: ciclos algébricos` em geral     |
| F6 | BSD               | 0,1 %       | `TODO: posto Mordell-Weil` analítico   |
| F7 | Poincaré          | — (resolvido) | Perelman 2003                         |

---

## Checklist de auditoria (obrigatório antes de qualquer submissão)

- [ ] Nenhum número finito (`9999`, `48M`, `25.516`, `-5e-05`, `-0.0459`,
      `tanh`, `6585.3223`) no núcleo da prova?
- [ ] Lean/Coq/Isabelle compila sem `sorry`/`admit`?
- [ ] `E_Res(ω)=0` provado analiticamente, não `≈_{ε,N}`?
- [ ] Falsificação Popper explícita: qual contraexemplo derrubaria?
- [ ] Auditoria: dependências, hipóteses ocultas, circularidade listadas?
- [ ] Revisão bibliográfica: comparado com Clay official, Annals, Inventiones?
- [ ] Reprodutibilidade: algoritmo, precisão, semente, complexidade documentados?
- [ ] Classificação: **teorema** vs **evidência** vs **hipótese** claramente marcada?

Se falhar 1 item → artigo é **Evidência numérica**, não **Teorema publicado**.

---

## Ordem de escrita recomendada

| Meses | Artigos    | Observação                               |
|-------|-----------|------------------------------------------|
| 1–2   | A1, A2, A3 | Fundamentos, literatura, alto aceite    |
| 3–8   | *.A (×7)   | Fundamentação por problema              |
| 9–14  | *.B (×7)   | Modelos com figuras — figuras fig1–fig6 |
| 15–20 | *.C (×7)   | Validação Popper                        |
| 21+   | F3, F1, …  | Só depois dos 24 DOIs em mãos           |

---

## Arquivos nesta pasta

```
docs/pipeline/
├── README.md                   ← este arquivo
├── dag.json                    ← grafo de dependências (DAG acíclico)
├── shared/
│   ├── lemas_compartilhados.tex
│   └── tabela_status_logico.csv
├── RH.B/
│   └── RH_B_template.tex       ← template LaTeX auditável completo
├── F3-Navier-Stokes/
│   └── F3_NS_skeleton.tex      ← esqueleto Clay com TODO explícito
└── build_pdfs.py               ← script reprodutível de geração de PDFs
```

---

## Regra oficial Clay (resumo)

> Artigo publicado em journal de prestígio (Annals, JAMS, Inventiones, Acta),
> **2 anos** sem ninguém achar furo, comunidade aceita, Clay convoca comitê.
> Sem isso não paga mesmo que esteja certo.

Fonte: [Clay Mathematics Institute — Millennium Problems](https://www.claymath.org/millennium-problems/)
