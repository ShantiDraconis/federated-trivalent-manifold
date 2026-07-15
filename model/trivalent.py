"""Strong Kleene K3 operations.

UNKNOWN is epistemic: the proposition is not decided in the selected theory.
It is not a claim that the proposition is both true and false.
"""

from __future__ import annotations
from enum import IntEnum


class Triv(IntEnum):
    FALSE = 0
    UNKNOWN = 1
    TRUE = 2


def negation(value: Triv) -> Triv:
    return {Triv.FALSE: Triv.TRUE, Triv.UNKNOWN: Triv.UNKNOWN, Triv.TRUE: Triv.FALSE}[value]


def conjunction(left: Triv, right: Triv) -> Triv:
    return Triv(min(int(left), int(right)))


def disjunction(left: Triv, right: Triv) -> Triv:
    return Triv(max(int(left), int(right)))


def implication(left: Triv, right: Triv) -> Triv:
    return disjunction(negation(left), right)
