from datetime import datetime

case_report = f"""
====================================
SOC INVESTIGATION CASE
====================================

Case ID: CASE-1001

Created:
{datetime.now()}

Severity:
Critical

MITRE ATT&CK:
T1059.001 - PowerShell

Timeline:

12:01 -> PowerShell Execution
12:03 -> Shadow Copy Deletion
12:05 -> Mass File Creation

Risk Score:
150

Response Actions:

1. Isolate Host
2. Preserve Evidence
3. Notify SOC Team
4. Begin Investigation

Case Status:
Open

====================================
"""

with open(
    r"C:\SOC_SOAR_LAB\reports\case_report.txt",
    "w"
) as f:
    f.write(case_report)

print("Case Created Successfully")