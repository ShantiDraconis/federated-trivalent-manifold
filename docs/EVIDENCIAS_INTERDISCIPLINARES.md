# Árvore de evidências interdisciplinares do HMOS v4.1

## Escopo

Este documento separa teoremas, hipóteses abertas, resultados numéricos e
analogias. O HMOS é um modelo de controle auditável; ele não prova nem refuta
problemas do milênio. Os estados `conditional`, `bounded` e `empirical`
classificam a evidência disponível, não constituem um terceiro valor de verdade.

## Árvore lógica

```text
Lógica clássica + aritmética real
├── Definições verificáveis
│   ├── epsilon = 10^-6
│   ├── W_step(w,l) = w + l + epsilon
│   ├── A(alpha,beta,t,e) = alpha*t² - beta*e²
│   └── S_eff² = A²
├── Teoremas incondicionais
│   ├── epsilon > 0
│   ├── l >= 0  →  w < W_step(w,l)
│   ├── A² = 1  ↔  A = 1 ou A = -1
│   └── P ou não-P (lógica clássica; não é método de decisão)
├── Hipóteses matemáticas abertas
│   ├── H1: Hipótese de Riemann
│   ├── H2: correlação de pares/GUE para zeros
│   └── H3: BSD e outras conjecturas, quando explicitamente assumidas
├── Evidência computacional
│   ├── zeros verificados em faixas finitas
│   ├── simulações do gateway
│   └── testes de regressão
└── Analogias de projeto (sem implicação matemática)
    ├── Rayleigh–Bénard ↔ transição de regime
    ├── potencial de ação ↔ detector por limiar
    ├── redox ↔ oscilação da série eta
    └── cosmologia ↔ ação acumulada
```

## Painéis e estatuto

| Área | Objeto | Estatuto | Conclusão permitida | Conclusão não permitida |
|---|---|---|---|---|
| Aritmética | Fórmula de Riemann–von Mangoldt | Teorema clássico | Conta assintoticamente zeros até altura `T` | Não localiza todos na reta crítica |
| Aritmética | zeros computados com parte real `1/2` numa faixa finita | Evidência limitada | Teste finito de consistência com RH | Prova de RH |
| Álgebra | peso `Div = 0.0641` | Parâmetro empírico | Calibração reproduzível do modelo | Constante de ZFC ou ligação Riemann–BSD |
| Física | `1-(sin(pi*x)/(pi*x))²` | Heurística/conjectura GUE | Modelo estatístico de correlação | RH ou Yang–Mills |
| Química | eta alternada como oscilação redox | Analogia | Visualização de alternância | Lei química derivada |
| Geofísica | limiar normalizado `S_eff²=1` | Escolha de projeto | Regra de chaveamento | Número de Rayleigh universal |
| Neurociência | gradiente `0.99`, margem `0.01` | Escolha de projeto | Detector de evento | Modelo biofísico de neurônio |
| Sistemas | incremento `10^-6` | Teorema sobre o modelo | Liveness do contador discreto | Disponibilidade ou imunidade a DoS |
| Cosmologia | integral de erro | Definição de custo | Agregação temporal | Lei cosmológica |

## Cálculos exatos dos parâmetros fornecidos

Com `alpha=0.10`, `beta=0.10887`, `t=3.155` e `e=0.3`:

```text
alpha*t²                 = 0.99540250
beta*e²                  = 0.0097983
A                         = 0.98560420
S_eff²                    = 0.97141563905764
beta para A=0 em e=0.3   = 11.060027777777...
```

O limite `S_eff²=1` equivale a `A=1` **ou** `A=-1`. Para os valores acima:

- ramo `A=1`: `beta*e²=alpha*t²-1=-0.0045975`; não há `e` real;
- ramo `A=-1`: `e=sqrt((alpha*t²+1)/beta) ≈ 4.2812`.

Logo, tratar o limite como um único ramo é incorreto. A formalização Lean prova a
equivalência dos dois ramos.

## Eta de Dirichlet e erro de truncamento

Para `s=sigma+i*tau`, `eta(s)=sum (-1)^(n-1)n^(-s)` converge para `sigma>0`,
mas os termos complexos não formam uma sequência alternada real. Portanto, o
limite elementar `|R_N| <= (N+1)^(-sigma)` só é usado neste projeto para
`tau=0`. Um limite conservador obtido por soma de Abel, registrado no script, é

```text
|R_N(s)| <= (1 + |s|/sigma) (N+1)^(-sigma), sigma > 0.
```

Em `sigma=0.5`, `tau≈14.134725`, `N=100`, o limite real seria `≈0.09950`,
enquanto o conservador complexo é `≈2.91`. Assim, um truncamento ingênuo com
`N=100` não certifica um zero na primeira altura crítica. Certificação requer
aritmética intervalar e limites específicos mais fortes.

## Forma correta da contagem de zeros

A forma principal é

```text
N(T) = T/(2*pi) log(T/(2*pi)) - T/(2*pi) + O(log T).
```

O termo `-T/(2*pi)` não deve ser omitido quando se apresenta a aproximação como
fórmula quantitativa. Ainda assim, a contagem não implica RH.

## Dependências formais

Os três arquivos de prova compartilham o mesmo núcleo: positividade de
`epsilon`, crescimento estrito de um passo com carga não negativa, terceiro
excluído e transporte de uma conclusão condicional. Lean é o artefato compilado
neste repositório. Coq e Isabelle são traduções independentes que devem ser
verificadas por seus próprios kernels antes de receber o estado `proved`.

## Critério de publicação

Uma alegação recebe `proved` somente se houver enunciado, hipóteses explícitas,
certificado e verificador identificado. Resultados numéricos recebem `bounded`
ou `empirical`; conjecturas recebem `open` ou `conditional`; analogias permanecem
analogias. Nenhum teste finito promove uma conjectura aberta a teorema.
