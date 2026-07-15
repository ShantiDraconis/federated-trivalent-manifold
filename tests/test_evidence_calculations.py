import unittest
from decimal import Decimal as D

from scripts.evidence_calculations import calculate, eta_complex_abel_bound, eta_real_alternating_bound


class EvidenceCalculationsTests(unittest.TestCase):
    def test_exact_temporal_term(self):
        self.assertEqual(D(calculate().temporal_term), D("0.99540250"))

    def test_reported_action_and_squared_stress(self):
        result = calculate()
        self.assertEqual(D(result.action_at_measured_point), D("0.98560420"))
        self.assertEqual(D(result.squared_stress_at_measured_point), D("0.9714156390576400"))

    def test_phase_boundary_has_only_negative_action_branch_at_measured_t(self):
        result = calculate()
        self.assertFalse(result.positive_branch_has_real_e)
        self.assertGreater(D(result.e_boundary_negative_branch), D("4.28"))

    def test_real_bound_is_not_reused_for_complex_s(self):
        real = eta_real_alternating_bound(100, D("0.5"))
        complex_ = eta_complex_abel_bound(100, D("0.5"), D("14.134725"))
        self.assertGreater(complex_, real * 20)

    def test_invalid_domains(self):
        with self.assertRaises(ValueError):
            eta_complex_abel_bound(0, D("0.5"), D(1))
        with self.assertRaises(ValueError):
            eta_real_alternating_bound(10, D(0))


if __name__ == "__main__":
    unittest.main()
