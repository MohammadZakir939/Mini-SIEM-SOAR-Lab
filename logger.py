from datetime import datetime

def write_log(message):

    with open(
        r"C:\SOC_SOAR_LAB\logs\soar.log",
        "a"
    ) as f:

        f.write(
            f"[{datetime.now()}] {message}\n"
        )