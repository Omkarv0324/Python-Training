# Week 4 (Advanced) — Optional Homework (Core → Stretch → Bonus)

Optional practice for the advanced block. Solutions in `solutions.md`.

## Session 4.1 — Classes deeper
- **Core:** Write a `Temperature` class storing `celsius`; add a `@property` `fahrenheit` that computes `c * 9/5 + 32`.
- **Stretch:** Add a class attribute `unit = "metric"` and a `@classmethod` `from_fahrenheit(cls, f)` alternative constructor.
- **Bonus:** Make the `celsius` setter reject values below absolute zero (-273.15) by raising `ValueError`.

## Session 4.2 — Inheritance, dunders, dataclasses
- **Core:** Make a `Shape` base class with `area()`; subclass `Rectangle` and `Circle` that override it.
- **Stretch:** Add `__repr__` and `__eq__` to a `Vector(x, y)` class; verify two equal vectors compare `True`.
- **Bonus:** Rewrite `Vector` as a `@dataclass(order=True)` and sort a list of vectors.

## Session 4.3 — Threading
- **Core:** Use `ThreadPoolExecutor.map` to run a `sleep(0.5)` "fetch" over 8 URLs; confirm it's ~0.5s not 4s.
- **Stretch:** Increment a shared counter from 4 threads WITHOUT a lock, then WITH a `Lock`; compare results.
- **Bonus:** Use `submit` + `as_completed` and print results in completion order.

## Session 4.4 — asyncio
- **Core:** Write two `async def` coroutines that `await asyncio.sleep(...)`; run them with `asyncio.gather`.
- **Stretch:** Time the gather version vs awaiting them sequentially; explain the difference.
- **Bonus:** Write an async function that fetches N fake URLs concurrently and returns a list of results.

## Session 4.5 — Multiprocessing + choosing the tool
- **Core:** Use `ProcessPoolExecutor.map` to run a CPU-bound `sum(i*i ...)` over 4 inputs.
- **Stretch:** Time sequential vs process-parallel; report the speedup.
- **Bonus:** Write a one-paragraph "which tool?" guide: when you'd pick threads vs asyncio vs multiprocessing vs nothing.
