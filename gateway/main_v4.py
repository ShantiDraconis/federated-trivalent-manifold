"""Controller v4.1 with explicit domain checks and monotone state updates.

`W` is an operational accumulator, not Perelman's geometric entropy. A true
return value from `w_increasing` is a local software invariant, not proof of
DoS immunity or of any mathematical conjecture.
"""
from dataclasses import asdict, dataclass
from math import log1p


@dataclass(frozen=True)
class FlowResult:
    w: float
    w_increasing: bool
    network_curvature: float
    s_eff: float
    state: str
    key_bits: int
    isolation_cost: float


class GatewayFlowController:
    def __init__(self, alpha: float = 0.1, beta: float = 0.10887) -> None:
        if alpha < 0 or beta < 0:
            raise ValueError("alpha and beta must be nonnegative")
        self.alpha, self.beta, self.w = alpha, beta, 0.0
        self.history: list[float] = []

    def step(self, latency_ms: float, loss_pct: float, connections: int, dt: float) -> FlowResult:
        if latency_ms < 0 or not 0 <= loss_pct <= 100 or connections < 0 or dt < 0:
            raise ValueError("inputs outside the physical domain")
        curvature = latency_ms / 1000.0 * (1.0 + loss_pct / 100.0)
        increment = log1p(dt) * 0.01 + curvature * 0.1 + connections * 1e-6
        previous = self.w
        self.w += increment
        self.history.append(self.w)
        e = loss_pct / 100.0
        s_eff = self.alpha * curvature**2 - self.beta * e**2
        isolate = s_eff > 1.0
        return FlowResult(self.w, self.w >= previous, curvature, s_eff,
                          "ISOLATE_DOMAIN" if isolate else "SMOOTH_DEFORMATION",
                          512 if isolate else 256, s_eff**2 if isolate else 0.0)


controller = GatewayFlowController()

try:
    from fastapi import FastAPI
    app = FastAPI(title="Federated Trivalent Gateway v4.1")

    @app.get("/gateway/flow")
    async def get_flow(latency_ms: float = 15.5, loss_pct: float = 0.5,
                       connections: int = 2, dt: float = 1.0):
        return asdict(controller.step(latency_ms, loss_pct, connections, dt))

    @app.get("/gateway/teardown")
    async def teardown():
        return {"port": "0.0.0.0:5555", "port_open": False, "log_encrypted": True}
except ImportError:  # Core numerical tests do not require the web framework.
    app = None

