"""Generate the four audit figures for the anomaly-kernel boundary.

The plots are classical deterministic computations.  They do not represent a
quantum computer, a proof of RH, or measured Quest latency.
"""

from pathlib import Path
import sys

import matplotlib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

from gateway.anomaly_kernel import certify_eta, e_derivative, seff_squared  # noqa: E402

OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({"figure.dpi": 200, "savefig.dpi": 200, "font.size": 9})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, bbox_inches="tight")
    plt.close(fig)


def eta_certificate_figure():
    s = 0.5 + 14.134725j
    ns = np.unique(np.logspace(1, 4.2, 90).astype(int))
    mags, bounds = [], []
    for n in ns:
        cert = certify_eta(s, int(n))
        mags.append(abs(cert.partial_sum))
        bounds.append(cert.tail_bound)
    fig, ax = plt.subplots(figsize=(8.2, 4.5))
    ax.loglog(ns, mags, label=r"$|\eta_N(s)|$", linewidth=1.8)
    ax.loglog(ns, bounds, label="rigorous tail upper bound", linewidth=1.8)
    ax.fill_between(ns, 0, bounds, alpha=0.15, label="zero cannot be excluded")
    ax.set(xlabel="terms N", ylabel="magnitude", title="Finite eta sums: certificate boundary")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend()
    ax.text(
        0.02,
        0.04,
        "A finite approximation certifies nonzero only if |eta_N| > tail bound.\n"
        "Otherwise the result is INCONCLUSIVE, never 'zero detected'.",
        transform=ax.transAxes,
        bbox={"facecolor": "white", "alpha": 0.9, "edgecolor": "0.7"},
    )
    save(fig, "fig15_eta_certificate_boundary.png")


def flow_figure():
    ts = np.linspace(0, 5, 180)
    es = np.linspace(0, 2, 150)
    t_grid, e_grid = np.meshgrid(ts, es)
    de = np.vectorize(e_derivative)(t_grid, e_grid, 0.0, 1.0, 1.0)
    s2 = seff_squared(t_grid, e_grid)
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.1))
    im = axes[0].pcolormesh(t_grid, e_grid, de, shading="auto", cmap="coolwarm")
    axes[0].contour(t_grid, e_grid, de, levels=[0], colors="black", linewidths=1)
    fig.colorbar(im, ax=axes[0], label=r"$de/dt$ at $\delta=0$")
    axes[0].set(xlabel="model time t", ylabel="state e", title="Declared e-flow is not global damping")
    cs = axes[1].contourf(t_grid, e_grid, s2, levels=np.linspace(0, 8, 17), cmap="viridis")
    axes[1].contour(t_grid, e_grid, s2, levels=[1], colors="white", linewidths=1.5)
    fig.colorbar(cs, ax=axes[1], label=r"$S_{eff}^2$")
    axes[1].set(xlabel="model time t", ylabel="state e", title="Model threshold $S_{eff}^2=1$")
    save(fig, "fig16_corrected_flow_dynamics.png")


def regimes_figure():
    fig, ax = plt.subplots(figsize=(9.2, 4.4))
    ax.axis("off")
    boxes = [
        (0.03, 0.63, 0.23, 0.22, "NUMERICAL INPUT\neta partial sum + error bound"),
        (0.38, 0.63, 0.23, 0.22, "CERTIFICATE\nnonzero / inconclusive"),
        (0.73, 0.63, 0.23, 0.22, "MODEL CONTROL\nSeff threshold only"),
        (0.12, 0.15, 0.28, 0.22, "EXACT-ZERO WITNESS\nexternal proof obligation"),
        (0.60, 0.15, 0.28, 0.22, "OPERATIONAL RESPONSE\nstandard crypto + sandbox policy"),
    ]
    for x, y, w, h, label in boxes:
        ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, linewidth=1.4))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")
    arrows = [((0.26, 0.74), (0.38, 0.74)), ((0.61, 0.74), (0.73, 0.74)), ((0.26, 0.63), (0.26, 0.37)), ((0.61, 0.63), (0.74, 0.37))]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 1.3})
    ax.text(0.5, 0.02, "No finite numerical result is promoted to an exact zero or an RH refutation.", ha="center")
    ax.set_title("Three-way trust boundary: certified nonzero, inconclusive, external witness")
    save(fig, "fig17_epistemic_regimes.png")


def architecture_figure():
    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    ax.axis("off")
    levels = [
        (0.35, 0.80, 0.30, 0.12, "FORMAL KERNEL\nLean theorem + explicit hypotheses"),
        (0.08, 0.55, 0.28, 0.12, "NUMERICAL LAYER\nfinite sums + certified bounds"),
        (0.64, 0.55, 0.28, 0.12, "POLICY LAYER\nregime selection, no theorem claims"),
        (0.08, 0.28, 0.28, 0.12, "EXPERIMENTS\nbenchmarks with provenance"),
        (0.64, 0.28, 0.28, 0.12, "OPERATIONS\nAES-256-GCM / isolation"),
        (0.35, 0.04, 0.30, 0.12, "AUDIT LOG\ninputs, versions, status, digest"),
    ]
    for x, y, w, h, label in levels:
        ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, linewidth=1.4))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center")
    links = [((0.42, 0.80), (0.29, 0.67)), ((0.58, 0.80), (0.71, 0.67)), ((0.22, 0.55), (0.22, 0.40)), ((0.78, 0.55), (0.78, 0.40)), ((0.22, 0.28), (0.42, 0.16)), ((0.78, 0.28), (0.58, 0.16))]
    for start, end in links:
        ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 1.2})
    ax.set_title("Hypothesis-management architecture with explicit trust boundaries")
    save(fig, "fig18_hmos_trust_architecture.png")


if __name__ == "__main__":
    eta_certificate_figure()
    flow_figure()
    regimes_figure()
    architecture_figure()
