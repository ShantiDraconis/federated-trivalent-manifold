import math
import pytest

from model.action import ActionParameters, integrate_action
from model.comparison import difference, jaccard
from model.trivalent import Triv, conjunction, disjunction, negation


def test_negation_is_involutive():
    for value in Triv:
        assert negation(negation(value)) == value


def test_k3_commutative_operations():
    for a in Triv:
        for b in Triv:
            assert conjunction(a, b) == conjunction(b, a)
            assert disjunction(a, b) == disjunction(b, a)


def test_action_zero_exodus_has_zero_imaginary_part():
    result = integrate_action(ActionParameters(exodus_amplitude=0))
    assert result.imaginary == 0
    assert math.isfinite(result.real)


def test_action_rejects_invalid_input():
    with pytest.raises(ValueError):
        integrate_action(ActionParameters(duration=0))


def test_comparison_is_bounded_and_complementary():
    connection = jaccard(("x", "t"), ("x", "y"))
    assert 0 <= connection <= 1
    assert difference(("x", "t"), ("x", "y")) == pytest.approx(1 - connection)
