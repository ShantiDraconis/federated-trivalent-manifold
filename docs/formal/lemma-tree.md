# Árvore formal de detecção e auditoria

## 1. Contrato do sistema

O sistema operacional de pesquisa não decide nenhum Problema do Milênio. Ele
recebe observações, hipóteses e certificados, aplica regras explícitas e devolve
uma classificação lógica:

- `PROVED`: consequência demonstrada a partir de dependências aceitas;
- `FINITE_CERTIFICATE`: verificação limitada por dimensão, altura ou precisão;
- `CONDITIONAL`: válida sob hipóteses declaradas;
- `EQUIVALENT`: reformulação equivalente ao problema aberto;
- `CONJECTURAL`: programa sem ponte demonstrada;
- `REFUTED`: incompatível com um contraexemplo ou cálculo certificado;
- `OPEN`: obrigação ainda não satisfeita.

Nenhum caminho de estados finitos para `PROVED` é permitido sem um lema de
passagem ao limite e a verificação de todas as suas hipóteses.

## 2. Núcleo lógico comum

### Definição C0 - Nó de conhecimento

Um nó é uma sêxtupla

\[
N=(id,P,H,D,S,E),
\]

onde `id` é estável, \(P\) é uma proposição, \(H\) são hipóteses, \(D\) são
dependências, \(S\) é o estado lógico e \(E\) é a evidência auditável.

### Lema C1 - Monotonicidade de dependências

Se um nó depende de outro nó `OPEN`, `CONJECTURAL` ou `REFUTED`, ele não pode
receber estado `PROVED` apenas por propagação automática.

**Prova.** Uma derivação válida exige todas as premissas. Uma premissa não
demonstrada não autoriza a regra de introdução da conclusão. Uma premissa
refutada torna a derivação inválida. \(\square\)

### Lema C2 - Barreira finito-universal

Uma família de certificados \(C_N\), verificada apenas para \(N\le N_0\), não
implica \(\forall N\,C_N\).

**Prova.** O modelo que satisfaz os primeiros \(N_0\) casos e falha em
\(N_0+1\) é logicamente compatível com as premissas finitas. \(\square\)

### Lema C3 - Barreira de amostragem

Uma propriedade observada num conjunto finito de parâmetros não implica sua
validade em domínio contínuo ou ilimitado sem regularidade e controle de erro.

### Lema C4 - Teste contrafactual de circularidade

Se a construção de um detector deixa de existir assim que se admite um
contraexemplo hipotético ao teorema-alvo, então a construção contém uma
hipótese equivalente ou mais forte que o alvo.

### Teorema C5 - Segurança classificatória

Se C1-C4 forem aplicados em cada transição, o motor nunca promove sozinho uma
evidência finita ou conjectural a prova universal.

## 3. Subárvore de Riemann

Escreva \(\rho=\tfrac12+\delta+i\gamma\) e
\(\rho^\sharp=1-\bar\rho=\tfrac12-\delta+i\gamma\).

### Lema RH-L1 - Simetria do par funcional

Se \(\rho\) é zero não trivial de \(\zeta\), então conjugação e equação
funcional geram os zeros simétricos, com multiplicidades correspondentes.

### Lema RH-L2 - Detector geométrico

Para

\[
R_c^2=\gamma^2+\tfrac14,\qquad
R_\pm^2=R_c^2\pm\delta+\delta^2,
\]

valem

\[
\delta=\frac{R_+^2-R_-^2}{2},\qquad
\Delta_{\rm par}=\frac{R_+^2+R_-^2}{2}-R_c^2=\delta^2\ge0.
\]

**Prova.** Soma e subtração direta das definições. \(\square\)

### Lema RH-L3 - Peso radial positivo

Com \(A=\gamma^2+\tfrac14+\delta^2\),

\[
w(\delta,\gamma)=\frac{2\delta^2}{A^2-\delta^2}\ge0,
\]

e \(w=0\) se e somente se \(\delta=0\), no domínio dos zeros não triviais.

### Lema RH-L4 - Supressão em grande altura

Para \(\delta\) fixo,

\[
w(\delta,\gamma)=\frac{2\delta^2}{\gamma^4}
-\frac{4\delta^2(\tfrac14+\delta^2)}{\gamma^6}+O(\gamma^{-8}).
\]

### Definição RH-D5 - Detectores de cauda

Para uma função de erro não nula e diferenciável \(T(x)\), defina

