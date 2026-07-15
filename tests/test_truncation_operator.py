import math
from evidence.truncation_operator import (
    cutoff, eta_truncated, finite_trace, projection,
    zeta_surrogate_residue_at_one,
)


def test_cutoff_is_idempotent():
    values = [complex(i) for i in range(8)]
    once = projection(values, 3)
    assert projection(once, 3) == once


def test_cutoff_spectrum_and_trace_in_finite_ambient_space():
    assert [cutoff(n, 3) for n in range(1, 6)] == [1, 1, 1, 0, 0]
    assert finite_trace(3, 8) == 3
    assert finite_trace(10, 8) == 8


def test_eta_n_is_finite_at_one_but_quotient_has_nonzero_residue():
    assert math.isfinite(abs(eta_truncated(1 + 0j, 100)))
    assert zeta_surrogate_residue_at_one(100) > 0.9
    assert zeta_surrogate_residue_at_one(9999) == pytest.approx(1.0, abs=1e-4)


def test_claimed_universal_inverse_sqrt_residue_is_false():
    N = 99
    actual = abs(eta_truncated(0.5 + 14j, N + 1) - eta_truncated(0.5 + 14j, N))
    claimed = 1 / math.sqrt(N + 1)
    assert actual != pytest.approx(claimed)


import pytest
