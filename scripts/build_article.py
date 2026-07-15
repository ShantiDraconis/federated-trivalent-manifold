from __future__ import annotations

from pathlib import Path
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, PageTemplate, Paragraph,
    PageBreak, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from gateway_model.model import Measurements, Parameters, action, beta_critical, mass_proxy


OUT = ROOT / "outputs"


def register_fonts() -> tuple[str, str]:
    regular = Path("C:/Windows/Fonts/arial.ttf")
    bold = Path("C:/Windows/Fonts/arialbd.ttf")
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("Article", str(regular)))
        pdfmetrics.registerFont(TTFont("Article-Bold", str(bold)))
        return "Article", "Article-Bold"
    return "Helvetica", "Helvetica-Bold"


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Article" if "Article" in pdfmetrics.getRegisteredFontNames() else "Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#56616f"))
    canvas.drawString(2 * cm, 1.25 * cm, "Modelo de acao de gateway - estudo reprodutivel")
    canvas.drawRightString(A4[0] - 2 * cm, 1.25 * cm, f"Pagina {doc.page}")
    canvas.restoreState()


def build() -> None:
    OUT.mkdir(exist_ok=True)
    font, bold = register_fonts()
    m, p = Measurements(), Parameters()
    s = action(p.alpha, p.beta, m.total, p.e_norm)
    bc = beta_critical(p.alpha, m.total, p.e_norm)

    source = f"""# Modelo de ação efetiva para um gateway multiagente

## Resumo
Este artigo apresenta um modelo reprodutível de custo para um pipeline com latência total de {m.total:.3f} s. A ação S = alpha t² - beta e² compara um termo temporal e um termo denominado êxodo. Os parâmetros são internos ao gateway; não constituem constantes nem provas de P versus NP, hipótese de Riemann ou Yang-Mills. Com alpha={p.alpha}, beta={p.beta} e e={p.e_norm}, obtemos S={s:.7f}. O ponto crítico correto é beta={bc:.8f}, não alpha aproximadamente beta.

## Resultados principais
- Tempo total: {m.total:.3f} s.
- Ação no ponto informado: {s:.7f}, regime temporal.
- Exemplo alpha=0.1, beta=5: {action(.1, 5, m.total, .3):.7f}, ainda temporal.
- Beta crítico: {bc:.8f}.
- Proxy de massa beta e: {mass_proxy(p.beta, p.e_norm):.6f}.

## Limites de interpretação
Os nomes de conexão e massa são rótulos ou analogias do modelo. Uma associação numérica escolhida pelo pesquisador não estabelece relação lógica entre problemas matemáticos. A formalização Lean prova somente identidades e desigualdades derivadas das definições declaradas.
"""
    (OUT / "artigo.md").write_text(source, encoding="utf-8")

    styles = getSampleStyleSheet()
    title = ParagraphStyle("Title2", parent=styles["Title"], fontName=bold, fontSize=22, leading=27,
                           textColor=colors.HexColor("#16324f"), alignment=TA_CENTER, spaceAfter=16)
    subtitle = ParagraphStyle("Subtitle2", parent=styles["Normal"], fontName=font, fontSize=11, leading=16,
                              alignment=TA_CENTER, textColor=colors.HexColor("#52606d"), spaceAfter=22)
    h1 = ParagraphStyle("H1x", parent=styles["Heading1"], fontName=bold, fontSize=15, leading=19,
                        textColor=colors.HexColor("#174a70"), spaceBefore=12, spaceAfter=8)
    h2 = ParagraphStyle("H2x", parent=styles["Heading2"], fontName=bold, fontSize=11.5, leading=15,
                        textColor=colors.HexColor("#255f85"), spaceBefore=9, spaceAfter=5)
    body = ParagraphStyle("Bodyx", parent=styles["BodyText"], fontName=font, fontSize=9.5, leading=14,
                          textColor=colors.HexColor("#202a33"), spaceAfter=7)
    note = ParagraphStyle("Notex", parent=body, backColor=colors.HexColor("#eef5f9"), borderColor=colors.HexColor("#7aa6c2"),
                          borderWidth=0.6, borderPadding=8, spaceBefore=6, spaceAfter=10)
    code = ParagraphStyle("Codex", parent=body, fontName="Courier", fontSize=8.3, leading=12,
                          backColor=colors.HexColor("#f3f4f6"), borderPadding=6)

    doc = BaseDocTemplate(str(OUT / "artigo_gateway.pdf"), pagesize=A4,
                          leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm, bottomMargin=2 * cm,
                          title="Modelo de ação efetiva para um gateway multiagente",
                          author="Estudo computacional reprodutível")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="article", frames=[frame], onPage=footer)])

    story = [Spacer(1, 1.0 * cm), Paragraph("Modelo de ação efetiva para um gateway multiagente", title),
             Paragraph("Análise numérica, testes automatizados e formalização em Lean 4", subtitle),
             Paragraph("Resumo", h1),
             Paragraph(f"Este trabalho define e verifica um modelo de custo para um pipeline multiagente. As latências medidas somam <b>{m.total:.3f} s</b>. A ação efetiva S = alpha t² - beta e² mede a diferença entre o custo temporal e o termo de êxodo. Para alpha={p.alpha}, beta={p.beta} e e={p.e_norm}, o valor exato representado numericamente é <b>S={s:.7f}</b>.", body),
             Paragraph("Escopo científico: todos os resultados são condicionais às definições do gateway. Nenhuma constante aqui pertence aos Problemas do Milênio, e nenhuma identidade algébrica apresentada prova P versus NP, a hipótese de Riemann ou a existência de um mass gap de Yang-Mills.", note),
             Paragraph("1. Definição e dados", h1),
             Paragraph("O pipeline é tratado como uma composição sequencial. A tabela registra os valores fornecidos; incertezas de medição não foram informadas, portanto os resultados não devem ser interpretados como estimativas estatísticas.", body)]

    data = [["Componente", "Latência (s)"], ["Llama", "0.800"], ["GPT", "1.200"], ["Claude", "1.100"],
            ["AES-GCM", "0.005"], ["Teardown", "0.050"], ["Total", f"{m.total:.3f}"]]
    table = Table(data, colWidths=[8.5 * cm, 4 * cm], hAlign="LEFT")
    table.setStyle(TableStyle([("FONT", (0,0), (-1,-1), font, 9), ("FONT", (0,0), (-1,0), bold, 9),
                               ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#174a70")), ("TEXTCOLOR", (0,0), (-1,0), colors.white),
                               ("GRID", (0,0), (-1,-1), 0.35, colors.HexColor("#b8c4cc")),
                               ("BACKGROUND", (0,-1), (-1,-1), colors.HexColor("#e8f0f5")), ("FONT", (0,-1), (-1,-1), bold, 9),
                               ("ALIGN", (1,1), (1,-1), "RIGHT"), ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5)]))
    story += [table, Spacer(1, 8), Paragraph("A equação operacional é:", body),
              Paragraph("S(alpha, beta, t, e) = alpha t² - beta e²", code),
              Paragraph("S positivo indica que o termo temporal é maior; S negativo indica que o termo de êxodo é maior; S igual a zero define a fronteira crítica. Esses nomes classificam apenas os dois termos da equação.", body),
              Paragraph("2. Derivação do ponto crítico", h1),
              Paragraph("Impondo S=0 e supondo e diferente de zero, a álgebra fornece beta_crit = alpha t²/e². Substituindo os valores do experimento:", body),
              Paragraph(f"beta_crit = 0.1 x ({m.total:.3f})² / (0.3)² = {bc:.8f}", code),
              Paragraph(f"Logo, beta={p.beta} está muito abaixo do valor crítico. A proximidade numérica entre alpha={p.alpha} e beta={p.beta} não caracteriza equilíbrio, porque t² e e² têm escalas muito diferentes.", note),
              Image(str(OUT / "action_regimes.png"), width=15.8 * cm, height=9.48 * cm),
              Paragraph("Figura 1. A ação cruza zero apenas em beta aproximadamente 11,060. O ponto informado permanece no domínio positivo.", body),
              Paragraph("3. Regimes e correção aritmética", h1)]

    regimes = [["Cenário", "alpha", "beta", "S", "Classificação"],
               ["Predomínio temporal", "5.0", "0.1", f"{action(5,.1,m.total,.3):.6f}", "temporal"],
               ["Exemplo beta=5", "0.1", "5.0", f"{action(.1,5,m.total,.3):.7f}", "temporal"],
               ["Ponto informado", "0.1", f"{p.beta:.6f}", f"{s:.7f}", "temporal"],
               ["Fronteira", "0.1", f"{bc:.6f}", "0", "crítico"]]
    rt = Table(regimes, colWidths=[4.3*cm, 2.1*cm, 2.4*cm, 3.1*cm, 3.1*cm])
    rt.setStyle(TableStyle([("FONT",(0,0),(-1,-1),font,8.4), ("FONT",(0,0),(-1,0),bold,8.4),
                            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#174a70")), ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                            ("GRID",(0,0),(-1,-1),.35,colors.HexColor("#aebbc5")), ("ALIGN",(1,1),(-2,-1),"RIGHT"),
                            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#f3f7fa")]),
                            ("TOPPADDING",(0,0),(-1,-1),5), ("BOTTOMPADDING",(0,0),(-1,-1),5)]))
    story += [rt, Spacer(1,8), Paragraph(f"O cálculo anteriormente atribuído ao cenário beta=5 omitia o termo alpha t². O valor correto é 0.9954025 - 0.45 = <b>{action(.1,5,m.total,.3):.7f}</b>, ainda positivo. Para obter S negativo mantendo alpha=0.1, t={m.total} e e=0.3, beta deve exceder {bc:.8f}.", body),
              Paragraph("4. Dinâmica de decaimento", h1),
              Paragraph("A extensão dinâmica e(t)=e0 exp(-lambda t) é uma hipótese adicional. Para lambda não negativo e tempo não negativo, a magnitude decai monotonicamente quando e0 é positivo. Ela não decorre da ação estática e deve ser validada contra observações se for usada como modelo físico ou operacional.", body),
              Image(str(OUT / "exodus_decay.png"), width=15.8 * cm, height=9.48 * cm),
              Paragraph("Figura 2. Sensibilidade do decaimento exponencial a lambda. O valor adotado no modelo é 0,2.", body),
              Paragraph("5. Verificação computacional", h1),
              Paragraph("A implementação Python separa funções puras, dados e geração de artefatos. Os testes verificam o total do pipeline, a ação informada, a correção do cenário beta=5, o ponto crítico, o proxy de massa, o decaimento e casos inválidos. Um teste estrutural rejeita os marcadores sorry e admit no arquivo Lean.", body),
              Paragraph("python -m unittest discover -s tests -v<br/>python scripts/run_experiment.py<br/>python scripts/build_article.py", code),
              Paragraph("6. Formalização em Lean", h1),
              Paragraph("A formalização usa números racionais exatos. Ela demonstra: soma exata das latências; ação exata; exemplo corrigido; beta crítico; anulação da ação no beta crítico para e não nulo; proxy de massa; e equivalência entre o sinal da ação e a ordem dos termos. Mathlib fornece norm_num, field_simp, ring e linarith.", body),
              Paragraph("O teorema geral central é: se e != 0, então action alpha (betaCritical alpha t e) t e = 0.", code),
              PageBreak(), Paragraph("7. Validade, limitações e falsificabilidade", h1),
              Paragraph("Validade interna: as identidades são consequências demonstráveis das definições. Validade empírica: depende da qualidade e repetibilidade das latências. Validade externa: não foi estabelecida; o modelo não autoriza inferência sobre complexidade computacional, zeros da função zeta ou teorias de calibre.", body),
              Paragraph("Para transformar o estudo em experimento empírico, devem ser coletadas distribuições de latência, intervalos de confiança, correlações entre etapas e uma definição observável de e. Alpha e beta precisam de procedimento de calibração independente; escolhê-los para produzir um regime desejado seria ajuste circular.", note),
              Paragraph("8. Reprodutibilidade", h1),
              Paragraph("Os artefatos incluem código Python, testes unitários, projeto Lake, teoremas Lean, JSON com resultados, figuras rasterizadas e este artigo. O JSON distingue explicitamente medições, parâmetros escolhidos e quantidades derivadas.", body),
              Paragraph("Conclusão", h1),
              Paragraph(f"O sistema informado está no regime temporal do modelo, com S={s:.7f}. A fronteira ocorre em beta={bc:.8f}. O trabalho fornece uma base verificável e extensível, preservando a distinção essencial entre uma analogia de gateway e uma afirmação matemática sobre problemas abertos.", body)]
    doc.build(story)


if __name__ == "__main__":
    build()
