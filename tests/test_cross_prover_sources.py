from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CrossProverSourceTests(unittest.TestCase):
    def test_no_incomplete_proof_markers(self):
        files = [
            ROOT / "FederatedTrivalent/Epistemic.lean",
            ROOT / "formal/coq/HMOS_Epistemic.v",
            ROOT / "formal/isabelle/HMOS_Epistemic.thy",
        ]
        banned = ("sorry", "admitted", "oops")
        for path in files:
            text = path.read_text(encoding="utf-8").lower()
            for marker in banned:
                self.assertNotIn(marker, text, f"{marker} in {path}")

    def test_all_provers_expose_same_statuses(self):
        files = [
            ROOT / "FederatedTrivalent/Epistemic.lean",
            ROOT / "formal/coq/HMOS_Epistemic.v",
            ROOT / "formal/isabelle/HMOS_Epistemic.thy",
        ]
        normalized = [p.read_text(encoding="utf-8").lower().replace("_", "") for p in files]
        for status in ("proved", "refuted", "conditional", "bounded", "specialcase", "independentfrom", "empirical", "open"):
            for text in normalized:
                self.assertIn(status, text)


if __name__ == "__main__":
    unittest.main()
