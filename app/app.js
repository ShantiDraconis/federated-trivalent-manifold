import { problems, STATUS, scenarios } from "./data.js";

const $ = (selector) => document.querySelector(selector);
const problemList = $("#problemList");
const problemHeader = $("#problemHeader");
const lemmaTree = $("#lemmaTree");
const legend = $("#legend");
let selected = problems[0];

function statusBadge(status) {
  const meta = STATUS[status];
  return `<span class="status ${meta.tone}">${meta.label}</span>`;
}

function renderOrbit() {
  const orbit = $("#orbit");
  problems.forEach((problem, index) => {
    const angle = (Math.PI * 2 * index) / problems.length - Math.PI / 2;
    const radius = index % 2 ? 40 : 34;
    const node = document.createElement("a");
    node.href = `#tree`;
    node.className = "orbit-node";
    node.textContent = problem.short;
    node.title = problem.name;
    node.style.left = `${50 + Math.cos(angle) * radius}%`;
    node.style.top = `${50 + Math.sin(angle) * radius}%`;
    node.addEventListener("click", () => selectProblem(problem.id));
    orbit.append(node);
  });
}

function renderStats() {
  const nodes = problems.flatMap((problem) => problem.nodes);
  $("#nodeCount").textContent = nodes.length;
  $("#openCount").textContent = nodes.filter((node) => ["OPEN", "EQUIVALENT"].includes(node[2])).length;
}

function renderProblemList() {
  problemList.innerHTML = problems.map((problem) => `
    <button class="problem-button ${problem.id === selected.id ? "active" : ""}" data-id="${problem.id}">
      <span class="short">${problem.short}</span><span><strong>${problem.name}</strong><small>${problem.maturity} · ${problem.domain}</small></span><i class="dot"></i>
    </button>`).join("");
  problemList.querySelectorAll("button").forEach((button) => button.addEventListener("click", () => selectProblem(button.dataset.id)));
}

function renderProblem() {
  problemHeader.innerHTML = `<p class="eyebrow">${selected.short} · ${selected.domain}</p><h3>${selected.name}</h3><p class="lead">${selected.summary}</p><div class="problem-meta"><span class="tag">maturidade ${selected.maturity}</span>${selected.metrics.map((metric) => `<span class="tag">${metric}</span>`).join("")}</div>`;
  legend.innerHTML = [...new Set(selected.nodes.map((node) => node[2]))].map(statusBadge).join("");
  lemmaTree.innerHTML = selected.nodes.map(([id, title, status, deps]) => {
    const meta = STATUS[status];
    return `<article class="lemma-node ${meta.tone}"><code>${id}</code><p><strong>${title}</strong><small>${deps.length ? `depende de ${deps.join(", ")}` : "nó de base"}</small></p>${statusBadge(status)}</article>`;
  }).join("");
}

function selectProblem(id) {
  selected = problems.find((problem) => problem.id === id) || problems[0];
  renderProblemList(); renderProblem();
}

function setupControls() {
  const controls = $("#controls");
  controls.innerHTML = `<h3>Cenário sintético</h3><p class="lead">Ajuste a classe candidata e observe a dificuldade de visibilidade.</p>` + scenarios.riemann.controls.map((control) => `
    <div class="control"><label for="${control.id}">${control.label}<output id="${control.id}Value">${control.value}</output></label><input id="${control.id}" type="range" min="${control.min}" max="${control.max}" step="${control.step}" value="${control.value}"></div>`).join("");
  controls.querySelectorAll("input").forEach((input) => input.addEventListener("input", updateLab));
  updateLab();
}

function updateLab() {
  const sigma = Number($("#sigma").value), gamma = Number($("#gamma").value), delta = Number($("#delta").value);
  $("#sigmaValue").value = sigma.toFixed(2); $("#gammaValue").value = gamma.toFixed(0); $("#deltaValue").value = delta.toFixed(2);
  const a = gamma ** 2 + .25 + delta ** 2;
  const w = delta === 0 ? 0 : 2 * delta ** 2 / (a ** 2 - delta ** 2);
  const conditioning = delta === 0 ? Infinity : 2 * gamma ** 2 / delta ** 2;
  drawPlot(sigma, gamma);
  $("#diagnostic").innerHTML = `
    <article><span>peso radial</span><strong>${w.toExponential(3)}</strong></article>
    <article><span>condicionamento</span><strong>${Number.isFinite(conditioning) ? conditioning.toExponential(2) : "∞"}</strong></article>
    <article><span>quarteto sintético</span><strong>${(4*w).toExponential(3)}</strong></article>
    <article><span>classificação</span><strong>${delta === 0 ? "linha crítica" : "contrafactual"}</strong></article>`;
}

function drawPlot(sigma, gamma) {
  const canvas = $("#plot"), ctx = canvas.getContext("2d");
  const width = canvas.width, height = canvas.height, pad = 52;
  ctx.clearRect(0, 0, width, height); ctx.fillStyle = getComputedStyle(document.body).getPropertyValue("--surface"); ctx.fillRect(0,0,width,height);
  const xMax = 120, yMin = .35, yMax = 1.05;
  const X = (x) => pad + x / xMax * (width - 2*pad), Y = (y) => height-pad-(y-yMin)/(yMax-yMin)*(height-2*pad);
  ctx.strokeStyle = "#64748b55"; ctx.lineWidth = 1;
  for(let i=0;i<=6;i++){const y=yMin+(yMax-yMin)*i/6;ctx.beginPath();ctx.moveTo(pad,Y(y));ctx.lineTo(width-pad,Y(y));ctx.stroke();ctx.fillStyle="#93a8c4";ctx.fillText(y.toFixed(2),8,Y(y)+4)}
  const series = [
    {color:"#5eead4", fn:(u)=>sigma+Math.log(Math.max(u,2))/Math.max(u,2)},
    {color:"#fbbf24", fn:(u)=>sigma+1/Math.max(u,2)+.055*Math.sin(gamma*u/180)*Math.exp(-u/80)},
    {color:"#c084fc", fn:(u)=>sigma+1.7/Math.max(u,3)},
  ];
  series.forEach(({color,fn})=>{ctx.beginPath();ctx.strokeStyle=color;ctx.lineWidth=3;for(let x=2;x<=xMax;x++){const px=X(x),py=Y(fn(x));x===2?ctx.moveTo(px,py):ctx.lineTo(px,py)}ctx.stroke()});
  ctx.setLineDash([8,7]);ctx.strokeStyle="#fb7185";ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(pad,Y(sigma));ctx.lineTo(width-pad,Y(sigma));ctx.stroke();ctx.setLineDash([]);
  ctx.fillStyle="#93a8c4";ctx.fillText("u = log x (escala compactificada)",width/2-80,height-12);
}

$("#themeToggle").addEventListener("click", () => { document.body.classList.toggle("light"); localStorage.setItem("ftm-theme", document.body.classList.contains("light") ? "light" : "dark"); updateLab(); });
if (localStorage.getItem("ftm-theme") === "light") document.body.classList.add("light");
if ("serviceWorker" in navigator) navigator.serviceWorker.register("./sw.js");
renderOrbit(); renderStats(); renderProblemList(); renderProblem(); setupControls();
