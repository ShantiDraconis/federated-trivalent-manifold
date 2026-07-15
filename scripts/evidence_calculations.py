"""Reproducible calculations for the epistemic audit.

No result in this module is evidence for a Millennium Problem.  It calculates
gateway thresholds and conservative numerical-error bounds for design review.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from decimal import Decimal, getcontext
from math import hypot

getcontext().prec = 40
D = Decimal


@dataclass(frozen=True)
class AuditCalculations:
    alpha: str
    beta: str
    t: str
    temporal_term: str
    action_at_measured_point: str
    squared_stress_at_measured_point: str
    critical_beta_for_zero_action: str
    e_boundary_negative_branch: str
    positive_branch_has_real_e: bool
    eta_real_alternating_bound_N100_sigma_half: str
    eta_complex_abel_bound_first_zero: str


def sqrt_decimal(x: Decimal) -> Decimal:
    if x < 0:
        raise ValueError("square root requires a nonnegative input")
    return x.sqrt()


def eta_real_alternating_bound(n: int, sigma: Decimal) -> Decimal:
    """Next-term bound valid for the real alternating series (imaginary part 0)."""
    if n < 1 or sigma <= 0:
        raise ValueError("n >= 1 and sigma > 0 required")
    return D(1) / (D(n + 1) ** sigma)


def eta_complex_abel_bound(n: int, sigma: Decimal, tau: Decimal) -> Decimal:
    """Conservative Abel-summation tail bound.

    |R_N(s)| <= (1 + |s|/sigma) (N+1)^(-sigma), for sigma > 0.
    This deliberately exposes the dependence on the imaginary part.
    """
    if n < 1 or sigma <= 0:
        raise ValueError("n >= 1 and sigma > 0 required")
    abs_s = D(str(hypot(float(sigma), float(tau))))
    return (D(1) + abs_s / sigma) / (D(n + 1) ** sigma)


def calculate() -> AuditCalculations:
    alpha, beta, t = D("0.10"), D("0.10887"), D("3.155")
    temporal = alpha * t * t
    action = temporal - beta * D("0.3") ** 2
    squared_stress = action * action
    beta_zero = temporal / (D("0.3") ** 2)
    # |alpha*t^2-beta*e^2|=1. The negative-action branch is beta*e^2=alpha*t^2+1.
    e_negative = sqrt_decimal((temporal + D(1)) / beta)
    positive_rhs = temporal - D(1)
    real_bound = eta_real_alternating_bound(100, D("0.5"))
    complex_bound = eta_complex_abel_bound(100, D("0.5"), D("14.134725"))
    return AuditCalculations(
        str(alpha), str(beta), str(t), str(temporal), str(action),
        str(squared_stress), str(beta_zero),
        str(e_negative), positive_rhs >= 0, str(real_bound), str(complex_bound)
    )


if __name__ == "__main__":
    import json
    print(json.dumps(asdict(calculate()), indent=2, ensure_ascii=False))
