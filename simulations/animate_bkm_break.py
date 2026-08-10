"""
animate_bkm_break.py
SE'ET Refutation Engine — Animation 1
Navier-Stokes BKM breakdown: vorticity tube instability at the critical frame.

Frame layout (18 frames, neon palette):
  1–5   : Stable vortex tube — ‖ω‖_{L^2} grows but stays bounded  [BEFORE]
  6–7   : BKM trigger — ∫‖ω‖_{L^∞} → ∞, core turns magenta      [BREAK]
  8–18  : Energy cascade, filament explosion, viscous dissipation   [AFTER]

Output: figures/anim_bkm_break.gif
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
CYAN = "#00ffe7"
MAGENTA = "#ff00cc"
YELLOW = "#ffe600"
WHITE = "#ffffff"
DIM = "#2a2a3a"

N_FRAMES = 18
BREAK_FRAMES = {5, 6}  # 0-indexed frames 5 and 6 → visual frames 6–7

# ── Helper ────────────────────────────────────────────────────────────────────

def vortex_profile(r: np.ndarray, t_norm: float, broken: bool, post_frames: int = 0) -> np.ndarray:
    """Vorticity magnitude profile on a radial slice."""
    if not broken:
        # Gaussian core growing slowly
        sigma = 0.18 + 0.04 * t_norm
        return np.exp(-(r ** 2) / (2 * sigma ** 2)) * (1.0 + 0.3 * t_norm)
    else:
        # Filament explosion: multiple lobes
        base = np.exp(-(r ** 2) / (2 * 0.08 ** 2)) * 3.5
        filaments = 0.0
        for k in range(1, post_frames + 2):
            rk = 0.25 + 0.06 * k
            filaments += 0.6 / k * np.exp(-((r - rk) ** 2) / (2 * 0.04 ** 2))
        decay = np.exp(-0.12 * post_frames)
        return (base + filaments) * decay


def enstrophy_curve(frame: int) -> np.ndarray:
    """Running ‖ω‖_{L^2} integral up to `frame`."""
    frames = np.arange(frame + 1)
    vals = np.where(
        frames < 5,
        1.0 + 0.15 * frames,          # slow growth
        np.where(
            frames < 7,
            1.75 + 2.5 * (frames - 5), # BKM spike
            4.75 * np.exp(-0.25 * (frames - 7)) + 0.8,  # decay
        ),
    )
    return frames, vals


def integral_linfty(frame: int) -> float:
    """Cumulative ∫‖ω‖_{L^∞} value."""
    if frame < 5:
        return 0.4 * frame
    if frame < 7:
        return 2.0 + 8.0 * (frame - 5)  # diverges
    return 18.0 + 0.3 * (frame - 7)     # already diverged


# ── Figure setup ──────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(13, 7), facecolor=BG)
fig.suptitle(
    "SE'ET — Animação 1: Quebra BKM  |  ∫₀^{T*} ‖ω‖_{L^∞} dt → ∞",
    color=CYAN, fontsize=12, fontweight="bold", y=0.97,
)

ax_vortex = fig.add_axes([0.04, 0.12, 0.45, 0.76], facecolor=BG)
ax_enstro = fig.add_axes([0.56, 0.55, 0.41, 0.33], facecolor=BG)
ax_linfty = fig.add_axes([0.56, 0.12, 0.41, 0.33], facecolor=BG)

for ax in (ax_vortex, ax_enstro, ax_linfty):
    ax.tick_params(colors=DIM)
    for spine in ax.spines.values():
        spine.set_edgecolor(DIM)

r = np.linspace(-1, 1, 400)
theta = np.linspace(0, 2 * np.pi, 400)
R, TH = np.meshgrid(np.linspace(0, 1, 200), theta)
X = R * np.cos(TH)
Y = R * np.sin(TH)


def draw_frame(i: int):
    for ax in (ax_vortex, ax_enstro, ax_linfty):
        ax.cla()
        ax.set_facecolor(BG)
        for spine in ax.spines.values():
            spine.set_edgecolor(DIM)
        ax.tick_params(colors=DIM)

    t_norm = i / (N_FRAMES - 1)
    broken = i >= 5
    post = max(0, i - 6)

    # ── Vortex cross-section (2-D contour) ──
    radial = vortex_profile(R.ravel(), t_norm, broken, post).reshape(R.shape)
    # clamp for contourf
    levels = np.linspace(0, radial.max() + 0.01, 30)
    cmap = "cool" if not broken else "spring"
    ax_vortex.contourf(X, Y, radial, levels=levels, cmap=cmap, alpha=0.92)
    # add tube outline
    circle_r = 0.22 + 0.04 * t_norm if not broken else 0.08
    circ = plt.Circle((0, 0), circle_r, color=MAGENTA if broken else CYAN,
                       fill=False, lw=2.0 + (2 if broken else 0))
    ax_vortex.add_patch(circ)
    if i in BREAK_FRAMES:
        ax_vortex.text(0, 0, "BKM\nTRIGGER", color=MAGENTA, fontsize=13,
                       fontweight="bold", ha="center", va="center")
    phase = "ANTES" if i < 5 else ("QUEBRA EXATA" if i < 7 else "DEPOIS")
    color_ph = CYAN if i < 5 else (MAGENTA if i < 7 else YELLOW)
    ax_vortex.set_title(f"Frame {i+1} / {N_FRAMES}  [{phase}]",
                        color=color_ph, fontsize=10)
    ax_vortex.set_xlabel("x", color=DIM)
    ax_vortex.set_ylabel("y", color=DIM)
    ax_vortex.set_xlim(-1.05, 1.05)
    ax_vortex.set_ylim(-1.05, 1.05)
    ax_vortex.set_aspect("equal")

    # ── Enstrophy ‖ω‖_{L^2} ──
    fr, ev = enstrophy_curve(i)
    ax_enstro.plot(fr, ev, color=CYAN, lw=2)
    ax_enstro.axvline(4.5, color=MAGENTA, lw=1.5, ls="--", label="BKM trigger")
    ax_enstro.scatter([i], [ev[-1]], color=YELLOW, s=60, zorder=5)
    ax_enstro.set_title("‖ω‖_{L²}  (Enstrofia)", color=CYAN, fontsize=9)
    ax_enstro.set_xlim(0, N_FRAMES - 1)
    ax_enstro.set_ylim(0, 6)
    ax_enstro.set_xlabel("frame", color=DIM, fontsize=8)
    ax_enstro.legend(fontsize=7, labelcolor=MAGENTA,
                     facecolor=BG, edgecolor=DIM)

    # ── ∫‖ω‖_{L^∞} ──
    lv = [integral_linfty(f) for f in range(i + 1)]
    ax_linfty.plot(range(i + 1), lv, color=MAGENTA, lw=2)
    ax_linfty.axvline(4.5, color=MAGENTA, lw=1.5, ls="--")
    ax_linfty.scatter([i], [lv[-1]], color=YELLOW, s=60, zorder=5)
    ax_linfty.set_title("∫₀ᵗ ‖ω‖_{L^∞} dτ  → ∞ em T*", color=MAGENTA, fontsize=9)
    ax_linfty.set_xlim(0, N_FRAMES - 1)
    ax_linfty.set_ylim(0, 22)
    ax_linfty.set_xlabel("frame", color=DIM, fontsize=8)

    return []


ani = animation.FuncAnimation(fig, draw_frame, frames=N_FRAMES,
                               interval=280, blit=False, repeat=True)

out_path = OUT / "anim_bkm_break.gif"
ani.save(str(out_path), writer="pillow", fps=4, dpi=110)
plt.close(fig)
print(f"Saved → {out_path}")
