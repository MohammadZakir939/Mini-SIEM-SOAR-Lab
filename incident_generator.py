import json
from datetime import datetime
import random

incident = {
    "incident_id": f"INC-{random.randint(1000,9999)}",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "severity": "High",
    "alert_name": "PowerShell Execution Detected",
    "mitre_technique": "T1059.001",
    "host": "ZakirsMustang",
    "status": "Open"
}

filename = f"C:\\SOC_SOAR_LAB\\incidents\\{incident['incident_id']}.json"

with open(filename, "w") as f:
    json.dump(incident, f, indent=4)

print(f"Created: {filename}")