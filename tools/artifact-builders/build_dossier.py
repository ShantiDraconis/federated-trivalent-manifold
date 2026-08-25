from pathlib import Path
import math
import textwrap

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"
TEX = OUT / "latex"
IMG = OUT / "images"
for directory in (OUT, TEX, IMG):
    directory.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 13,
    "axes.labelsize": 10,
    "figure.dpi": 150,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(IMG / f"{name}.png", dpi=260, bbox_inches="tight")
    fig.savefig(IMG / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)


def weight(delta, gamma):
    a = gamma**2 + 0.25 + delta**2
    return 2 * delta**2 / (a**2 - delta**2)


def box(ax, x, y, text, color="#e8f1fb", edge="#245b8a", width=0.25, height=0.11):
    from matplotlib.patches import FancyBboxPatch
    patch = FancyBboxPatch((x-width/2, y-height/2), width, height,
                           boxstyle="round,pad=0.012", facecolor=color,
                           edgecolor=edge, linewidth=1.3)
    ax.add_patch(patch)
    ax.text(x, y, text, ha="center", va="center", fontsize=8.5)


def arrow(ax, a, b, label=None, color="#334155"):
    ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="->", lw=1.4, color=color))
    if label:
        ax.text((a[0]+b[0])/2, (a[1]+b[1])/2+0.025, label, ha="center", fontsize=8, color=color)


# 1. Geometric detector
delta, gamma = 0.28, 1.05
fig, ax = plt.subplots(figsize=(7.3, 5.4))
ax.axvline(0.5, color="#64748b", ls="--", lw=1.2, label=r"linha crítica $\Re s=1/2$")
pts = [(0.5+delta, gamma), (0.5-delta, gamma)]
for x, y in pts:
    ax.plot(x, y, "o", ms=8, color="#b42318")
    ax.plot([0, x], [0, y], color="#245b8a", lw=1.7)
ax.plot([pts[0][0], pts[1][0]], [gamma, gamma], color="#d97706", lw=2)
ax.annotate(r"$2\delta$", (0.5, gamma+0.06), ha="center", color="#9a3412")
ax.text(0.5+delta+0.025, gamma, r"$\rho=\frac{1}{2}+\delta+i\gamma$", va="center")
ax.text(0.5-delta-0.025, gamma, r"$1-\bar\rho=\frac{1}{2}-\delta+i\gamma$", ha="right", va="center")
ax.text(0.04, 0.09, r"$R_+^2=R_c^2+\delta+\delta^2$"+"\n"+r"$R_-^2=R_c^2-\delta+\delta^2$"+"\n"+r"$\Delta_{par}=\frac{R_+^2+R_-^2}{2}-R_c^2=\delta^2$",
        transform=ax.transAxes, bbox=dict(boxstyle="round", fc="#f8fafc", ec="#94a3b8"))
ax.set(xlim=(0, 1), ylim=(0, 1.35), xlabel=r"parte real $\beta$", ylabel=r"parte imaginária $\gamma$", title="Detector geométrico local")
ax.set_aspect("equal", adjustable="box")
ax.legend(loc="lower right")
save(fig, "01-detector-geometrico")

# 2. Quartet symmetry
fig, ax = plt.subplots(figsize=(6.6, 5.5))
quartet = [(0.5+delta, gamma), (0.5-delta, gamma), (0.5+delta, -gamma), (0.5-delta, -gamma)]
ax.axvline(0.5, color="#64748b", ls="--")
ax.axhline(0, color="#64748b", lw=.8)
for x, y in quartet:
    ax.plot(x, y, "o", color="#7c3aed", ms=8)
ax.plot([q[0] for q in [quartet[1], quartet[0], quartet[2], quartet[3], quartet[1]]],
        [q[1] for q in [quartet[1], quartet[0], quartet[2], quartet[3], quartet[1]]], color="#a78bfa")
ax.text(.5, 0, r"simetrias: $\rho\mapsto\bar\rho$ e $\rho\mapsto1-\rho$", ha="center", va="bottom")
ax.set(xlim=(0,1), ylim=(-1.3,1.3), xlabel=r"$\Re s$", ylabel=r"$\Im s$", title="Quarteto funcional de um zero fora da linha")
save(fig, "02-quarteto-simetrias")

