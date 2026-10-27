# Python Automation Training — Instructor Course Pack (3 Weeks, Breadth-First)

A 3-week, **lecture + demo driven** Python course for **complete beginners** (and people
with light experience in other languages). Automation is the recurring theme. The goal is
to **cover as much ground as possible** — concepts are taught via explanation and live
demos the instructor runs, with crisp **takeaways** per session. Hands-on coding is
**optional homework**, not in-class time.

- **Sessions:** 15 core one-hour sessions (3 weeks × 5/week) + a 5-session **advanced
  add-on** (Week 4: OOP & concurrency) for after the beginner arc
- **OS:** Fully OS-agnostic — works on Windows, macOS, and Linux
- **Format:** Instructor explains + runs demos; learners absorb + keep takeaways.
- **Design goal:** You can **never run out of material** — each session is topic-dense,
  and the overflow bank holds more.

---

## Session Format (breadth-first, 60 min)

| Time      | Segment              | Purpose                                            |
|-----------|----------------------|----------------------------------------------------|
| 0–5 min   | Recap + takeaways    | Review prior session's takeaways in one slide      |
| 5–50 min  | Topics + live demos  | Cover a cluster of topics; run demo scripts        |
| 50–57 min | Real-world framing   | How these topics show up in automation             |
| 57–60 min | Takeaways + homework | Recap key points; assign optional practice         |

No long in-class coding. The instructor drives; learners follow and keep the takeaways.
Exercises exist (in `exercises.md` / `solutions.md`) purely as **optional homework**.

---

## How to Use This Pack

```
python-training/
├── README.md
├── overflow-bank.md
├── cheat-sheets/
│   └── week-NN-cheatsheet.md
└── week-NN-topic/
    ├── lesson-plan.md     # topic-dense plan + takeaways per session
    ├── exercises.md       # OPTIONAL homework (core/stretch/bonus)
    ├── solutions.md
    └── demo-scripts/      # scripts the instructor runs live
```

Each session's lesson plan lists: topics covered, demo scripts to run, real-world framing,
and a **Takeaways** block to share verbatim.

---

## 3-Week Session Index (15 sessions, dense)

Because in-class coding is removed, each session covers more. Advanced topics are back in.

### Week 1 — Foundations & Core Data
1. Python intro, REPL, scripts, `print()`, comments, variables
2. Numbers, math, types, type conversion
3. Strings: methods, slicing, f-strings, `input()`
4. Lists & tuples: create, index, slice, methods
5. Dicts & sets: key–value data, membership, when to use each

### Week 2 — Logic, Loops & Reusable Code
1. `if`/`elif`/`else`, comparison & logical operators, truthiness
2. `for` loops, `range()`, iterating collections
3. `while` loops, `break`/`continue`; comprehensions (list/dict)
4. Functions: define, params, returns, defaults/keyword, scope
5. `*args`/`**kwargs`, lambdas, and building a reusable helper module

### Week 3 — Applied Automation & Beyond
1. Files: read/write/append, `with`, `pathlib`, folders (`os`, `shutil`)
2. Structured data: CSV & JSON
3. Error handling (`try`/`except`/`finally`), raising, `logging`
4. Modules, `pip`, `venv`; stdlib tour; `subprocess`; HTTP with `requests`; JSON APIs
5. **Capstone walkthrough** + light OOP intro + next-steps roadmap (testing, scraping, git)

### Week 4 — Advanced Add-On: OOP & Concurrency *(run after the beginner arc)*
1. Classes deeper: instance vs class attributes, `@property`, `@classmethod`/`@staticmethod`
2. Inheritance, polymorphism, `super()`, dunder methods, `@dataclass`
3. Concurrency concepts + the GIL; threading; `ThreadPoolExecutor`; race conditions & locks
4. Async with `asyncio`: `async`/`await`, the event loop, `asyncio.gather`
5. Multiprocessing (`ProcessPoolExecutor`) + choosing the right tool (threads vs async vs processes)

> **Week 4 is intermediate/advanced.** It assumes Weeks 1–3 (especially functions, errors,
> and the light OOP intro in 3.5). Treat it as a separate advanced course or enrichment for
> learners who finished the fundamentals.

> If a session runs light, pull from `overflow-bank.md`. If it runs heavy, push the last
> topic cluster to homework — the takeaways still stand alone.

---

## Setup Checklist (share before Week 1)

1. Install Python 3.12+ from https://python.org (check "Add to PATH" on Windows).
2. Install VS Code + the official Python extension.
3. Verify: `python --version` (or `python3 --version`).
4. Create a course folder.

> **OS note:** Use `python` (Windows) or `python3` (macOS/Linux). All code runs identically
> on every OS.
