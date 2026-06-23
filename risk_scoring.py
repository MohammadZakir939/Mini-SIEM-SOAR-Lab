alerts = [
    "PowerShell Alert",
    "vssadmin Alert",
    "Mass File Creation Alert"
]

risk_score = 0

for alert in alerts:

    if alert == "PowerShell Alert":
        risk_score += 30

    elif alert == "vssadmin Alert":
        risk_score += 50

    elif alert == "Mass File Creation Alert":
        risk_score += 70

print(f"Risk Score: {risk_score}")

if risk_score >= 100:
    print("Severity: Critical")

elif risk_score >= 70:
    print("Severity: High")

elif risk_score >= 40:
    print("Severity: Medium")

else:
    print("Severity: Low")