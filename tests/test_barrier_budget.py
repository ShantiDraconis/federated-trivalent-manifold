from decimal import Decimal
import math
import pytest
from evidence.barrier_budget import (
    barrier_derivative, idealized_exponential_budget,
    integrate_barrier, normalized_eta_residue_error,
)


def test_residue_error_sign_and_value_for_odd_cutoff():
    err = normalized_eta_residue_error(9999)
    assert err > 0
    assert float(err) == pytest.approx(7.213835878203236e-5, rel=1e-12)


def test_barrier_has_zero_equilibrium_and_preserves_sign_numerically():
    assert barrier_derivative(0.0) == 0.0
    assert barrier_derivative(1.0) < 0
    assert barrier_derivative(-1.0) > 0
    value = integrate_barrier(0.1, 50.0, dt=1e-3)
    assert value > 0
    assert value == pytest.approx(1.134280475e-6, rel=2e-8)


def test_euler_value_is_not_an_exact_equilibrium():
    value = integrate_barrier(0.1, 50.0)
    assert value != pytest.approx(1.1196461076e-6, rel=1e-4)
    assert barrier_derivative(value) < 0


def test_budget_is_conditional_and_integer_threshold_is_25():
    budget = idealized_exponential_budget(3e9, 0.016)
    assert budget["nodes"] == 48_000_000
    assert budget["continuous_n"] == pytest.approx(25.516531070045332)
    assert budget["largest_integer_n"] == 25
    assert 2**25 <= budget["nodes"] < 2**26
