# Árvore canônica do repositório

```text
federated-trivalent-manifold/
├── .github/workflows/
│   ├── formal.yml              # Python, Lean e Agda
│   └── pages.yml               # publicação do aplicativo
├── app/
│   ├── index.html              # shell acessível e metadados
│   ├── app.js                  # interação e simuladores
│   ├── data.js                 # catálogo visual dos sete programas
│   ├── styles.css              # sistema visual responsivo
│   ├── manifest.webmanifest    # instalação PWA
│   ├── sw.js                   # funcionamento offline
│   ├── icon.svg
│   ├── robots.txt
│   └── sitemap.xml
├── docs/
│   ├── architecture/
│   │   └── repository-tree.md
│   ├── articles/
│   │   ├── eclipse-correspondence.md
│   │   └── research-os-methodology.md
│   ├── formal/
│   │   └── lemma-tree.md
│   ├── problems/
│   │   ├── riemann-audit/      # PDFs, LaTeX e imagens
│   │   └── *.md                # caderno de cada problema
│   ├── fundamentos.md
│   ├── matriz-milenio.md
│   └── roadmap.md
├── hub/
│   ├── data/
│   │   ├── research-tree.json
│   │   ├── research-tree.schema.json
│   │   └── reference-calculations.json
│   ├── formal/
│   │   ├── lean/               # projeto Lake compilável
│   │   └── agda/Audit.agda     # núcleo sem postulados
│   ├── python/
│   │   ├── src/ftm_hub/        # motor e CLI
│   │   ├── tests/              # testes unitários
│   │   └── pyproject.toml
│   └── README.md
├── .gitignore
└── README.md
```

## Fluxo de dados

```text
artigos e observações
        ↓
research-tree.json + schema
        ↓
motor Python ──→ cálculos de referência
        ↓
classificador de estados
        ↓
Lean/Agda verificam invariantes do classificador
        ↓
FTM Observatory apresenta a árvore
        ↓
GitHub Actions repete testes e publica a PWA
```

## Fonte de verdade

- proposições e estados: `hub/data/research-tree.json`;
- significado lógico: `docs/formal/lemma-tree.md`;
- validação executável: `hub/python/src/ftm_hub/audit.py`;
- invariantes mecanizados: `hub/formal/lean` e `hub/formal/agda`;
- apresentação: `app/`.

Duplicações visuais em `app/data.js` são uma projeção editorial e não substituem
a base formal JSON.
