import json

# Read Splunk export
with open(
    r"C:\SOC_SOAR_LAB\splunk_exports\exported_alert.json",
    "r"
) as f:
    export = json.load(f)

# Convert to SOAR alert format
alert = {
    "alert_name": export["search_name"],
    "host": export["host"],
    "event_id": export["event_id"],
    "mitre_id": "T1059.001",
    "timestamp": export["timestamp"]
}

# Save into alerts folder
with open(
    r"C:\SOC_SOAR_LAB\alerts\powershell_alert.json",
    "w"
) as f:
    json.dump(alert, f, indent=4)

print("Alert Ingested Successfully")
print(f"Alert Name: {alert['alert_name']}")
print(f"Host: {alert['host']}")