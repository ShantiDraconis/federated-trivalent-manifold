"""Guard the stated no-placeholder boundary of the finite formal core."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = (
    "formal/lean/RadialGeometry.lean",
    "formal/lean/FiniteEvidence.lean",
    "formal/coq/WMonotone.v",
    "formal/coq/Renormalization.v",
    "formal/isabelle/WMonotone.thy",
    "formal/isabelle/Renormalization.thy",
    "formal/agda/WMonotone.agda",
)
FORBIDDEN = ("sorry", "admit", "admitted", "axiom", "postulate", "axiomatization")


def test_verified_core_has_no_placeholder_or_assumption_markers():
    for relative in CORE:
        text = (ROOT / relative).read_text(encoding="utf-8").lower()
        assert not any(marker in text for marker in FORBIDDEN), relative


def test_open_obligations_identify_noncore_placeholder_modules():
    ledger = (ROOT / "formal/OPEN_OBLIGATIONS.md").read_text(encoding="utf-8")
    for name in ("Behaviors.lean", "NumeroComComportamento.lean", "Lemas_Master.lean"):
        assert name in ledger
