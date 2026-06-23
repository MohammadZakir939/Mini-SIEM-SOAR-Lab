events = [
    ("12:01", "PowerShell Execution"),
    ("12:03", "Shadow Copy Deletion"),
    ("12:05", "Mass File Creation")
]

print("\n=== INCIDENT TIMELINE ===\n")

for time, event in events:
    print(f"{time} -> {event}")

print("\nAttack Sequence Complete")