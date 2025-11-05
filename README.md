
# Cloud Resilience & Self‑Healing Automation — Terraform + Multi‑Cloud Kubernetes

A Python **AIOps** starter that detects anomalies (Prometheus/Datadog) and triggers **automated remediation** via Kubernetes Jobs. Deploy the cluster using Terraform on **EKS, AKS, GKE, or OKE**, then install the AIOps components.

> Working on this project. I'm very excited!

## Steps
1) Provision a cluster (pick a cloud) under `infra/terraform/<cloud>`
2) `kubectl apply -f k8s/` to install RBAC/namespace
3) `python src/main.py` to start detectors
4) Confirm remediation jobs under `kubectl get jobs -n sre`

See `docs/GETTING_STARTED.md` for absolute beginner steps.