\[
G_0(x)=\frac{\log|T(x)|}{\log x},\qquad
\sigma_D(x)=x\frac{T'(x)}{T(x)},
\]

e, onde \(I(x)=\int_{x_0}^xT(t)\,dt\ne0\),

\[
\sigma_I(x)=\frac{xT(x)}{I(x)}-1.
\]

### Lema RH-L6 - Modelo de potência lentamente variável

Se \(T(x)=x^\sigma L(x)\), com \(L(x)>0\), diferenciável,
\(\log L(x)/\log x\to0\) e \(xL'(x)/L(x)\to0\), então

\[
G_0(x)\to\sigma,\qquad \sigma_D(x)\to\sigma.
\]

**Prova.** Substituição direta e diferenciação logarítmica. \(\square\)

### Lema RH-L7 - Detector integral sob regularidade

Se, além das hipóteses de RH-L6, \(L\) é lentamente variável e
\(\sigma>-1\), então o teorema de Karamata fornece

\[
I(x)\sim\frac{x^{\sigma+1}L(x)}{\sigma+1},
\qquad \sigma_I(x)\to\sigma.
\]

O lema não se aplica diretamente a uma cauda oscilatória com cancelamentos e
zeros frequentes.

### Lema RH-L8 - Singularidade dos detectores brutos

Se \(T(x_*)=0\), então \(G_0\) e \(\sigma_D\) não estão definidos em \(x_*\).
Logo estacionariedade pontual não caracteriza uma classe assintótica.

### Definição RH-D9 - Regularização quadrática

Em \(u=\log x\), para janela \(H>0\), defina

\[
A_H(u)=\left(\frac1H\int_{u-H/2}^{u+H/2}|T(e^v)|^2\,dv\right)^{1/2}.
\]

Ela evita cancelamento de sinal, mas sua interpretação espectral exige um lema
uniforme sobre a janela e os termos truncados.

### Conjectura RH-C10 - Persistência coerente

Uma classe candidata \(C(\sigma_0)\) requer, numa faixa logarítmica crescente,
coerência entre versões regularizadas de \(G_0,\sigma_D,\sigma_I\), estabilidade
sob mudança de janela e erro certificado. A equivalência entre essa persistência
e a existência de zero com parte real \(\sigma_0>1/2\) permanece `OPEN`.

### Teorema RH-E11 - Nó equivalente

Qualquer teorema incondicional que exclua toda classe persistente
\(\sigma_0>1/2\), com uma ponte provada entre classes e zeros, é pelo menos tão
forte quanto a RH. Portanto esse nó deve ser marcado `EQUIVALENT`, não
`PROVED`, enquanto a ponte não for demonstrada.

## 4. Subárvores dos demais problemas

### P versus NP

- `P-N1`: fixar codificação binária e medida de tamanho;
- `P-N2`: provar verificação polinomial do certificado;
- `P-N3`: construir redução many-one explícita;
- `P-N4`: provar limite inferior contra todos os algoritmos do modelo;
- `P-GAP`: superar ou contornar relativização, natural proofs e algebrização.

### Navier-Stokes

- `NS-N1`: existência local no espaço funcional escolhido;
- `NS-N2`: identidade ou desigualdade de energia;
- `NS-N3`: consistência e compacidade de aproximações;
- `NS-N4`: estimativa uniforme em norma crítica;
- `NS-GAP`: impedir blow-up ou produzir cenário admissível de ruptura.

### Yang-Mills e gap de massa

- `YM-N1`: regularização finita positiva;
- `YM-N2`: estimativas uniformes em malha e volume;
- `YM-N3`: limite contínuo com axiomas de reconstrução;
- `YM-N4`: não trivialidade;
- `YM-GAP`: gap positivo sobrevivendo aos limites.

### Hodge

- `H-N1`: domínio suave e projetivo sobre \(\mathbb C\);
- `H-N2`: cálculo correto da decomposição de Hodge;
- `H-N3`: compatibilidade do mapa de ciclos;
- `H-GAP`: sobrejetividade racional para classes \((p,p)\).

### Birch-Swinnerton-Dyer

- `BSD-N1`: fatores locais e condutor;
- `BSD-N2`: continuação e produto global de \(L(E,s)\);
- `BSD-N3`: posto, alturas e regulador;
- `BSD-N4`: Selmer e controle de \(\Sha\);
- `BSD-GAP`: igualdade entre ordem de anulação e posto, com fórmula refinada.

### Poincaré como banco de validação

- `PC-N1`: codificar triangulações e espinhas;
- `PC-N2`: invariância sob movimentos de Pachner;
- `PC-N3`: preservar \(\pi_1\) e tipo PL;
- `PC-TEST`: recuperar corretamente casos conhecidos, sem alegar nova prova.

## 5. Regra operacional final

O motor pode detectar incoerência, dependências abertas, regressões numéricas e
possíveis comportamentos adversariais. Ele não pode declarar um Problema do
Milênio resolvido. Esse estado só pode ser importado após prova completa,
revisão especializada e atualização explícita da base de conhecimento.
