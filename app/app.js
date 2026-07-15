const problems={
 PvsNP:{label:"P versus NP",statement:"P ≠ NP",dominant:"t",law:"segurança criptográfica não implica P ≠ NP"},
 Riemann:{label:"Hipótese de Riemann",statement:"todo zero não trivial tem parte real 1/2",dominant:"x",law:"resultados são condicionais a RH"},
 Hodge:{label:"Conjetura de Hodge",statement:"classes de Hodge racionais são algébricas",dominant:"z",law:"a obstrução deve ser definida geometricamente"},
 NavierStokes:{label:"Navier–Stokes",statement:"existência e suavidade global em 3D",dominant:"x,y,z,t",law:"simulação finita não decide regularidade global"},
 YangMills:{label:"Yang–Mills",statement:"existência quântica e gap de massa positivo",dominant:"e",law:"e não é literalmente o gap de massa"},
 BSD:{label:"Birch–Swinnerton-Dyer",statement:"ordem do zero de L(E,s) é o rank",dominant:"x,y",law:"Sha finito é hipótese adicional"},
 Poincare:{label:"Poincaré",statement:"toda 3-variedade fechada simplesmente conexa é S³",dominant:"x,y,z",law:"teorema resolvido; serve apenas como referência"}
};
const langs=["Lean","Coq","Isabelle","Agda","LaTeX","JSON"]; let generated={};
for(const [k,v] of Object.entries(problems)) problem.add(new Option(v.label,k));
function ident(s){return s.replace(/[^A-Za-z0-9]/g,"")}
function calculate(p){let n=Math.max(2,p.samples),dt=p.duration/(n-1),real=0,imag=0;for(let i=0;i<n;i++){let t=i*dt,e=p.exodus*Math.sin(Math.PI*t/p.duration),speed=1;let L=speed*speed+p.alpha*t*t-p.beta*e*e;let w=(i===0||i===n-1)?.5:1;real+=w*L*dt;imag+=w*e*dt}return{real,imag,dt}}
function spec(){return{problem:problem.value,truth:truth.value,axiom:axiom.checked,alpha:+alpha.value,beta:+beta.value,duration:+duration.value,samples:+samples.value,exodus:+exodus.value}}
function exportsFor(p,c){let q=problems[p.problem],N=ident(p.problem),ax=p.axiom;
 let proposition=`${N}Statement`; let status=ax?"axiom":"def";
 return {
 Lean:`inductive Triv where | false | half | true\n\ndef ${proposition} : Prop := ${ax?"True":"True -- TODO: encode the mathematical statement"}\n${ax?`axiom ${N}Axiom : ${proposition}`:`-- obligation: prove or refute ${proposition}`}\n\ndef regime : Triv := .${p.truth}\n\n-- Numeric approximation is evidence about this model, not a proof.\ndef actionReal : Float := ${c.real.toFixed(8)}\ndef actionImag : Float := ${c.imag.toFixed(8)}`,
 Coq:`Inductive Triv := F | H | T.\nDefinition ${proposition} : Prop := True.\n${ax?`Axiom ${N}Axiom : ${proposition}.`:`(* Proof obligation: ${proposition} *)`}\nDefinition regime : Triv := ${p.truth==='false'?'F':p.truth==='half'?'H':'T'}.`,
 Isabelle:`theory ${N} imports Main begin\ndatatype triv = F | H | T\ndefinition ${proposition} :: bool where \"${proposition} ≡ True\"\n${ax?`axiomatization where ${N}_axiom: \"${proposition}\"`:`text ‹Proof obligation: ${proposition}›`}\nend`,
 Agda:`module ${N} where\n\ndata Triv : Set where F H T : Triv\n\npostulate\n  ${proposition} : Set\n${ax?`  ${N}Axiom : ${proposition}`:`-- No inhabitant is postulated: this is an open obligation.`}`,
 LaTeX:`\\section{${q.label}}\n\\textbf{Status:} ${ax?'Axioma de trabalho':'Obrigação aberta'}.\\\n\\[S[\\gamma] \\approx ${c.real.toFixed(5)} + i\,${c.imag.toFixed(5)}\\]\nO valor numérico caracteriza apenas a trajetória escolhida. Não demonstra: ``${q.statement}''.`,
 JSON:JSON.stringify({...p,statement:q.statement,dominantAxis:q.dominant,action:c,classification:ax?"assumption":"proof-obligation"},null,2)} }
function render(lang){output.textContent=generated[lang];[...tabs.children].forEach(b=>b.classList.toggle('active',b.textContent===lang))}
form.addEventListener('submit',e=>{e.preventDefault();let p=spec(),c=calculate(p),q=problems[p.problem];generated=exportsFor(p,c);badges.innerHTML=`<span class="badge">eixo ${q.dominant}</span><span class="badge gold">${p.axiom?'axioma assumido':'obrigação aberta'}</span>`;metrics.innerHTML=`<dt>Re S[γ]</dt><dd>${c.real.toFixed(6)}</dd><dt>Im S[γ]</dt><dd>${c.imag.toFixed(6)}</dd><dt>Δt</dt><dd>${c.dt.toFixed(6)}</dd><dt>Regime</dt><dd>${p.truth}</dd>`;warning.textContent=q.law+". A integração é trapezoidal e depende dos parâmetros escolhidos.";tabs.innerHTML='';langs.forEach(l=>{let b=document.createElement('button');b.textContent=l;b.type='button';b.onclick=()=>render(l);tabs.appendChild(b)});render('Lean')});form.requestSubmit();
