from __future__ import annotations

from decimal import Decimal, getcontext

getcontext().prec = 50


def radial_weight(delta: Decimal, gamma: Decimal) -> Decimal:
    """Exact decimal evaluation of 2δ² / ((γ²+1/4+δ²)²-δ²)."""
    if gamma == 0 and abs(delta) == Decimal("0.5"):
        raise ValueError("singular denominator")
    delta_sq = delta * delta
    a = gamma * gamma + Decimal("0.25") + delta_sq
    denominator = a * a - delta_sq
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return Decimal(2) * delta_sq / denominator


def eclipse_umbra_radius(
    moon_distance_km: Decimal,
    sun_moon_distance_km: Decimal = Decimal("149216000"),
    moon_radius_km: Decimal = Decimal("1737.4"),
    sun_radius_km: Decimal = Decimal("696340"),
) -> Decimal:
    """Umbra radius in a plane normal to the Sun-Moon axis at Earth distance.

    This is not the projected surface path width.
    """
    if moon_distance_km <= 0 or sun_moon_distance_km <= 0:
        raise ValueError("distances must be positive")
    return moon_radius_km - moon_distance_km * (sun_radius_km - moon_radius_km) / sun_moon_distance_km
