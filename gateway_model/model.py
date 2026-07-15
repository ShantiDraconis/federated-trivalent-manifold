"""Pure equations for the gateway action model.

Names such as ``mass_proxy`` are analogies internal to this model; they are not
physical mass gaps or mathematical invariants of Millennium Prize Problems.
"""
from dataclasses import dataclass
from math import exp, isfinite


@dataclass(frozen=True)
class Measurements:
    llama: float = 0.8
    gpt: float = 1.2
    claude: float = 1.1
    aes_gcm: float = 0.005
    teardown: float = 0.05

    @property
    def total(self) -> float:
        return self.llama + self.gpt + self.claude + self.aes_gcm + self.teardown


@dataclass(frozen=True)
class Parameters:
    alpha: float = 0.1
    beta: float = 0.108870
    e_norm: float = 0.3
    decay_lambda: float = 0.2
    connection_proxy: float = 0.70


def _finite(*values: float) -> None:
    if not all(isfinite(x) for x in values):
        raise ValueError("all inputs must be finite")


def action(alpha: float, beta: float, t: float, e: float) -> float:
    _finite(alpha, beta, t, e)
    return alpha * t**2 - beta * e**2


def beta_critical(alpha: float, t: float, e: float) -> float:
    _finite(alpha, t, e)
    if e == 0:
        raise ValueError("e must be nonzero")
    return alpha * t**2 / e**2


def classify(s: float, tolerance: float = 1e-12) -> str:
    _finite(s, tolerance)
    if tolerance < 0:
        raise ValueError("tolerance must be nonnegative")
    return "critical" if abs(s) <= tolerance else ("temporal" if s > 0 else "exodus")


def decay(e0: float, decay_lambda: float, time: float) -> float:
    _finite(e0, decay_lambda, time)
    if decay_lambda < 0 or time < 0:
        raise ValueError("decay_lambda and time must be nonnegative")
    return e0 * exp(-decay_lambda * time)


def mass_proxy(beta: float, e_norm: float) -> float:
    _finite(beta, e_norm)
    return beta * e_norm

