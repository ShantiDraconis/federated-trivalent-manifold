"""
animate_eclipse_break.py
SE'ET Refutation Engine — Animation 2
Eclipse model refutation: spherical vs flat geometry at the critical frame.

Frame layout (18 frames, neon palette):
  1–5   : Spherical model aligned — umbra 187 km, speed 1.71 km/s East [BEFORE]
  6–7   : Flat-Earth prediction diverges — W_pred−W_obs = 3287 km,
           χ²_flat = 335.2 vs χ²_sphere = 1.12, 18.3σ refutation      [BREAK]
  8–18  : Post-break — spherical track continues correctly,
           flat model diverges South                                     [AFTER]

Output: figures/anim_eclipse_break.gif

Reference values (Lema L_B1 / NASA 2023):
  umbra_sphere  = 187 km
  speed_sphere  = 1.71 km/s  (East)
  umbra_flat    = 3000 km
  speed_flat    = 0.50 km/s  (West)
  chi2_sphere   = 1.12
  chi2_flat     = 335.2
  sigma_refute  = 18.3
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

# ── Neon palette ──────────────────────────────────────────────────────────────
BG = "#0a0a0f"
GREEN = "#00ff88"
MAGENTA = "#ff00cc"
CYAN = "#00ffe7"
YELLOW = "#ffe600"
RED = "#ff3333"
DIM = "#2a2a3a"
WHITE = "#ffffff"

N_FRAMES = 18
BREAK_FRAMES = {5, 6}

# ── Physical reference values ─────────────────────────────────────────────────
UMBRA_SPH = 187.0      # km
UMBRA_FLAT = 3000.0    # km
SPEED_SPH = 1.71       # km/s  East → positive
SPEED_FLAT = -0.50     # km/s  West → negative
CHI2_SPH = 1.12
CHI2_FLAT = 335.2
SIGMA = 18.3

# ── Earth / Sun geometry helpers ──────────────────────────────────────────────

def shadow_radius(frame: int) -> tuple[float, float]:
    """Return (sphere_shadow_radius, flat_shadow_radius) as fractions of plot."""
    if frame < 5:
        return 0.08, 0.08  # both look the same before break
    if frame < 7:
        # Flat model 'inflates' abruptly
        ratio = (frame - 4) / 2.0
        return 0.08, 0.08 + ratio * 0.35
    post = frame - 6
    return 0.08, 0.43 + 0.01 * post  # flat stays large; sphere stays small


def track_position(frame: int) -> tuple[float, float]:
    """Return (sphere_x, flat_x) as fractions [-1, 1] of plot width."""
    # Sphere moves East (positive x)
    sph = -0.6 + 0.07 * frame
    # Flat model reverses sign and drifts South after break
    if frame < 5:
        flat = sph  # same
    elif frame < 7:
        flat = sph - 0.1 * (frame - 4)  # starts diverging
    else:
        flat = sph - 0.3 - 0.06 * (frame - 6)  # continues diverging
    return sph, flat


def chi2_values(frame: int) -> tuple[float, float]:
    """χ² values up to current frame."""
    if frame < 5:
        return CHI2_SPH, CHI2_SPH + 2 * frame
    if frame < 7:
        spike = (frame - 4) / 2.0
        return CHI2_SPH, CHI2_SPH + 2 * 4 + spike * (CHI2_FLAT - CHI2_SPH - 8)
    return CHI2_SPH, CHI2_FLAT


# ── Figure setup ──────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 7), facecolor=BG)
fig.suptitle(
    "SE'ET — Animação 2: Quebra Modelo Eclipse  |  χ²_esf = 1.12  vs  χ²_plano = 335.2  (18.3σ)",
    color=GREEN, fontsize=11, fontweight="bold", y=0.97,
)

ax_map = fig.add_axes([0.04, 0.12, 0.50, 0.76], facecolor=BG)
ax_chi = fig.add_axes([0.60, 0.55, 0.37, 0.33], facecolor=BG)
ax_bar = fig.add_axes([0.60, 0.12, 0.37, 0.33], facecolor=BG)

for ax in (ax_map, ax_chi, ax_bar):
    ax.tick_params(colors=DIM)
    for spine in ax.spines.values():
        spine.set_edgecolor(DIM)


def draw_frame(i: int):
    for ax in (ax_map, ax_chi, ax_bar):
        ax.cla()
        ax.set_facecolor(BG)
        for spine in ax.spines.values():
            spine.set_edgecolor(DIM)
        ax.tick_params(colors=DIM)

    broken = i >= 5
    post = max(0, i - 6)
    sph_r, flat_r = shadow_radius(i)
    sph_x, flat_x = track_position(i)
    chi_sph, chi_flat = chi2_values(i)

    # ── Map view (top-down Earth slice) ──
    # Background: simplified coast-like Brazil blob
    theta = np.linspace(0, 2 * np.pi, 200)
    braz_x = 0.18 * np.cos(theta) - 0.1
    braz_y = 0.32 * np.sin(theta) - 0.1
    ax_map.fill(braz_x, braz_y, color="#1a3a2a", alpha=0.5, zorder=1)
    ax_map.plot(braz_x, braz_y, color=DIM, lw=0.8, zorder=1)
    ax_map.text(-0.1, -0.05, "BR", color=DIM, fontsize=8, ha="center", zorder=2)

    # Umbra circles
    sph_shadow = plt.Circle((sph_x, 0.0), sph_r, color=CYAN, alpha=0.35, zorder=3)
    ax_map.add_patch(sph_shadow)
    ax_map.plot(*plt.Circle((sph_x, 0.0), sph_r).get_center(),
                'o', color=CYAN, ms=4, zorder=4)

    if broken or i >= 4:
        flat_shadow = plt.Circle((flat_x, -0.2), flat_r, color=MAGENTA,
                                  alpha=0.25, zorder=2)
        ax_map.add_patch(flat_shadow)

    # Sphere track
    track_fr = range(i + 1)
    tx = [-0.6 + 0.07 * f for f in track_fr]
    ty = [0.0] * len(tx)
    ax_map.plot(tx, ty, color=CYAN, lw=1.8, ls="-", label="Esférico (NASA)", zorder=5)

    # Flat track
    if i >= 4:
        fx = [track_position(f)[1] for f in range(5, i + 1)]
        fy = [-0.02 * (f - 4) for f in range(5, i + 1)]
        ax_map.plot(fx, fy, color=MAGENTA, lw=1.8, ls="--",
                    label="Plano (diverge)", zorder=5)

    # Break annotation
    if i in BREAK_FRAMES:
        ax_map.annotate(
            f"W_pred − W_obs = 3287 km\n{SIGMA}σ refutação",
            xy=(sph_x, 0.0), xytext=(0.2, 0.45),
            color=MAGENTA, fontsize=8, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=MAGENTA, lw=1.5),
        )

    phase = "ANTES" if i < 5 else ("QUEBRA EXATA" if i < 7 else "DEPOIS")
    ph_color = CYAN if i < 5 else (MAGENTA if i < 7 else YELLOW)
    ax_map.set_title(f"Frame {i+1} / {N_FRAMES}  [{phase}]",
                     color=ph_color, fontsize=10)
    ax_map.set_xlim(-0.85, 0.85)
    ax_map.set_ylim(-0.75, 0.75)
    ax_map.set_aspect("equal")
    ax_map.set_xlabel("Longitude rel.", color=DIM, fontsize=8)
    ax_map.set_ylabel("Latitude rel.", color=DIM, fontsize=8)
    ax_map.legend(fontsize=7, facecolor=BG, edgecolor=DIM,
                  labelcolor=[CYAN, MAGENTA] if broken else [CYAN])

    # ── χ² time series ──
    chi_hist_sph = [CHI2_SPH] * (i + 1)
    chi_hist_flat = [chi2_values(f)[1] for f in range(i + 1)]
    ax_chi.plot(range(i + 1), chi_hist_sph, color=CYAN, lw=2, label="χ² esférico")
    ax_chi.plot(range(i + 1), chi_hist_flat, color=MAGENTA, lw=2, label="χ² plano")
    ax_chi.axvline(4.5, color=MAGENTA, lw=1, ls="--")
    ax_chi.set_title("χ² — Esférico vs Plano", color=GREEN, fontsize=9)
    ax_chi.set_xlim(0, N_FRAMES - 1)
    ax_chi.set_ylim(0, CHI2_FLAT * 1.1)
    ax_chi.set_xlabel("frame", color=DIM, fontsize=8)
    ax_chi.legend(fontsize=7, facecolor=BG, edgecolor=DIM,
                  labelcolor=[CYAN, MAGENTA])

    # ── Bar chart: current χ² comparison ──
    labels = ["Esférico", "Plano"]
    values = [chi_sph, chi_flat]
    colors = [CYAN, MAGENTA]
    bars = ax_bar.bar(labels, values, color=colors, alpha=0.85)
    ax_bar.axhline(CHI2_SPH, color=GREEN, lw=1, ls="--",
                   label=f"χ²_esf = {CHI2_SPH}")
    ax_bar.set_title(f"χ² atual  (σ_refut = {SIGMA}σ)", color=GREEN, fontsize=9)
    ax_bar.set_ylim(0, CHI2_FLAT * 1.15)
    for bar, val in zip(bars, values):
        ax_bar.text(bar.get_x() + bar.get_width() / 2, val + 3,
                    f"{val:.1f}", ha="center", color=WHITE, fontsize=8)
    ax_bar.legend(fontsize=7, facecolor=BG, edgecolor=DIM, labelcolor=GREEN)

    return []


ani = animation.FuncAnimation(fig, draw_frame, frames=N_FRAMES,
                               interval=280, blit=False, repeat=True)

out_path = OUT / "anim_eclipse_break.gif"
ani.save(str(out_path), writer="pillow", fps=4, dpi=110)
plt.close(fig)
print(f"Saved → {out_path}")
