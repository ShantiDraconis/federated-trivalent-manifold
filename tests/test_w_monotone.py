import math
import pytest

from gateway.main_v4_1_corrigido import Input, evaluate, regulator_step


@pytest.mark.parametrize("w,score", [(0.0, 0.0), (1.0, 2.0), (1e9, 1e-9)])
def test_step_strictly_grows(w, score):
    assert regulator_step(w, score) > w


def test_nonpositive_epsilon_rejected():
    with pytest.raises(ValueError):
        regulator_step(0.0, 1.0, 0.0)


def test_nonfinite_rejected():
    with pytest.raises(ValueError):
        regulator_step(0.0, math.inf)


def test_response_does_not_claim_security():
    result = evaluate(Input(time_s=3.0, risk_score=0.2, latency_ms=10, packet_loss=0.01))
    assert result["liveness_t1"] is True
    assert result["cipher_policy"] == "AES-256"
    assert result["non_claims"]["dos_immunity"] is False
    assert result["non_claims"]["availability_proof"] is False
    assert result["hypotheses"]["H2_risk_semantics_validated"] is False
