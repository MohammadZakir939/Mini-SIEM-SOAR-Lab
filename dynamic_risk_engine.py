import json
from pathlib import Path

alert_folder = Path(r"C:\SOC_SOAR_LAB\alerts")

risk_score = 0

for file in alert_folder.glob("*.json"):

    with open(file, "r") as f:
        alert = json.load(f)

    if alert["alert_name"] == "PowerShell Alert":
        risk_score += 30

    elif alert["alert_name"] == "vssadmin Alert":
        risk_score += 50

    elif alert["alert_name"] == "Mass File Creation Alert":
        risk_score += 70

print(f"Risk Score: {risk_score}")

if risk_score >= 100:
    severity = "Critical"

elif risk_score >= 70:
    severity = "High"

elif risk_score >= 40:
    severity = "Medium"

else:
    severity = "Low"

print(f"Severity: {severity}")