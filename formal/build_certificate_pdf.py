"""Render the scoped formal verification certificate as a reviewable PDF."""

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
    canvas.drawString(20 * mm, 12 * mm, "FTM scoped formal verification certificate")
    canvas.drawRightString(190 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def p(text, style="BodyText"):
    return Paragraph(text, styles[style])


def build():
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=18 * mm, bottomMargin=20 * mm, title="FTM formal verification certificate"
    )
    checks = [
        ["Check", "Result"],
        ["Lean", "4.8.0 / df668f00e6c0"],
        ["Mathlib", "v4.8.0 / b5eba595428809e96f3ed113bc7ba776c5f801ac"],
        ["lake build", "SUCCESS"],
        ["Python", "18 tests passed"],
        ["Ruff", "SUCCESS"],
        ["Lean holes", "0 sorry; 0 admit"],
        ["Explicit axioms", "CryptoAssumption; RiemannHypothesisAssumption"],
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
        p("Scoped Formal Verification Certificate", "Heading1"),
        p("Issued from a reproducible local build on 15 July 2026."),
        Spacer(1, 5 * mm), table,
        p("Certified scope", "Heading1"),
        p(
            "The checker accepted the versioned finite K3 laws, state-coordinate invariants, regulated scalar-rate positivity, affine-clock monotonicity, finite truncation cardinality, threshold-indicator correctness and elementary properties of the declared linear-flow expression."
        ),
        p("Excluded scope", "Heading1"),
        p(
            "This certificate is not evidence for the Riemann hypothesis, P versus NP, Navier-Stokes smoothness, Yang-Mills mass gap, Hodge, BSD, black-hole information, cryptographic security, network availability or a unification of those subjects. Explicit assumptions remain assumptions."
        ),
        p("Epistemic verdict", "Heading1"),
        p(
            "Finite numerical eta evaluation can certify non-vanishing under an error bound, but cannot certify an exact zero. Finite resource equivalence does not identify asymptotic complexity classes. The claimed interdisciplinary couplings remain definitions, hypotheses or rejected inferences as recorded in docs/claim-ledger.md."
        ),
        p("Integrity", "Heading1"),
        p(
            "The complete SHA-256 ledger is versioned in formal/CERTIFICATE.md. Re-run the GitHub Actions workflow or lake build in formal/lean to reproduce checker acceptance."
        ),
    ]
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build()
