"""Reproduce the remaining v4.1 behaviors from explicit definitions."""

from math import exp, log, pi, sin, sqrt
from statistics import mean, median, pstdev, stdev

ALPHA, BETA, EPSILON = 0.10, 0.10887, 1e-6
ZEROS = [14.13, 21.02, 25.01, 30.42, 32.93, 37.58, 40.91, 43.32]


def threshold_time(e: float) -> float:
    """Positive-t solution of (alpha*t^2-beta*e^2)^2=1 on q=+1."""
    return sqrt((1 + BETA * e * e) / ALPHA)


def zeta_force(sigma: float, e: float) -> float:
    return (sigma - 0.5) ** 2 * e


def gauge_decay(t: float, gap: float = 0.032) -> float:
    return exp(-gap * t)


def complexity_decay(t: float) -> tuple[float, float]:
    return exp(-0.01 * t), 1 / (1 + t)


def w_profile(e_function, end: float = 10.0, steps: int = 10_000) -> float:
    width = end / steps
    total = 0.0
    for i in range(steps):
        t = (i + 0.5) * width
        e = e_function(t)
        total += ((ALPHA * t * t - BETA * e * e) ** 2 + EPSILON) * width
    return total


def zero_statistics() -> dict[str, float | list[float]]:
    spacings = [b - a for a, b in zip(ZEROS, ZEROS[1:])]
    return {
        "count": len(ZEROS),
        "minimum": min(ZEROS),
        "maximum": max(ZEROS),
        "range": max(ZEROS) - min(ZEROS),
        "mean": mean(ZEROS),
        "median": median(ZEROS),
        "population_sd": pstdev(ZEROS),
        "sample_sd": stdev(ZEROS),
        "spacings": spacings,
        "spacing_mean": mean(spacings),
        "spacing_median": median(spacings),
        "spacing_sample_sd": stdev(spacings),
        "spacing_cv": stdev(spacings) / mean(spacings),
    }


def main() -> None:
    print("threshold e=0.1", threshold_time(0.1))
    print("threshold e=0.6", threshold_time(0.6))
    print("W constant", w_profile(lambda _t: 0.3))
    print("W exponential", w_profile(lambda t: 0.3 * exp(-0.2 * t)))
    print("W oscillating", w_profile(lambda t: 0.3 * (1 + sin(2 * pi * t)) / 2))
    print(zero_statistics())
    reported = [0.014487, 0.149067, 0.170396, 0.533967, 0.834535, 1.117441, 4.180106]
    probabilities = [value / sum(reported) for value in reported]
    effective_rank = exp(-sum(p * log(p) for p in probabilities))
    print("reported spectrum effective rank (not independently reproduced)", effective_rank)


if __name__ == "__main__":
    main()
