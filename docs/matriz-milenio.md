# Matriz de ligação com os Problemas do Milênio

## Legenda

- **Direta:** o formalismo instancia objetos do enunciado oficial.
- **Instrumental:** fornece discretização, linguagem ou invariantes.
- **Analógica:** semelhança estrutural sem implicação lógica conhecida.
- **Ausente:** ainda não existe mapa matemático definido.

O padrão normativo é a [descrição oficial do CMI](https://www.claymath.org/millennium-problems/). Nenhuma linha constitui solução.

| Problema | Ligação inicial | Interface possível | Obrigação antes de alegação forte |
|---|---|---|---|
| Poincaré (resolvido) | direta/instrumental | decomposições trivalentes, triangulações, fluxo de Ricci | representar as 3-variedades relevantes e preservar \(\pi_1\), curvatura e singularidades |
| Hodge | instrumental/analógica | variedades projetivas complexas, complexos celulares, classes de ciclo | exigir \(X/\mathbb C\) suave e projetiva; provar compatibilidade com Hodge e mapa de ciclo racional |
| Yang–Mills e gap | instrumental | fibrados, conexões locais e descida; redes | construir QFT não trivial em \(\mathbb R^4\) e gap uniforme no limite contínuo; gap finito não basta |
| Navier–Stokes | instrumental | discretização e domínios colados | consistência, estabilidade e convergência; estimativa crítica uniforme que implique suavidade ou blow-up admissível |
| P versus NP | analógica/instrumental | reconhecimento e consistência local-global | linguagem, codificação binária, tamanho, verificador e reduções polinomiais |
| Riemann | analógica | operador espectral ou zeta do complexo | identidade rigorosa com \(\xi(s)\) e equivalência lógica; ajuste numérico não basta |
| Birch–Swinnerton-Dyer | analógica/instrumental | modelos de redução de curvas e descida aritmética | recuperar \(L(E,s)\), posto, regulador, Tamagawa e Tate–Shafarevich |

## Poincaré: banco de validação

A conjectura já foi resolvida. O formalismo deve funcionar como teste: uma 3-variedade fechada e simplesmente conexa precisa ser compatível com \(S^3\).

**P1.** Definir um funtor de triangulações ou espinhas trivalentes para 3-variedades e provar invariância sob movimentos que ligam apresentações equivalentes.

## Hodge

Uma variedade topológica ou suave genérica está fora do enunciado.

**H1.** Para \(X/\mathbb C\) suave e projetiva, construir um complexo global e provar que restrições respeitam \(H^{p,q}(X)\), cup product e classes de ciclos algébricos.

## Yang–Mills e gap de massa

Descida de conexões é natural, mas o problema exige construção quântica rigorosa em quatro dimensões e gap positivo.

**YM1.** Para regularizações de malha \(a\), provar limites uniformes, existência do limite \(a\to0\), axiomas pertinentes e passagem de \(\inf_a\Delta_a>0\) ao limite.

## Navier–Stokes

Malhas trivalentes podem apoiar métodos numéricos, mas o problema oficial pergunta existência e suavidade global ou breakdown em 3D.

**NS1.** Definir gradiente, divergência e Laplaciano discretos; provar incompressibilidade, desigualdade de energia, consistência e convergência. O passo decisivo é estimativa uniforme em escala crítica.

## P versus NP

“Federação” só toca complexidade depois de uma codificação finita.

**C1.** Definir FTM-CONSISTENCY: dada uma apresentação finita, existe dado global que satisfaz os cociclos? Fixar representação, tamanho e certificado e classificar por reduções. NP-completude desse problema não prova \(P\ne NP\).

## Hipótese de Riemann

Zetas de grafos podem imitar zetas aritméticas sem identificar seus zeros.

**RH1.** Construir \(D\) e provar, não postular,
\[
\det_{\rm reg}(D-s)=E(s)\xi(s),
\]
com \(E\) explícita e sem zeros relevantes, domínio, auto-adjunticidade e regularização justificados. Só então propriedades espectrais poderiam implicar RH.

## Birch–Swinnerton-Dyer

Modelos de grafos aparecem em degenerações, mas BSD é uma igualdade aritmética global fina.

**BSD1.** Para cada curva elíptica \(E/\mathbb Q\), construir functorialmente \(F(E)\) que recupere fatores locais do \(L\)-funcional e os termos da fórmula principal. Provar equivalência, não correlação.

## Conclusão auditável

A ligação hoje mais sólida é metodológica com 3-variedades e com descida de conexões de gauge. As demais são programas instrumentais ou analógicos. Não há, neste estágio, cadeia de implicações para qualquer problema ainda aberto.
