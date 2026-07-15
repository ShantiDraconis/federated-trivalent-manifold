# Navier–Stokes — caderno formal

## Equações-alvo

Para velocidade incompressível \(u:\mathbb R^3\times[0,\infty)\to\mathbb R^3\),
\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u+f,\qquad \nabla\cdot u=0.
\]
O alvo oficial pede existência e suavidade global sob os dados prescritos, ou um cenário admissível de breakdown.

## Discretização FTM

Em uma família refinável \(F_h\), definir espaços \(V_h,Q_h\) e operadores
\[
\nabla_h,\quad \operatorname{div}_h,\quad \Delta_h,\quad P_h
\]
com compatibilidade de colagem e, idealmente, um complexo discreto exato.

## Obrigações

**NS1 — consistência:** resíduos tendem a zero para soluções suaves.

**NS2 — estabilidade energética:**
\[
\|u_h(t)\|_2^2+2\nu\int_0^t\|\nabla_hu_h\|_2^2\,ds
\le \|u_h(0)\|_2^2+\text{forçamento}.
\]

**NS3 — compacidade:** extrair limite que resolva as equações.

**NS4 — estimativa crítica:** obter controle uniforme numa norma com escala correta, suficiente para regularidade global; ou construir limite singular que satisfaça exatamente as hipóteses oficiais.

Convergência para solução fraca não resolve regularidade. Simulação de vórtices não prova blow-up.

## Testes

Fluxos com solução conhecida, conservação/incompressibilidade, refinamento anisotrópico, independência da decomposição federada e análise do termo convectivo.

**Maturidade atual:** M1 conceitual; NS1–NS4 OPEN.
