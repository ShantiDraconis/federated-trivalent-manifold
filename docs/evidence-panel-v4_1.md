# Painel de evidências científicas HMOS v4.1

## Regra de leitura

Uma evidência pode motivar uma hipótese ou validar uma implementação; não substitui uma redução matemática nem prova um Problema do Milênio. Cada entrada declara objeto, valor, proveniência, incerteza/escopo e estatuto.

## E1 - Aritmética: primos e zeros de zeta

| Campo | Registro auditável |
|---|---|
| Resultado incondicional | Teorema dos Números Primos: \(\pi(x)\sim\operatorname{Li}(x)\) |
| Resultado condicional | RH implica estimativas do tipo \(\pi(x)=\operatorname{Li}(x)+O(\sqrt{x}\log x)\), com formulação assintótica e constantes conforme o teorema citado |
| Evidência computacional | Platt-Trudgian verificam rigorosamente RH para todos os zeros com \(0<\gamma\le3\cdot10^{12}\), usando aritmética intervalar |
| Correção da imagem | \(3\cdot10^{12}\) é altura, não contagem de \(10^{13}\) zeros |
| Estatuto HMOS | motivação para H1; não prova RH e não valida segurança |

A fórmula de Riemann-von Mangoldt deve ser citada com a convenção exata para \(S(T)\); “limitada sob RH” é ambíguo e não deve aparecer sem a ordem assintótica pretendida.

## E2 - Física matemática: GUE e caos quântico

A correlação de pares de Montgomery e os cálculos de Odlyzko sustentam uma correspondência estatística entre zeros altos de zeta e estatísticas do GUE. Isso é estrutura estatística/heurística, não periodicidade, não implica que todos os zeros estejam na reta crítica e não é detector de intrusão de rede.

| Objeto | Estatuto |
|---|---|
| \(1-(\sin \pi x/(\pi x))^2\) | lei limite/correlação em normalização apropriada |
| comparação numérica com zeros | evidência estatística |
| “heartbeat quântico” | metáfora/feature experimental, requer estudo de detecção |
| repetição após infinito | rejeitada: não decorre de GUE |

## E3 - Álgebra: funções-L e BSD

Para uma curva elíptica \(E/\mathbb Q\), BSD relaciona a ordem de anulação de \(L(E,s)\) em \(s=1\) ao posto de \(E(\mathbb Q)\). Produto de Euler, continuação analítica e equação funcional pertencem à teoria da função-L; a forma normalizada da equação funcional depende da convenção e do condutor.

O peso HMOS \(0.0641\) não é consequência de BSD. É parâmetro de projeto H2 até que exista:

1. definição da métrica;
2. derivação do peso;
3. invariância sob escolhas de representação;
4. análise de sensibilidade;
5. validação fora da amostra.

Usar valores de \(L(E,s)\) para entropia ou PRNG exige uma construção criptográfica separada. Similaridade estrutural não fornece segurança.

## E4 - Engenharia: HMOS v4.1

| Quantidade | Valor | Estatuto |
|---|---:|---|
| incremento discreto do regulador | \(W'=W+score^2+1\) | teorema Lean/Coq/Agda |
| \(\epsilon_{margin}\) | 0.01 | parâmetro calibrado H3 |
| \(\alpha^*\) | 0.10 | parâmetro calibrado H3 |
| \(\beta^*\) | 0.10887 | parâmetro calibrado H3 |
| política criptográfica | AES-256 | decisão de engenharia; bloco AES de 128 bits |
| disponibilidade/DoS | não provada | fora do teorema de liveness |

Valores só podem ser chamados “medidos” quando acompanhados por dispositivo, versão, protocolo, amostra, unidade, timestamp, incerteza e dados brutos. Sem isso são valores configurados.

## Operador de truncamento

Em um espaço de sequências, defina

\[
(P_Na)_n=\begin{cases}a_n,&n<N,\\0,&n\ge N.\end{cases}
\]

Então \(P_N^2=P_N\). Em dimensão ambiente finita \(d\), \(\operatorname{Tr}P_N=\min(N,d)\). No espaço infinito, \(P_N\) é de posto finito e o traço é \(N\), depois de fixadas indexação e convenção.

Para

\[
\eta_N(s)=\sum_{n=1}^N(-1)^{n-1}n^{-s},
\]

\(\eta_N\) é inteira. Contudo,

\[
Z_N(s)=\frac{\eta_N(s)}{1-2^{1-s}}
\]

geralmente possui polo em \(s=1\), pois o denominador tem zero simples e \(\eta_N(1)\ne0\). Seu resíduo é

\[
\operatorname{Res}_{s=1}Z_N(s)=\frac{\eta_N(1)}{\log 2},
\]

que tende a 1. Portanto, truncar não “zera o resíduo”.

Se \(N\) é constante no tempo, \([d/dt,P_N]=0\) para sequências diferenciáveis componente a componente. Um cutoff dependente do tempo exige definir \(N(t)\); saltos produzem termos de fronteira/distribucionais. Não existe identidade universal

\[
\|R_N(1/2+it)\|=1/\sqrt{N+1}.
\]

O termo descartado individual em \(n=N+1\) tem módulo \((N+1)^{-\sigma}\), mas isso não é, por si só, a norma da cauda nem de um comutador.

## Três noções que não devem ser confundidas

1. **Horizonte computacional:** limite dependente de formato numérico, escala, algoritmo e tolerância; não existe um \(t_{max}\) universal.
2. **Compactificação por um ponto:** construção topológica \(\mathbb R\cup\{\infty\}\); não cria “último número” nem ponto imediatamente anterior.
3. **Hiperreais:** extensão ordenada com elementos infinitos e infinitésimos; \(10^{-6}\) é real positivo comum, não infinitésimo de Robinson.

Nenhuma dessas construções implica RH, GUE além de todo limite, mass gap, P versus NP, suavidade de Navier-Stokes ou uma política criptográfica.

## Obrigações ainda abertas

- especificar e validar a ponte telemetria \(\Phi\);
- implementar aritmética intervalar e certificados, não limiar de resíduo simples;
- fornecer datasets brutos HMOS e protocolo de medição;
- formalizar estimativas analíticas da cauda em biblioteca apropriada;
- definir modelo de ameaça e provar/testar propriedades de disponibilidade;
- remover linguagem de “solução”, “refutação”, “infinito triplo” e “segurança absoluta”.

## Referências primárias

- Platt, D.; Trudgian, T., *The Riemann hypothesis is true up to \(3\cdot10^{12}\)*.
- NIST DLMF, Chapter 25, Riemann zeta and related functions.
- Clay Mathematics Institute, official BSD problem description.
- NIST FIPS 197, Advanced Encryption Standard.
