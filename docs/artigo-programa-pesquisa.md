# Programa de Pesquisa: Zeros Fora da Linha Crítica

**Roteiro LaTeX / artigo — rascunho para submissão**
Estado: programa de 12 meses, 70% publicação, 0 axioma RH.

---

## Estrutura LaTeX sugerida

```latex
\documentclass[11pt]{amsart}
\usepackage{amsmath,amssymb,amsthm,hyperref}
\usepackage{booktabs}   % tabelas
\usepackage{listings}   % código Lean

\title{Off-Critical Zero Geometry and the Radial Defect Program}
\author{...}
\date{\today}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{openquestion}[theorem]{Open Question}

\begin{document}
\maketitle
```

---

## Seção 1 — Introdução

**Objetivo.** Estudar o comportamento de zeros hipotéticos fora da linha crítica sem assumir a Hipótese de Riemann. O programa é auditável: cada afirmação é um teorema formal (Lean 4 + Mathlib) ou uma conjectura explicitamente aberta.

**Convenção.** Escrevemos \(\rho = \beta + i\gamma\), \(\delta = \beta - \tfrac{1}{2}\). A linha crítica corresponde a \(\delta = 0\).

```latex
\section{Introduction}
% objetivo e convenções; citar CMI para RH oficial
```

---

## Seção 2 — Eixo 1: Geometria Local Off-Critical (Teorema)

**Definições:**
\[
R_+^2 = |\rho|^2 = \beta^2 + \gamma^2, \quad
R_-^2 = |1-\rho|^2 = (1-\beta)^2 + \gamma^2, \quad
R_c^2 = \gamma^2 + \tfrac{1}{4}.
\]

**Teorema 2.1** (Rigidez Local, provado em Lean):
\[
\delta^2 = \frac{R_+^2 + R_-^2}{2} - R_c^2.
\]

*Prova.* Substituição direta, cálculo algébrico. Ver `OffCriticalProgram.lean`, `local_rigidity_zero_iff`. $\square$

**Corolário 2.2.** Seja \(P = A^2 - \delta^2\) com \(A = \gamma^2 + \tfrac{1}{4} + \delta^2\). Então
\[
P = |\rho|^2 \cdot |1-\rho|^2 \geq 0,
\]
com igualdade somente em \(\gamma = 0\), \(\beta \in \{0, 1\}\).

```latex
\section{Axis 1: Local Off-Critical Geometry}
\begin{theorem}[Local Rigidity]
  $\delta^2 = (R_+^2 + R_-^2)/2 - R_c^2$.
\end{theorem}
\begin{proof}
  Direct substitution; verified in Lean~4 (\texttt{local\_rigidity\_zero\_iff}).
\end{proof}
\begin{corollary}
  $P = |\rho|^2\,|1-\rho|^2 \ge 0$.
\end{corollary}
```

---

## Seção 3 — Eixo 2: Defeito Global e Perda de Sensibilidade

**Definições:**
\[
w(\rho) = \frac{2\delta^2}{P}, \qquad
W_4(\rho) = 4w(\rho) \approx \frac{8\delta^2}{\gamma^4} \text{ para } |\gamma| \gg 1,
\]
\[
\mathfrak{D}_{\mathrm{rad}}(T) = \sum_{|\gamma| \leq T} w(\rho).
\]

**Questão aberta 3.1 (decaimento).** Existe \(C > 0\) tal que
\[
\frac{\mathfrak{D}_{\mathrm{rad}}(T)}{N(T)} \leq C \frac{\log T}{T^3}\,?
\]

**Questão aberta 3.2 (precisão).** \(W_4(0.1, 10^3) \approx 7{,}99 \times 10^{-14}\) — abaixo da dupla precisão IEEE 754. Calcular \(\mathfrak{D}_{\mathrm{rad}}(T)\) para \(T = 10^6\) requer aritmética de intervalo com \(\geq 200\) dígitos (e.g., Arb/MPFI).

**Tabela 3.1** — Valores de \(W_4(\delta, \gamma)\) (extrato; tabela completa em `data/off-critical-w4.csv`):

| δ     | γ      | W₄ (CSV)        | 8δ²/γ⁴ (aprox.) | erro rel. (%) |
|-------|--------|-----------------|-----------------|---------------|
| 0.001 | 100    | 7.99960001×10⁻¹⁴ | 8.00000000×10⁻¹⁴ | 0.005000     |
| 0.100 | 1 000  | 7.99999584×10⁻¹⁴ | 8.00000000×10⁻¹⁴ | 0.000052     |
| 0.500 | 1 000  | 1.99999800×10⁻¹² | 2.00000000×10⁻¹² | 0.000100     |

```latex
\section{Axis 2: Global Defect and Sensitivity Loss}
% definições, tabela de W4, conjecturas 3.1 e 3.2
\begin{table}[h]
  \caption{Sample $W_4(\delta,\gamma)$ values; full table in \texttt{data/off-critical-w4.csv}.}
  ...
\end{table}
```

---

## Seção 4 — Eixo 3: Janela Espectral e Custo de Detecção

**Definições:**
\[
X_{\eta,\Delta} = e^{2\pi\Delta/\eta}, \qquad
d_{\mathrm{médio}}(T) = \frac{2\pi}{\log(T/2\pi)}.
\]

**Teorema 4.1** (provado em Lean): quando \(\eta = c \cdot d_{\mathrm{médio}}(T)\),
\[
X_{\eta,\Delta} = \left(\frac{T}{2\pi}\right)^{\Delta/c}.
\]
O custo é *potencial* em \(T\), não superexponencial.

