"""Build a compact static PDF research report from the reproducible artefacts."""
from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output" / "chebyshev_tail_diagnostics.pdf"
FIGURES = ROOT / "figures"


def heading(text: str, styles) -> Paragraph:
    return Paragraph(text, styles["Heading2"])


def body(text: str, styles) -> Paragraph:
    return Paragraph(text, styles["BodyText"])


def build() -> Path:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleNote", parent=styles["Title"], spaceAfter=10))
    styles["BodyText"].leading = 14
    document = SimpleDocTemplate(
        str(OUT), pagesize=A4, rightMargin=1.8 * cm, leftMargin=1.8 * cm,
        topMargin=1.6 * cm, bottomMargin=1.6 * cm,
    )
    story = [
        Paragraph("Finite Chebyshev-Tail Diagnostics", styles["TitleNote"]),
        body("A reproducible research module for finite experiments with psi(x)-x. "
             "This report does not prove or disprove the Riemann Hypothesis.", styles),
        Spacer(1, 10),
        heading("Scope", styles),
        body("The module evaluates the Chebyshev function psi(x)=sum_{p^k <= x} log p "
             "on a finite integer range. It reports finite values, a normalized window "
             "amplitude, a generic symmetry orbit, and a Fibonacci control experiment.", styles),
        heading("Formal boundary", styles),
        body("The exact finite identities are: prime-power accumulation defines psi; a generic "
             "off-critical zero is closed under conjugation and reflection about Re(s)=1/2; "
             "and the radial parity defect equals delta squared. No finite sample determines "
             "the location of all nontrivial zeros.", styles),
    ]
    table = Table([
        ["Artefact", "Status", "Permitted conclusion"],
        ["psi(x)-x on the grid", "computed", "finite numerical value"],
        ["fourfold orbit", "algebraic symmetry", "generic reflected orbit"],
        ["windowed RMS", "diagnostic", "candidate anomaly only"],
        ["RH", "open", "no conclusion from this report"],
    ], colWidths=[4.0 * cm, 4.0 * cm, 8.0 * cm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#173f5f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#bbbbbb")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("LEADING", (0, 0), (-1, -1), 10),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f4f7fa")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story += [Spacer(1, 8), table, PageBreak(), heading("Finite tail diagnostic", styles)]
    story.append(body("The line chart is computed directly from prime powers below the selected "
                      "cutoff. It illustrates finite fluctuations; it is not an asymptotic bound.", styles))
    story += [Spacer(1, 8), Image(str(FIGURES / "chebyshev_tail.png"), width=16.5 * cm, height=8.8 * cm)]
    story += [Spacer(1, 8), heading("Windowed normalized amplitude", styles)]
    story.append(body("The RMS window suppresses isolated sign changes but does not supply a "
                      "consistent estimator for a hypothetical off-critical real part.", styles))
    story += [Spacer(1, 8), Image(str(FIGURES / "window_energy.png"), width=16.5 * cm, height=8.8 * cm)]
    story += [PageBreak(), heading("Symmetry and control", styles)]
    story.append(body("The red points below are a deliberately hypothetical input (sigma=0.72, "
                      "t=14.134725), displayed only to show the fourfold symmetry. They are not "
                      "claimed zeta zeros.", styles))
    story += [Spacer(1, 8), Image(str(FIGURES / "zero_orbit_geometry.png"), width=12.5 * cm, height=10 * cm)]
    story.append(body("The Fibonacci chart is a solved recurrence control. Its exponential tail "
                      "does not transfer a theorem to prime-number fluctuations.", styles))
    story += [Spacer(1, 8), Image(str(FIGURES / "fibonacci_control.png"), width=15 * cm, height=8.5 * cm)]
    story += [PageBreak(), heading("Reproduction", styles)]
    story.append(body("Run: python simulations/chebyshev_tail.py --max-x 20000 --out "
                      "research/chebyshev_tail; then python research/chebyshev_tail/build_pdf.py. "
                      "The Lean modules RadialGeometry.lean and FiniteEvidence.lean prove only "
                      "the stated finite algebraic and logical lemmas, with no sorry or axioms.", styles))
    story += [Spacer(1, 8), heading("References", styles)]
    story.append(body("NIST Digital Library of Mathematical Functions, Section 25.16, Mathematical "
                      "Applications of the Riemann zeta function. Clay Mathematics Institute, "
                      "Problems of the Millennium: The Riemann Hypothesis, E. Bombieri.", styles))
    document.build(story)
    return OUT


if __name__ == "__main__":
    print(build())
