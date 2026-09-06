"""Render a deliberately scoped, reviewable formal-build record as a PDF."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "ftm_formal_verification_certificate.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Tiny", parent=styles["BodyText"], fontSize=7.5, leading=9.5))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#53636d"))
    canvas.drawString(20 * mm, 12 * mm, "FTM scoped finite-core build record")
    canvas.drawRightString(190 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def p(text, style="BodyText"):
    return Paragraph(text, styles[style])


def build():
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=18 * mm, bottomMargin=20 * mm, title="FTM scoped finite-core build record"
    )
    checks = [
        ["Check", "Result"],
        ["Lean", "4.8.0 / df668f00e6c0"],
        ["Mathlib", "v4.8.0 / b5eba595428809e96f3ed113bc7ba776c5f801ac"],
        ["Scoped Lean build", "SUCCESS before remote integration; re-run on this tree"],
        ["Finite core scan", "0 sorry; 0 admit; 0 Axiom; 0 postulate"],
        ["Repository-wide status", "exploratory files with explicitly documented gaps exist"],
    ]
    table = Table([[p(c, "Tiny") for c in row] for row in checks], colWidths=[55 * mm, 115 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#173b4d")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#80929b")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#eef3f4")]),
    ]))
    story = [
        p("Federated Trivalent Manifold", "Title"),
        p("Scoped Finite-Core Build Record", "Heading1"),
        p("Issued with an explicit boundary on 10 August 2026."),
        Spacer(1, 5 * mm), table,
        p("Certified scope", "Heading1"),
        p(
            "The stated core consists only of no-placeholder finite algebraic and discrete lemmas: reflected-radius identities, non-negativity of a square, a finite delayed-witness construction, elementary natural-number growth, and finite cutoff/drift facts."
        ),
        p("Excluded scope", "Heading1"),
        p(
            "This record is not evidence for the Riemann hypothesis, P versus NP, Navier-Stokes smoothness, Yang-Mills mass gap, Hodge, BSD, black-hole information, cryptographic security, network availability or a unification of those subjects. Explicit assumptions remain assumptions."
        ),
        p("Epistemic verdict", "Heading1"),
        p(
            "Finite numerical eta evaluation can certify non-vanishing under an error bound, but cannot certify an exact zero. Finite resource equivalence does not identify asymptotic complexity classes. The repository includes exploratory modules with placeholders or axioms; they are excluded and catalogued in formal/OPEN_OBLIGATIONS.md."
        ),
        p("Integrity", "Heading1"),
        p(
            "The exact core file list is versioned in formal/VERIFIED_CORE.md. Re-run the relevant GitHub Actions workflow or checker command after every source change; no checker run is implied when its toolchain is unavailable."
        ),
    ]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build()
