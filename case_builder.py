import json
from pathlib import Path
from datetime import datetime

alert_folder = Path(r"C:\SOC_SOAR_LAB\alerts")

alerts = []
risk_score = 0

for file in alert_folder.glob("*.json"):

    with open(file, "r") as f:
        alert = json.load(f)

    alerts.append(alert)

    if alert["alert_name"] == "PowerShell Alert":
        risk_score += 30

    elif alert["alert_name"] == "vssadmin Alert":
        risk_score += 50

    elif alert["alert_name"] == "Mass File Creation Alert":
        risk_score += 70

if risk_score >= 100:
    severity = "Critical"
elif risk_score >= 70:
    severity = "High"
elif risk_score >= 40:
    severity = "Medium"
else:
    severity = "Low"

case = {
    "case_id": f"CASE-{datetime.now().strftime('%Y%m%d%H%M%S')}",
    "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "severity": severity,
    "risk_score": risk_score,
    "status": "Open",
    "alert_count": len(alerts),
    "alerts": [a["alert_name"] for a in alerts]
}

with open(r"C:\SOC_SOAR_LAB\reports\case.json", "w") as f:
    json.dump(case, f, indent=4)

print("Case Created")
print(f"Risk Score: {risk_score}")
print(f"Severity: {severity}")