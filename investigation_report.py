import json

with open(r"C:\SOC_SOAR_LAB\reports\case.json", "r") as f:
    case = json.load(f)

report = f"""
==================================================
SOC INCIDENT INVESTIGATION REPORT
==================================================

CASE INFORMATION
----------------
Case ID: {case['case_id']}
Status: {case['status']}
Severity: {case['severity']}
Risk Score: {case['risk_score']}

ALERT SUMMARY
-------------
Total Alerts Correlated: {case['alert_count']}

Alerts Observed:
"""

for alert in case["alerts"]:
    report += f"\n- {alert}"

report += """

ATTACK ANALYSIS
---------------
Observed activity is consistent with ransomware
precursor behavior.

Indicators:
- PowerShell Execution
- Shadow Copy Deletion
- Mass File Creation

MITRE ATT&CK
------------
T1059.001 - PowerShell
T1490 - Inhibit System Recovery

RECOMMENDED ACTIONS
-------------------
1. Isolate Endpoint
2. Preserve Evidence
3. Collect Memory Artifacts
4. Review User Activity
5. Initiate Incident Response

CONCLUSION
----------
Incident classified as CRITICAL and requires
immediate investigation.

==================================================
"""

with open(
    r"C:\SOC_SOAR_LAB\reports\investigation_report.txt",
    "w"
) as f:
    f.write(report)

print("Investigation Report Generated")