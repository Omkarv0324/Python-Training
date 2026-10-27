# Week 4 (Advanced) — Homework Solutions

## Session 4.1
```python
# Core + Stretch + Bonus combined
class Temperature:
    unit = "metric"                      # class attribute

    def __init__(self, celsius):
        self.celsius = celsius           # goes through the setter below

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):            # Bonus: validation
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):                # Core
        return self._celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f):         # Stretch
        return cls((f - 32) * 5 / 9)


t = Temperature(25)
print(t.fahrenheit)                      # 77.0
print(Temperature.from_fahrenheit(212).celsius)   # 100.0
```

## Session 4.2
```python
# Core
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

print(Rectangle(3, 4).area(), round(Circle(2).area(), 2))

# Stretch + Bonus
from dataclasses import dataclass

@dataclass(order=True)
class Vector:
    x: int
    y: int

print(Vector(1, 2) == Vector(1, 2))          # True
print(sorted([Vector(3, 0), Vector(1, 9)]))  # ordered by (x, y)
```

## Session 4.3
```python
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch(url):
    time.sleep(0.5)
    return f"{url} OK"

urls = [f"u{i}" for i in range(8)]

# Core
with ThreadPoolExecutor(max_workers=8) as pool:
    print(list(pool.map(fetch, urls)))   # ~0.5s total

# Bonus
with ThreadPoolExecutor(max_workers=8) as pool:
    futures = [pool.submit(fetch, u) for u in urls]
    for f in as_completed(futures):
        print(f.result())

# Stretch: see demo-scripts/race_condition.py for the lock comparison
```

## Session 4.4
```python
import asyncio, time

async def work(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(work("a", 1), work("b", 1), work("c", 1))
    print(results, f"{time.perf_counter() - start:.2f}s")   # ~1s, not 3s

asyncio.run(main())
```

## Session 4.5
```python
import time
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

def main():
    nums = [2_000_000] * 4
    start = time.perf_counter()
    seq = [heavy(n) for n in nums]
    seq_t = time.perf_counter() - start

    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        par = list(pool.map(heavy, nums))
    par_t = time.perf_counter() - start

    print(f"seq {seq_t:.2f}s  par {par_t:.2f}s  speedup {seq_t/par_t:.1f}x")

if __name__ == "__main__":
    main()
```

### Bonus "which tool?" guide
- **Threads (`ThreadPoolExecutor`)** — I/O-bound work at moderate scale (downloads, API calls, disk). Simple and effective.
- **asyncio** — I/O-bound at large scale (thousands of concurrent connections); one thread, an event loop, async libraries.
- **Multiprocessing (`ProcessPoolExecutor`)** — CPU-bound work (math, image processing); uses all cores, bypasses the GIL.
- **Nothing** — if the task is already fast or truly sequential, don't add concurrency; it adds complexity and bugs.
