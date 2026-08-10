"""Audited numerical annex for HMOS v4.1.

The budget model is conditional on one useful operation per clock cycle.
It has no implication for P versus NP.
"""
from __future__ import annotations
from decimal import Decimal, localcontext
import math


def normalized_eta_residue_error(N: int, precision: int = 50) -> Decimal:
    """Return eta_N(1)/ln(2)-1 with controlled decimal arithmetic."""
    if N < 1 or precision < 20:
        raise ValueError("require N >= 1 and precision >= 20")
    with localcontext() as ctx:
        ctx.prec = precision
        eta = sum((Decimal(1) if n % 2 else Decimal(-1)) / Decimal(n)
                  for n in range(1, N + 1))
        return eta / Decimal(2).ln() - Decimal(1)


def barrier_derivative(e: float, a: float = 0.21774, b0: float = 0.01) -> float:
    if a <= 0 or b0 < 0 or not all(map(math.isfinite, (e, a, b0))):
        raise ValueError("require finite e, a > 0 and b0 >= 0")
    return -a * e - b0 * math.tanh(e)


def integrate_barrier(e0: float, t: float, dt: float = 1e-3,
                      a: float = 0.21774, b0: float = 0.01) -> float:
    """Fourth-order Runge-Kutta integration of the barrier ODE."""
    if e0 < 0 or t < 0 or dt <= 0:
        raise ValueError("require e0,t >= 0 and dt > 0")
    steps = max(1, math.ceil(t / dt))
    h = t / steps
    e = e0
    f = lambda x: barrier_derivative(x, a, b0)
    for _ in range(steps):
        k1 = f(e)
        k2 = f(e + h * k1 / 2)
        k3 = f(e + h * k2 / 2)
        k4 = f(e + h * k3)
        e += h * (k1 + 2*k2 + 2*k3 + k4) / 6
    return e


def idealized_exponential_budget(clock_hz: float, frame_s: float,
                                 cycles_per_node: float = 1.0) -> dict:
    """Budget for a toy 2**n enumeration model."""
    if min(clock_hz, frame_s, cycles_per_node) <= 0:
        raise ValueError("all budget parameters must be positive")
    nodes = clock_hz * frame_s / cycles_per_node
    continuous = math.log2(nodes)
    return {
        "nodes": nodes,
        "continuous_n": continuous,
        "largest_integer_n": math.floor(continuous),
        "assumption": "one serial search node costs cycles_per_node cycles",
    }
