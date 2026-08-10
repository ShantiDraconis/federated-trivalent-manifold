# Eclipse de 3 de novembro de 1994: correspondência fraca e refutação

## Escopo

Um eclipse testa modelos geométricos e dinâmicos. Ele não prova um Problema do
Milênio. A conclusão válida tem a forma: um modelo quantitativo, previamente
especificado, é incompatível com observações dentro de um orçamento de erro.

## Geometria

Para raios lunar e solar (R_M,R_S), distância Sol-Lua (D_{SM}) e distância
Lua-Terra (D_{ME}), o raio da seção umbral num plano normal ao eixo é

\[
r_u=R_M-D_{ME}\frac{R_S-R_M}{D_{SM}}.
\]

Essa seção não é a largura da faixa projetada sobre a superfície terrestre. A
faixa depende da inclinação do eixo, curvatura terrestre, perfil do limbo,
topografia e velocidade relativa.

Os cálculos reproduzíveis em
[`hub/data/reference-calculations.json`](../../hub/data/reference-calculations.json)
mostram também por que a distância média de 384.400 km não deve ser inserida
automaticamente num eclipse total: com os demais valores médios fixados, o raio
do cone já seria negativo nesse plano. O eclipse de 1994 ocorreu próximo ao
perigeu; é indispensável usar distâncias dependentes do tempo.

## Teorema de correspondência fraca

Seja (M) um modelo que determina um vetor preditivo (P_M), seja (O) o
vetor observado e seja (Sigma) o modelo de erro. Defina

\[
R_M=\|\Sigma^{-1/2}(P_M-O)\|_2.
\]

Se (R_M>K), se os parâmetros foram fixados antes da comparação e se não há
graus de liberdade não contabilizados, então o par modelo-parâmetros é
incompatível com os dados no nível codificado por (K).

## Estudo de caso

O eclipse total de 3 de novembro de 1994 atravessou o sul do Brasil. O vetor de
referência deve separar circunstâncias locais em Criciúma dos valores do máximo
global sobre o Atlântico. Não se identifica diretamente a distância média
Terra-Lua a partir de uma única largura observada.

## Limites

- não refuta uma família indefinida de “modelos planos”;
- não transfere validade empírica para uma conjectura matemática;
- não converte previsão computável de eclipse em (P=NP);
- não converte suavidade observada de plasma em regularidade global de
  Navier-Stokes;
- não cria ligação analítica com os zeros de (zeta).
