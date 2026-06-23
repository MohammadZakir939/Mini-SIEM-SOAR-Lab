import json
from pathlib import Path

alert_folder = Path(r"C:\SOC_SOAR_LAB\alerts")

alerts = []

for file in alert_folder.glob("*.json"):
    with open(file, "r") as f:
        alerts.append(json.load(f))

alert_names = [a["alert_name"] for a in alerts]

print("\n=== ALERTS DETECTED ===\n")

for alert in alert_names:
    print(alert)

if (
    "PowerShell Alert" in alert_names and
    "vssadmin Alert" in alert_names and
    "Mass File Creation Alert" in alert_names
):
    severity = "Critical"

elif (
    "PowerShell Alert" in alert_names and
    "vssadmin Alert" in alert_names
):
    severity = "High"

elif "PowerShell Alert" in alert_names:
    severity = "Medium"

else:
    severity = "Low"

print(f"\nCorrelated Severity: {severity}")