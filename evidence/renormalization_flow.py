"""Audited HMOS boundary ODE.

The unconstrained equation e' = -a*e-b approaches -b/a, not zero.
A nonnegative physical state requires an explicit saturation/projection rule.
"""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class BoundaryFlow:
    a: float = 0.21774
    b: float = 0.01

    def __post_init__(self) -> None:
        if not (math.isfinite(self.a) and self.a > 0):
            raise ValueError("a must be finite and positive")
        if not (math.isfinite(self.b) and self.b >= 0):
            raise ValueError("b must be finite and nonnegative")

    @property
    def equilibrium(self) -> float:
        return -self.b / self.a

    def derivative(self, e: float) -> float:
        if not math.isfinite(e):
            raise ValueError("e must be finite")
        return -self.a * e - self.b

    def exact(self, t: float, e0: float) -> float:
        if t < 0 or not (math.isfinite(t) and math.isfinite(e0)):
            raise ValueError("require finite t >= 0 and finite e0")
        return (e0 + self.b / self.a) * math.exp(-self.a * t) - self.b / self.a

    def hitting_time_zero(self, e0: float) -> float:
        if e0 < 0 or not math.isfinite(e0):
            raise ValueError("require finite e0 >= 0")
        if self.b == 0:
            return math.inf
        return math.log1p(self.a * e0 / self.b) / self.a

    def saturated(self, t: float, e0: float) -> float:
        """Projected engineering policy; not the unconstrained ODE solution."""
        return max(0.0, self.exact(t, e0))
