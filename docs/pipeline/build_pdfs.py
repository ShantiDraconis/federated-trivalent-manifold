#!/usr/bin/env python3
"""
build_pdfs.py — Script reprodutível de geração de PDFs do pipeline de 24 artigos.

Parâmetros fixos para reprodutibilidade:
  - Engine: pdflatex (TeX Live 2023)
  - Duas passadas para referências cruzadas e índices
  - Saída: docs/pipeline/pdf/

Uso:
    python3 docs/pipeline/build_pdfs.py
    python3 docs/pipeline/build_pdfs.py --only RH.B
    python3 docs/pipeline/build_pdfs.py --only F3

Reprodutibilidade: este script não usa seed nem geração aleatória.
Os PDFs são determinísticos dado o .tex de entrada.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
PIPELINE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PIPELINE_DIR / "pdf"

SOURCES = {
    "RH.B": PIPELINE_DIR / "RH.B" / "RH_B_template.tex",
    "F3": PIPELINE_DIR / "F3-Navier-Stokes" / "F3_NS_skeleton.tex",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def compile_latex(tex_path: Path, out_dir: Path, label: str) -> bool:
    """Compile a .tex file twice with pdflatex, output PDF to out_dir."""
    pdflatex = shutil.which("pdflatex")
    if pdflatex is None:
        print(f"  [ERRO] pdflatex não encontrado. Instale texlive-latex-base.")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        pdflatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={out_dir}",
        str(tex_path),
    ]

    for passada in (1, 2):
        print(f"  [pass {passada}/2] {label} ...", end=" ", flush=True)
        result = subprocess.run(
            cmd, capture_output=True, cwd=tex_path.parent
        )
        stdout_text = result.stdout.decode("latin-1", errors="replace")
        if result.returncode != 0:
            print("FALHA")
            log_lines = stdout_text.splitlines()[-20:]
            print("\n".join(log_lines))
            return False
        print("ok")

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera PDFs do pipeline de 24 artigos.")
    parser.add_argument(
        "--only",
        choices=list(SOURCES.keys()),
        help="Compilar apenas um artigo específico.",
    )
    args = parser.parse_args()

    targets = {args.only: SOURCES[args.only]} if args.only else SOURCES

    print(f"Pipeline de PDFs — {datetime.now(timezone.utc).isoformat()}")
    print(f"Saída: {OUTPUT_DIR}")
    print()

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "engine": "pdflatex (TeX Live 2023)",
        "articles": {},
    }

    success_count = 0
    for label, tex_path in targets.items():
        print(f"[{label}] {tex_path.relative_to(REPO_ROOT)}")
        if not tex_path.exists():
            print(f"  [ERRO] Arquivo .tex não encontrado: {tex_path}")
            continue

        src_sha = sha256_file(tex_path)
        print(f"  SHA256 fonte: {src_sha}")

        ok = compile_latex(tex_path, OUTPUT_DIR, label)
        pdf_path = OUTPUT_DIR / tex_path.with_suffix(".pdf").name

        if ok and pdf_path.exists():
            pdf_sha = sha256_file(pdf_path)
            size_kb = pdf_path.stat().st_size // 1024
            print(f"  PDF gerado: {pdf_path.name} ({size_kb} KB)")
            print(f"  SHA256 PDF: {pdf_sha}")
            manifest["articles"][label] = {
                "source": str(tex_path.relative_to(REPO_ROOT)),
                "source_sha256": src_sha,
                "pdf": str(pdf_path.relative_to(REPO_ROOT)),
                "pdf_sha256": pdf_sha,
                "size_bytes": pdf_path.stat().st_size,
                "status": "ok",
            }
            success_count += 1
        else:
            manifest["articles"][label] = {
                "source": str(tex_path.relative_to(REPO_ROOT)),
                "source_sha256": src_sha,
                "status": "failed",
            }
        print()

    # Write manifest
    manifest_path = OUTPUT_DIR / "manifest.json"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"Manifesto: {manifest_path.relative_to(REPO_ROOT)}")
    print(f"Resultado: {success_count}/{len(targets)} artigo(s) compilado(s) com sucesso.")

    # Print audit checklist reminder
    print()
    print("=" * 60)
    print("CHECKLIST DE AUDITORIA (verificar antes de submeter):")
    print("  [ ] Nenhum numero finito (9999, 25.516, -5e-05) no nucleo?")
    print("  [ ] Lean/Coq compila sem sorry/admit?")
    print("  [ ] E_Res(omega)=0 provado analitico (nao aprox)?")
    print("  [ ] Falsificacao Popper explícita listada?")
    print("  [ ] SHA256 do PDF registrado no manifesto?")
    print("=" * 60)

    return 0 if success_count == len(targets) else 1


if __name__ == "__main__":
    sys.exit(main())
