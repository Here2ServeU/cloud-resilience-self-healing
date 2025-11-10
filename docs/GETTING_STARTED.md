# Getting Started with Cloud Resilience & Self-Healing Automation (AIOps Starter)
**Author:** Emmanuel Naweji  
**Role:** Principal SRE | DevOps | Cloud & AI Platform Engineer  
© 2025 Emmanuel Naweji — All Rights Reserved  

---

## Overview
This guide helps you deploy the AIOps-based cloud resilience platform from scratch.  
You will provision Kubernetes clusters using Terraform, deploy observability and self-healing components with Helm, and verify AIOps anomaly detection and remediation in action.  

By the end, you will have:  
- A running Kubernetes cluster (EKS, AKS, GKE, or OKE)  
- A Python-based anomaly detector running inside Kubernetes  
- Prometheus & Grafana observability stack  
- Automated remediation jobs triggered by the AIOps logic  

---

## 1. Prerequisites

### Install Required Tools
| Tool | Version | Purpose |
|------|----------|----------|
| Terraform | ≥ 1.6 | Infrastructure as Code |
| kubectl | ≥ 1.28 | Kubernetes CLI |
| Helm | ≥ 3.14 | Application deployment |
| Python | ≥ 3.10 | AIOps logic |
| Cloud CLI | AWS CLI / Azure CLI / GCloud / OCI | Cloud provisioning |

### Configure Authentication
Depending on your cloud provider:

- AWS:  
  ```bash
  aws configure
  ```

- Azure:  
  ```bash
  az login
  ```

- Google Cloud:  
  ```bash
  gcloud auth login
  ```

- Oracle Cloud:  
  Set your `~/.oci/config` file and test with:
  ```bash
  oci os ns get
  ```

---

## 2. Clone the Repository

```bash
git clone https://github.com/Here2ServeU/cloud-resilience-aiops.git
cd cloud-resilience-aiops
```

---

## 3. Provision the Kubernetes Cluster

Choose your preferred cloud under `infra/terraform/<cloud>`.

Example for AWS EKS:
```bash
cd infra/terraform/aws-eks
terraform init
terraform apply -auto-approve
```

After provisioning:
```bash
aws eks update-kubeconfig --region us-east-1 --name aiops-eks
kubectl get nodes
```
Output should show your worker nodes in Ready state.

---

## 4. Deploy the AIOps Platform via Helm

From the project root:
```bash
helm install aiops ./helm -n sre --create-namespace
```

This command installs:
- Namespace sre
- RBAC and ConfigMap
- AIOps Detector (Python Pod)
- Job template for remediation
- Prometheus + Grafana stack for observability  

Check that all pods are running:
```bash
kubectl get pods -n sre
```

---

## 5. Validate Anomaly Detection

You can view the detector logs:
```bash
kubectl logs -l app=aiops-detector -n sre
```

Expected output:
```
[INFO] Monitoring metrics from Prometheus...
[INFO] Detected anomaly in metric: cpu_usage (zscore=3.8)
[INFO] Triggering remediation job aiops-remediation-2025xxxx
```

Confirm the remediation job:
```bash
kubectl get jobs -n sre
kubectl logs job/<job-name> -n sre
```

---

## 6. Access Grafana for Observability

Forward the Grafana service:
```bash
kubectl -n monitoring port-forward svc/kube-prom-grafana 3000:80
```

Access http://localhost:3000  
Login: admin / prom-operator

Create a dashboard and use sample queries:
```promql
rate(container_cpu_usage_seconds_total{namespace="apps"}[2m])
```

---

## 7. Cleanup

When finished:
```bash
helm uninstall aiops -n sre
terraform destroy -auto-approve
```

---

## 8. Troubleshooting

| Issue | Possible Fix |
|--------|---------------|
| Pods stuck in Pending | Check node capacity: `kubectl describe node` |
| No remediation jobs | Ensure RBAC allows Job creation |
| Prometheus connection refused | Check PROM_URL in ConfigMap |
| Helm upgrade fails | Run `helm uninstall aiops -n sre` then reinstall |
| Terraform destroy stuck | Manually delete load balancer in your cloud console |

---

## 9. Next Steps

- Integrate Argo CD for GitOps deployment  
- Add Slack / ServiceNow integration for remediation alerts  
- Enable GPU nodes for AI/ML-based anomaly detection  
- Extend AIOps logic using Isolation Forest or LSTM time-series prediction  

---

## 10. License
This project is distributed under the MIT License.  
© 2025 Emmanuel Naweji — All Rights Reserved  
