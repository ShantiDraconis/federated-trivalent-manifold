# Auditoria estrutural da Hipótese de Riemann

Este diretório reúne o pacote técnico sobre o detector geométrico
\(\Delta_{\mathrm{par}}=\delta^2\), o defeito radial, a forma de Weil,
matrizes de Gram truncadas e o teste de circularidade para extensões por
\(\epsilon^2=\Delta_{\mathrm{par}}\).

> **Estado científico:** o material não reivindica uma prova da Hipótese de
> Riemann. Identidades locais, certificados finitos, equivalências e hipóteses
> conjecturais são classificados separadamente.

## Documentos PDF

- [Dossiê de auditoria](pdf/dossie-auditoria-rh.pdf): exposição matemática e
  classificação lógica completa.
- [Atlas de visualizações](pdf/atlas-visualizacoes.pdf): doze diagramas e
  gráficos detalhados.
- [Caderno de fórmulas](pdf/caderno-formulas.pdf): fórmulas, expansões e
  checklist de não circularidade.

## Fontes reproduzíveis

- [Dossiê em LaTeX](latex/dossie-auditoria-rh.tex)
- [Atlas em LaTeX](latex/atlas-visualizacoes.tex)
- [Caderno em LaTeX](latex/caderno-formulas.tex)
- [`images/`](images/) contém cada visualização em PNG e PDF vetorial.
- [`archive/README-geracao.md`](archive/README-geracao.md) preserva as instruções
  do pacote gerado antes da integração. Todos os componentes do pacote estão
  versionados individualmente neste diretório.

## Conteúdo visual

1. detector geométrico local;
2. quarteto funcional e simetrias;
3. parábola do defeito local;
4. peso radial versus desvio;
5. decaimento com a altura;
6. mapa multiescala de invisibilidade;
7. condicionamento numérico;
8. hierarquia do defeito não holomorfo;
9. classificação lógica;
10. três vias de fechamento;
11. teste explícito de circularidade;
12. matriz hermitiana ilustrativa de dimensão 13.

## Limite lógico auditado

O pacote separa as identidades elementares

\[
\delta=\frac{R_+^2-R_-^2}{2},\qquad
\Delta_{\mathrm{par}}
=\frac{R_+^2+R_-^2}{2}-R_c^2
=\delta^2
\]

da passagem global ainda aberta para
\(\mathfrak D_{\mathrm{rad}}=0\), positividade universal da forma de Weil ou
positividade de uma família completa de matrizes de Gram com controle uniforme
do limite.
