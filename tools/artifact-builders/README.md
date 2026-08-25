# Geradores de artefatos

- `build_dossier.py`: gera as doze visualizações e os três fontes LaTeX.
- `render_pdfs.py`: produz os PDFs finais com ReportLab.

Os scripts gravam resultados em `outputs/`, que é uma área de build local. Os
artefatos publicados permanecem em `docs/problems/riemann-audit/`.

```bash
python tools/artifact-builders/build_dossier.py
python tools/artifact-builders/render_pdfs.py
```

Dependências: Python 3.11+, NumPy, Matplotlib, Pillow e ReportLab.