# 3. Delta parabola
d = np.linspace(-.49, .49, 500)
fig, ax = plt.subplots(figsize=(7,4.4))
ax.plot(d, d*d, color="#0f766e", lw=2.4)
ax.fill_between(d, 0, d*d, color="#99f6e4", alpha=.45)
ax.scatter([0],[0], color="#b42318", zorder=3)
ax.annotate("mínimo global; derivada nula", (0,0), (0.12,.08), arrowprops=dict(arrowstyle="->"))
ax.set(xlabel=r"desvio $\delta$", ylabel=r"$\Delta_{par}=\delta^2$", title="Escala microscópica do detector parabólico")
ax.grid(alpha=.25)
save(fig, "03-parabola-delta")

# 4. Weight vs delta
fig, ax = plt.subplots(figsize=(7,4.5))
for g, c in [(14.1347,"#2563eb"),(100,"#7c3aed"),(1000,"#b42318")]:
    ds=np.logspace(-8, math.log10(.49), 500)
    ax.loglog(ds, weight(ds,g), color=c, label=fr"$\gamma={g:g}$")
ax.set(xlabel=r"$|\delta|$", ylabel=r"$w(\delta,\gamma)$", title=r"Peso radial: crescimento quadrático em $\delta$")
ax.grid(which="both", alpha=.22); ax.legend()
save(fig, "04-peso-versus-delta")

# 5. Gamma decay
fig, ax = plt.subplots(figsize=(7,4.5))
gs=np.logspace(1,12,600)
for dd,c in [(.1,"#b42318"),(.01,"#d97706"),(1e-3,"#2563eb")]:
    ax.loglog(gs,weight(dd,gs),color=c,label=fr"$\delta={dd:g}$")
ax.loglog(gs,2*.1**2/gs**4,"k--",alpha=.7,label=r"referência $2\delta^2/\gamma^4$")
ax.set(xlabel=r"altura $\gamma$", ylabel=r"$w$", title=r"Perda macroscópica de sensibilidade: $w\sim2\delta^2/\gamma^4$")
ax.grid(which="both",alpha=.22); ax.legend()
save(fig, "05-decaimento-gamma")

# 6. Heatmap
ld=np.linspace(-10,math.log10(.49),300); lg=np.linspace(1,12,320)
D,G=np.meshgrid(10**ld,10**lg); Z=np.log10(weight(D,G))
fig, ax=plt.subplots(figsize=(7.4,5.2))
im=ax.imshow(Z,origin="lower",aspect="auto",extent=[ld.min(),ld.max(),lg.min(),lg.max()],cmap="viridis")
cs=ax.contour(ld,lg,Z,levels=[-90,-70,-50,-30,-10],colors="white",linewidths=.75)
ax.clabel(cs,fmt=lambda x:f"$10^{{{int(x)}}}$",fontsize=8)
fig.colorbar(im,ax=ax,label=r"$\log_{10}w$")
ax.set(xlabel=r"$\log_{10}|\delta|$",ylabel=r"$\log_{10}\gamma$",title="Mapa multiescala da invisibilidade radial")
save(fig,"06-mapa-log-peso")

# 7. Conditioning
fig,ax=plt.subplots(figsize=(7,4.6))
gs=np.logspace(0,12,500); u=2**-52
for dd,c in [(1e-1,"#0f766e"),(1e-3,"#2563eb"),(1e-6,"#b42318")]:
    k=2*gs**2/dd**2
    ax.loglog(gs,k,color=c,label=fr"$\delta={dd:g}$")
ax.axhline(1/u,color="black",ls="--",label=r"$1/u$ (IEEE 754 dupla)")
ax.set(xlabel=r"$\gamma$",ylabel=r"$\kappa_{pair}\approx2\gamma^2/\delta^2$",title="Condicionamento da recuperação por diferença de raios")
ax.grid(which="both",alpha=.22);ax.legend()
save(fig,"07-condicionamento")

