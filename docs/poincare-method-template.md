# Molde de Poincaré: formalização, limites e desbloqueio

## Arquitetura reutilizável

1. definir uma evolução;
2. provar uma quantidade monótona e coerciva;
3. obter não-colapso e modelos de singularidade;
4. realizar cirurgia apenas em regiões canônicas, preservando a semântica;
5. provar continuação e ausência de acumulação patológica;
6. classificar estados terminais;
7. traduzir a classificação para o teorema-alvo.

Não é correto dizer que “só sobra esfera” para toda 3-variedade. No caso simplesmente conexo, extinção finita e classificação implicam Poincaré; o programa completo trata geometrização.

## Metateorema Lean

O arquivo **FTM/PoincareMethod.lean** exige seis provas: invariância semântica, monotonicidade, não-colapso, correção da cirurgia, chegada global a estado terminal e classificação terminal. O teorema é condicional e não assume nenhum Problema do Milênio.

**FTM/MillenniumAdapters.lean** registra as seis instâncias abertas. Todos os indicadores começam falsos. Destravar significa substituir uma obrigação aberta por teorema, não mudar o booleano manualmente.

## Correções indispensáveis

### P versus NP

A fórmula \(\partial_t Circuit=-Complexity(Circuit)\) não está tipada: circuitos são discretos e complexidade não é circuito. É preciso definir transformação discreta, preservar a linguagem e controlar tamanho. Relativização é barreira a técnicas que relativizam; não significa literalmente que um oráculo recria uma singularidade.

### Riemann

O fluxo \(\dot s=-(\operatorname{Re}s-1/2)\) força qualquer ponto à reta por definição, mas não preserva zeros de \(\zeta\). Primeiro é necessária uma realização espectral ou identidade de determinante; depois, uma deformação que a preserve.

### Yang–Mills

Autovalor de operador geométrico clássico não é gap de massa quântico 4D. O funcional candidato deve sobreviver aos limites contínuo e de volume infinito, preservar positividade e provar não trivialidade. Não há fonte primária registrada para “Witten tentou construir \(\mathcal W_{YM}\)”; isso não deve ser afirmado sem referência exata.

### Hodge

Preservar uma classe ou seu tipo \((p,p)\) no Kähler–Ricci flow não prova algebraicidade. Esse é justamente o obstáculo da conjectura. O caso \(c_1=0\) é uma subclasse, não o domínio inteiro.

### Navier–Stokes

O próprio PDE já é um fluxo. Falta uma estimativa crítica que impeça blow-up. Cirurgia que altera a solução deixa de resolver o PDE original, salvo teorema de equivalência.

### BSD

Proximidade com RH não autoriza “o mesmo fluxo”. BSD envolve uma família \(L(E,s)\) e dados aritméticos. A transformação deve preservar fatores locais, condutor, posto e a fórmula refinada.

## Métricas Div, Conn, R, I e U

Percentuais não são resultados até definir espaço de características, métrica, pesos, invariância de apresentação, calibração, incerteza e um teorema ligando a métrica a redução lógica. Até lá, seu estado é **HEURISTIC**.

## Ordem de desbloqueio

1. provar FTM-T0;
2. instanciar o molde no caso conhecido de Ricci flow como teste;
3. provar uma instância finita simples com as seis obrigações;
4. em cada problema aberto, atacar somente a primeira obrigação ainda falsa;
5. declarar redução apenas com teorema entre o enunciado oficial e a instância FTM.

## Referências primárias

- G. Perelman, [Entropy formula](https://arxiv.org/abs/math/0211159).
- G. Perelman, [Ricci flow with surgery](https://arxiv.org/abs/math/0303109).
- G. Perelman, [Finite extinction time](https://arxiv.org/abs/math/0307245).
- CMI, [descrições oficiais](https://www.claymath.org/resource/book-title-the-millennium-prize-problems/).
