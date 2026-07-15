# Auditoria v4.1

## Escopo

Esta auditoria separa formalmente hipótese, teorema, simulação e alegação operacional.

| ID | Alegação | Classe | Estado |
|---|---|---|---|
| H1 | epsilon é estritamente positivo | hipótese/parametrização | declarada |
| T1 | W(n+1)=W(n)+epsilon+s(n)^2 é estritamente crescente | teorema aritmético | formalizável |
| H2 | o score representa risco real | hipótese de modelo | não validada |
| H3 | limiar do score melhora segurança/disponibilidade | hipótese causal | não validada |
| E1 | testes executam sem regressão nas amostras | evidência experimental | limitada à amostra |
| C1 | o controlador é imune a DoS | alegação de segurança | não demonstrada |
| C2 | a matriz Div mede proximidade dos Problemas do Milênio | alegação matemática | mal posta sem métrica/dados |
| C3 | a arquitetura resolve Problema do Milênio | alegação matemática | falsa/não demonstrada |

## Correções obrigatórias

1. Somente AES-128/192/256 são nomes padronizados pelo FIPS 197. O projeto usa AES-256 como rótulo de política; não implementa criptografia.
2. T1 prova crescimento aritmético do regulador, não disponibilidade, isolamento ou segurança.
3. Testes de carga são evidência empírica e devem registrar hardware, software, distribuição, duração e erros.
4. Div é apenas uma matriz configurada enquanto espaço de características, métrica, pesos, calibração e incerteza não forem definidos.
5. Lean/Coq/Agda/Isabelle verificam a proposição codificada, não a adequação do score ao mundo.

## Critério de publicação

O paper deve distinguir: Definições; Hipóteses H1-H3; Teorema incondicional T1; Evidência E1; Limitações; e Trabalhos futuros. Nenhuma conclusão operacional pode usar T1 sem uma ponte causal provada.
