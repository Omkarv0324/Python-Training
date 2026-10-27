# Week 3 Cheat Sheet — Applied Automation

## Files
```python
with open("f.txt", "r") as f:      # modes: r, w, a
    content = f.read()
    for line in f: ...

with open("f.txt", "w") as f:      # overwrite
    f.write("line\n")
with open("f.txt", "a") as f:      # append
    f.write("more\n")
```

## pathlib (OS-agnostic)
```python
from pathlib import Path
p = Path("data") / "report.csv"    # use / to join
p.name  p.stem  p.suffix  p.parent
p.exists()  p.is_dir()
for item in Path(".").iterdir(): ...
Path("out").mkdir(exist_ok=True)
```

## CSV
```python
import csv
with open("f.csv", newline="") as f:
    for row in csv.DictReader(f):   # row is a dict
        print(row["name"])

with open("f.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "score"])
    w.writeheader(); w.writerows(rows)
```

## JSON
```python
import json
json.dump(obj, f, indent=2)        # write to file
data = json.load(f)                # read from file
json.dumps(obj)  /  json.loads(s)  # string <-> object
```

## Errors & logging
```python
try:
    risky()
except FileNotFoundError:
    ...
except ValueError as e:
    print(e)
else:
    print("ok")        # no exception
finally:
    cleanup()          # always runs

raise ValueError("bad input")

import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("app")
log.info("..."); log.warning("..."); log.exception("...")
```

## Modules, venv, subprocess, HTTP
```
python -m venv .venv
.venv\Scripts\activate         # Windows
source .venv/bin/activate      # macOS/Linux
pip install requests
```
```python
import subprocess, sys
r = subprocess.run([sys.executable, "--version"],
                   capture_output=True, text=True)
r.returncode, r.stdout, r.stderr

import requests
requests.get(url, timeout=5).json()
```

## Classes (light OOP)
```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
    def complete(self):
        self.done = True
    def __str__(self):
        return self.title

t = Task("write report"); t.complete()
```
