import math
import pytest
from evidence.renormalization_flow import BoundaryFlow


def test_exact_solution_initial_value_and_equilibrium():
    flow = BoundaryFlow()
    assert flow.exact(0.0, 2.0) == pytest.approx(2.0)
    assert flow.exact(1e4, 2.0) == pytest.approx(flow.equilibrium)
    assert flow.equilibrium == pytest.approx(-0.01 / 0.21774)


def test_derivative_is_negative_for_nonnegative_state():
    flow = BoundaryFlow()
    for e in [0.0, 1e-9, 1.0, 1e6]:
        assert flow.derivative(e) < 0


def test_unconstrained_flow_crosses_zero_not_converges_to_zero():
    flow = BoundaryFlow()
    hit = flow.hitting_time_zero(1.0)
    assert flow.exact(hit, 1.0) == pytest.approx(0.0, abs=1e-12)
    assert flow.exact(hit + 1.0, 1.0) < 0


def test_saturation_is_explicit_policy():
    flow = BoundaryFlow()
    assert flow.saturated(flow.hitting_time_zero(1.0) + 1.0, 1.0) == 0.0


def test_invalid_parameters_rejected():
    with pytest.raises(ValueError):
        BoundaryFlow(a=0)
    with pytest.raises(ValueError):
        BoundaryFlow(b=-1)
