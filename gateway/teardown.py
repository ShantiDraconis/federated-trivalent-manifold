"""Idempotent, observable ADB teardown."""

from __future__ import annotations
from dataclasses import dataclass
import subprocess


@dataclass(frozen=True)
class Step:
    name: str
    succeeded: bool
    detail: str


def run(args: list[str], timeout: float = 10.0) -> Step:
    if not args or any(not isinstance(x, str) for x in args):
        raise ValueError("command must be a non-empty string list")
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=timeout, check=False)
        detail = (result.stdout or result.stderr).strip()[-500:]
        return Step(" ".join(args[:2]), result.returncode == 0, detail)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return Step(" ".join(args[:2]), False, type(exc).__name__)


def teardown(serial: str) -> list[Step]:
    if not serial or any(c.isspace() for c in serial):
        raise ValueError("invalid ADB serial")
    return [run(["adb", "disconnect", serial]), run(["adb", "devices"])]
