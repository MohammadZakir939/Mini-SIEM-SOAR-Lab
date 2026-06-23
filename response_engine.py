severity = "Critical"

if severity == "Critical":

    with open(
        r"C:\SOC_SOAR_LAB\reports\response_action.txt",
        "w"
    ) as f:

        f.write(
            "CRITICAL INCIDENT DETECTED\n"
            "Recommended Actions:\n"
            "1. Isolate Host\n"
            "2. Preserve Evidence\n"
            "3. Notify SOC Team\n"
            "4. Begin Investigation\n"
        )

    print("Response Action Created")

else:
    print("No Action Required")