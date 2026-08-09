import pytest

from gateway.main_v4_1 import FlowEngine, ManifoldInput


def state(t: float, e: float = 0.3) -> ManifoldInput:
    return ManifoldInput(0.5, 0.0, 0.0, t, e)


def test_published_reference_values():
    engine = FlowEngine()
    assert engine.seff_squared(3.15, 0.3) == pytest.approx(0.9652113428328899)
    assert engine.seff_squared(0.0, 10.0) == pytest.approx(118.526769)


def test_w_is_non_decreasing_for_ordered_time():
    engine = FlowEngine()
    values = [engine.process(state(t)).w for t in (0.0, 0.1, 1.0, 3.155)]
    assert values == sorted(values)


def test_surgery_halves_e_and_preserves_x():
    result = FlowEngine().process(state(5.0, 0.1))
    assert result.regime == "ISOLATION"
    assert result.delta_e == pytest.approx(-0.05)
    assert result.next_x == 0.5


def test_time_regression_is_rejected():
    engine = FlowEngine()
    engine.process(state(2.0))
    with pytest.raises(ValueError):
        engine.process(state(1.0))