# 8. Identity hierarchy
fig,ax=plt.subplots(figsize=(9,5.8));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
box(ax,.12,.82,r"Hadamard + equação\nfuncional",width=.22)
box(ax,.39,.82,r"soma holomorfa\n$\sum[\rho(1-\rho)]^{-1}=C_\xi$",width=.29)
box(ax,.70,.82,r"soma não holomorfa\n$\sum|\rho|^{-2}$",color="#fff7ed",edge="#c2410c",width=.24)
box(ax,.70,.55,r"$D_{rad}=\sum w(\rho)$",color="#fff7ed",edge="#c2410c",width=.24)
box(ax,.40,.28,r"$D_{rad}=0$",color="#fef2f2",edge="#b42318",width=.21)
box(ax,.12,.28,r"RH",color="#fef2f2",edge="#b42318",width=.15)
arrow(ax,(.23,.82),(.245,.82));arrow(ax,(.54,.82),(.575,.82),"ruptura");arrow(ax,(.70,.76),(.70,.62));arrow(ax,(.58,.55),(.50,.32),"aberto");arrow(ax,(.295,.28),(.205,.28),"equivale")
ax.set_title("Hierarquia do defeito e ponto de ruptura não holomorfo",pad=12)
save(fig,"08-hierarquia-defeito")

# 9. Logical status pipeline
fig,ax=plt.subplots(figsize=(10,5.6));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
items=[(.10,.72,"Identidades locais\n"+r"$\Delta_{par}=\delta^2$","#ecfdf3","#067647"),(.31,.72,"Pesos e caudas\n"+r"$w, W_4, \tau(T)$","#ecfdf3","#067647"),(.53,.72,"Certificados\nfinitos $G_N$","#eff6ff","#1d4ed8"),(.75,.72,"Completude +\npositividade uniforme","#fff7ed","#c2410c"),(.90,.35,"RH","#fef2f2","#b42318")]
for x,y,t,c,e in items:box(ax,x,y,t,color=c,edge=e,width=.17 if x<.9 else .12)
for a,b in [((.185,.72),(.225,.72)),((.395,.72),(.445,.72)),((.615,.72),(.665,.72)),((.82,.67),(.87,.40))]:arrow(ax,a,b)
ax.text(.20,.88,"PROVADO",color="#067647",ha="center",weight="bold");ax.text(.53,.88,"CERTIFICADO FINITO",color="#1d4ed8",ha="center",weight="bold");ax.text(.75,.88,"LACUNA",color="#c2410c",ha="center",weight="bold")
ax.set_title("Classificação lógica: o que cada bloco realmente estabelece")
save(fig,"09-status-logico")

# 10. Three routes
fig,ax=plt.subplots(figsize=(9.5,6.2));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
box(ax,.50,.90,"RH",color="#fef2f2",edge="#b42318",width=.12)
cols=[(.18,"Via radial",r"Derivar $D(T)$\ndo lado dos primos",r"Provar $D(T)\to0$\nsem usar $\delta=0$"),(.50,"Via Weil",r"Construir $T$ de primos\n+ arquimediano",r"Provar $Q_W(g)=\|Tg\|^2$\nsem definir $T=\sqrt{Q_W}$"),(.82,"Via Gram",r"Construir base densa\n$V_N\subset A$",r"Provar $G_N\geq0$ e\ncontrole uniforme do erro")]
for x,title,a,b in cols:
    box(ax,x,.68,title,color="#eff6ff",edge="#1d4ed8",width=.22)
    box(ax,x,.45,a,width=.25,height=.13)
    box(ax,x,.20,b,color="#fff7ed",edge="#c2410c",width=.27,height=.15)
    arrow(ax,(x,.61),(x,.52));arrow(ax,(x,.37),(x,.285));arrow(ax,(x,.775),(x,.84))
ax.set_title("As três vias não circulares e suas obrigações de prova")
save(fig,"10-tres-vias")

# 11. Circularity epsilon
fig,ax=plt.subplots(figsize=(9,6.4));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
nodes=[(.5,.89,r"Definir $\Delta_{par}=\delta^2$ independentemente"),(.5,.70,r"Extensão $A[\epsilon]/(\epsilon^2-\Delta_{par})$"),(.5,.50,r"Mundo contrafactual: $\delta_0\ne0$"),(.27,.27,r"Álgebra continua consistente\n$\epsilon^2=\delta_0^2>0$"),(.73,.27,r"Construção força $\epsilon=0$\nou colapsa"),(.27,.08,"Passa no teste; ainda não prova RH"),(.73,.08,"Circularidade ou hipótese equivalente")]
for i,(x,y,t) in enumerate(nodes):
    bad=x>.5 and y<.4
    good=x<.5 and y<.4
    box(ax,x,y,t,color="#fef2f2" if bad else "#ecfdf3" if good else "#eff6ff",edge="#b42318" if bad else "#067647" if good else "#1d4ed8",width=.34 if y<.4 else .48,height=.12)
