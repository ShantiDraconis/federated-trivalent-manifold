export const STATUS = {
  PROVED: { label: "Provado", tone: "proved" },
  FINITE_CERTIFICATE: { label: "Certificado finito", tone: "finite" },
  CONDITIONAL: { label: "Condicional", tone: "conditional" },
  EQUIVALENT: { label: "Equivalente ao alvo", tone: "equivalent" },
  CONJECTURAL: { label: "Conjectural", tone: "conjectural" },
  REFUTED: { label: "Refutado", tone: "refuted" },
  OPEN: { label: "Aberto", tone: "open" },
};

export const problems = [
  {
    id: "riemann",
    short: "RH",
    name: "Hipótese de Riemann",
    domain: "Teoria analítica dos números",
    maturity: "M1",
    status: "OPEN",
    summary: "Audita detectores de cauda, defeito radial, forma de Weil e pontes primo-zero.",
    metrics: ["G₀", "σD", "σI", "A_H", "Δpar", "D_rad"],
    nodes: [
      ["RH-L1", "Simetrias dos zeros", "PROVED", []],
      ["RH-L2", "Detector geométrico Δpar = δ²", "PROVED", ["RH-L1"]],
      ["RH-L3", "Positividade do peso radial", "PROVED", ["RH-L2"]],
      ["RH-L4", "Supressão γ⁻⁴", "PROVED", ["RH-L3"]],
      ["RH-L6", "Convergência para potência lentamente variável", "CONDITIONAL", []],
      ["RH-L7", "Detector integral por Karamata", "CONDITIONAL", ["RH-L6"]],
      ["RH-D9", "Regularização quadrática A_H", "PROVED", []],
      ["RH-C10", "Persistência coerente implica classe espectral", "OPEN", ["RH-L6", "RH-L7", "RH-D9"]],
      ["RH-E11", "Excluir classes σ₀ > 1/2", "EQUIVALENT", ["RH-C10"]],
    ],
  },
  {
    id: "p-vs-np", short: "P/NP", name: "P versus NP", domain: "Complexidade computacional",
    maturity: "M0", status: "OPEN", summary: "Separa modelagem de linguagens, reduções e limites inferiores universais.",
    metrics: ["tamanho", "certificado", "redução", "barreiras"],
    nodes: [
      ["P-N1", "Codificação e tamanho", "OPEN", []], ["P-N2", "Verificador polinomial", "OPEN", ["P-N1"]],
      ["P-N3", "Redução many-one", "OPEN", ["P-N1"]], ["P-N4", "Limite inferior universal", "OPEN", ["P-N2", "P-N3"]],
      ["P-GAP", "Contornar barreiras conhecidas", "OPEN", ["P-N4"]],
    ],
  },
  {
    id: "navier-stokes", short: "NS", name: "Navier-Stokes", domain: "EDPs e análise",
    maturity: "M1", status: "OPEN", summary: "Monitora energia, consistência, compacidade e normas críticas.",
    metrics: ["energia", "enstrofia", "norma crítica", "resíduo"],
    nodes: [
      ["NS-N1", "Existência local", "PROVED", []], ["NS-N2", "Desigualdade de energia", "PROVED", ["NS-N1"]],
      ["NS-N3", "Compacidade de aproximações", "CONDITIONAL", ["NS-N2"]], ["NS-N4", "Estimativa crítica uniforme", "OPEN", ["NS-N3"]],
      ["NS-GAP", "Regularidade global ou blow-up admissível", "OPEN", ["NS-N4"]],
    ],
  },
  {
    id: "yang-mills", short: "YM", name: "Yang-Mills e gap de massa", domain: "Teoria quântica de campos",
    maturity: "M1", status: "OPEN", summary: "Audita regularização, limites, axiomas, não trivialidade e gap.",
    metrics: ["positividade", "escala a", "volume", "gap Δ"],
    nodes: [
      ["YM-N1", "Regularização finita", "FINITE_CERTIFICATE", []], ["YM-N2", "Estimativas uniformes", "OPEN", ["YM-N1"]],
      ["YM-N3", "Limite contínuo", "OPEN", ["YM-N2"]], ["YM-N4", "Não trivialidade", "OPEN", ["YM-N3"]],
      ["YM-GAP", "Gap no limite infinito", "OPEN", ["YM-N3", "YM-N4"]],
    ],
  },
  {
    id: "hodge", short: "H", name: "Conjectura de Hodge", domain: "Geometria algébrica",
    maturity: "M0", status: "OPEN", summary: "Verifica domínio, decomposição de Hodge e mapa de ciclos.",
    metrics: ["Hᵖᵖ", "ciclos", "cohomologia", "descida"],
    nodes: [
      ["H-N1", "Domínio suave projetivo", "OPEN", []], ["H-N2", "Descida preserva tipo (p,p)", "OPEN", ["H-N1"]],
      ["H-N3", "Compatibilidade do mapa de ciclos", "OPEN", ["H-N2"]], ["H-GAP", "Sobrejetividade racional", "OPEN", ["H-N3"]],
    ],
  },
  {
    id: "bsd", short: "BSD", name: "Birch-Swinnerton-Dyer", domain: "Geometria aritmética",
    maturity: "M1", status: "OPEN", summary: "Rastreia fatores locais, L-função, posto, Selmer e Sha.",
    metrics: ["ord L", "posto", "Selmer", "Sha", "regulador"],
    nodes: [
      ["BSD-N1", "Fatores locais e condutor", "CONDITIONAL", []], ["BSD-N2", "Produto global", "OPEN", ["BSD-N1"]],
      ["BSD-N3", "Posto e regulador", "CONDITIONAL", []], ["BSD-N4", "Selmer e Sha", "OPEN", ["BSD-N3"]],
      ["BSD-GAP", "Ordem de anulação igual ao posto", "OPEN", ["BSD-N2", "BSD-N4"]],
    ],
  },
  {
    id: "poincare", short: "PC", name: "Poincaré (banco de validação)", domain: "Topologia geométrica",
    maturity: "M1", status: "PROVED", summary: "Problema resolvido usado para testar fidelidade do formalismo FTM.",
    metrics: ["π₁", "homologia", "tipo PL", "Pachner"],
    nodes: [
      ["PC-N1", "Codificar triangulações", "OPEN", []], ["PC-N2", "Invariância por Pachner", "OPEN", ["PC-N1"]],
      ["PC-N3", "Preservar π₁ e tipo PL", "OPEN", ["PC-N2"]], ["PC-TEST", "Recuperar casos conhecidos", "FINITE_CERTIFICATE", ["PC-N3"]],
    ],
  },
];

export const scenarios = {
  riemann: {
    controls: [
      { id: "sigma", label: "σ₀ candidato", min: 0.5, max: 0.99, step: 0.01, value: 0.75 },
      { id: "gamma", label: "altura γ", min: 10, max: 1000, step: 10, value: 100 },
      { id: "delta", label: "desvio δ", min: 0, max: 0.49, step: 0.01, value: 0.1 },
    ],
  },
};
