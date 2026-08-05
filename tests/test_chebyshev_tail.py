import math

from simulations.chebyshev_tail import (
    chebyshev_psi_values,
    fibonacci_ratio_error,
    primes_up_to,
    window_rms,
    zero_orbit,
)


def test_sieve_small_primes() -> None:
    assert primes_up_to(11) == [2, 3, 5, 7, 11]


def test_psi_ten_is_log_2520() -> None:
    assert math.isclose(chebyshev_psi_values(10)[10], math.log(2520), rel_tol=1e-12)


def test_generic_orbit_is_closed_under_conjugation_and_reflection() -> None:
    orbit = zero_orbit(0.72, 14.0)
    assert complex(0.72, -14.0) in orbit
    assert complex(0.28, 14.0) in orbit
    assert complex(0.28, -14.0) in orbit


def test_fibonacci_control_decays() -> None:
    assert abs(fibonacci_ratio_error(25)) < abs(fibonacci_ratio_error(10))


def test_window_rms_is_nonnegative() -> None:
    assert window_rms([1.0, -2.0, 3.0], 2) == [math.sqrt(2.5), math.sqrt(6.5)]
