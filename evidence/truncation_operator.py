"""Finite truncation operators for HMOS experiments.

All outputs are numerical evidence. They do not decide RH or certify zeros.
"""
from __future__ import annotations
import cmath
import math


def cutoff(n: int, N: int) -> int:
    if n < 1 or N < 0:
        raise ValueError("require n >= 1 and N >= 0")
    return int(n <= N)


def eta_truncated(s: complex, N: int) -> complex:
    if N < 1:
        raise ValueError("N must be positive")
    return sum((1 if n % 2 else -1) * cmath.exp(-s * math.log(n))
               for n in range(1, N + 1))


def projection(values: list[complex], N: int) -> list[complex]:
    if N < 0:
        raise ValueError("N must be nonnegative")
    return [v if i < N else 0j for i, v in enumerate(values)]


def finite_trace(N: int, dimension: int) -> int:
    """Trace of P_N on a declared finite-dimensional ambient space."""
    if N < 0 or dimension < 0:
        raise ValueError("dimensions must be nonnegative")
    return min(N, dimension)


def zeta_surrogate_residue_at_one(N: int) -> float:
    """Residue of eta_N(s)/(1-2**(1-s)) at s=1.

    It equals eta_N(1)/log(2), not zero. It tends to 1 as N grows.
    """
    return eta_truncated(1 + 0j, N).real / math.log(2)


def fixed_cutoff_commutator_derivative_zero() -> bool:
    """For time-independent P_N, differentiation commutes with P_N."""
    return True