arrow(ax,(.5,.82),(.5,.77));arrow(ax,(.5,.63),(.5,.57));arrow(ax,(.44,.44),(.32,.34),"sim");arrow(ax,(.56,.44),(.68,.34),"não");arrow(ax,(.27,.20),(.27,.15));arrow(ax,(.73,.20),(.73,.15))
ax.set_title(r"Teste explícito de circularidade para $\epsilon^2=\Delta_{par}$")
save(fig,"11-teste-circularidade")

# 12. Synthetic G13
n=13
i=np.arange(n); Gm=np.exp(-abs(i[:,None]-i[None,:])/2.2)+.035*np.cos((i[:,None]+1)*(i[None,:]+1))
Gm=(Gm+Gm.T)/2
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,4.5),gridspec_kw={"width_ratios":[1.15,1]})
im=ax1.imshow(Gm,cmap="coolwarm");fig.colorbar(im,ax=ax1,fraction=.046);ax1.set_title(r"Exemplo hermitiano $G_{13}$");ax1.set_xlabel("j");ax1.set_ylabel("i")
ev=np.linalg.eigvalsh(Gm);ax2.plot(np.arange(1,n+1),ev,"o-",color="#1d4ed8");ax2.axhline(0,color="#b42318",ls="--");ax2.set(title="Espectro do exemplo",xlabel="índice",ylabel="autovalor");ax2.grid(alpha=.25)
fig.suptitle("169 entradas não substituem densidade nem controle uniforme",y=1.02)
save(fig,"12-matriz-g13")


common = r"""
\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.2cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,mathtools,bm}
\usepackage{graphicx,booktabs,longtable,array,microtype,xcolor,hyperref,fancyhdr,enumitem}
\graphicspath{{../images/}}
\definecolor{navy}{HTML}{17324D}\definecolor{rust}{HTML}{A33A2B}\definecolor{green}{HTML}{176B4D}
\hypersetup{colorlinks=true,linkcolor=navy,urlcolor=rust,citecolor=green}
\pagestyle{fancy}\fancyhf{}\lhead{Auditoria estrutural da RH}\rhead{Dossiê técnico}\cfoot{\thepage}
\newcommand{\Drad}{\mathfrak D_{\mathrm{rad}}}
\newcommand{\Dpar}{\Delta_{\mathrm{par}}}
\newcommand{\status}[2]{\par\noindent\colorbox{#1!12}{\textcolor{#1}{\textbf{#2}}}\quad}
\begin{document}
"""

