"""Transparent comparison scores based on declared feature sets."""

from collections.abc import Iterable


def jaccard(left: Iterable[str], right: Iterable[str]) -> float:
    a, b = set(left), set(right)
    union = a | b
    return len(a & b) / len(union) if union else 1.0


def difference(left: Iterable[str], right: Iterable[str]) -> float:
    return 1.0 - jaccard(left, right)
