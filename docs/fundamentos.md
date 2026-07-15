# Fundamentos formais (v0.1)

## 1. Convenções

Fixe uma categoria de regularidade \(\mathcal R\) — por exemplo Top, PL, \(C^k\) ou \(C^\infty\) — e uma dimensão \(n\). Toda afirmação deve indicar ambas; resultados não são transferidos automaticamente entre categorias.

## 2. Célula trivalente decorada

Uma **célula trivalente decorada** é uma quíntupla
\[
T=(X,\Gamma,\iota,\mathcal F,\lambda),
\]
onde:

1. \(X\) é uma variedade \(n\)-dimensional, possivelmente com bordo, em \(\mathcal R\);
2. \(\Gamma=(V,E)\) é um grafo finito cujos vértices internos têm grau 3;
3. \(\iota:|\Gamma|\to X\) é uma imersão ou incorporação especificada;
4. \(\mathcal F\) é um feixe, fibrado ou campo de dados sobre \(X\);
5. \(\lambda\) contém os dados geométricos ou analíticos exigidos (métrica, conexão, operador, medida ou energia).

“Trivalente” qualifica \(\Gamma\), não a variedade: uma variedade não possui valência combinatória por si só.

## 3. Atlas federado

Um **atlas federado trivalente** sobre \(M\) é
\[
\mathfrak A=(I,\{T_i\},\{U_{ij}\},\{g_{ij}\},\{\alpha_{ij}\}),
\]
com cartas locais, sobreposições, mapas de transição e isomorfismos das decorações. Em interseções triplas exige-se
\[
g_{ij}g_{jk}=g_{ik},\qquad \alpha_{ij}\alpha_{jk}=\alpha_{ik},
\]
ou uma coerência superior explicitamente definida.

A federação é **efetiva** quando o dado de descida produz um objeto global \((M,\Gamma_M,\mathcal F_M,\lambda_M)\), único até o isomorfismo pertinente, cujas restrições recuperam os dados locais.

## 4. Morfismos e invariantes

Um morfismo preserva variedade, incidência, decoração e descida. Igualdade de invariantes numéricos não basta para equivalência.

Invariantes iniciais: tipo de homotopia, \(\pi_k\), homologia e cohomologia, característica de Euler, classes características, espectro de operadores, energia/ação e complexidade das apresentações finitas.

## 5. Teorema obrigatório T0 (colagem)

Dar hipóteses necessárias e suficientes para que um atlas federado efetivo produza um objeto global Hausdorff, segundo contável e pertencente a \(\mathcal R\). Provar que decorações e operadores colam e que o resultado é único até equivalência.

Sem T0, expressões globais como espectro, classe de Hodge, fluxo, ação de Yang–Mills ou complexidade não estão bem definidas.

## 6. Política de afirmações

Cada resultado deve declarar hipóteses quantificadas, conclusão, categoria, dependências, prova ou referência e teste de falha. Simulações fornecem evidência; não substituem prova de existência, regularidade ou universalidade.
