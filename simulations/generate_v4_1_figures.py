"""Generate figures 9-14 from explicit v4.1 definitions."""

from pathlib import Path
from math import sqrt
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
ALPHA = 0.10
BETA = 0.10887
EPS = 1e-6
plt.rcParams.update(
    {
        "figure.facecolor": "#f7f5ef",
        "axes.facecolor": "#fffefa",
        "axes.grid": True,
        "grid.alpha": 0.2,
    }
)


def save(name):
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=200, bbox_inches="tight")
    plt.close()


def thresholds():
    t = np.linspace(0, 5, 500)
    plt.figure(figsize=(8, 5))
    for e in (0.1, 0.3, 0.6):
        plt.plot(
            t,
            (ALPHA * t * t - BETA * e * e) ** 2,
            label=f"e={e}; T*={sqrt((1 + BETA * e * e) / ALPHA):.3f}",
        )
    plt.axhline(1, c="#d1495b", ls="--", label="defined isolation threshold")
    plt.xlabel("t")
    plt.ylabel("q(t,e)^2")
    plt.title("Threshold behavior under the declared model")
    plt.legend()
    save("fig9_seff_thresholds.png")


def w_profiles():
    t = np.linspace(0, 10, 2001)
    profiles = {
        "constant": np.full_like(t, 0.3),
        "exponential": 0.3 * np.exp(-0.2 * t),
        "oscillating": 0.15 * (1 + np.sin(2 * np.pi * t)),
    }
    plt.figure(figsize=(8, 5))
    for name, e in profiles.items():
        rate = (ALPHA * t * t - BETA * e * e) ** 2 + EPS
        w = np.concatenate([[0], np.cumsum((rate[1:] + rate[:-1]) / 2 * np.diff(t))])
        plt.plot(t, w, label=name)
    plt.xlabel("t")
    plt.ylabel("W(t)-W(0)")
    plt.title("Monotone accumulators by construction")
    plt.legend()
    save("fig10_w_profiles.png")


def zeta():
    sigma = np.linspace(0, 1, 400)
    plt.figure(figsize=(8, 5))
    for e in (0.1, 0.3, 0.6):
        plt.plot(sigma, (sigma - 0.5) ** 2 * e, label=f"e={e}")
    plt.xlabel("sigma")
    plt.ylabel("defined force")
    plt.title("Quadratic alignment force; not evidence about zeta zeros")
    plt.legend()
    save("fig11_zeta_force.png")


def decays():
    t = np.linspace(0, 100, 500)
    plt.figure(figsize=(8, 5))
    plt.plot(t, np.exp(-0.032 * t), label="gauge-inspired exp(-0.032t)")
    plt.plot(t, np.exp(-0.01 * t), label="complexity coordinate exp(-0.01t)")
    plt.plot(t, 1 / (1 + t), label="exodus 1/(1+t)")
    plt.xlabel("t")
    plt.ylabel("normalized value")
    plt.title("Declared decay laws, without cross-domain implication")
    plt.legend()
    save("fig12_declared_decays.png")


def zeros():
    g = np.array([14.13, 21.02, 25.01, 30.42, 32.93, 37.58, 40.91, 43.32])
    d = np.diff(g)
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].scatter(np.full_like(g, 0.5), g)
    ax[0].axvline(0.5, ls="--", c="#d1495b")
    ax[0].set(xlabel="Re(s), fixed", ylabel="gamma", title="Points placed at Re(s)=1/2")
    ax[1].bar(range(1, len(d) + 1), d)
    ax[1].axhline(d.mean(), ls="--", c="#d1495b", label=f"mean={d.mean():.2f}")
    ax[1].set(xlabel="spacing index", ylabel="Delta gamma", title="Successive spacings")
    ax[1].legend()
    save("fig13_zero_spacing_audit.png")


def reported_spectrum():
    eig = np.array([0.014487, 0.149067, 0.170396, 0.533967, 0.834535, 1.117441, 4.180106])
    order = eig[::-1]
    explained = order / order.sum()
    plt.figure(figsize=(8, 5))
    plt.bar(range(1, 8), explained * 100)
    plt.plot(range(1, 8), np.cumsum(explained) * 100, "o-", label="cumulative")
    plt.ylabel("percent")
    plt.xlabel("component")
    plt.title("Spectrum reported in attachment - source matrix absent")
    plt.legend()
    save("fig14_reported_spectrum_unreproduced.png")


if __name__ == "__main__":
    for fn in (thresholds, w_profiles, zeta, decays, zeros, reported_spectrum):
        fn()
