"""Metadata for the seven Clay Millennium problems.

The coordinate assignments are modelling choices, not canonical mathematics.
Poincare is marked solved; the remaining entries are open as of this model.
"""

from dataclasses import dataclass
from enum import Enum
from .trivalent import Triv


class MillenniumProblem(str, Enum):
    P_VS_NP = "p_vs_np"
    RIEMANN = "riemann"
    HODGE = "hodge"
    NAVIER_STOKES = "navier_stokes"
    YANG_MILLS = "yang_mills"
    BSD = "bsd"
    POINCARE = "poincare"


@dataclass(frozen=True)
class ProblemSpec:
    problem: MillenniumProblem
    title: str
    proposition: str
    dominant_axes: tuple[str, ...]
    default_truth: Triv
    caveat: str


PROBLEMS = {
    MillenniumProblem.P_VS_NP: ProblemSpec(
        MillenniumProblem.P_VS_NP,
        "P versus NP",
        "P != NP",
        ("t",),
        Triv.UNKNOWN,
        "Cryptographic practice does not prove P != NP.",
    ),
    MillenniumProblem.RIEMANN: ProblemSpec(
        MillenniumProblem.RIEMANN,
        "Riemann Hypothesis",
        "All non-trivial zeta zeros have real part 1/2",
        ("x", "y"),
        Triv.UNKNOWN,
        "A plotted critical line is not a proof.",
    ),
    MillenniumProblem.HODGE: ProblemSpec(
        MillenniumProblem.HODGE,
        "Hodge Conjecture",
        "Rational Hodge classes are algebraic",
        ("x", "y", "z"),
        Triv.UNKNOWN,
        "The exodus coordinate is only an illustrative obstruction.",
    ),
    MillenniumProblem.NAVIER_STOKES: ProblemSpec(
        MillenniumProblem.NAVIER_STOKES,
        "Navier-Stokes",
        "Global existence and smoothness in 3D",
        ("x", "y", "z", "t"),
        Triv.UNKNOWN,
        "Finite simulations do not decide global regularity.",
    ),
    MillenniumProblem.YANG_MILLS: ProblemSpec(
        MillenniumProblem.YANG_MILLS,
        "Yang-Mills",
        "Quantum Yang-Mills exists with a positive mass gap",
        ("x", "y", "z", "t"),
        Triv.UNKNOWN,
        "The model coordinate e is not literally the mass gap.",
    ),
    MillenniumProblem.BSD: ProblemSpec(
        MillenniumProblem.BSD,
        "Birch and Swinnerton-Dyer",
        "Analytic rank equals algebraic rank",
        ("x", "y"),
        Triv.UNKNOWN,
        "Finiteness of Sha is a separate hypothesis.",
    ),
    MillenniumProblem.POINCARE: ProblemSpec(
        MillenniumProblem.POINCARE,
        "Poincare Conjecture",
        "A closed simply connected 3-manifold is S^3",
        ("x", "y", "z"),
        Triv.TRUE,
        "Solved; included only as a reference class.",
    ),
}
