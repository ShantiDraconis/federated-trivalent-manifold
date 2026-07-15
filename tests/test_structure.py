from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class StructureTests(unittest.TestCase):
    def test_lean_has_no_sorry_or_admit(self):
        lean = (ROOT / "GatewayModel" / "Classes.lean").read_text(encoding="utf-8")
        self.assertNotIn("sorry", lean.lower())
        self.assertNotIn("admit", lean.lower())

    def test_scientific_scope_is_explicit(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("proves nothing about P vs NP", text)


if __name__ == "__main__":
    unittest.main()
