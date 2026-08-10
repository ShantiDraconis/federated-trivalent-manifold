# FTM Research Hub

O hub reúne quatro camadas que permanecem logicamente separadas:

1. **Conhecimento:** nós, dependências, estados e evidências em JSON;
2. **Motor:** validação e cálculos reproduzíveis em Python;
3. **Formalização:** invariantes do classificador em Lean 4 e Agda;
4. **Interface:** FTM Observatory em `app/`.

O hub não contém uma prova de qualquer Problema do Milênio. Ele impede que
certificados finitos, analogias físicas ou hipóteses abertas sejam promovidos a
provas universais.

## Comandos

```bash
python -m pip install -e "hub/python[dev]"
ftm-hub validate hub/data/research-tree.json
ftm-hub eclipse --moon-distance 357000
ftm-hub radial --delta 0.1 --gamma 1000
pytest hub/python/tests
```

Para Lean:

```bash
cd hub/formal/lean
lake build
```

O código Agda usa apenas módulos builtin e não contém `postulate`.

## Regra de segurança

Uma conclusão pode ser `PROVED` somente quando todas as dependências exigidas
estão provadas e a regra de inferência é explicitamente reconhecida. O motor
rejeita transições automáticas de `FINITE_CERTIFICATE`, `OPEN`, `CONJECTURAL`
ou `EQUIVALENT` para `PROVED`.
