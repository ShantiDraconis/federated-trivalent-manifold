"""Reproduce the numerical audit without SciPy."""

from math import exp

ALPHA, BETA, EPSILON, T = 0.10, 0.10887, 1e-6, 3.155


def seff_squared(t: float, e: float) -> float:
    return (ALPHA * t * t - BETA * e * e) ** 2


def trapezoid(function, start: float, end: float, steps: int = 200_000) -> float:
    width = (end - start) / steps
    interior = sum(function(start + i * width) for i in range(1, steps))
    return width * (0.5 * function(start) + interior + 0.5 * function(end))


def main() -> None:
    cases = [(0, 0), (3.15, 0.3), (0, 10), (5, 0.1), (4, 0.3), (1, 2)]
    for t, e in cases:
        print(f"t={t:g} e={e:g} Seff2={seff_squared(t, e):.12f}")
    constant = trapezoid(lambda t: seff_squared(t, 0.3) + EPSILON, 0, T)
    decaying = trapezoid(lambda t: seff_squared(t, 0.3 * exp(-0.2 * t)) + EPSILON, 0, T)
    endpoint = 0.3 * exp(-0.2 * T)
    print(f"constant integral={constant:.12f}; plus e(T)={constant + 0.3:.12f}")
    print(f"decaying integral={decaying:.12f}; plus e(T)={decaying + endpoint:.12f}")


if __name__ == "__main__":
    main()
