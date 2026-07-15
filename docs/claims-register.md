# Registro de afirmações

Este arquivo é a fonte de verdade para o estado lógico do projeto.

## Estados permitidos

- **DEFINITION:** convenção adotada.
- **PROVED:** prova completa no repositório, com dependências verificadas.
- **CITED:** teorema externo com referência exata e hipóteses conferidas.
- **CONDITIONAL:** provado supondo itens explicitamente listados.
- **OPEN:** enunciado preciso sem prova.
- **HEURISTIC:** evidência numérica, física ou analógica.
- **REFUTED:** contraexemplo conhecido.

## Registro v0.1

| ID | Afirmação | Estado | Dependências |
|---|---|---|---|
| FTM-D1 | célula trivalente decorada como quíntupla | DEFINITION | fundamentos |
| FTM-D2 | atlas federado e cociclos | DEFINITION | FTM-D1 |
| FTM-T0 | descida efetiva produz objeto global bem comportado | OPEN | categoria e hipóteses de colagem |
| P-CONSTR | triangulações de 3-variedades induzem objetos FTM | OPEN | FTM-T0 |
| P-MOVE | movimentos de Pachner induzem equivalências FTM | OPEN | P-CONSTR |
| H-DESC | hipercobertura FTM calcula cohomologia | OPEN | FTM-T0 |
| H-TYPE | descida preserva decomposição de Hodge | OPEN | H-DESC |
| H-CYCLE | ciclos locais compatíveis algebrizam globalmente | OPEN | H-TYPE |
| YM1–YM5 | regularização, limite, não trivialidade e gap | OPEN | FTM-T0 + QFT construtiva |
| NS1–NS4 | consistência até controle crítico | OPEN | operadores discretos definidos |
| C1–C4 | codificação e classificação de FTM-DESCENT | OPEN | modelo finito |
| RH1–RH4 | operador, determinante e equivalência com RH | OPEN | construção espectral |
| BSD1–BSD5 | fatores locais até equivalência BSD | OPEN | categoria FTM aritmética |

## Regra de promoção

Nenhum item muda para PROVED por edição apenas deste quadro. A promoção exige:

1. enunciado versionado;
2. prova completa ou verificação formal;
3. auditoria das dependências;
4. testes de casos-limite;
5. revisão independente registrada.

CONDITIONAL nunca deve ser apresentado sem suas hipóteses.
