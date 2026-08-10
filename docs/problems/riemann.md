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

## Dossiê suplementar

O pacote [Auditoria estrutural da Hipótese de Riemann](riemann-audit/README.md)
detalha o detector geométrico local, o defeito radial não holomorfo, a forma de
Weil, matrizes truncadas e o teste de circularidade. O material preserva a
classificação M0 e não substitui as obrigações RH1–RH4.
