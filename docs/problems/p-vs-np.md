# P versus NP — caderno formal

## Modelo computacional

Fixe máquina de Turing determinística, codificação binária e custo por comprimento da entrada. Toda apresentação FTM finita deve possuir serialização canônica verificável em tempo polinomial.

## Linguagem candidata

\[
\mathrm{FTM\mbox{-}DESCENT}=
\{\langle\mathfrak A\rangle:\text{existe dado global compatível com todos os cociclos}\}.
\]

Para afirmar \(\mathrm{FTM\mbox{-}DESCENT}\in NP\), o certificado global deve ter tamanho polinomial e sua compatibilidade ser verificável em tempo polinomial. Isso pode falhar para dados contínuos ou equivalências não efetivas.

## Programa de complexidade

**C1.** Especificar gramática, tamanho e semântica da entrada.

**C2.** Provar pertencimento a NP ou à classe correta.

**C3.** Investigar NP-dureza por redução many-one explícita, preservando respostas sim/não.

**C4.** Identificar subclasses tratáveis (árvores, largura limitada, grupos finitos fixos).

Mesmo que FTM-DESCENT seja NP-completo, isso não separa \(P\) de \(NP\). Uma separação requer argumento aplicável a todas as máquinas/algoritmos polinomiais e enfrentar barreiras conhecidas da área.

## Falsificadores

Certificados exponenciais, números reais de precisão ilimitada, equivalência indecidível ou custo oculto na construção das cartas.

**Maturidade atual:** M0; a linguagem ainda precisa de codificação finita definitiva.
