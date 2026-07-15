import unittest

from gateway.main_v4 import GatewayFlowController


class GatewayFlowControllerTests(unittest.TestCase):
    def test_w_is_monotone_on_valid_domain(self):
        flow = GatewayFlowController()
        values = [flow.step(15.5, 0.5, 2, dt).w for dt in (0.0, 0.1, 1.0, 5.0)]
        self.assertEqual(values, sorted(values))

    def test_w_is_strict_at_zero_load(self):
        flow = GatewayFlowController()
        first = flow.step(0, 0, 0, 0).w
        second = flow.step(0, 0, 0, 0).w
        self.assertGreater(first, 0)
        self.assertGreater(second, first)

    def test_nominal_mode(self):
        result = GatewayFlowController().step(15.5, 0.5, 2, 1.0)
        self.assertEqual(result.state, "SMOOTH_DEFORMATION")
        self.assertEqual(result.key_bits, 256)

    def test_isolation_mode(self):
        flow = GatewayFlowController()
        result = flow.step(5000, 0, 4, 1.0)
        self.assertEqual(result.state, "ISOLATE_DOMAIN")
        self.assertEqual(result.key_bits, 512)
        self.assertGreater(result.isolation_cost, 0)
        self.assertFalse(flow.health()["ready"])

    def test_invalid_domain_rejected(self):
        flow = GatewayFlowController()
        for args in [(-1, 0, 1, 1), (1, 101, 1, 1), (1, 0, -1, 1), (1, 0, 1, -1)]:
            with self.assertRaises(ValueError):
                flow.step(*args)


if __name__ == "__main__":
    unittest.main()
