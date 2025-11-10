# Cloud Resilience & Self-Healing Automation — Terraform + Multi-Cloud Kubernetes (AIOps Starter)
**Author:** Emmanuel Naweji  
**Role:** Principal SRE | DevOps | Cloud & AI Platform Engineer  
© 2025 Emmanuel Naweji — All Rights Reserved  

---

## Overview
This project demonstrates **cloud resilience and AIOps-based self-healing** in multi-cloud Kubernetes environments.  
It uses **Terraform** for provisioning clusters across **AWS EKS, Azure AKS, Google GKE, and Oracle OKE**, then deploys a **Python-based AIOps detector** that integrates with **Prometheus or Datadog** to identify anomalies and trigger **automated remediation jobs** in Kubernetes.

The system serves as a foundation for enterprises seeking to build **intelligent, self-healing platforms** that maintain high availability, reliability, and compliance across hybrid and multi-cloud infrastructures.

---

## Project Structure
```
cloud-resilience-aiops/
├── helm/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── namespace.yaml
│       ├── rbac.yaml
│       ├── configmap.yaml
│       ├── deployment.yaml
│       └── job-template.yaml
├── k8s-legacy/
│   ├── namespace.yaml
│   ├── rbac.yaml
│   ├── job-template.yaml
│   └── configmap.yaml
├── infra/
│   └── terraform/
│       ├── aws-eks/
│       ├── azure-aks/
│       ├── gcp-gke/
│       └── oci-oke/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── docs/
│   └── GETTING_STARTED.md
├── requirements.txt
└── README.md
```

---

## One-Command Deployment (Helm)
```bash
# Clone and deploy
git clone https://github.com/Here2ServeU/cloud-resilience-aiops.git
cd cloud-resilience-aiops

# Provision Kubernetes (choose provider)
cd infra/terraform/aws-eks
terraform init && terraform apply -auto-approve
cd ../../..

# Deploy AIOps stack
helm install aiops ./helm -n sre --create-namespace
```

Check the deployment:
```bash
kubectl get pods -n sre
kubectl logs -l app=aiops-detector -n sre
kubectl get jobs -n sre
```

---

## Observability
```bash
kubectl -n monitoring port-forward svc/kube-prom-grafana 3000:80
```
Visit **http://localhost:3000** — default login: `admin / prom-operator`

---

## Cleanup
```bash
helm uninstall aiops -n sre
terraform destroy -auto-approve
```

---

## Results & Value
- Automated anomaly detection and Kubernetes job-based remediation  
- Cross-cloud IaC with Terraform and Helm integration  
- Scalable, observable, and self-healing foundation for AIOps/ML workloads  
- Demonstrates operational excellence and automation maturity  

---

## License
This project is distributed under the MIT License.  
© 2025 Emmanuel Naweji — All Rights Reserved  
