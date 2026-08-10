"""Numerical action for an explicitly selected illustrative path."""

from dataclasses import dataclass
from math import isfinite, pi, sin


@dataclass(frozen=True)
class ActionParameters:
    alpha: float = 1.0
    beta: float = 1.0
    duration: float = 10.0
    samples: int = 200
    exodus_amplitude: float = 0.2

    def validate(self) -> None:
        values = (self.alpha, self.beta, self.duration, self.exodus_amplitude)
        if not all(isfinite(v) for v in values):
            raise ValueError("parameters must be finite")
        if self.alpha < 0 or self.beta < 0 or self.duration <= 0:
            raise ValueError("alpha/beta must be non-negative and duration positive")
        if not 2 <= self.samples <= 1_000_000:
            raise ValueError("samples must be in [2, 1_000_000]")


@dataclass(frozen=True)
class ActionResult:
    real: float
    imaginary: float
    step: float
    method: str = "composite trapezoidal rule"


def integrate_action(parameters: ActionParameters) -> ActionResult:
    parameters.validate()
    dt = parameters.duration / (parameters.samples - 1)
    real = imaginary = 0.0
    for index in range(parameters.samples):
        t = index * dt
        e = parameters.exodus_amplitude * sin(pi * t / parameters.duration)
        lagrangian = 1.0 + parameters.alpha * t * t - parameters.beta * e * e
        weight = 0.5 if index in (0, parameters.samples - 1) else 1.0
        real += weight * lagrangian * dt
        imaginary += weight * e * dt
    return ActionResult(real, imaginary, dt)