**Tabela 4.1** — Espaçamento e custo (\(\Delta=0.1\), \(c=0.5\); tabela completa em `data/off-critical-spectral.csv`):

| T       | d_médio | X(Δ=0.1, c=0.5) |
|---------|---------|-----------------|
| 10⁴     | 0.8523  | 4.37            |
| 10⁶     | 0.5246  | 10.97           |
| 10⁸     | 0.3789  | 27.57           |
| 10¹⁰    | 0.2965  | 69.24           |
| 10¹²    | 0.2436  | 173.9           |

**Questão aberta 4.1.** Qual \(\Delta\) minimiza o custo para detectar desvio \(\eta = 0.01\)?
Para \(\Delta = 0.1\) fixo: \(X = e^{2\pi \cdot 0.1/0.01} \approx 1.94 \times 10^{27}\) — inviável computacionalmente. Requer \(\eta \geq 0.1\) ou \(T \gg 10^{12}\).

```latex
\section{Axis 3: Spectral Window and Detection Cost}
\begin{theorem}
  $X_{\eta,\Delta} = (T/2\pi)^{\Delta/c}$ when $\eta = c\,d_{\text{avg}}(T)$.
\end{theorem}
```

---

## Seção 5 — Eixo 4: Estrutura de Correlação \(V_\Omega\)

**Definição:**
\[
V_\Omega = \operatorname{Var}_\Omega(\delta) - \operatorname{Var}_\Omega(\gamma) + 2i\operatorname{Cov}_\Omega(\delta,\gamma).
\]

**Proposição 5.1** (fibra única \(|\Omega|=1\)): \(V_\Omega = \delta_0^2 \geq 0\).

**Contraexemplo 5.2** (dois zeros na linha, \(\delta=0\)): Seja \(\Omega = \{14.13i,\, 21.02i\}\) (ambos na linha crítica).
\[
\operatorname{Var}(\delta)=0,\quad \operatorname{Var}(\gamma)=\left(\frac{21.02-14.13}{2}\right)^2 \approx 11.87,\quad V_\Omega \approx -11.87.
\]
Logo \(V_\Omega \neq \delta^2 = 0\) — a igualdade geral falha. (Provado em Lean: `V_Omega_can_be_negative`.)

**Questão aberta 5.1.** Para janelas \(\Omega = [T, T + 10\,d_{\mathrm{médio}}(T)]\), como evolui \(\operatorname{Re}(V_\Omega)\) com \(T\)? Mede clustering off-critical?

```latex
\section{Axis 4: Correlation Structure $V_\Omega$}
\begin{proposition}
  For $|\Omega|=1$, $V_\Omega = \delta_0^2 \ge 0$.
\end{proposition}
\begin{example}[Two on-line zeros]
  $\gamma_1=14.13$, $\gamma_2=21.02$, both with $\delta=0$:
  $V_\Omega \approx -11.87 < 0$.
\end{example}
```

---

## Seção 6 — Roteiro de 12 meses

| Período  | Tarefa | Alvo |
|----------|--------|------|
| Mês 1–3  | Publicar Eixo 1: `local_rigidity_zero_iff` + P>0, w≥0 | J. Formalized Reasoning |
| Mês 4–6  | Calcular \(\mathfrak{D}_{\mathrm{rad}}(T)\) para T=10⁶, Arb 200 dígitos; tabela w, W₄ | Math. Comp. |
| Mês 7–9  | Provar cotas X_{η,Δ} e d_médio com aritmética intervalar; corrigir os valores aproximados usados na literatura anterior (d_médio ≈ 0.2 → valor exato 0.5246 para T=10⁶; d_médio ≈ 0.07 → valor exato 0.2436 para T=10¹²) | — |
| Mês 10–12 | Estudo V_Ω em [T, T+10d_médio]; mostrar V ≠ δ² com dados; exemplo 2 zeros → −11.87 | — |

```latex
\section{12-Month Roadmap}
% tabela de tarefas
```

---

## Seção 7 — Critérios de Falsificação

1. Se encontrado zero \(\rho\) com \(\delta \neq 0\): P explode? w → ∞? Contradição com Eixo 1?
2. Se \(\mathfrak{D}_{\mathrm{rad}}(T)/N(T)\) não decai como \(T^{-3}\): conjectura 3.1 é falsa.
3. Se \(V_\Omega\) não distingue clustering: Eixo 4 é irrelevante.

```latex
\section{Falsification Criteria}
% lista de testes que podem refutar cada eixo
```

---

## Apêndice — Código Lean 4

Arquivo: `lean/OffCriticalProgram.lean`.
Verificar com `lake build` em repositório com dependência `mathlib4`.

```latex
\appendix
\section{Lean 4 Skeleton}
\lstinputlisting[language=Haskell]{lean/OffCriticalProgram.lean}
```

---

## Referências

- Clay Mathematics Institute. *Millennium Problems*. <https://www.claymath.org/millennium-problems/>
- Titchmarsh, E.C. *The Theory of the Riemann Zeta-Function*. Oxford, 1986.
- Bombieri, E. *Problems of the Millennium: The Riemann Hypothesis*. CMI, 2000.
- Lean 4 + Mathlib4: <https://leanprover-community.github.io/>
- Johansson, F. *Arb: efficient arbitrary-precision midpoint-radius interval arithmetic*. IEEE Trans. Comput., 2017.

```latex
\bibliography{refs}
\end{document}
```
