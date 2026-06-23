import json
from pathlib import Path

incident_folder = Path(r"C:\SOC_SOAR_LAB\incidents")

latest_file = max(
    incident_folder.glob("*.json"),
    key=lambda x: x.stat().st_mtime
)

with open(latest_file, "r") as f:
    incident = json.load(f)

report = f"""
=============================
SOC INCIDENT REPORT
=============================

Incident ID: {incident['incident_id']}

Timestamp: {incident['timestamp']}

Severity: {incident['severity']}

Alert Name:
{incident['alert_name']}

MITRE Technique:
{incident['mitre_technique']}

Host:
{incident['host']}

Status:
{incident['status']}

=============================
"""

with open(
    r"C:\SOC_SOAR_LAB\reports\incident_report.txt",
    "w"
) as f:
    f.write(report)

print("Dynamic Report Generated")