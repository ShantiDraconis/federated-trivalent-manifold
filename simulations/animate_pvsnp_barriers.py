"""
animate_pvsnp_barriers.py
SE'ET Refutation Engine — Animation 3
P vs NP: three formal barriers to circuit lower-bound proofs.

Frame layout (18 frames, neon palette):
  1–4   : AC⁰[p] — Razborov-Smolensky lower bounds work, depth d=O(1)  [BEFORE]
  5–7   : Three barriers fire sequentially                               [BREAK]
            Frame 5 : Natural Proofs barrier (Razborov-Rudich 1994)
            Frame 6 : Relativisation barrier (Baker-Gill-Solovay 1975)
            Frame 7 : Algebrisation barrier (Aaronson-Wigderson 2008)
  8–18  : Post-break — degree bound D = n^{O(log log S)} explodes,
           current techniques cannot separate P from NP                  [AFTER]

Output: figures/anim_pvsnp_barriers.gif

Key values (Lema L_A1_2 / L_C2):
  N_max_finite = 25.516  (finite barrier, O(2^N) at 16ms Quest3)
  D_degree     = (log S)^d  → n^{O(log log S)} when d = log n  (out of control)
  sigma_refute = N/A (complexity, not statistics)
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.animation as animation
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

# ── Neon palette ──────────────────────────────────────────────────────────────
BG = "#0a0a0f"
CYAN = "#00ffe7"
MAGENTA = "#ff00cc"
YELLOW = "#ffe600"
ORANGE = "#ff8800"
GREEN = "#00ff88"
DIM = "#2a2a3a"
WHITE = "#ffffff"

N_FRAMES = 18

BARRIERS = [
    ("Natural Proofs\n(Razborov-Rudich 1994)", MAGENTA, 4),
    ("Relativisation\n(Baker-Gill-Solovay 1975)", ORANGE, 5),
    ("Algebrisation\n(Aaronson-Wigderson 2008)", YELLOW, 6),
]


# ── Degree blow-up curve ──────────────────────────────────────────────────────

def degree_bound(frame: int, n: float = 100.0, S: float = 1e6) -> float:
    """Polynomial degree required by the Razborov-Smolensky extension."""
    log_S = np.log2(S)
    if frame < 5:
        d = 1.0 + 0.5 * frame          # d = O(1) — AC⁰ regime
    elif frame < 8:
        d = 2.0 + 2.0 * (frame - 4)   # d starts growing at break
    else:
        d = 10.0 + 3.0 * (frame - 7)  # d = log n territory
    if d <= np.log2(n):
        return log_S ** d              # (log S)^d — under control
    # d > log n: degree = n^{O(log log S)}
    return n ** (np.log2(log_S) * (d / np.log2(n)))


def circuit_complexity_curve(frames_range: range) -> np.ndarray:
    """Effective circuit-size lower bound derivable at each frame."""
    vals = []
    for f in frames_range:
        if f < 5:
            # Smolensky bound: exp(n^{1/d}) for small d
            d = 1.0 + 0.5 * f
            vals.append(min(np.exp(100 ** (1 / max(d, 0.5))), 1e9))
        elif f < 8:
            # Barrier hits — bound collapses
            vals.append(max(1e9 - 2e8 * (f - 4), 100.0))
        else:
            # Post-break: technique yields only trivial bounds
            vals.append(max(100.0 - 5.0 * (f - 7), 1.0))
    return np.array(vals, dtype=float)


# ── Circuit diagram helper ────────────────────────────────────────────────────

def draw_circuit(ax, frame: int):
    """Schematic circuit of depth d with neon gates."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_aspect("equal")
    ax.set_facecolor(BG)
    ax.set_title("Circuito de profundidade d", color=CYAN, fontsize=9)
    ax.axis("off")

    broken = frame >= 5
    post = frame >= 8

    depth = min(frame + 1, 5) if not broken else (5 if not post else 5)
    gate_color = CYAN if not broken else (MAGENTA if frame < 8 else DIM)
    wire_color = CYAN if not broken else MAGENTA

    # Draw layers of gates (simplified)
    for layer in range(depth):
        y = 5.0 - layer * 0.9
        n_gates = 2 + layer
        xs = np.linspace(1, 9, n_gates)
        for x in xs:
            rect = mpatches.FancyBboxPatch(
                (x - 0.3, y - 0.25), 0.6, 0.5,
                boxstyle="round,pad=0.05",
                facecolor=gate_color, edgecolor=wire_color,
                alpha=0.85 if not post else 0.3,
            )
            ax.add_patch(rect)
            ax.text(x, y, "∧", ha="center", va="center",
                    color=BG, fontsize=7, fontweight="bold")
        # Wires to next layer
        if layer < depth - 1:
            y_next = 5.0 - (layer + 1) * 0.9
            xs_next = np.linspace(1, 9, n_gates + 1)
            for x in xs:
                for xn in xs_next[max(0, int(x) - 1): int(x) + 2]:
                    ax.plot([x, xn], [y - 0.25, y_next + 0.25],
                            color=wire_color, lw=0.6, alpha=0.5)

    # Barrier overlays
    for k, (name, color, trigger_frame) in enumerate(BARRIERS):
        if frame >= trigger_frame:
            y_b = 5.0 - (k + 1) * 0.9
            ax.axhline(y_b, color=color, lw=2.5, ls="--", alpha=0.8)
            ax.text(9.5, y_b, name.split("\n")[0][:12],
                    color=color, fontsize=6, va="center", ha="right")

    if post:
        ax.text(5, 2.5, "D = n^{O(log log S)}\nFora de controle",
                color=MAGENTA, fontsize=10, fontweight="bold",
                ha="center", va="center", alpha=0.9)


