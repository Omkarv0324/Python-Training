# Week 3 — Applied Automation & Beyond · Lesson Plans (Breadth-First)

Five topic-dense, demo-driven sessions. This is where scripts start touching the real
world: files, data formats, errors, external tools, and a capstone. OS-agnostic.

---

## Session 3.1 — Files & the File System

**Topics covered**
- Reading text: `open()`, `.read()`, `.readlines()`, looping over a file
- Writing & appending: modes `"w"` vs `"a"`
- The `with open(...) as f:` context manager (auto-closes files)
- OS-agnostic paths with `pathlib.Path` (`/` operator, `.exists()`, `.suffix`, `.name`)
- Listing/creating folders and moving files (`Path.iterdir()`, `os`, `shutil`)

**Demos to run:** `demo-scripts/read_write.py`, `demo-scripts/paths_demo.py`

**Real-world framing:** Reading inputs and writing outputs is the core of nearly every
automation. `pathlib` makes your scripts run unchanged on Windows, macOS, and Linux.

**Takeaways**
- Always use `with open(path) as f:` — it closes the file for you.
- Modes: `"r"` read, `"w"` overwrite, `"a"` append.
- Use `pathlib.Path` for paths — never hand-build strings with `\` or `/`.

---

## Session 3.2 — Structured Data: CSV & JSON

**Topics covered**
- CSV with the `csv` module: `csv.reader`, `csv.DictReader`, `csv.DictWriter`
- JSON with the `json` module: `json.load/loads`, `json.dump/dumps`
- When to use which (CSV = tabular/spreadsheets, JSON = nested/API data)
- Round-tripping: read → transform → write

**Demos to run:** `demo-scripts/csv_demo.py`, `demo-scripts/json_demo.py`

**Real-world framing:** Reports, exports, configs, and API payloads are almost always CSV
or JSON. Being fluent in both is what makes Python a data-automation workhorse.

**Takeaways**
- `csv.DictReader` gives each row as a dict keyed by header — very readable.
- `json.dump(obj, f, indent=2)` writes pretty JSON; `json.load(f)` reads it back.
- CSV values are strings — convert numbers yourself.

---

## Session 3.3 — Error Handling & Logging

**Topics covered**
- Reading tracebacks (bottom line = the actual error)
- `try` / `except` / `else` / `finally`
- Catching specific exceptions (`FileNotFoundError`, `ValueError`) vs bare `except`
- Raising your own errors with `raise`; input validation
- `logging` basics (levels, why it beats `print` for automation)

**Demos to run:** `demo-scripts/errors_demo.py`, `demo-scripts/logging_demo.py`

**Real-world framing:** Unattended automation MUST handle the unexpected — a missing file,
a bad row, a flaky network. Good error handling + logging is the difference between a
script you trust overnight and one that silently fails.

**Takeaways**
- Catch specific exceptions; let unexpected ones surface.
- `finally` always runs — use it for cleanup.
- Prefer `logging` over `print` for anything that runs unattended.

---

## Session 3.4 — Modules, `pip`/`venv`, Stdlib, `subprocess` & HTTP APIs

**Topics covered**
- Importing stdlib modules; a quick tour: `datetime`, `random`, `pathlib`, `collections`
- Third-party packages: `pip install`, and why virtual environments (`venv`) matter
- Creating/activating a venv (commands shown for every OS)
- Running external programs with `subprocess.run()`
- Fetching data over HTTP with `requests`; parsing a JSON API response
  (concept + code shown; live network optional)

**Demos to run:** `demo-scripts/stdlib_tour.py`, `demo-scripts/subprocess_demo.py`,
`demo-scripts/api_demo.py` (network-optional; has an offline fallback)

**Real-world framing:** Real automations pull in libraries, call other tools, and talk to
web APIs. `venv` keeps each project's dependencies isolated and reproducible.

**Takeaways**
- One venv per project: create, activate, then `pip install`.
- `subprocess.run([...], capture_output=True, text=True)` runs any command.
- `requests.get(url).json()` fetches and parses JSON in two steps.

**venv quick reference (share verbatim)**
```
python -m venv .venv
# Windows:        .venv\Scripts\activate
# macOS / Linux:  source .venv/bin/activate
pip install requests
```

---

## Session 3.5 — Capstone Walkthrough + Light OOP Intro + Roadmap

**Topics covered**
- Light OOP: what a `class` is, `__init__`, `self`, methods — just enough to structure a project
- Capstone walkthrough: a **file organizer** that sorts a folder by file type, with logging
  and error handling (combines Weeks 1–3)
- Project structure & a good `README`
- Next-steps roadmap: testing with `pytest`, web scraping, Git — all in `overflow-bank.md`

**Demos to run:** `demo-scripts/oop_intro.py`, `demo-scripts/capstone_file_organizer.py`

**Real-world framing:** The capstone is a genuinely useful tool they can run on their own
Downloads folder. It ties together files, loops, functions, dicts, and error handling —
the whole course in one script.

**Takeaways**
- A class bundles data + behavior; `self` refers to the instance.
- The capstone shows the full automation shape: read a folder → decide → act → log.
- You now have the foundation to learn testing, scraping, and Git on your own.

---

### Course wrap
From "what is Python" to a working file-organizer in 15 sessions. Point learners to
`overflow-bank.md` for deeper dives and `cheat-sheets/` for quick reference.