main_body = r"""
\begin{titlepage}\centering
{\sffamily\bfseries\Huge Auditoria do ponto de ruptura\par}\vspace{.5cm}
{\Large Detector geométrico, defeito radial, forma de Weil e teste de circularidade\par}
\vfill
{\large Dossiê matemático e programa de pesquisa\par}\vspace{.3cm}
{\small Documento deliberadamente não reivindica uma prova da Hipótese de Riemann.\par}
\vfill{\large Agosto de 2026}\end{titlepage}
\tableofcontents\clearpage

\section{Escopo e regra de auditoria}
Este dossiê organiza o material fornecido em quatro classes: \textbf{provado}, \textbf{certificado finito}, \textbf{equivalente à RH} e \textbf{conjectural}. O objetivo é tornar explícita a passagem que ainda falta, sem converter evidência numérica ou uma definição algébrica em prova global.

\section{Geometria local do par funcional}
Escreva
\[\rho=\tfrac12+\delta+i\gamma,\qquad \rho^\sharp=1-\overline\rho=\tfrac12-\delta+i\gamma.\]
Defina
\[R_c^2=\gamma^2+\tfrac14,\quad R_+^2=R_c^2+\delta+\delta^2,\quad R_-^2=R_c^2-\delta+\delta^2.\]
Então
\[\delta=\frac{R_+^2-R_-^2}{2},\qquad \Dpar=\frac{R_+^2+R_-^2}{2}-R_c^2=\delta^2.\]
\begin{figure}[ht]\centering\includegraphics[width=.85\linewidth]{01-detector-geometrico.pdf}\caption{Detector geométrico local.}\end{figure}

\section{Simetrias e quartetos}
Fora da linha crítica, as simetrias por conjugação e pela equação funcional geram, em geral, um quarteto. Cada elemento possui o mesmo valor do peso radial definido adiante.
\begin{figure}[ht]\centering\includegraphics[width=.72\linewidth]{02-quarteto-simetrias.pdf}\caption{Quarteto associado a um desvio transversal.}\end{figure}

\section{Denominador e peso radial}
Com $A=\gamma^2+\tfrac14+\delta^2$,
\[P(\delta,\gamma)=|\rho|^2|1-\rho|^2=A^2-\delta^2,\qquad
w(\delta,\gamma)=\frac{2\delta^2}{P(\delta,\gamma)}.\]
Logo $w\ge0$ e, no domínio não trivial, $w=0$ se e somente se $\delta=0$. Para um quarteto completo, $W_4=4w$.
\begin{figure}[ht]\centering\includegraphics[width=.82\linewidth]{03-parabola-delta.pdf}\caption{O detector é exatamente quadrático.}\end{figure}
\begin{figure}[ht]\centering\includegraphics[width=.82\linewidth]{04-peso-versus-delta.pdf}\caption{Dependência do peso em $\delta$.}\end{figure}

\section{Regime de grande altura}
Para $\gamma\to\infty$ e $\delta$ fixo,
\[w(\delta,\gamma)=\frac{2\delta^2}{\gamma^4}-\frac{4\delta^2(\tfrac14+\delta^2)}{\gamma^6}+O(\gamma^{-8}).\]
O decaimento $\gamma^{-4}$ explica por que um zero muito alto, mesmo fora da linha, pode produzir perturbação extremamente pequena num detector radial truncado.
\begin{figure}[ht]\centering\includegraphics[width=.82\linewidth]{05-decaimento-gamma.pdf}\caption{Decaimento macroscópico.}\end{figure}
\begin{figure}[ht]\centering\includegraphics[width=.88\linewidth]{06-mapa-log-peso.pdf}\caption{Mapa multiescala de $w$.}\end{figure}

\section{Condicionamento numérico}
A identidade por raios é exata, mas o cálculo de $\delta^2$ por subtração de grandezas de ordem $\gamma^2$ é mal condicionado. Uma estimativa representativa é
\[\kappa_{\mathrm{pair}}\approx\frac{2\gamma^2}{\delta^2}.\]
Portanto, cálculos confiáveis devem usar $\delta=\beta-\tfrac12$ diretamente ou aritmética intervalar de precisão arbitrária.
\begin{figure}[ht]\centering\includegraphics[width=.84\linewidth]{07-condicionamento.pdf}\caption{Explosão do número de condição.}\end{figure}

\section{Identidade radial e ruptura não holomorfa}
Considere a constante
\[C_\xi=2+\gamma_E-\log(4\pi).\]
A fórmula de Hadamard e a equação funcional controlam somas holomorfas do tipo $\sum_\rho[\rho(1-\rho)]^{-1}$. A quantidade $\sum_\rho|\rho|^{-2}$ mistura $\rho$ e $\overline\rho$ e, por isso, não é obtida automaticamente pelas fórmulas explícitas holomorfas usuais. A diferença positiva é codificada por
\[\Drad=\sum_\rho \frac{2(\Re\rho-\tfrac12)^2}{|\rho|^2|1-\rho|^2}=\sum_\rho w(\rho).\]
Sob convergência e contagem de multiplicidades adequadas, $\Drad=0$ equivale a todos os termos serem nulos, portanto à RH.
\begin{figure}[ht]\centering\includegraphics[width=.94\linewidth]{08-hierarquia-defeito.pdf}\caption{A ruptura é a passagem ao termo não holomorfo.}\end{figure}

\section{Critério de Weil e matrizes truncadas}
Para funções teste admissíveis, o critério de Weil afirma que a positividade global da forma $Q_W$ é equivalente à RH. Uma família finita $\{\phi_j\}_{j=1}^N$ produz uma matriz de Gram hermitiana
\[(G_N)_{ij}=Q_W(\phi_i,\phi_j).\]
Certificar $G_N\succeq0$ para valores isolados de $N$ é evidência finita; para concluir positividade global ainda são necessários densidade da união dos espaços, continuidade de $Q_W$ e controle uniforme dos erros.
\begin{figure}[ht]\centering\includegraphics[width=.95\linewidth]{12-matriz-g13.pdf}\caption{Exemplo ilustrativo de uma matriz hermitiana $13\times13$; não representa dados certificados.}\end{figure}

\section{As três vias de fechamento}
\begin{figure}[ht]\centering\includegraphics[width=.98\linewidth]{10-tres-vias.pdf}\caption{Obrigações independentes de cada via.}\end{figure}
\paragraph{Via radial.} Derivar do lado dos primos uma representação de $\mathfrak D(T)$ e provar seu limite nulo sem usar previamente $\Re\rho=1/2$.
\paragraph{Via Weil.} Construir um operador $T$ a partir de dados primos e arquimedianos com $Q_W(g)=\|Tg\|^2$. Definir $T$ como uma raiz abstrata de $Q_W$ seria circular.
\paragraph{Via Gram.} Provar positividade certificada para todos os níveis, densidade da base e passagem contínua ao limite.

\section{Extensão algébrica e teste de circularidade}
Se $\Dpar$ é definido independentemente, a extensão
\[\mathcal A[\epsilon]/(\epsilon^2-\Dpar)\]
é uma codificação algébrica, não uma prova. Em um mundo contrafactual com $\delta_0\ne0$, ela deve permanecer coerente e satisfazer $\epsilon^2=\delta_0^2>0$. Se a construção força $\epsilon=0$ sem uma lei independente derivada dos primos, a conclusão foi embutida.
\begin{figure}[ht]\centering\includegraphics[width=.94\linewidth]{11-teste-circularidade.pdf}\caption{Teste contrafactual obrigatório.}\end{figure}

\section{Classificação final}
\begin{figure}[ht]\centering\includegraphics[width=.98\linewidth]{09-status-logico.pdf}\caption{Separação dos níveis de evidência.}\end{figure}
\begin{longtable}{p{.19\linewidth}p{.72\linewidth}}
\toprule Status & Conteúdo \\\midrule
Provado & Identidades de $R_c,R_\pm$, $\Dpar=\delta^2$, positividade local de $w$, simetrias e expansões assintóticas elementares.\\
Certificado finito & Qualquer verificação computacional em altura ou dimensão explicitamente limitada, desde que acompanhada de aritmética intervalar e dados reproduzíveis.\\
Equivalente & $\Drad=0$, positividade de Weil para todas as funções admissíveis e positividade de toda uma família completa de Gram com passagem ao limite.\\
Conjectural & Núcleo primo não derivado, métrica destrutiva, conservação que exclua $\epsilon\ne0$ e extensões para outros problemas do milênio.\\
\bottomrule
\end{longtable}

\section{Conclusão}
O detector local e sua análise multiescala são matematicamente úteis e auditáveis. O ponto de ruptura permanece a obtenção, por meios independentes da RH, de uma lei coerciva que anule o defeito global. O programa de pesquisa é válido como estrutura falsificável; não constitui solução da RH sem essa ponte.
"""

