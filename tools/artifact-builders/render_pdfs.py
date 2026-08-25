from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle,
    KeepTogether,
)


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"
IMG = OUT / "images"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER,
                          textColor=colors.HexColor("#17324D"), fontSize=25, leading=30, spaceAfter=18))
styles.add(ParagraphStyle(name="SubTitle", parent=styles["Heading2"], alignment=TA_CENTER,
                          textColor=colors.HexColor("#A33A2B"), fontSize=14, leading=18))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], textColor=colors.HexColor("#17324D"),
                          fontSize=17, leading=21, spaceBefore=10, spaceAfter=8))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], textColor=colors.HexColor("#176B4D"),
                          fontSize=13, leading=17, spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyX", parent=styles["BodyText"], fontSize=10.2, leading=14.2,
                          spaceAfter=7, textColor=colors.HexColor("#1F2937")))
styles.add(ParagraphStyle(name="Formula", parent=styles["BodyText"], fontName="Courier", fontSize=9.2,
                          leading=13, leftIndent=14, rightIndent=14, borderColor=colors.HexColor("#CBD5E1"),
                          borderWidth=.6, borderPadding=7, backColor=colors.HexColor("#F8FAFC"), spaceAfter=9))
styles.add(ParagraphStyle(name="CaptionX", parent=styles["BodyText"], alignment=TA_CENTER,
                          fontSize=8.5, leading=11, textColor=colors.HexColor("#475569"), spaceAfter=10))


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.line(2*cm, A4[1]-1.45*cm, A4[0]-2*cm, A4[1]-1.45*cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(2*cm, A4[1]-1.15*cm, "Auditoria estrutural da Hipótese de Riemann")
    canvas.drawRightString(A4[0]-2*cm, 1.1*cm, f"Página {doc.page}")
    canvas.restoreState()


def doc(path, title, subtitle, story):
    target = OUT / path
    flow = [Spacer(1, 3.8*cm), Paragraph(title, styles["TitleCenter"]),
            Paragraph(subtitle, styles["SubTitle"]), Spacer(1, 1.2*cm),
            Paragraph("Dossiê técnico - agosto de 2026", styles["CaptionX"]), PageBreak()]
    flow.extend(story)
    SimpleDocTemplate(str(target), pagesize=A4, rightMargin=2*cm, leftMargin=2*cm,
                      topMargin=1.8*cm, bottomMargin=1.7*cm,
                      title=title, author="Codex").build(flow, onFirstPage=header_footer, onLaterPages=header_footer)
    return target


def p(text): return Paragraph(text, styles["BodyX"])
def h(text): return Paragraph(text, styles["H1x"])
def h2(text): return Paragraph(text, styles["H2x"])
def formula(text): return Paragraph(text, styles["Formula"])


def fig(name, caption, width=16.2*cm, height=11.2*cm):
    image = Image(str(IMG / f"{name}.png"))
    image._restrictSize(width, height)
    return KeepTogether([image, Paragraph(caption, styles["CaptionX"])])


story = [
    h("1. Escopo e regra de auditoria"),
    p("O material é organizado em quatro classes: <b>provado</b>, <b>certificado finito</b>, "
      "<b>equivalente à RH</b> e <b>conjectural</b>. Evidência numérica e definições algébricas "
      "não são promovidas a afirmações universais."),
    h("2. Geometria local"),
    formula("rho = 1/2 + delta + i gamma;   rho# = 1/2 - delta + i gamma"),
    formula("Rc^2 = gamma^2 + 1/4;   R+^2 = Rc^2 + delta + delta^2;   R-^2 = Rc^2 - delta + delta^2"),
    formula("delta = (R+^2 - R-^2)/2;   Delta_par = (R+^2 + R-^2)/2 - Rc^2 = delta^2"),
    fig("01-detector-geometrico", "Figura 1 - Detector geométrico local."),
    fig("02-quarteto-simetrias", "Figura 2 - Simetrias funcional e por conjugação."),
    h("3. Peso radial e escalas"),
    formula("A = gamma^2 + 1/4 + delta^2;   P = A^2 - delta^2 = |rho|^2 |1-rho|^2"),
    formula("w(delta,gamma) = 2 delta^2 / P;   W4 = 4w"),
    p("Cada termo é não negativo e se anula exatamente quando o desvio transversal é zero. "
      "Em grande altura, o detector perde sensibilidade como gamma^-4."),
    fig("03-parabola-delta", "Figura 3 - Comportamento parabólico de Delta_par."),
    fig("04-peso-versus-delta", "Figura 4 - Crescimento quadrático do peso em |delta|."),
    formula("w = 2 delta^2 gamma^-4 - 4 delta^2(1/4 + delta^2) gamma^-6 + O(gamma^-8)"),
    fig("05-decaimento-gamma", "Figura 5 - Decaimento do peso com a altura."),
    fig("06-mapa-log-peso", "Figura 6 - Mapa multiescala da invisibilidade radial."),
    h("4. Condicionamento"),
    formula("kappa_pair approximately 2 gamma^2 / delta^2"),
    p("A identidade por raios é exata, mas sua avaliação em ponto flutuante sofre cancelamento. "
      "A implementação deve calcular delta diretamente ou usar intervalos de precisão arbitrária."),
    fig("07-condicionamento", "Figura 7 - Número de condição da recuperação por raios."),
    h("5. Ruptura não holomorfa"),
    formula("C_xi = 2 + gamma_E - log(4 pi) approximately 0.0461914179322420676"),
    formula("D_rad = sum_rho 2(Re rho - 1/2)^2 / (|rho|^2 |1-rho|^2)"),
    p("A soma holomorfa controlada por Hadamard e pela equação funcional não fornece automaticamente "
      "a soma de |rho|^-2. Esta mistura rho e seu conjugado: é o ponto de ruptura lógico."),
    fig("08-hierarquia-defeito", "Figura 8 - Hierarquia do defeito e ruptura não holomorfa."),
    h("6. Forma de Weil e matrizes"),
    formula("Q_W(g) = sum_rho g~(rho) conjugate(g~(1-conjugate(rho)))"),
    p("Certificar matrizes truncadas é evidência finita. Uma conclusão global exige positividade em todos "
      "os níveis, densidade da base, continuidade da forma e controle uniforme dos erros."),
    fig("12-matriz-g13", "Figura 9 - Exemplo ilustrativo G13; não representa dados certificados."),
    h("7. Três vias não circulares"),
    fig("10-tres-vias", "Figura 10 - Obrigações de prova nas vias radial, Weil e Gram."),
    h("8. Teste de circularidade"),
    formula("RC = A[epsilon] / (epsilon^2 - Delta_par)"),
    p("A extensão é uma codificação se Delta_par foi definido antes. Num cenário contrafactual com "
      "delta diferente de zero, ela deve continuar consistente e manter epsilon^2 = delta^2 > 0. "
      "Forçar epsilon = 0 sem uma lei independente embute a conclusão."),
    fig("11-teste-circularidade", "Figura 11 - Teste contrafactual para epsilon."),
    h("9. Veredito"),
    fig("09-status-logico", "Figura 12 - Separação entre prova, certificado, lacuna e RH."),
    p("As identidades locais e a análise de escala são auditáveis. A passagem para D_rad = 0, "
      "positividade global de Weil ou completude positiva de todas as matrizes permanece aberta e "
      "equivalente ao núcleo da Hipótese de Riemann."),
]
doc("dossie-auditoria-rh.pdf", "Auditoria do ponto de ruptura",
    "Detector geométrico, defeito radial, forma de Weil e circularidade", story)


names = [
    ("01-detector-geometrico", "Detector geométrico local"),
    ("02-quarteto-simetrias", "Quarteto e simetrias"),
    ("03-parabola-delta", "Parábola do defeito local"),
    ("04-peso-versus-delta", "Peso versus desvio"),
    ("05-decaimento-gamma", "Decaimento com a altura"),
    ("06-mapa-log-peso", "Mapa multiescala"),
    ("07-condicionamento", "Condicionamento numérico"),
    ("08-hierarquia-defeito", "Hierarquia do defeito"),
    ("09-status-logico", "Classificação lógica"),
    ("10-tres-vias", "Três vias de fechamento"),
    ("11-teste-circularidade", "Teste de circularidade"),
    ("12-matriz-g13", "Matriz hermitiana G13"),
]
atlas = []
for index, (name, caption) in enumerate(names, 1):
    atlas += [h(f"{index}. {caption}"), fig(name, f"Visualização {index} - {caption}.", 17*cm, 18.5*cm)]
    if index != len(names): atlas.append(PageBreak())
doc("atlas-visualizacoes.pdf", "Atlas completo de visualizações",
    "Do detector local ao teste de circularidade", atlas)


rows = [
    ["Objeto", "Fórmula / obrigação"],
    ["Zero", "rho = 1/2 + delta + i gamma"],
    ["Raios", "Rc^2 = gamma^2+1/4; R+-^2 = Rc^2 +- delta + delta^2"],
    ["Detector", "Delta_par = delta^2"],
    ["Denominador", "P = (gamma^2+1/4+delta^2)^2-delta^2"],
    ["Peso", "w = 2 delta^2/P; W4 = 4w"],
    ["Assíntota", "w approximately 2 delta^2/gamma^4"],
    ["Condicionamento", "kappa_pair approximately 2 gamma^2/delta^2"],
    ["Defeito global", "D_rad = sum w(rho)"],
    ["Weil", "Construir T dos primos com Q_W(g)=||Tg||^2"],
    ["Gram", "G_N >= 0 + densidade + continuidade + erro uniforme"],
]
table = Table(rows, colWidths=[4*cm, 12*cm], repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#17324D")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("GRID", (0,0), (-1,-1), .5, colors.HexColor("#CBD5E1")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME", (1,1), (1,-1), "Courier"),
    ("FONTSIZE", (0,0), (-1,-1), 8.6),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
    ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
appendix = [h("1. Tabela-mestra"), table, Spacer(1, .4*cm), h("2. Expansão assintótica"),
            formula("P = gamma^4 + 2(1/4+delta^2)gamma^2 + (1/4+delta^2)^2-delta^2"),
            formula("1/P = gamma^-4[1-2(1/4+delta^2)gamma^-2+O(gamma^-4)]"),
            formula("w = 2delta^2 gamma^-4 - 4delta^2(1/4+delta^2)gamma^-6 + O(gamma^-8)"),
            h("3. Checklist de não circularidade"),
            p("1. Definir os objetos antes de assumir RH.<br/>2. Repetir a construção com um zero sintético fora da linha.<br/>"
              "3. Identificar o lema que falha nesse cenário.<br/>4. Derivar esse lema do lado dos primos.<br/>"
              "5. Não converter certificados finitos em quantificadores universais."),
            h("4. Status formal"),
            p("<b>Provado:</b> identidades locais, positividade do peso e expansão elementar.<br/>"
              "<b>Certificado finito:</b> verificações com altura e dimensão limitadas.<br/>"
              "<b>Equivalente:</b> D_rad=0, positividade global de Weil e família Gram completa.<br/>"
              "<b>Conjectural:</b> núcleo primo coercivo, métrica destrutiva e conservação que exclua epsilon diferente de zero."),
            h("5. Nota sobre epsilon"),
            p("No quociente A[epsilon]/(epsilon^2-Delta_par), epsilon não é nilpotente quando "
              "Delta_par é diferente de zero. Impor epsilon^2=0 universalmente seleciona previamente o setor crítico.")]
doc("caderno-formulas.pdf", "Caderno de fórmulas e verificações",
    "Detector radial e obrigações de prova", appendix)

print("Rendered final PDFs")
