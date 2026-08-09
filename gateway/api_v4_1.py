"""FastAPI application for the v4.1 flow engine.

Exposes a single POST endpoint that wraps FlowEngine.process.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from gateway.main_v4_1 import FlowEngine, ManifoldInput

app = FastAPI(title="Federated Trivalent Manifold — v4.1")

_engine = FlowEngine()


class StateRequest(BaseModel):
    x: float
    y: float
    z: float
    t: float
    e: float


@app.post("/process")
def process(req: StateRequest):
    try:
        result = _engine.process(ManifoldInput(**req.model_dump()))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return result.__dict__
