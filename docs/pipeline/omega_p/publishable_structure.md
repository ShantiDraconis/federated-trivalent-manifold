# Estrutura publicável padrão (artigos do programa \Omega_p)

## Sequência recomendada de seções

1. **Introdução**
   - problema, motivação, contribuição, escopo e limitações.
2. **Estado da arte**
   - literatura diretamente relacionada e diferença objetiva da contribuição.
3. **Notação e definições**
   - símbolos, convenções (incluindo \(\operatorname{Res}_\infty\)), axiomas e domínio.
4. **Resultados preliminares (lemas mínimos)**
   - apenas ferramentas estritamente necessárias ao resultado principal.
5. **Teorema principal**
   - enunciado formal com hipóteses completas e verificáveis.
6. **Provas**
   - prova integral, com dependências internas explícitas.
7. **Provado vs. Conjectural**
   - tabela com classificação lógica de cada afirmação relevante.
8. **Limitações e falsificabilidade**
   - fronteiras de validade e condições de refutação empírica/formal.
9. **Conclusão**
   - síntese sem extrapolações além do que foi provado.
10. **Apêndice computacional** (quando houver constantes numéricas)
    - algoritmo, precisão, tolerâncias, semente e reprodutibilidade.

## Critérios mínimos de aceitação interna
- Notação consistente de ponta a ponta.
- Nenhum uso de resultado ainda não demonstrado no próprio artigo ou pré-requisito explícito.
- Toda afirmação numérica com método e erro.
- Declaração explícita do que o artigo **não** prova.

## Dependências lógicas
- Cada artigo deve declarar pré-requisitos formais em formato de DAG.
- Artigos de aplicação (por exemplo, RH/NS) só podem usar definições e teoremas já fechados em artigos de base.
