"""Auditable numerical boundary tester for the Dirichlet eta function.

This module does not decide whether zeta has a zero.  A finite sum can certify
non-vanishing when its distance from zero exceeds a rigorous tail bound; all
other cases remain inconclusive.  No quantum computation is implemented.
"""

from dataclasses import dataclass
from enum import Enum
from math import isfinite


class ZeroStatus(str, Enum):
    CERTIFIED_NONZERO = "CERTIFIED_NONZERO"
    INCONCLUSIVE = "INCONCLUSIVE"


@dataclass(frozen=True)
class EtaCertificate:
    s: complex
    terms: int
    partial_sum: complex
    tail_bound: float
    status: ZeroStatus


def eta_partial(s: complex, terms: int) -> complex:
    """Return the N-term alternating Dirichlet sum for eta(s)."""
    if not (isfinite(s.real) and isfinite(s.imag)) or s.real <= 0:
        raise ValueError("eta series certificate requires finite Re(s) > 0")
    if terms < 1:
        raise ValueError("terms must be positive")
    return sum((1 if n % 2 else -1) * n ** (-s) for n in range(1, terms + 1))


def eta_tail_bound(s: complex, terms: int) -> float:
    """Conservative Dirichlet/partial-summation tail bound.

    With bounded partial sums of (-1)^(n-1), integration by parts gives
    |R_N| <= (N+1)^(-sigma) * (1 + |s|/sigma).
    """
    if s.real <= 0 or terms < 1:
        raise ValueError("bound requires Re(s) > 0 and terms > 0")
    return (terms + 1) ** (-s.real) * (1.0 + abs(s) / s.real)


def certify_eta(s: complex, terms: int) -> EtaCertificate:
    partial = eta_partial(s, terms)
    bound = eta_tail_bound(s, terms)
    status = (
        ZeroStatus.CERTIFIED_NONZERO if abs(partial) > bound else ZeroStatus.INCONCLUSIVE
    )
    return EtaCertificate(s, terms, partial, bound, status)


def exact_misalignment(s: complex, *, exact_zero_witness: bool) -> float:
    """Mathematical delta, requiring an external exact-zero witness.

    In the open critical strip eta and zeta have the same zeros because
    1 - 2^(1-s) is nonzero there.  A numerical candidate is not such a witness.
    """
    if not 0.0 < s.real < 1.0:
        raise ValueError("misalignment is restricted to the open critical strip")
    return abs(s.real - 0.5) if exact_zero_witness else 0.0


def seff_squared(t: float, e: float, alpha: float = 0.10, beta: float = 0.10887) -> float:
    return (alpha * t * t - beta * e * e) ** 2


def partial_e_seff_squared(
    t: float, e: float, alpha: float = 0.10, beta: float = 0.10887
) -> float:
    """Exact derivative d/de [(alpha*t^2-beta*e^2)^2]."""
    return -4.0 * beta * e * (alpha * t * t - beta * e * e)


def e_derivative(
    t: float,
    e: float,
    delta: float,
    gamma: float,
    chi: float,
    alpha: float = 0.10,
    beta: float = 0.10887,
) -> float:
    if min(e, delta, gamma, chi) < 0:
        raise ValueError("e, delta, gamma and chi must be non-negative")
    return -gamma * partial_e_seff_squared(t, e, alpha, beta) - chi * delta


def w_derivative(t: float, e: float, epsilon: float = 1e-6) -> float:
    """Strictly positive model derivative; not an OS availability guarantee."""
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    return seff_squared(t, e) + epsilon
