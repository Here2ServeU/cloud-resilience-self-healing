
# Getting Started (Absolute Beginners)

1. Install Terraform, kubectl, Helm, Python 3.10+
2. Pick your cloud under `infra/terraform/*` and run `terraform init && terraform apply`
3. Export kubeconfig using the output hint from Terraform
4. Install Prometheus (optional quick start):
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm upgrade --install kube-prom prometheus-community/kube-prometheus-stack -n monitoring --create-namespace
   ```
5. Create SRE namespace & apply job template:
   ```bash
   kubectl apply -f k8s/namespace.yaml
   kubectl apply -f k8s/job-template.yaml
   ```
6. Run the detector:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   python src/main.py
   ```
