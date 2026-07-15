import math
import unittest

from gateway_model.model import Measurements, Parameters, action, beta_critical, classify, decay, mass_proxy


class GatewayModelTests(unittest.TestCase):
    def setUp(self):
        self.m = Measurements()
        self.p = Parameters()

    def test_pipeline_total(self):
        self.assertAlmostEqual(self.m.total, 3.155, places=12)

    def test_reported_action(self):
        self.assertAlmostEqual(action(self.p.alpha, self.p.beta, self.m.total, self.p.e_norm), 0.9856042, places=7)

    def test_false_example(self):
        self.assertAlmostEqual(action(5.0, 0.1, self.m.total, 0.3), 49.761125, places=6)

    def test_true_example_correction(self):
        self.assertAlmostEqual(action(0.1, 5.0, self.m.total, 0.3), 0.5454025, places=7)
        self.assertEqual(classify(action(0.1, 5.0, self.m.total, 0.3)), "temporal")

    def test_critical_beta(self):
        beta = beta_critical(0.1, self.m.total, 0.3)
        self.assertAlmostEqual(beta, 11.06002777777778)
        self.assertAlmostEqual(action(0.1, beta, self.m.total, 0.3), 0.0)

    def test_mass_proxy(self):
        self.assertAlmostEqual(mass_proxy(self.p.beta, self.p.e_norm), 0.032661)

    def test_decay(self):
        self.assertAlmostEqual(decay(0.3, 0.2, 5.0), 0.3 / math.e)
        self.assertLess(decay(0.3, 0.2, 5.0), decay(0.3, 0.2, 1.0))

    def test_zero_exodus_rejected_for_critical_beta(self):
        with self.assertRaises(ValueError):
            beta_critical(0.1, 3.155, 0.0)


if __name__ == "__main__":
    unittest.main()

