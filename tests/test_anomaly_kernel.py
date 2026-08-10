import pytest

from gateway.anomaly_kernel import (
    ZeroStatus,
    certify_eta,
    e_derivative,
    eta_partial,
    exact_misalignment,
    partial_e_seff_squared,
    w_derivative,
)


def test_eta_at_two_approaches_known_value():
    assert eta_partial(2 + 0j, 20_000).real == pytest.approx(3.141592653589793**2 / 12, rel=1e-8)


def test_certificate_never_calls_inconclusive_a_zero():
    cert = certify_eta(0.5 + 14.134725j, 1_000)
    assert cert.status in {ZeroStatus.CERTIFIED_NONZERO, ZeroStatus.INCONCLUSIVE}
    assert cert.tail_bound > 0


def test_delta_requires_exact_external_witness():
    s = 0.4 + 20j
    assert exact_misalignment(s, exact_zero_witness=False) == 0
    assert exact_misalignment(s, exact_zero_witness=True) == pytest.approx(0.1)


def test_symbolic_partial_derivative_matches_finite_difference():
    t, e, h = 2.3, 0.7, 1e-6

    def f(x):
        return (0.10 * t * t - 0.10887 * x * x) ** 2

    numeric = (f(e + h) - f(e - h)) / (2 * h)
    assert partial_e_seff_squared(t, e) == pytest.approx(numeric, rel=1e-8)


def test_declared_e_flow_is_not_globally_damping():
    assert e_derivative(t=3, e=0.2, delta=0, gamma=1, chi=1) > 0


def test_w_rate_is_strictly_positive():
    assert w_derivative(0, 0) == pytest.approx(1e-6)
