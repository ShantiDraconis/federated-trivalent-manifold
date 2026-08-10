"""Conditional v4.1 controller.

H1: epsilon > 0.
T1: the returned arithmetic increment is positive by construction.
H2/H3 (risk meaning and operational benefit) are unvalidated.
"""
from math import isfinite
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Conditional FTM controller v4.1", version="4.1-corrected")


class Input(BaseModel):
    time_s: float = Field(ge=0.0)
    risk_score: float = Field(ge=0.0)
    latency_ms: float = Field(ge=0.0)
    packet_loss: float = Field(ge=0.0, le=1.0)


def regulator_step(w: float, score: float, epsilon: float = 1e-6) -> float:
    if epsilon <= 0:
        raise ValueError("H1 requires epsilon > 0")
    result = w + epsilon + score * score
    if not isfinite(result):
        raise ValueError("non-finite result")
    return result


def evaluate(m: Input) -> dict:
    alpha, beta = 0.10, 0.10887
    effective = alpha * m.time_s**2 - beta * m.risk_score**2
    score = effective**2
    next_w = regulator_step(0.0, score)
    return {
        "w_next": next_w,
        "liveness_t1": next_w > 0.0,
        "action": "QUARANTINE_REQUEST" if score > 1.0 else "MONITOR",
        "cipher_policy": "AES-256",
        "hypotheses": {"H1_epsilon_positive": True, "H2_risk_semantics_validated": False, "H3_security_effect_validated": False},
        "non_claims": {"dos_immunity": False, "availability_proof": False, "millennium_solution": False},
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/gateway/evaluate")
def endpoint(m: Input) -> dict:
    try:
        return evaluate(m)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