# ── Figure setup ──────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 7), facecolor=BG)
fig.suptitle(
    "SE'ET — Animação 3: Barreiras P vs NP  |  Natural Proofs · Relativização · Algebrização",
    color=YELLOW, fontsize=11, fontweight="bold", y=0.97,
)

ax_circuit = fig.add_axes([0.04, 0.12, 0.40, 0.76], facecolor=BG)
ax_degree  = fig.add_axes([0.52, 0.55, 0.44, 0.33], facecolor=BG)
ax_bound   = fig.add_axes([0.52, 0.12, 0.44, 0.33], facecolor=BG)

for ax in (ax_circuit, ax_degree, ax_bound):
    ax.tick_params(colors=DIM)
    for spine in ax.spines.values():
        spine.set_edgecolor(DIM)

all_degrees = [degree_bound(f) for f in range(N_FRAMES)]
all_bounds  = circuit_complexity_curve(range(N_FRAMES))
max_deg = max(all_degrees)
max_bnd = max(all_bounds)


def draw_frame(i: int):
    for ax in (ax_circuit, ax_degree, ax_bound):
        ax.cla()
        ax.set_facecolor(BG)
        for spine in ax.spines.values():
            spine.set_edgecolor(DIM)
        ax.tick_params(colors=DIM)

    # Phase label
    if i < 4:
        phase, ph_color = "ANTES", CYAN
    elif i < 8:
        phase, ph_color = "QUEBRA EXATA", MAGENTA
    else:
        phase, ph_color = "DEPOIS", YELLOW

    # ── Circuit diagram ──
    draw_circuit(ax_circuit, i)
    ax_circuit.set_title(
        f"Frame {i+1}/{N_FRAMES}  [{phase}]  d = profundidade",
        color=ph_color, fontsize=9,
    )

    # Barrier annotation on break frames
    for k, (name, color, trigger_frame) in enumerate(BARRIERS):
        if i == trigger_frame:
            ax_circuit.text(
                5, 0.4 - k * 0.1,
                f"BARREIRA: {name.split(chr(10))[0]}",
                color=color, fontsize=8, fontweight="bold",
                ha="center", va="bottom",
            )

    # ── Degree blow-up ──
    degs = [degree_bound(f) for f in range(i + 1)]
    ax_degree.plot(range(i + 1), degs, color=YELLOW, lw=2)
    ax_degree.axvline(4.5, color=MAGENTA, lw=1.2, ls="--", label="1ª barreira")
    ax_degree.scatter([i], [degs[-1]], color=CYAN, s=55, zorder=5)
    ax_degree.set_yscale("log")
    ax_degree.set_title("Grau D = (log S)^d  → n^{O(log log S)}", color=YELLOW, fontsize=9)
    ax_degree.set_xlim(0, N_FRAMES - 1)
    ax_degree.set_xlabel("frame", color=DIM, fontsize=8)
    ax_degree.legend(fontsize=7, facecolor=BG, edgecolor=DIM, labelcolor=MAGENTA)

    # Barrier vertical lines on degree plot
    for _, color, tf in BARRIERS:
        if i >= tf:
            ax_degree.axvline(tf, color=color, lw=1, ls=":", alpha=0.7)

    # ── Circuit lower bound ──
    bnds = circuit_complexity_curve(range(i + 1))
    ax_bound.plot(range(i + 1), bnds, color=GREEN, lw=2)
    ax_bound.axvline(4.5, color=MAGENTA, lw=1.2, ls="--")
    ax_bound.scatter([i], [bnds[-1]], color=CYAN, s=55, zorder=5)
    ax_bound.set_yscale("log")
    ax_bound.set_title("Lower bound derivável (técnica atual)", color=GREEN, fontsize=9)
    ax_bound.set_xlim(0, N_FRAMES - 1)
    ax_bound.set_xlabel("frame", color=DIM, fontsize=8)

    if i >= 8:
        ax_bound.text(
            N_FRAMES * 0.6, max(bnds) * 0.5,
            "Técnica falha\npara P vs NP geral",
            color=MAGENTA, fontsize=8, fontweight="bold",
            ha="center",
        )

    return []


ani = animation.FuncAnimation(
    fig, draw_frame, frames=N_FRAMES, interval=280, blit=False, repeat=True,
)

out_path = OUT / "anim_pvsnp_barriers.gif"
ani.save(str(out_path), writer="pillow", fps=4, dpi=110)
plt.close(fig)
print(f"Saved → {out_path}")
