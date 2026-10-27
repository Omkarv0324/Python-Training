# Week 1 — Foundations & Core Data · Lesson Plans (Breadth-First)

Five topic-dense, demo-driven sessions. Instructor explains + runs demos; learners keep
the takeaways. Exercises are optional homework (see `exercises.md`). OS-agnostic.

---

## Session 1.1 — Python Intro, REPL, Scripts, `print()`, Comments, Variables

**Topics covered**
- What Python is and why it's ideal for automation (readable, batteries-included)
- Installing + verifying (`python --version`); the REPL vs running `.py` files
- `print()` for output; `#` comments and `"""docstrings"""`
- Variables as named values; assignment; PEP 8 snake_case naming

**Demos to run:** `demo-scripts/hello.py`, `demo-scripts/startup_banner.py`

**Real-world framing (50–57):** A script is just a saved list of instructions you can
re-run anytime — the atom of automation. Show the startup banner as "a tiny bot I run
every morning."

**Takeaways**
- Run code two ways: REPL (quick experiments) and `.py` files (saved, repeatable).
- `print()` shows output; `#` comments are notes Python ignores.
- Variables store values: `name = "Ada"`. Use clear snake_case names.

---

## Session 1.2 — Numbers, Math, Types & Type Conversion

**Topics covered**
- `int` vs `float`; booleans (`True`/`False`)
- Operators: `+ - * / // % **`
- `type()` to inspect a value's type
- Converting between types: `int()`, `float()`, `str()`
- Rounding with `round()`; integer vs true division

**Demos to run:** `demo-scripts/math_basics.py`, `demo-scripts/invoice_total.py`

**Real-world framing:** Automations constantly compute — totals, tax, durations, counts.
Reliable arithmetic that never makes a typo is a quiet superpower.

**Takeaways**
- `/` always gives a float; `//` floors; `%` gives the remainder; `**` is power.
- `type(x)` tells you what something is; `int()`/`float()`/`str()` convert.
- `input()` gives a string — convert before doing math (covered next session).

---

## Session 1.3 — Strings: Methods, Slicing, f-strings, `input()`

**Topics covered**
- Quotes (single/double), concatenation, `len()`
- Indexing & slicing: `s[0]`, `s[-1]`, `s[1:4]`, `s[::-1]`
- Core methods: `.upper() .lower() .title() .strip() .replace() .split() .startswith()`
- f-strings & number formatting: `f"{price:.2f}"`, alignment
- `input()` returns a string; `int(input(...))` pattern

**Demos to run:** `demo-scripts/greeter.py`, `demo-scripts/text_clean.py`,
`demo-scripts/file_namer.py`

**Real-world framing:** Most automation is text wrangling — cleaning names, reformatting
logs, generating consistent filenames. String methods are the workhorse.

**Takeaways**
- Slicing extracts parts: `s[start:stop]` (stop is excluded).
- String methods return NEW strings; chain them: `s.strip().lower()`.
- f-strings are the modern way to format: `f"Total: {total:.2f}"`.

---

## Session 1.4 — Lists & Tuples

**Topics covered**
- Lists: create, index, slice, `.append() .extend() .insert() .remove() .pop() .sort()`
- `len()`, membership with `in`, a gentle `for` loop preview
- Tuples: fixed, immutable sequences; when to prefer them
- Tuple unpacking: `x, y = point`

**Demos to run:** `demo-scripts/list_basics.py`, `demo-scripts/tuples_demo.py`

**Real-world framing:** Lists hold batches to process (files, rows, records). Tuples group
fixed data (coordinates, RGB colors, a record that shouldn't change).

**Takeaways**
- Lists are ordered and changeable: `items.append(x)`.
- Tuples are ordered and fixed: `point = (3, 4)`.
- Unpack with `a, b = pair`; check membership with `x in items`.

---

## Session 1.5 — Dicts & Sets

**Topics covered**
- Dictionaries: `{key: value}`, lookup `d[key]`, `.get()`, add/update, `.keys()/.values()/.items()`
- Looping over a dict
- Sets: uniqueness, membership tests, `|` `&` `-` operations
- Choosing the right structure (list vs tuple vs dict vs set)

**Demos to run:** `demo-scripts/dict_basics.py`, `demo-scripts/set_basics.py`

**Real-world framing:** Dicts model records ("name→value" config, JSON responses). Sets
dedupe and answer "have I seen this before?" fast — great for processing logs/IDs.

**Takeaways**
- Dict = labeled data: `user["email"]`; use `.get(key, default)` to avoid errors.
- Set = unique items + fast membership: `seen = set()`.
- Rule of thumb: ordered list → `list`; fixed group → `tuple`; labeled → `dict`; unique → `set`.

---

### Week 1 recap slide (use at start of Week 2)
You can now: run scripts, do math, wrangle strings, and store data in lists, tuples, dicts,
and sets. Next: making decisions and repeating work with logic and loops.
