# Kubernetes deployment

These manifests deploy the heuristic telemetry controller. They do not certify
availability, DoS resistance, cryptographic security, or a mathematical proof.

Before deployment:

1. build and scan the container;
2. publish the exact image tag or, preferably, digest;
3. configure TLS/authentication at an ingress or service mesh;
4. add NetworkPolicy, PodDisruptionBudget and monitoring appropriate to the cluster;
5. run load, fault-injection and security tests in the target environment.

The HPA requires Metrics Server. The image reference is a placeholder until a
release image is built and published.
