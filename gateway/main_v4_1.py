"""Experimental v4.1 controller.

This module does not implement cryptography, a DoS defence, or Perelman's
entropy. The terminology is an engineering analogy and is labelled as such.
"""

from dataclasses import dataclass
from math import isfinite
from threading import Lock


@dataclass(frozen=True)
class ManifoldInput:
    x: float
    y: float
    z: float
    t: float
    e: float


@dataclass(frozen=True)
class FlowResult:
    w: float
    seff_squared: float
    regime: str
    next_e: float
    delta_e: float
    next_x: float


class FlowEngine:
    """Thread-safe state machine using elapsed model time.

    W[n+1] = W[n] + (Seff^2 + epsilon) * delta_t.
    Strict growth follows only when delta_t > 0 and finite arithmetic does not
    underflow. It does not imply availability or resistance to network attacks.
    """

    def __init__(self, alpha: float = 0.10, beta: float = 0.10887, epsilon: float = 1e-6):
        if alpha < 0 or beta < 0 or epsilon <= 0:
            raise ValueError("alpha/beta must be non-negative and epsilon positive")
        self.alpha, self.beta, self.epsilon = alpha, beta, epsilon
        self._w = 0.0
        self._last_t: float | None = None
        self._lock = Lock()

    def seff_squared(self, t: float, e: float) -> float:
        return (self.alpha * t * t - self.beta * e * e) ** 2

    def process(self, state: ManifoldInput) -> FlowResult:
        values = (state.x, state.y, state.z, state.t, state.e)
        if not all(isfinite(value) for value in values):
            raise ValueError("state coordinates must be finite")
        if state.t < 0 or state.e < 0:
            raise ValueError("this model requires t >= 0 and e >= 0")
        with self._lock:
            delta_t = 0.0 if self._last_t is None else state.t - self._last_t
            if delta_t < 0:
                raise ValueError("timestamps must be non-decreasing")
            seff2 = self.seff_squared(state.t, state.e)
            self._w += (seff2 + self.epsilon) * delta_t
            self._last_t = state.t
            surgery = seff2 > 1.0
            next_e = state.e * 0.5 if surgery else state.e
            return FlowResult(
                w=self._w,
                seff_squared=seff2,
                regime="ISOLATION" if surgery else "SMOOTH",
                next_e=next_e,
                delta_e=next_e - state.e,
                next_x=state.x,
            )
