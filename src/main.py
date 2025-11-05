
import time, random, subprocess, yaml, os

NAMESPACE = os.environ.get("AIOPS_NAMESPACE", "sre")
THRESHOLD = float(os.environ.get("ANOMALY_THRESHOLD", "0.85"))

def detect_anomaly(v):
  return v > THRESHOLD

def remediate():
  print("[AIOps] Triggering remediation job...")
  subprocess.run(["kubectl","apply","-f","k8s/job-template.yaml","-n",NAMESPACE], check=False)

def loop():
  print("[AIOps] Detector running. Ctrl+C to stop.")
  while True:
    val = random.random()
    print(f"[AIOps] metric={val:.3f}")
    if detect_anomaly(val):
      remediate()
    time.sleep(5)

if __name__ == "__main__":
  loop()
