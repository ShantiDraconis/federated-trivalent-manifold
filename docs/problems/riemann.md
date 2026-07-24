# Hipótese de Riemann — caderno formal

## Enunciado-alvo

Todo zero não trivial \(\rho\) de \(\zeta(s)\) satisfaz \(\operatorname{Re}\rho=1/2\). É conveniente usar a função completada \(\xi(s)\), inteira e simétrica.

## Rota espectral FTM

Construir um espaço de Hilbert \(\mathcal H_F\) e um operador \(D_F\). Uma conexão forte exige identidade demonstrada
\[
\det_{\mathrm{reg}}(D_F-z)=E(z)\,\xi(1/2+iz),
\]
onde \(E\) é explícita e não introduz/remove zeros relevantes.

## Obrigações

**RH1 — operador:** domínio denso, fechamento e auto-adjunticidade de \(D_F\).

**RH2 — determinante:** regularização existe e a identidade vale como igualdade de funções, incluindo multiplicidades.

**RH3 — ausência de fatores espúrios:** zeros de \(E\) são controlados.

**RH4 — equivalência:** espectro real de \(D_F\) é logicamente equivalente à localização dos zeros.

Zetas de grafos, equações funcionais semelhantes, estatísticas espectrais e ajuste dos primeiros zeros são evidência heurística, não RH2/RH4.

## Testes de sanidade

Contagem de zeros, termo principal e termos inferiores; simetria funcional; zeros triviais; multiplicidades; estabilidade no limite federado.

**Maturidade atual:** M0. Nenhum operador com RH1–RH4 foi construído.

---

## Programa off-critical (anexo auditável)

Independente de RH1–RH4, o repositório mantém um programa de pesquisa sobre zeros hipotéticos **fora** da linha crítica. Nenhuma afirmação deste programa implica ou assume RH.

**Arquivo Lean 4:** [`lean/OffCriticalProgram.lean`](../../lean/OffCriticalProgram.lean) — 0 axiomas externos, 0 sorry no Eixo 1.

**Quatro eixos:**

| Eixo | Tema | Estado |
|------|------|--------|
| 1 | Geometria local: \(\delta^2 = (R_+^2+R_-^2)/2 - R_c^2\) | Provado (`ring`) |
| 2 | Defeito global \(\mathfrak{D}_\mathrm{rad}(T) = \sum w_\rho\); decaimento \(\gamma^{-4}\) | Aberto; dados em `data/off-critical-w4.csv` |
| 3 | Custo espectral \(X_{\eta,\Delta} = (T/2\pi)^{\Delta/c}\) | Provado; cotas para \(\eta=0.01\) em aberto |
| 4 | Correlação \(V_\Omega\); contraexemplo \(V_\Omega = -11.87 \neq \delta^2\) | Provado (dois zeros na linha) |

**Roteiro do artigo:** [`docs/artigo-programa-pesquisa.md`](../artigo-programa-pesquisa.md)

**Dados numéricos:** `data/off-critical-w4.csv`, `data/off-critical-spectral.csv`
