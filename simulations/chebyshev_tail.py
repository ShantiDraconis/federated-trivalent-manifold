"""Finite Chebyshev-tail diagnostics.

This module deliberately computes only finite quantities.  It must not be used
as a zero finder or as evidence that RH has been proved.
"""
from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path
from typing import Iterable


def primes_up_to(limit: int) -> list[int]:
    """Return all primes at most ``limit`` by an elementary sieve."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if sieve[candidate]:
            sieve[candidate * candidate : limit + 1 : candidate] = b"\x00" * (
                ((limit - candidate * candidate) // candidate) + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def chebyshev_psi_values(limit: int) -> list[float]:
    """Compute psi(n) for every 0 <= n <= limit from prime powers."""
    increments = [0.0] * (limit + 1)
    for prime in primes_up_to(limit):
        power = prime
        while power <= limit:
            increments[power] += math.log(prime)
            power *= prime
    values = [0.0] * (limit + 1)
    running = 0.0
    for n, increment in enumerate(increments):
        running += increment
        values[n] = running
    return values


def log_grid(limit: int, count: int = 160) -> list[int]:
    """Return increasing unique integer points in [2, limit]."""
    if limit < 2:
        raise ValueError("limit must be at least 2")
    values = {max(2, round(math.exp(math.log(2) + i * (math.log(limit) - math.log(2)) / (count - 1)))) for i in range(count)}
    return sorted(values)


def window_rms(values: Iterable[float], width: int) -> list[float]:
    """Finite rolling RMS, defined only from the supplied sequence."""
    data = list(values)
    if width <= 0 or width > len(data):
        raise ValueError("width must be between 1 and len(values)")
    return [math.sqrt(sum(v * v for v in data[i : i + width]) / width) for i in range(len(data) - width + 1)]


def zero_orbit(sigma: float, height: float) -> tuple[complex, complex, complex, complex]:
    """Return the symmetry orbit of a generic hypothetical zero."""
    rho = complex(sigma, height)
    return rho, rho.conjugate(), 1 - rho, 1 - rho.conjugate()


def fibonacci_ratio_error(n: int) -> float:
    """Return F_(n+1)/F_n - phi for n >= 2, an exact-model control."""
    if n < 2:
        raise ValueError("n must be at least 2")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b / a - (1 + math.sqrt(5)) / 2


def write_report(output: Path, limit: int) -> None:
    """Generate finite CSV and labelled diagnostic figures."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    output.mkdir(parents=True, exist_ok=True)
    figure_dir = output / "figures"
    data_dir = output / "data"
    figure_dir.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)

    psi = chebyshev_psi_values(limit)
    grid = log_grid(limit)
    tails = [psi[x] - x for x in grid]
    normalized = [tail / math.sqrt(x) for x, tail in zip(grid, tails)]
    rms = window_rms(normalized, min(12, len(normalized)))

    with (data_dir / "chebyshev_tail.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["x", "psi_x", "psi_x_minus_x", "normalized_by_sqrt_x"])
        writer.writerows((x, psi[x], tail, norm) for x, tail, norm in zip(grid, tails, normalized))

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, axis = plt.subplots(figsize=(9, 4.8))
    axis.plot(grid, tails, color="#175f8f", linewidth=1.4)
    axis.axhline(0, color="#333333", linewidth=0.8)
    axis.set_xscale("log")
    axis.set_xlabel("x (finite sampled integers)")
    axis.set_ylabel("psi(x) - x")
    axis.set_title("Finite Chebyshev-tail diagnostic - not a proof of RH")
    fig.tight_layout()
    fig.savefig(figure_dir / "chebyshev_tail.png", dpi=300)
    plt.close(fig)

    fig, axis = plt.subplots(figsize=(9, 4.8))
    axis.plot(grid[: len(rms)], rms, color="#a04b00", linewidth=1.4)
    axis.set_xscale("log")
    axis.set_xlabel("left endpoint x")
    axis.set_ylabel("rolling RMS of (psi(x)-x)/sqrt(x)")
    axis.set_title("Finite windowed amplitude - diagnostic only")
    fig.tight_layout()
    fig.savefig(figure_dir / "window_energy.png", dpi=300)
    plt.close(fig)

    orbit = zero_orbit(0.72, 14.134725)
    fig, axis = plt.subplots(figsize=(6.5, 5.2))
    axis.axvline(0.5, color="#333333", linestyle="--", linewidth=1, label="critical line")
    axis.axhline(0, color="#333333", linewidth=0.8)
    axis.scatter([z.real for z in orbit], [z.imag for z in orbit], color="#9b1b30", s=55)
    axis.set_xlim(0, 1)
    axis.set_xlabel("Re(s)")
    axis.set_ylabel("Im(s)")
    axis.set_title("Generic symmetry orbit (hypothetical input)")
    axis.legend()
    fig.tight_layout()
    fig.savefig(figure_dir / "zero_orbit_geometry.png", dpi=300)
    plt.close(fig)

    ns = list(range(2, 31))
    errors = [abs(fibonacci_ratio_error(n)) for n in ns]
    fig, axis = plt.subplots(figsize=(8, 4.8))
    axis.semilogy(ns, errors, color="#3d7f35", marker="o", markersize=3)
    axis.set_xlabel("n")
    axis.set_ylabel("|F_(n+1)/F_n - phi|")
    axis.set_title("Fibonacci control: known exponential tail")
    fig.tight_layout()
    fig.savefig(figure_dir / "fibonacci_control.png", dpi=300)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-x", type=int, default=20_000)
    parser.add_argument("--out", type=Path, default=Path("research/chebyshev_tail"))
    args = parser.parse_args()
    write_report(args.out, args.max_x)


if __name__ == "__main__":
    main()
