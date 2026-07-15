"""Build visually reviewable PDFs; LaTeX remains the authoritative source."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image,
    Table,
    TableStyle,
    KeepTogether,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)
FIG = ROOT / "figures"

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="PaperTitle",
        parent=styles["Title"],
        fontSize=19,
        leading=23,
        alignment=TA_CENTER,
        spaceAfter=12,
    )
)
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8.5, leading=11))
styles["BodyText"].fontSize = 9.5
styles["BodyText"].leading = 13
styles["Heading1"].fontSize = 14
styles["Heading1"].spaceBefore = 10
styles["Heading1"].spaceAfter = 6
styles["Heading2"].fontSize = 11
styles["Heading2"].spaceBefore = 8


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#53636d"))
    canvas.drawString(22 * mm, 12 * mm, "Federated Trivalent Manifold - review draft, 15 July 2026")
    canvas.drawRightString(188 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


def p(text, style="BodyText"):
    return Paragraph(text, styles[style])


def image(name, caption):
    path = FIG / name
    return KeepTogether(
        [
            Image(str(path), width=145 * mm, height=86 * mm, kind="proportional"),
            p(caption, "Small"),
            Spacer(1, 4 * mm),
        ]
    )


def build_preprint():
    doc = SimpleDocTemplate(
        str(OUT / "ftm_preprint_v4_1.pdf"),
        pagesize=A4,
        rightMargin=22 * mm,
        leftMargin=22 * mm,
        topMargin=18 * mm,
        bottomMargin=20 * mm,
        title="FTM preprint v4.1",
    )
    s = [
        p(
            "A Trivalent Specification Calculator with Auditable Numerical Actions and Multi-Prover Exports",
            "PaperTitle",
        ),
        p("Shanti Draconis - affiliation and ORCID to be confirmed", "Small"),
        Spacer(1, 6 * mm),
        p("Abstract", "Heading1"),
        p(
            "We present an experimental framework that separates definitions, assumptions, numerical evidence, proof obligations and checker-verified theorems. It implements strong Kleene three-valued logic, a sampled complex action, multi-prover exports and an audited v4.1 flow controller. The established invariants are properties of the defined model; they are not results about Perelman entropy, cryptographic security, network availability or any Millennium Prize Problem."
        ),
        p("1. Scope and epistemic status", "Heading1"),
        p(
            "The values F, U and T mean refuted, undecided and proved in a selected theory. U is not the claim that a proposition and its negation are both true. Generated text receives an explicit status and cannot become a verified theorem without a checker record."
        ),
        p("2. Numerical model", "Heading1"),
        p(
            "For a declared path gamma, S[gamma] is the integral of a chosen Lagrangian plus i times the integral of e(t). The implementation uses composite trapezoidal quadrature. A run with n samples is O(n); only one integrand evaluation is constant-time with respect to n."
        ),
        image(
            "fig4_exodo.png",
            "Figure 1. Chosen exodus term and accumulated integral. This is a model visualization, not a proof.",
        ),
        p("3. Version 4.1 audit", "Heading1"),
        p(
            "Define q(t,e)=alpha t^2-beta e^2 and W[k+1]=W[k]+(q[k]^2+epsilon) delta-t. Under non-negative delta-t and epsilon, exact arithmetic gives non-decrease. This is a direct consequence of the definition and does not imply denial-of-service resistance."
        ),
        p(
            "With alpha=0.10, beta=0.10887 and epsilon=10^-6, q(3.15,0.3)^2=0.965211342833. The earlier value 0.9714 is not reproduced. Constant e=0.3 over T=3.155 gives integral 0.605003007857 and 0.905003007857 after adding e(T). Exponential e gives 0.617104804182 and 0.776722646806 respectively."
        ),
        image(
            "fig3_alpha_beta.png",
            "Figure 2. Parameter map. The diagonal is not a decidability boundary.",
        ),
        p("4. Comparison matrix", "Heading1"),
        p(
            "The supplied divergence matrix is symmetric, zero-diagonal and bounded. Its off-diagonal mean is 0.6751333; including diagonal entries gives 0.5786857. These checks validate table structure only. A score of one denotes disjoint declared features, not impossibility of a mathematical reduction."
        ),
        image(
            "fig5_conn_matrix.png",
            "Figure 3. Transparent feature similarity in the repository model.",
        ),
        p("5. Formal and operational layers", "Heading1"),
        p(
            "Lean, Coq, Isabelle/HOL and Agda fragments prove finite K3 laws. The v4.1 Lean fragment states domain hypotheses for coordinate reduction and accumulator monotonicity. The Python engine rejects non-finite states and time regression and serializes state changes. It does not implement encryption. The non-standard phrase AES-512 has been removed."
        ),
        image("fig6_trivalent.png", "Figure 4. Strong Kleene conjunction and disjunction tables."),
        p("6. Limitations", "Heading1"),
        p(
            "The five coordinates, action and scores are proposed definitions. They are not canonical bridges among topology, number theory, complexity, PDEs and quantum field theory. Formal compiler logs, independently motivated features, controlled benchmarks and a security threat model remain required."
        ),
        p("7. Remaining behavior audit", "Heading1"),
        p(
            "The q-squared isolation threshold on the positive branch occurs at t=3.1640 for e=0.1 and t=3.2237 for e=0.6. These are algebraic consequences of the chosen coefficients, not measured Quest buffering thresholds. Constant, exponential and oscillating W profiles are monotone because their integrand was defined as a square plus a positive regulator."
        ),
        image(
            "fig9_seff_thresholds.png",
            "Figure 5. Isolation thresholds under the declared model.",
        ),
        image(
            "fig10_w_profiles.png",
            "Figure 6. Accumulated W profiles; monotonicity is by construction.",
        ),
        p(
            "The zeta-alignment force is zero at sigma=0.5 by definition. The gauge and complexity curves are selected decay laws, not transported theorems. The eight points have mean imaginary part 30.665 and mean spacing 4.17, while their real parts equal 0.5 by construction."
        ),
        image(
            "fig13_zero_spacing_audit.png",
            "Figure 7. Fixed critical-line coordinates and successive sample spacings.",
        ),
        p(
            "A second matrix spectrum was supplied only through seven eigenvalues. Without the complete matrix it cannot be independently reproduced. It differs from the matrix obtained as one minus the versioned divergence table, which has a negative eigenvalue and is not positive definite."
        ),
        image(
            "fig14_reported_spectrum_unreproduced.png",
            "Figure 8. Reported spectrum, explicitly marked as unreproduced.",
        ),
        p("8. Anomaly-kernel trust boundary", "Heading1"),
        p(
            "The exact indicator of a zeta zero is a definition, not a finite-computation oracle. In the open critical strip eta and zeta share zeros, but the implementation certifies only non-vanishing when a partial-sum magnitude exceeds a rigorous tail bound. Every other result is inconclusive."
        ),
        image(
            "fig15_eta_certificate_boundary.png",
            "Figure 9. Finite eta sums and the conservative certificate boundary.",
        ),
        p(
            "The exact e derivative of the declared squared potential is minus four beta e times q. The resulting equation is not globally damping. The verified W rate is S2 plus positive epsilon; this algebraic fact is not operational liveness."
        ),
        image(
            "fig16_corrected_flow_dynamics.png",
            "Figure 10. Corrected derivative field and model-only threshold.",
        ),
        image(
            "fig17_epistemic_regimes.png",
            "Figure 11. Numerical uncertainty remains a first-class state.",
        ),
        KeepTogether(
            [
                p("AI usage disclosure", "Heading1"),
                p(
                    "Generative AI assisted drafting, coding, auditing and manuscript preparation. The author remains responsible for independent verification, authorship, references and final approval."
                ),
                p("Software availability", "Heading1"),
                p(
                    "Repository: github.com/ShantiDraconis/federated-trivalent-manifold. A tagged archive DOI is required before journal submission."
                ),
            ]
        ),
    ]
    doc.build(s, onFirstPage=footer, onLaterPages=footer)


def build_formal():
    doc = SimpleDocTemplate(
        str(OUT / "ftm_formal_methods_draft.pdf"),
        pagesize=A4,
        rightMargin=24 * mm,
        leftMargin=24 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title="FTM formal methods draft",
    )
    s = [
        p(
            "Epistemic Status Discipline for a Multi-Prover Trivalent Specification Calculator",
            "PaperTitle",
        ),
        p("Formal-methods journal draft - publisher class still required", "Small"),
        p("Abstract", "Heading1"),
        p(
            "This draft defines a finite strong-Kleene status algebra and a typed boundary among assumptions, open obligations, tests and checker-verified results. The contribution is specification discipline, not an open-problem solution."
        ),
        p("1. Semantics", "Heading1"),
        p(
            "K3={F,U,T}. Negation fixes U; conjunction and disjunction are minimum and maximum in the declared order. Involution and commutativity are proved by finite cases."
        ),
        p("2. Trust boundary", "Heading1"),
        p(
            "Each exporter must preserve a status label. Verification requires tool name, pinned version, source digest and successful result. An axiom extends a theory but remains an assumption relative to the unextended theory."
        ),
        p("3. Refinement case study", "Heading1"),
        p(
            "The isolation operator maps e to e/2 and preserves x. The non-increase result requires e>=0. The accumulator step is monotone under non-negative epsilon, squared term and time increment. These hypotheses are stated in the Lean fragment."
        ),
        image(
            "fig8_axiom_accepted.png",
            "Figure 1. Separation between assumption, derivation and conditional conclusion.",
        ),
        p("4. Evaluation still required", "Heading1"),
        p(
            "Compile all files with pinned Lean, Coq, Isabelle and Agda releases; archive logs; add mutation tests; compare with proof-document interoperability systems; and test whether generated statements retain semantics across backends."
        ),
        p("5. Threats to validity", "Heading1"),
        p(
            "Small truth tables do not establish semantic equivalence between proof assistants. Float computations are not proof terms. Cross-domain labels do not create mathematical reductions."
        ),
        p("AI disclosure", "Heading1"),
        p(
            "Generative AI assisted drafting and implementation. Human verification and accountability are mandatory before submission."
        ),
    ]
    doc.build(s, onFirstPage=footer, onLaterPages=footer)


def build_audit():
    doc = SimpleDocTemplate(
        str(OUT / "ftm_v4_1_audit_and_submission_checklist.pdf"),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=20 * mm,
        title="FTM v4.1 audit",
    )
    rows = [
        ["Claim", "Audit result"],
        ["Seff^2 at 3.15, 0.3", "0.965211342833; circulated 0.9714 not reproduced"],
        ["Constant-e integral", "0.605003007857; plus endpoint = 0.905003007857"],
        ["Exponential-e integral", "0.617104804182; plus endpoint = 0.776722646806"],
        ["Matrix mean", "0.6751333 off-diagonal; 0.5786857 including diagonal"],
        ["Complexity", "quadrature O(n); single evaluation O(1)"],
        ["Latency", "must be measured end-to-end; never zero"],
        ["Cryptography", "AES-512 removed; no cipher implemented"],
        ["DoS", "monotone W does not prove availability"],
        ["Div=1", "feature disjointness only; not a refutation"],
    ]
    table = Table(
        [[p(str(c), "Small") for c in row] for row in rows],
        colWidths=[55 * mm, 115 * mm],
        repeatRows=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#173b4d")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#80929b")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#eef3f4")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    s = [
        p("Version 4.1 Numerical Audit and Editorial Readiness", "PaperTitle"),
        p("Reproducible review report", "Small"),
        p("Atomic verdict", "Heading1"),
        p(
            "Several arithmetic values reproduce, but the strongest engineering and mathematical conclusions do not follow from them. The corrected package narrows claims to tested software invariants and explicitly defined model properties."
        ),
        table,
        p("Remaining behaviors", "Heading1"),
        p(
            "The threshold calculations and zero-spacing statistics reproduce from explicit inputs. The claimed positive-definite connection matrix does not: the attachment contains its spectrum but not the full matrix. Publication must include the matrix and its construction before PCA, determinant or conditioning claims are treated as reproduced."
        ),
        image(
            "fig14_reported_spectrum_unreproduced.png",
            "Reported component fractions; source matrix is absent.",
        ),
        p("Journal routing", "Heading1"),
        p(
            "Preprint: closest to ready after author metadata, bibliography validation, TeX compilation and category/endorsement checks."
        ),
        p(
            "Formal Aspects of Computing: draft only. Requires the current publisher class, complete proof-assistant logs, deeper formal semantics and related-work comparison."
        ),
        p(
            "JOSS: do not submit now. Current requirements include a public repository, at least six months of distributed public development history, demonstrated research use, feature completeness, tests, documentation and a short 750-1750 word paper with AI disclosure."
        ),
        p("Mandatory checklist", "Heading1"),
        p(
            "Confirm author name, affiliation, ORCID, funding, conflicts and correspondence. Make claims reproducible. Publish feature provenance. Pin all proof toolchains. Create a tagged release and archival DOI. Re-check journal rules on submission day. Do not submit the same manuscript simultaneously where policies prohibit it."
        ),
        p("Anomaly-kernel verdict", "Heading1"),
        p(
            "Finite eta evaluation has only certified-nonzero and inconclusive outcomes. The proposed e-flow is not globally damping, and S2 plus 10^-6 t plus e is zero at the origin. The Lean theorem instead uses S2 plus epsilon with epsilon positive. No Rijndael-512 or quantum implementation is present."
        ),
        image(
            "fig17_epistemic_regimes.png",
            "Trust boundary used by the numerical anomaly audit.",
        ),
        PageBreak(),
        image(
            "fig7_teardown_fsm.png",
            "Figure 1. Operational teardown stages; the abstract state update is not physical evidence.",
        ),
        image(
            "fig8_axiom_accepted.png",
            "Figure 2. Axiom acceptance creates conditional conclusions, not an unconditional proof.",
        ),
    ]
    doc.build(s, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_preprint()
    build_formal()
    build_audit()
