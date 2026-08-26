# Auditoria técnica — programa \Omega_p

## Escopo
Este documento consolida os pontos críticos de rigor para evitar circularidade, ambiguidades semânticas e extrapolações não demonstradas no programa \(\Omega_p\).

## Pontos críticos e correções obrigatórias

### 1) Convenção de resíduo no infinito
- **Risco:** usar \(\operatorname{Res}_\infty f\) como “coeficiente de \(1/z\)” sem declarar convenção.
- **Padrão clássico:** \(\operatorname{Res}_\infty f = -a_{-1}\), onde \(a_{-1}\) é o coeficiente de \(1/z\).
- **Correção:** declarar na seção de notação qual convenção é usada e manter sinal consistente em todo artigo.

### 2) Mistura de objetos sem definição unívoca
- **Risco:** \(\Omega_p\), \(\bot\), “infinito comprimido” e “eixos” aparecem como número, símbolo algébrico e limite analítico ao mesmo tempo.
- **Correção:** separar camadas formais:
  1. camada não padrão (ultrapotência),
  2. camada analítica (funções/expansões assintóticas),
  3. camada algébrica estendida (wheel/estrutura parcial).

### 3) Salto de heurística local para teorema global
- **Risco:** expansões de \(f_1, f_2, f_{avg}\) são locais e não implicam universalidade sem hipóteses adicionais.
- **Correção:** incluir lema de passagem (hipóteses, domínio de validade e limite de erro) antes de qualquer teorema de universalidade.

### 4) Identificação \(0/0 = \bot = \Omega_p\)
- **Risco:** incompatível com análise/álgebra clássica quando não há axiomatização explícita do sistema estendido.
- **Correção:** separar formalmente:
  - resultados no sistema clássico,
  - resultados condicionais no sistema estendido.

### 5) Conexão com RH insuficiente
- **Risco:** afirmações sobre zeros “fora da linha” sem definição completa de \(\zeta_{\Omega_p}\), domínio e relação com \(\zeta\) clássica.
- **Correção:** exigir definição formal de \(\zeta_{\Omega_p}\), teoremas de compatibilidade e critérios de falsificação.

### 6) Constantes \(C_1,\dots,C_6\)
- **Risco:** apenas valores numéricos sem problema bem-posto (equações exatas, unicidade, erro numérico).
- **Correção:** para cada constante, fornecer:
  - equação de definição,
  - intervalo de existência,
  - prova/justificativa de unicidade,
  - método numérico e erro certificado.

### 7) Dependências lógicas entre artigos
- **Risco:** circularidade entre artigos de base e artigos de aplicação.
- **Correção:** manter DAG acíclico explícito, com pré-requisitos formais por artigo e sem uso antecipado de resultados futuros.

## Matriz de status lógico obrigatória
Cada afirmação central deve ser rotulada como:
- **Teorema provado** (com prova completa no texto),
- **Teorema condicional** (hipóteses explícitas),
- **Conjectura/programa** (sem prova).

## Testes de rejeição editorial (gatekeeping)
Antes de submeter, verificar:
1. ausência de ambiguidade de notação;
2. ausência de circularidade entre resultados;
3. distinção explícita entre evidência numérica e demonstração;
4. limites de aplicabilidade e falsificabilidade descritos;
5. nenhuma extrapolação para Problemas do Milênio sem ponte teórica completa.
