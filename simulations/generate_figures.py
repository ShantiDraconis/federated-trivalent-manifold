"""Generate the eight explanatory figures. They are illustrations, not proofs."""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
STYLE = {
    "figure.facecolor": "#f7f5ef",
    "axes.facecolor": "#fffefa",
    "axes.grid": True,
    "grid.alpha": 0.2,
}
plt.rcParams.update(STYLE)


def save(name: str) -> None:
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=200, bbox_inches="tight")
    plt.close()


def manifold() -> None:
    t = np.linspace(0, 8 * np.pi, 800)
    r = np.linspace(0.2, 1.0, 800)
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection="3d")
    ax.plot(r * np.cos(t), r * np.sin(t), t / (8 * np.pi), c="#087f8c", lw=2)
    ax.scatter([0], [0], [0], c="#d1495b", s=70, label="estado inicial")
    ax.set(xlabel="x", ylabel="y", zlabel="tempo normalizado")
    ax.set_title("Trajetória projetada do modelo 5D")
    ax.legend()
    save("fig1_manifold_5d.png")


def critical_line() -> None:
    ys = np.array([14.1347, 21.022, 25.0109, 30.4249, 32.9351, 37.5862])
    plt.figure(figsize=(8, 5))
    plt.axvspan(0, 1, color="#e6edf0")
    plt.axvline(0.5, c="#d1495b", ls="--", label="Re(s)=1/2")
    plt.scatter(np.full_like(ys, 0.5), ys, c="#087f8c")
    plt.xlim(-0.1, 1.1)
    plt.xlabel("Re(s)")
    plt.ylabel("Im(s)")
    plt.title("Zeros amostrados na reta crítica (ilustração)")
    plt.legend()
    save("fig2_riemann_critical.png")


def alpha_beta() -> None:
    a = np.linspace(0, 2, 200)
    b = np.linspace(0, 2, 200)
    A, B = np.meshgrid(a, b)
    Z = A - B
    plt.figure(figsize=(7, 6))
    plt.contourf(A, B, Z, levels=30, cmap="coolwarm")
    plt.colorbar(label="α−β")
    plt.plot(a, a, "k--", label="α=β")
    plt.xlabel("α")
    plt.ylabel("β")
    plt.title("Mapa paramétrico, não fronteira de decidibilidade")
    plt.legend()
    save("fig3_alpha_beta.png")


def exodus() -> None:
    t = np.linspace(0, 10, 500)
    e = 0.2 * np.sin(np.pi * t / 10)
    integ = np.concatenate([[0], np.cumsum((e[1:] + e[:-1]) / 2 * np.diff(t))])
    plt.figure(figsize=(8, 5))
    plt.plot(t, e, label="e(t)")
    plt.plot(t, integ, label="∫e(t)dt")
    plt.xlabel("t")
    plt.title("Termo de êxodo escolhido e integral acumulada")
    plt.legend()
    save("fig4_exodo.png")


def connection() -> None:
    names = ["P/NP", "RH", "Hodge", "NS", "YM", "BSD", "Poincaré"]
    feats = [
        {"t", "discrete"},
        {"x", "analytic"},
        {"x", "y", "z", "geometry"},
        {"x", "y", "z", "t", "pde"},
        {"x", "y", "z", "t", "qft"},
        {"x", "y", "arithmetic"},
        {"x", "y", "z", "geometry"},
    ]
    m = np.array([[len(a & b) / len(a | b) for b in feats] for a in feats])
    plt.figure(figsize=(8, 7))
    plt.imshow(m, vmin=0, vmax=1, cmap="viridis")
    plt.colorbar(label="Jaccard das características declaradas")
    plt.xticks(range(7), names, rotation=45, ha="right")
    plt.yticks(range(7), names)
    plt.title("Matriz de conexão transparente")
    save("fig5_conn_matrix.png")


def trivalent() -> None:
    table = np.array([[0, 0, 0], [0, 0.5, 0.5], [0, 0.5, 1]])
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))
    labels = ["F", "U", "T"]
    for ax, data, title in [
        (axs[0], table, "AND K3"),
        (axs[1], np.flip(np.flip(1 - table, 0), 1), "OR K3"),
    ]:
        ax.imshow(data, vmin=0, vmax=1, cmap="RdYlGn")
        ax.set_xticks(range(3), labels)
        ax.set_yticks(range(3), labels)
        ax.set_title(title)
        for i in range(3):
            for j in range(3):
                ax.text(j, i, labels[int(data[i, j] * 2)], ha="center", va="center")
    save("fig6_trivalent.png")


def teardown() -> None:
    plt.figure(figsize=(10, 3))
    plt.axis("off")
    xs = [0.1, 0.38, 0.66, 0.9]
    labels = ["processos ativos", "terminação", "ADB disconnect", "estado observado"]
    for x, label in zip(xs, labels):
        plt.text(
            x,
            0.5,
            label,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round", fc="#d7f0ed", ec="#087f8c"),
        )
    for a, b in zip(xs, xs[1:]):
        plt.annotate("", (b - 0.08, 0.5), (a + 0.08, 0.5), arrowprops=dict(arrowstyle="->"))
    plt.title("Teardown operacional idempotente")
    save("fig7_teardown_fsm.png")


def axiom_layers() -> None:
    plt.figure(figsize=(9, 5))
    plt.axis("off")
    levels = [
        ("AXIOMA", 0.8, "hipótese adicionada à teoria"),
        ("DERIVAÇÃO", 0.55, "regras verificadas no sistema formal"),
        ("CONCLUSÃO CONDICIONAL", 0.3, "válida apenas sob a hipótese"),
    ]
    for title, y, desc in levels:
        plt.text(
            0.5,
            y,
            f"{title}\n{desc}",
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=.6", fc="#f2d492", ec="#735d2c"),
        )
    plt.annotate("", (0.5, 0.63), (0.5, 0.72), arrowprops=dict(arrowstyle="->"))
    plt.annotate("", (0.5, 0.38), (0.5, 0.47), arrowprops=dict(arrowstyle="->"))
    plt.title("Assumir RH não é provar RH")
    save("fig8_axiom_accepted.png")


if __name__ == "__main__":
    for fn in (
        manifold,
        critical_line,
        alpha_beta,
        exodus,
        connection,
        trivalent,
        teardown,
        axiom_layers,
    ):
        fn()
