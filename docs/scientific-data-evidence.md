# Dados atômicos, cosmológicos e bioquímicos: ontologia e limites de prova

## 1. Regra fundamental

Um dado empírico \(d\) nunca prova diretamente um enunciado matemático abstrato \(P\). A cadeia válida é

\[
d \xrightarrow{\text{calibração}} D
\xrightarrow{\text{inferência}} M
\xrightarrow{\text{ponte provada }B} P.
\]

Sem um teorema \(B:(D,M)\Rightarrow P\), o dado pode calibrar implementação, restringir/refutar modelo físico, revelar contraexemplo auxiliar, sugerir construção ou testar consequências computáveis; mas não promover \(P\) para **PROVED**.

O arquivo **FTM/EvidenceStates.lean** demonstra a regra mínima: se a redução não foi provada, a auditoria não estabelece o alvo.

## 2. Três estados e estados adicionais

### Estados de proposição formal

1. **PROVED:** derivação válida nas hipóteses e axiomas declarados.
2. **REFUTED:** prova da negação ou contraexemplo pertencente ao domínio.
3. **OPEN:** nem prova nem refutação conhecidas.

### Outros estados

- **INDEPENDENT_OF_AXIOMS:** nem \(P\) nem \(\neg P\) são deriváveis do sistema, supondo consistência.
- **INCONSISTENT_PREMISES:** hipóteses implicam contradição.
- **ILL_POSED:** termos, domínio ou quantificadores indefinidos.
- **OUT_OF_DOMAIN:** dado/contraexemplo não satisfaz hipóteses.
- **MODEL_DEPENDENT:** conclusão válida somente sob modelos declarados.
- **UNDERDETERMINED:** múltiplos modelos explicam os dados.
- **DISPUTED, RETRACTED, SUPERSEDED, CENSORED:** estados do ciclo de evidência.
- **INCONSISTENT_DATA:** tensão além do modelo de erro declarado.

Os últimos descrevem evidência, não a verdade lógica de \(P\). Misturar eixos é erro de tipo.

## 3. Catálogo atômico

“Todos os dados atômicos” não é tabela finita estável. O catálogo referencia bases versionadas e registra observações pelo esquema JSON.

| Família | Objetos | Classes numéricas | Operadores |
|---|---|---|---|
| constantes | \(c,h,e,m_e,m_p,\alpha,R_\infty\) | exato, medição, covariância | ajuste, incerteza, conversão SI |
| partículas | massa, carga, spin, vida, branching ratios | intervalos, limites, distribuições | combinação, likelihood, sistemáticos |
| núcleos/isótopos | \(Z,A\), massa, ligação, meia-vida | inteiros + medidas | energia, cadeias de decaimento |
| espectroscopia | níveis, linhas, larguras | frequências/energias | Fourier, ajuste, deconvolução |
| colisões | seções de choque, amplitudes | funções/tensores | ondas parciais, integração, unfolding |
| estrutura eletrônica | densidade, matrizes, orbitais | funções/autovalores | Schrödinger/Dirac, diagonalização |
| termoquímica | entalpia, entropia, potencial | medidas condicionais | Legendre, normalização |

Fontes-base: CODATA/NIST e PDG. Versão e correlações são obrigatórias.

## 4. Catálogo cosmológico

Parâmetros são frequentemente inferidos sob modelo, não medidos diretamente.

| Camada | Dados | Classe | Operadores |
|---|---|---|---|
| instrumentação | timestream, apontamento, beam, ruído | séries/tensores | calibração, filtragem |
| mapas | CMB, galáxias, lensing | campos | map-making, harmônicos |
| sumários | \(C_\ell\), BAO, distâncias SN | espectros/covariâncias | estimadores, janelas |
| parâmetros | \(H_0,\Omega_b,\Omega_c,n_s,\tau,\sigma_8\) | posterior | Bayes/MCMC |
| estrutura | halos, voids, funções de massa | catálogos/grafos | clustering, inversão |
| transientes | supernovas, GRBs, ondas gravitacionais | séries/likelihood | matched filtering |

Um \(H_0\) sem likelihood, covariância, dados e modelo não é registro suficiente.

## 5. Catálogo bioquímico

| Família | Dados | Classe | Operadores |
|---|---|---|---|
| sequência | DNA/RNA/proteína, variantes | palavra categórica | alinhamento, tradução, homologia |
| estrutura | coordenadas, ocupância, B-factor | tensor + incerteza | superposição, refinamento |
| cinética | \(K_m,k_{cat},K_d,k_{on},k_{off}\) | medidas | ajuste não linear |
| termodinâmica | \(\Delta G,\Delta H,\Delta S\) | medidas | ciclos, integração |
| ômicas | contagens/abundâncias | distribuições | normalização, teste múltiplo |
| redes | interação/metabolismo | grafo/hipergrafo | fluxo, estequiometria |
| função | atividade/localização/fenótipo | ontologia + evidência | curadoria, causalidade |
| química | átomos/ligações/estereoquímica | grafo rotulado | subestrutura, dinâmica |

UniProt distingue anotação revisada e automática; wwPDB usa PDBx/mmCIF com dicionários e integridade referencial.

## 6. Matriz domínio × Problema

### Poincaré

Dados dos três domínios fornecem nuvens, campos e redes para testar reconstrução topológica. Podem refutar um **algoritmo FTM** que classifique um complexo conhecido incorretamente; não provam Poincaré. Se a ponte falha, refuta-se o reconstrutor, não o teorema.

