"""Session 3.2 demo — reading and writing CSV files."""

import csv

# Write a CSV using DictWriter
rows = [
    {"name": "Ada", "team": "automation", "score": 92},
    {"name": "Alan", "team": "security", "score": 88},
    {"name": "Grace", "team": "automation", "score": 95},
]

with open("people.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "team", "score"])
    writer.writeheader()
    writer.writerows(rows)

# Read it back with DictReader (each row is a dict keyed by header)
print("--- high scorers (>= 90) ---")
with open("people.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # CSV values are strings — convert for math.
        if int(row["score"]) >= 90:
            print(row["name"], row["score"])

import os
os.remove("people.csv")
