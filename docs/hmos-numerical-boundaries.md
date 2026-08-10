# HMOS v4.1 — fronteiras numéricas e estatuto epistemológico

## Escopo

Este documento audita a interpretação de somas truncadas de Dirichlet, do polo de \(\zeta\), dos parâmetros do controlador e das pontes propostas para os Problemas do Milênio. O HMOS é um controlador experimental de hipóteses. Não é um decisor para a Hipótese de Riemann, não substitui prova matemática e não transfere resultados de engenharia para os enunciados do Clay Mathematics Institute.

## 1. Eta truncada não certifica zeros

Definimos apenas a quantidade computável

\[
\eta_N(s)=\sum_{n=1}^{N}(-1)^{n-1}n^{-s}.
\]

Para \(\operatorname{Re}(s)>0\), a série infinita de Dirichlet eta converge; a convergência é absoluta apenas para \(\operatorname{Re}(s)>1\). Na borda \(\operatorname{Re}(s)=0\), os termos não tendem a zero em módulo, portanto a série ordinária não converge. Isso não implica que o erro de uma soma finita “cresça exponencialmente”: o comportamento depende de \(s\), \(N\), do método de continuação/aceleração e da precisão numérica.

Um pequeno valor de \(|\eta_N(s)|\) é um candidato numérico dependente do truncamento. Não demonstra \(\eta(s)=0\). Um detector implementável deve registrar no mínimo \(s\), \(N\), precisão, método, resíduo, estimativa/limite de erro e proveniência.

O operador teórico

\[
\delta(s)=\left|\operatorname{Re}(s)-\tfrac12\right|\mathbf 1_{Z_\eta}(s)
\]

é bem definido como objeto matemático depois de definido \(Z_\eta=\{s:\eta(s)=0\}\). Ele não exige que a pertinência a \(Z_\eta\) seja decidível por um algoritmo finito para todo número complexo. O problema de implementação é distinto: entradas complexas arbitrárias não têm representação finita uniforme, e testes numéricos de igualdade a zero exigem certificados analíticos ou intervalares. Portanto, o código deve usar \(\widehat\delta_{N,p,\tau}\), um estimador explicitamente parametrizado, nunca a função indicadora exata.

## 2. O polo está em zeta, não em eta

A função \(\zeta(s)\) possui polo simples em \(s=1\). Já

\[
\eta(s)=(1-2^{1-s})\zeta(s)
\]

tem singularidade removível nesse ponto e \(\eta(1)=\log 2\). Assim, uma visualização pode mostrar a barreira de \(\zeta\), mas não deve atribuir a mesma explosão à eta truncada nem afirmar que tráfego de rede “colide” matematicamente com o polo. Qualquer associação entre telemetria e \(s\) é uma função de engenharia que precisa ser definida e validada separadamente.

## 3. “Falta de parâmetros” é falta de ponte, não defeito dos problemas

Os Problemas do Milênio não estão incompletos por falta de parâmetros. A lacuna está no HMOS quando ele tenta ligar observáveis de rede a objetos analíticos:

1. falta uma função de observação \(\Phi:\text{telemetria}\to\mathbb C\) com domínio, unidades e incerteza;
2. falta um estimador certificado para zero ou distância a um conjunto de zeros;
3. falta uma redução demonstrada entre a propriedade monitorada e o enunciado matemático;
4. faltam garantias de controle e segurança independentes das analogias.

Isso não se resolve apenas “deduzindo uma métrica de ZFC”. ZFC fornece uma fundação possível para formalizar conjuntos e análise, mas não torna automaticamente computável uma distância, não fornece calibração física e não valida uma redução entre domínios.

## 4. Parâmetros do controlador

Se \(\alpha^*=0.10\), \(\beta^*=0.10887\), \(10^{-6}\) e \(\epsilon_{margin}=0.01\) foram escolhidos por calibração, são parâmetros de projeto. Devem ter unidade, intervalo admissível, procedimento de ajuste, análise de sensibilidade e dados de validação.

Uma equação como

\[
\dot{\mathcal W}=(\alpha^*t^2-\beta^*e^2)^2+10^{-6}
\]

permite concluir \(\dot{\mathcal W}\ge10^{-6}>0\) sob os tipos e hipóteses declarados. Isso prova somente crescimento do estado regulador. Não prova atendimento de requisições, resistência a DoS, segurança criptográfica, estabilidade física, RH, BSD ou mass gap.

A variante que adiciona termos sem sinal controlado, como \(+e\), só preserva essa desigualdade se também for assumido/provado \(e\ge0\) ou houver outro limite inferior.

## 5. Política criptográfica

A política do repositório permanece AES-256. Pelo FIPS 197, AES sempre usa blocos de 128 bits e chaves de 128, 192 ou 256 bits. “Rijndael-512”, “bloco estendido de 512 bits” ou chaveamento causado por RH/Yang–Mills não integra a garantia do HMOS v4.1 e não deve aparecer como mecanismo aprovado sem especificação, implementação, análise criptográfica e validação próprias.

## 6. Estados auditáveis

| Estado | Significado | Exemplo |
|---|---|---|
| Definição | símbolo com semântica declarada | \(\eta_N(s)\) |
| Teorema verificado | consequência dedutiva no modelo formal | crescimento discreto de \(W\) |
| Hipótese | premissa ainda não demonstrada | ponte telemetria–objeto analítico |
| Evidência numérica | resultado reprodutível com erro | resíduo de \(\eta_N\) |
| Parâmetro calibrado | escolha empírica documentada | \(\epsilon_{margin}\) |
| Refutado no modelo | contraexemplo dentro do modelo declarado | uma desigualdade que falha para \(e<0\) |
| Fora de escopo | não decorre da implementação | solução de RH ou imunidade a DoS |

## 7. Critério de blindagem

Cada gráfico deve distinguir valor exato, aproximação, limite de erro e hipótese de ponte. Cada mecanismo de segurança deve ser justificado por um modelo de ameaça e por testes próprios. O HMOS permanece defensável ao afirmar:

> O sistema executa um controlador condicional e registra indicadores numéricos. A única garantia formal atual é a propriedade de liveness especificada nos assistentes de prova; nenhuma telemetria decide um Problema do Milênio.

## Referências primárias

- NIST, FIPS 197: Advanced Encryption Standard.
- NIST DLMF, capítulo 25: Riemann zeta e funções relacionadas.
- Clay Mathematics Institute, regras dos Millennium Prize Problems.
