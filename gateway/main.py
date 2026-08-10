"""Heuristic telemetry controller.

This service does not implement Ricci flow and does not prove mathematical,
cryptographic, or availability properties.
"""
from math import isfinite
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FTM heuristic telemetry controller", version="0.1.0")


class Telemetry(BaseModel):
    time_s: float = Field(ge=0.0)
    risk_score: float = Field(ge=0.0)
    latency_ms: float = Field(ge=0.0)
    packet_loss_fraction: float = Field(ge=0.0, le=1.0)


class Controller:
    def __init__(self, alpha: float = 0.10, beta: float = 0.10887, epsilon: float = 1e-6):
        self.alpha = alpha
        self.beta = beta
        self.epsilon = epsilon

    def evaluate(self, m: Telemetry) -> dict:
        effective = self.alpha * m.time_s**2 - self.beta * m.risk_score**2
        score = effective**2
        increment = score + self.epsilon
        if not all(isfinite(v) for v in (effective, score, increment)):
            raise ValueError("non-finite controller result")

        quarantine = score > 1.0
        return {
            "heuristic_score": score,
            "positive_increment_by_definition": increment,
            "action": "QUARANTINE_REQUEST" if quarantine else "MONITOR",
            "cipher_policy": "AES-256",
            "claims": {
                "ricci_flow": False,
                "perelman_noncollapse_proved": False,
                "dos_immunity_proved": False,
                "millennium_problem_proved": False,
            },
        }


controller = Controller()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/gateway/evaluate")
def evaluate(m: Telemetry) -> dict:
    try:
        return controller.evaluate(m)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
