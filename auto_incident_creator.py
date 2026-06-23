import json
import random
from datetime import datetime

# Load alert
with open(
    r"C:\SOC_SOAR_LAB\alerts\powershell_alert.json",
    "r"
) as f:
    alert = json.load(f)

# Load MITRE database
with open(
    r"C:\SOC_SOAR_LAB\mitre_mapping.json",
    "r"
) as f:
    mitre_db = json.load(f)

mitre_id = alert["mitre_id"]

# Dynamic severity
severity = "Medium"

incident = {
    "incident_id": f"INC-{random.randint(1000,9999)}",
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "alert_name": alert["alert_name"],
    "host": alert["host"],
    "event_id": alert["event_id"],
    "mitre_id": mitre_id,
    "mitre_tactic": mitre_db[mitre_id]["tactic"],
    "mitre_technique": mitre_db[mitre_id]["technique"],
    "severity": severity,
    "status": "Open"
}

filename = (
    f"C:\\SOC_SOAR_LAB\\incidents\\"
    f"{incident['incident_id']}.json"
)

with open(filename, "w") as f:
    json.dump(incident, f, indent=4)

print("Incident Created Automatically")
print(f"Incident ID: {incident['incident_id']}")
print(f"Severity: {severity}")