atlas_body = r"""
\begin{titlepage}\centering{\Huge\sffamily\bfseries Atlas completo de visualizações\par}\vfill{\Large Auditoria estrutural e formalização lógica\par}\vfill Agosto de 2026\end{titlepage}
\tableofcontents\clearpage
""" + "\n".join(
    f"\\section{{{title}}}\n\\begin{{center}}\\includegraphics[width=.98\\linewidth,height=.78\\textheight,keepaspectratio]{{{name}.pdf}}\\end{{center}}\\clearpage"
    for name,title in [
        ("01-detector-geometrico","Detector geométrico"),("02-quarteto-simetrias","Quarteto e simetrias"),("03-parabola-delta","Parábola do defeito local"),("04-peso-versus-delta","Peso versus desvio"),("05-decaimento-gamma","Decaimento com a altura"),("06-mapa-log-peso","Mapa multiescala"),("07-condicionamento","Condicionamento numérico"),("08-hierarquia-defeito","Hierarquia do defeito"),("09-status-logico","Classificação lógica"),("10-tres-vias","Três vias de fechamento"),("11-teste-circularidade","Teste de circularidade"),("12-matriz-g13","Matriz hermitiana de dimensão 13")])

appendix_body = r"""
\begin{titlepage}\centering{\Huge\sffamily\bfseries Caderno de fórmulas e verificações\par}\vfill{\Large Detector radial e obrigações de prova\par}\vfill Agosto de 2026\end{titlepage}
\section{Parâmetros fundamentais}
\begin{align*}
\rho&=\tfrac12+\delta+i\gamma,& \rho^\sharp&=1-\bar\rho=\tfrac12-\delta+i\gamma,\\
R_c^2&=\gamma^2+\tfrac14,& R_\pm^2&=R_c^2\pm\delta+\delta^2,\\
A&=\gamma^2+\tfrac14+\delta^2,& P&=A^2-\delta^2.
\end{align*}
\section{Reconstrução exata}
\[\delta=\frac{R_+^2-R_-^2}{2},\qquad \delta^2=\frac{R_+^2+R_-^2}{2}-R_c^2.\]
\section{Positividade local}
\[w=\frac{2\delta^2}{P}\ge0,\qquad w=0\Longleftrightarrow\delta=0,\qquad W_4=4w.\]
Para $|\delta|<1/2$ e $\gamma\ne0$, o denominador é estritamente positivo porque é o produto $|\rho|^2|1-\rho|^2$.
\section{Expansão assintótica}
Pondo $a=\tfrac14+\delta^2$,
\begin{align*}
P&=\gamma^4+2a\gamma^2+(a^2-\delta^2),\\
P^{-1}&=\gamma^{-4}\left(1-2a\gamma^{-2}+O(\gamma^{-4})\right),\\
w&=2\delta^2\gamma^{-4}-4\delta^2a\gamma^{-6}+O(\gamma^{-8}).
\end{align*}
\section{Constante radial}
\[C_\xi=2+\gamma_E-\log(4\pi)\approx0.0461914179322420676.\]
\section{Defeito global}
\[\Drad=\sum_\rho\frac{2(\Re\rho-\tfrac12)^2}{|\rho|^2|1-\rho|^2}.\]
Cada parcela é não negativa. A dificuldade não está nessa positividade, mas em provar a anulação da soma por uma identidade independente que alcance o termo não holomorfo.
\section{Forma de Weil}
\[Q_W(g)=\sum_\rho\widetilde g(\rho)\overline{\widetilde g(1-\bar\rho)}.\]
A obrigação construtiva é produzir $T$ a partir do lado dos primos e provar $Q_W(g)=\|Tg\|^2$ sem assumir a positividade que se deseja concluir.
\section{Matrizes de Gram}
\[(G_N)_{ij}=Q_W(\phi_i,\phi_j),\qquad G_N=G_N^*,\qquad G_N\succeq0.\]
Uma conclusão global exige: (i) positividade em todos os níveis; (ii) união densa dos espaços; (iii) módulo de continuidade para $Q_W$; (iv) erros intervalares uniformes.
\section{Extensão por $\epsilon$}
\[\mathbb{RC}=\mathcal A[\epsilon]/(\epsilon^2-\Dpar).\]
Em geral $\epsilon$ não é nilpotente quando $\Dpar\ne0$. Declarar $\epsilon^2=0$ universalmente é equivalente a impor o setor crítico.
\section{Checklist de não circularidade}
\begin{enumerate}[label=\arabic*.]
\item Definir todos os objetos antes de assumir RH.
\item Repetir a construção num cenário com um zero sintético fora da linha.
\item Identificar exatamente qual lema falha nesse cenário.
\item Exigir que esse lema seja derivado de dados primos e arquimedianos.
\item Não converter certificados finitos em quantificadores universais.
\end{enumerate}
"""

for filename, body in [("dossie-auditoria-rh.tex", main_body), ("atlas-visualizacoes.tex", atlas_body), ("caderno-formulas.tex", appendix_body)]:
    (TEX / filename).write_text(common + body + "\n\\end{document}\n", encoding="utf-8")

readme = """# Pacote de auditoria estrutural

## PDFs
- `dossie-auditoria-rh.pdf`: exposição matemática completa e classificação lógica.
- `atlas-visualizacoes.pdf`: as 12 imagens, uma por seção.
- `caderno-formulas.pdf`: fórmulas, expansões e checklist de circularidade.

## Fontes
Os fontes LaTeX estão em `latex/`; cada imagem existe em PNG e PDF vetorial em `images/`.

## Compilação
Execute `xelatex` duas vezes em cada arquivo dentro da pasta `latex/`.

## Nota científica
O pacote não reivindica prova da Hipótese de Riemann. Resultados locais, certificados finitos, equivalências e conjecturas são separados explicitamente.
"""
(OUT / "README.md").write_text(readme, encoding="utf-8")
print(f"Generated in {OUT}")
