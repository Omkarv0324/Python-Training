"""Session 3.2 demo — reading and writing JSON."""

import json

config = {
    "app": "report-bot",
    "version": 2,
    "enabled": True,
    "recipients": ["ops@example.com", "lead@example.com"],
    "thresholds": {"warn": 80, "critical": 95},
}

# Write pretty JSON to a file
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

# Read it back into a Python dict
with open("config.json", "r") as f:
    loaded = json.load(f)

print("App:", loaded["app"])
print("Recipients:", loaded["recipients"])
print("Critical threshold:", loaded["thresholds"]["critical"])

# dumps/loads work with strings (no file) — handy for APIs
as_text = json.dumps(config)
print("As string length:", len(as_text))

import os
os.remove("config.json")
