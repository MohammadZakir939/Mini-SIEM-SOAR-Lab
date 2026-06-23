import subprocess
from logger import write_log

write_log("SOAR Pipeline Started")

scripts = [
    "alert_ingestion.py",
    "auto_incident_creator.py",
    "dynamic_risk_engine.py",
    "case_builder.py"
]

for script in scripts:

    print(f"\nRunning {script}...\n")

    write_log(f"Running {script}")

    subprocess.run(
        ["python", script],
        check=True
    )

write_log("SOAR Pipeline Completed")

print("\nSOAR Pipeline Completed Successfully")