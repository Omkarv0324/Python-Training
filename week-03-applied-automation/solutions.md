# Week 3 — Homework Solutions

## Session 3.1
```python
# Core
with open("log.txt", "w") as f:
    f.write("a\nb\nc\n")
with open("log.txt") as f:
    print(f.read())

# Stretch
with open("log.txt", "a") as f:
    f.write("d\n")
with open("log.txt") as f:
    for line in f:
        print(line.rstrip())

# Bonus
from pathlib import Path
p = Path("data/report_2026.csv")
print(p.name, p.stem, p.suffix)   # report_2026.csv report_2026 .csv
```

## Session 3.2
```python
# Core
import csv
rows = [{"name": "Ada", "score": 92}, {"name": "Alan", "score": 88}, {"name": "Grace", "score": 95}]
with open("s.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "score"])
    w.writeheader(); w.writerows(rows)
with open("s.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row)

# Stretch
with open("s.csv", newline="") as f:
    for row in csv.DictReader(f):
        if int(row["score"]) >= 90:
            print(row["name"])

# Bonus
import json
with open("config.json", "w") as f:
    json.dump({"enabled": True, "level": "info"}, f, indent=2)
with open("config.json") as f:
    print(json.load(f)["level"])
```

## Session 3.3
```python
# Core
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

# Stretch
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")

# Bonus
def set_price(p):
    if p < 0:
        raise ValueError("price cannot be negative")
    return p
try:
    set_price(-1)
except ValueError as e:
    print(e)
```

## Session 3.4
```python
# Core
import datetime
print(datetime.date.today().strftime("%Y-%m-%d"))

# Stretch
import subprocess, sys
r = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
print(r.stdout.strip())

# Bonus
import json
data = json.loads('{"id": 1, "title": "demo"}')
print(data["id"], data["title"])
```

## Session 3.5
```python
# Core
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("Woof")
Dog("Rex").bark()

# Stretch
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog named {self.name}"
print(Dog("Rex"))

# Bonus — add to CATEGORIES in the capstone:
# "audio": {".mp3", ".wav", ".flac"},
```
