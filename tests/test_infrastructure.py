from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class InfrastructureManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = (ROOT / "infrastructure/kubernetes/gateway.yaml").read_text(encoding="utf-8")

    def test_high_availability_controls_present(self):
        for token in ("replicas: 3", "kind: PodDisruptionBudget", "kind: HorizontalPodAutoscaler"):
            self.assertIn(token, self.manifest)

    def test_probes_are_not_conflated(self):
        self.assertIn("path: /health/live", self.manifest)
        self.assertIn("path: /health/ready", self.manifest)

    def test_custom_stress_metric_is_declared(self):
        self.assertIn("name: gateway_stress", self.manifest)
        self.assertIn("autoscaling/v2", self.manifest)

    def test_container_is_hardened_and_versioned(self):
        self.assertNotIn(":latest", self.manifest)
        for token in ("runAsNonRoot: true", "readOnlyRootFilesystem: true", "allowPrivilegeEscalation: false"):
            self.assertIn(token, self.manifest)


if __name__ == "__main__":
    unittest.main()

