#!/usr/bin/env bash
# build_finais.sh — Federated Trivalent Manifold
# Builds the 7 prize-paper final skeletons (F1–F7) into PDFs.
# Run after build_all.sh or independently.
# Usage: ./build_finais.sh [--skip-latex]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAPER_DIR="$ROOT/paper"
OUT_DIR="$ROOT/output/finais"

SKIP_LATEX=false
for arg in "$@"; do
  [[ $arg == "--skip-latex" ]] && SKIP_LATEX=true
done

FINALS=(
  F1_Riemann_Annals
  F2_PvsNP_JACM
  F3_NavierStokes_Annals
  F4_Hodge_JAMS
  F5_Poincare_Annals
  F6_BSD_Inventiones
  F7_YangMills_CMP
)

sep() {
  echo
  echo "══════════════════════════════════════════════════════════"
  echo "  $*"
  echo "══════════════════════════════════════════════════════════"
}

sep "build_finais.sh — 7 Prize-Paper Skeletons"
echo "  Framing rule: BARRIER = proven / HYPOTHESIS = axiom + TODO PROVAR \$1M"
echo "  F3 critical rule: e=-0.0459 is NUMERICAL, NOT a Navier-Stokes proof"

# ── Step 1: verify Python checks pass ────────────────────────────────────────
sep "STEP 1 — Verify Phase-1 lemmas"
python3 "$ROOT/simulations/verifica_lemas.py"

# ── Step 2: LaTeX 7 PDFs ─────────────────────────────────────────────────────
sep "STEP 2 — Compile 7 prize-paper PDFs"

if $SKIP_LATEX; then
  echo "  [skipped via --skip-latex]"
elif ! command -v pdflatex &>/dev/null; then
  echo "  [WARNING] pdflatex not found — skipping"
else
  mkdir -p "$OUT_DIR"
  FAILED=0
  for NAME in "${FINALS[@]}"; do
    TEX="$PAPER_DIR/$NAME/main.tex"
    if [[ ! -f "$TEX" ]]; then
      echo "  [MISSING] $NAME/main.tex — skipping"
      continue
    fi
    echo -n "  Compiling $NAME ... "
    # two passes for table of contents
    if pdflatex -interaction=nonstopmode \
          -output-directory="$PAPER_DIR/$NAME" "$TEX" >/dev/null 2>&1 \
       && pdflatex -interaction=nonstopmode \
          -output-directory="$PAPER_DIR/$NAME" "$TEX" >/dev/null 2>&1; then
      cp "$PAPER_DIR/$NAME/main.pdf" "$OUT_DIR/${NAME}.pdf"
      PAGES=$(pdfinfo "$OUT_DIR/${NAME}.pdf" 2>/dev/null | awk '/Pages:/{print $2}')
      echo "OK (${PAGES:-?} pages)"
    else
      echo "FAILED"
      FAILED=$((FAILED + 1))
    fi
  done
  PDF_COUNT=$(find "$OUT_DIR" -maxdepth 1 -name 'F*.pdf' | wc -l)
  echo
  echo "  PDFs generated: $PDF_COUNT / ${#FINALS[@]}"
  if [[ $FAILED -gt 0 ]]; then
    echo "  [ERROR] $FAILED PDF(s) failed — check LaTeX logs in paper/F*/main.log"
    exit 1
  fi
fi

# ── Step 3: TODO PROVAR checklist ────────────────────────────────────────────
sep "STEP 3 — TODO PROVAR \$1M checklist"
echo "  F1 RH:   Construct self-adjoint H, prove all zeros on Re(s)=1/2"
echo "  F2 PvsNP: Super-polynomial circuit lower bound avoiding all barriers"
echo "  F3 NS:   Prove e_lin(omega)>=0 in omega-limit (NOT from e=-0.0459)"
echo "  F4 Hodge: All rational (p,p)-classes are algebraic for any smooth X"
echo "  F5 PC:   Prove/disprove SPC4 (smooth Poincare in dim 4)"
echo "  F6 BSD:  Full BSD formula for rank>=2 elliptic curves + Sha finite"
echo "  F7 YM:   Construct 4D quantum YM measure + prove mass gap Delta>0"
echo
echo "  All items above are axiom -- TODO PROVAR in formal/lean/Lemas_Master.lean"
echo "  None are claimed as resolved."

# ── Step 4: Zenodo ZIP ────────────────────────────────────────────────────────
sep "STEP 4 — Zenodo ZIP (finais)"
mkdir -p "$ROOT/output"
(cd "$ROOT" && zip -r "output/finais-prize-papers.zip" \
    output/finais/ \
    paper/F1_Riemann_Annals/ \
    paper/F2_PvsNP_JACM/ \
    paper/F3_NavierStokes_Annals/ \
    paper/F4_Hodge_JAMS/ \
    paper/F5_Poincare_Annals/ \
    paper/F6_BSD_Inventiones/ \
    paper/F7_YangMills_CMP/ \
    formal/lean/Lemas_Master.lean \
    formal/coq/Lemas_Master.v \
    formal/isabelle/Lemas_Master.thy \
    simulations/verifica_lemas.py \
    CITATION.cff \
    README.md \
    2>/dev/null || true)
echo "  ZIP: output/finais-prize-papers.zip"

sep "BUILD FINAIS COMPLETE"
echo "  PDFs: $OUT_DIR/"
echo "  ZIP:  $ROOT/output/finais-prize-papers.zip"