### Hodge

Modelos atômicos/cosmológicos podem gerar variedades de parâmetros; dados bioquímicos podem gerar topologia persistente. Nada disso produz automaticamente ciclos algébricos racionais. Um cálculo formal pode refutar uma alegação auxiliar sobre ciclo explícito. Prova universal exige sobrejetividade do mapa de ciclos no domínio oficial.

### Yang–Mills

Dados de partículas calibram teorias efetivas e regularizações; cosmologia restringe campos; dinâmica molecular é analogia estatística. Uma observação pode refutar regularização que viole gauge/positividade/limite. Decaimento exponencial finito não prova gap quântico 4D.

### Navier–Stokes

Dinâmica molecular testa emergência do contínuo; plasmas cosmológicos muitas vezes não pertencem ao PDE incompressível oficial; microfluídica fornece benchmarks. Dados podem refutar esquemas e estimativas. Nenhuma amostra finita prova suavidade global. Blow-up numérico precisa de erro certificado e passagem ao limite.

### P versus NP

Annealing, problemas inversos cosmológicos, folding e docking geram instâncias. Podem refutar alegação concreta de desempenho por família adversarial. Desempenho finito não separa classes. É necessária redução polinomial e análise assintótica.

### Riemann

Espectros atômicos podem exibir estatísticas semelhantes; outros sinais testam métodos. Um zero certificado fora da reta refutaria RH. Verificação até altura \(T\) não prova o infinito. Falha de analogia espectral não refuta RH.

### BSD

Os domínios fornecem workloads, não cobrem curvas sobre \(\mathbb Q\). Curva explícita com invariantes certificados poderia refutar BSD; famílias verificadas apenas validam casos. Falha de ponte RH–BSD não decide nenhuma conjectura.

## 7. Tabela dos estados de uma ponte \(B:D\to P\)

| Ponte | Dados | Conclusão permitida |
|---|---|---|
| provada, hipóteses satisfeitas | validado | consequência formal para \(P\) |
| provada | contraditório certificado | refuta hipótese/modelo/\(P\), conforme direção |
| refutada | qualquer | rota falha; \(P\) mantém estado |
| aberta | favorável | suporte heurístico |
| aberta | desfavorável | tensão com versão concreta de \(B\) |
| independente | qualquer | mudar axiomas/reformular |
| mal posta | qualquer | nenhuma inferência |
| dados inconsistentes | — | revisar calibração/covariância/modelo |

## 8. Operadores e operações

- **Metrológicos:** calibração, rastreabilidade, unidade, fundo, deconvolução, incerteza e covariância.
- **Estatísticos:** likelihood, Bayes, bootstrap, testes, multiplicidade, seleção, causalidade, sensibilidade.
- **Analíticos:** limite, derivada, integral, Fourier/Laplace, espectro, regularização, renormalização, coarse-graining.
- **Algébrico-topológicos:** funtores, quocientes, tensor, homologia, cohomologia, classes, mapas de ciclos, gauge.
- **Computacionais:** codificação, redução, certificado, aritmética intervalar, hashing e esquema.
- **Bioinformáticos:** alinhamento, variantes, filogenia, superposição, fluxo metabólico e ontologias.

## 9. Classes numéricas

Inteiros/racionais exatos; algébricos; floats; intervalos reais/complexos certificados; medições com incerteza/covariância; limites e censura; distribuições/posteriores; séries, sequências, grafos, tensores; categorias e ontologias.

Não se converte automaticamente posterior em verdade, float em real exato ou correlação em causalidade.

## 10. Auditoria das alegações v4.1 do anexo

| Alegação | Estado correto | Motivo |
|---|---|---|
| \(10^{-6}\) prova não-colapso | REFUTED | só prova crescimento da variável definida, não coercividade |
| W crescente prova imunidade a DoS | REFUTED | não limita CPU, memória, fila ou rede |
| AES-512 | REFUTED como AES padrão | FIPS 197 define 128/192/256 |
| \(O(1)\) implica latência zero | REFUTED | assintótico não fixa constante, concorrência ou I/O |
| 10 mil requisições provam segurança | REFUTED | teste amostral não é prova universal/adversarial |
| \(S_{eff}^2\) é “\(S^2\) de Perelman” | HEURISTIC | quadrado não cria identidade geométrica |
| matriz Div é universal | ILL_POSED | conjuntos, medida, pesos e proveniência ausentes |
| 65,2% de igualdade RH–BSD | UNSUPPORTED | deriva de matriz sem protocolo reproduzível |
| Lean compila, logo física é verdadeira | REFUTED | Lean verifica codificação/axiomas, não adequação empírica |
| cirurgia reduz \(e\) pela metade | DEFINITION | regra de algoritmo, não teorema sobre vulnerabilidade |

## 11. Ingestão e fontes

- NIST/CODATA: constantes, unidades, incertezas e correlações.
- PDG: partículas, revisões e limites.
- ESA/Planck: mapas, likelihoods e parâmetros condicionais.
- UniProtKB: sequências/anotações revisadas e automáticas.
- wwPDB/PDBx-mmCIF: estruturas, metadados e dicionários.

O repositório guarda identificadores e versões, não cópias integrais. Ingestões futuras devem gerar hashes, registrar licença e preservar a fonte.
