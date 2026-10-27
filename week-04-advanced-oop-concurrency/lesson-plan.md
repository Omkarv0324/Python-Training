# Week 4 (Advanced Add-On) — OOP & Concurrency · Lesson Plans

A dedicated **advanced block** to run *after* the beginner arc (Weeks 1–3). Assumes
learners are comfortable with functions, errors, files, and basic data structures.
Same breadth-first, demo-driven format: instructor explains + runs demos; learners keep
takeaways. Exercises are optional homework. OS-agnostic.

> **Prerequisite:** Week 1–3, especially functions (2.4–2.5), errors (3.3), and the light
> OOP intro (3.5). Session 4.1 picks up exactly where 3.5 left off.

---

## Session 4.1 — Classes, Deeper: State, Methods, Properties

**Topics covered**
- Recap of `class`, `__init__`, `self`, methods (from 3.5)
- Instance attributes vs **class attributes** (shared across instances)
- `@property` — computed/validated attributes that look like plain fields
- `@staticmethod` and `@classmethod` (and the `cls` parameter)
- Encapsulation convention: `_private` / name-mangled `__very_private`

**Demos to run:** `demo-scripts/bank_account.py`, `demo-scripts/class_vs_instance.py`

**Real-world framing:** Classes model "things with state + behavior" — a bank account, a
download job, a config object. Properties let you add validation without breaking existing
`obj.balance` usage.

**Takeaways**
- Instance attributes are per-object; class attributes are shared by all instances.
- `@property` turns a method into a read-only/validated attribute.
- Use `@classmethod` for alternative constructors; `@staticmethod` for related helpers.

---

## Session 4.2 — Inheritance, Polymorphism, Dunders & Dataclasses

**Topics covered**
- Inheritance: subclassing, overriding, `super().__init__(...)`
- Polymorphism: same method name, different behavior per class
- Dunder (magic) methods: `__repr__`, `__str__`, `__eq__`, `__len__`, `__lt__`
- `@dataclass` — auto `__init__`/`__repr__`/`__eq__`, `field(default_factory=...)`, `order=True`
- When a dataclass beats a hand-written class (and when it doesn't)

**Demos to run:** `demo-scripts/inheritance.py`, `demo-scripts/dunders.py`,
`demo-scripts/dataclasses_demo.py`

**Real-world framing:** Inheritance models "is-a" relationships (a `RetryTask` is a `Task`).
Dunders make your objects behave like built-ins (sortable, comparable, printable).
Dataclasses remove boilerplate for the record-like objects automation is full of.

**Takeaways**
- `super().__init__()` runs the parent's setup; override methods to specialize.
- Implement `__repr__` for debugging and `__eq__`/`__lt__` to compare/sort objects.
- Reach for `@dataclass` for data-holding classes — less code, fewer bugs.

---

## Session 4.3 — Concurrency Concepts + Threading

**Topics covered**
- **Why concurrency:** overlap waiting (network, disk) to finish sooner
- Key distinction: **I/O-bound** vs **CPU-bound** work
- The **GIL** (Global Interpreter Lock) in plain terms: threads don't run Python bytecode
  truly in parallel, but they DO help when waiting on I/O
- `threading.Thread` basics; the danger of shared mutable state (race conditions) + `Lock`
- `concurrent.futures.ThreadPoolExecutor` — the modern, simpler API (`map`, `submit`)

**Demos to run:** `demo-scripts/threading_basics.py`, `demo-scripts/threadpool.py`,
`demo-scripts/race_condition.py`

**Real-world framing:** Downloading 50 files or hitting 50 API endpoints: threads let the
waiting overlap, turning minutes into seconds. This is the #1 automation win from concurrency.

**Takeaways**
- Threads shine for **I/O-bound** work (network/disk), not CPU-heavy math (GIL).
- Prefer `ThreadPoolExecutor` over raw `Thread` — cleaner and safer.
- Shared mutable state needs a `Lock`, or you get race conditions.

---

## Session 4.4 — Async with `asyncio`

**Topics covered**
- `async def`, `await`, coroutines, and the event loop
- `asyncio.run(main())`, `asyncio.gather(...)` to run many coroutines concurrently
- `asyncio.sleep` vs blocking `time.sleep` (why blocking breaks async)
- Threads vs async: both tackle I/O-bound work — async = one thread, many awaited tasks
- Mention of async HTTP (`aiohttp`/`httpx`) without requiring a network for the demo

**Demos to run:** `demo-scripts/asyncio_basics.py`, `demo-scripts/asyncio_gather.py`

**Real-world framing:** Async scales to thousands of concurrent I/O tasks with low overhead
— ideal for high-volume API scraping, chat bots, or websocket feeds. One event loop juggles
them all.

**Takeaways**
- `await` yields control while waiting, letting other coroutines run.
- `asyncio.gather(*tasks)` runs coroutines concurrently and collects results.
- Never call blocking functions (`time.sleep`, heavy CPU) inside async code — use the async
  equivalents or offload to a thread/process.

---

## Session 4.5 — Multiprocessing + Choosing the Right Tool

**Topics covered**
- `multiprocessing` / `ProcessPoolExecutor`: real parallelism across CPU cores (bypasses GIL)
- Process overhead and why data is pickled between processes
- **Decision framework:**
  - I/O-bound, moderate scale → **threads** (`ThreadPoolExecutor`)
  - I/O-bound, huge scale → **asyncio**
  - CPU-bound → **multiprocessing** (`ProcessPoolExecutor`)
  - Simple/sequential is fine → don't add concurrency at all
- Pitfalls: race conditions, deadlocks, over-parallelizing, debugging difficulty

**Demos to run:** `demo-scripts/multiprocessing_demo.py`, `demo-scripts/cpu_vs_io.py`

**Real-world framing:** Resizing 10,000 images or crunching numbers benefits from
multiprocessing (uses all cores). The `cpu_vs_io` demo shows *measured* timings so learners
see why the tool must match the workload.

**Takeaways**
- GIL means threads DON'T speed up CPU-bound work — use processes for that.
- `ProcessPoolExecutor` mirrors `ThreadPoolExecutor` — same API, real parallelism.
- Match the tool to the workload: threads/async for I/O, processes for CPU, nothing if it's
  already fast enough.

---

### Advanced block wrap
Learners can now model problems with classes (inheritance, dunders, dataclasses) and speed
up automation with the right concurrency tool. These are intermediate/advanced skills —
encourage practice on real scripts (parallel downloaders, batch processors) to cement them.
