from decimal import Decimal

import pytest

from ftm_hub.calculators import eclipse_umbra_radius, radial_weight


def test_radial_weight_zero_exactly_on_critical_line():
    assert radial_weight(Decimal(0), Decimal("14.134725")) == 0


def test_radial_weight_is_positive_off_line():
    assert radial_weight(Decimal("0.1"), Decimal("1000")) > 0


def test_radial_weight_rejects_singularity():
    with pytest.raises(ValueError):
        radial_weight(Decimal("0.5"), Decimal(0))


def test_eclipse_radius_is_positive_near_perigee():
    radius = eclipse_umbra_radius(Decimal("357000"))
    assert Decimal("70") < radius < Decimal("80")
