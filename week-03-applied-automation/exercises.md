# Week 3 — Optional Homework (Core → Stretch → Bonus)

Optional practice to accompany the demo-driven sessions. Solutions in `solutions.md`.

## Session 3.1 — Files & pathlib
- **Core:** Write 3 lines to `log.txt`, then read and print the file.
- **Stretch:** Append a 4th line, then print the file line by line.
- **Bonus:** Use `pathlib.Path` to print the `.name`, `.stem`, and `.suffix` of `"data/report_2026.csv"`.

## Session 3.2 — CSV & JSON
- **Core:** Write 3 rows (name, score) to a CSV with `DictWriter`, then read and print them.
- **Stretch:** Read the CSV and print only rows with score >= 90.
- **Bonus:** Save a dict to `config.json` with `indent=2`, then load and print one value.

## Session 3.3 — Errors & logging
- **Core:** Write `safe_int(text)` that returns `int(text)` or `0` if it fails (`ValueError`).
- **Stretch:** Add a `finally` block that prints "done" regardless of success.
- **Bonus:** Write `set_price(p)` that raises `ValueError` if `p < 0`; catch and print the message.

## Session 3.4 — modules, subprocess, APIs
- **Core:** Use `datetime` to print today's date formatted as `YYYY-MM-DD`.
- **Stretch:** Use `subprocess.run([sys.executable, "--version"], ...)` and print the version.
- **Bonus:** Use the offline-safe API pattern to read `id`/`title` from a JSON payload.

## Session 3.5 — OOP & capstone
- **Core:** Write a `Dog` class with `name` and a `bark()` method that prints "Woof".
- **Stretch:** Add `__str__` to `Dog` so `print(dog)` shows a friendly string.
- **Bonus:** Extend the capstone: add a new category (e.g., `"audio": {".mp3", ".wav"}`).
