# Week 4 Cheat Sheet — Advanced OOP & Concurrency

## Classes (deeper)
```python
class Account:
    currency = "USD"              # CLASS attribute (shared)

    def __init__(self, owner, balance=0):
        self.owner = owner        # INSTANCE attribute
        self._balance = balance   # _ = internal by convention

    @property                     # read like an attribute: a.balance
    def balance(self):
        return self._balance

    @balance.setter               # validate on assignment
    def balance(self, v):
        if v < 0: raise ValueError("no negative")
        self._balance = v

    @classmethod                  # alternative constructor
    def joint(cls, a, b):
        return cls(f"{a} & {b}")

    @staticmethod                 # related helper, no self/cls
    def valid(amount):
        return amount > 0
```

## Inheritance & polymorphism
```python
class Base:
    def run(self): return "base"

class Child(Base):
    def __init__(self, x):
        super().__init__()        # call parent __init__
        self.x = x
    def run(self):                # override
        return super().run() + " + child"

isinstance(obj, Base)             # True for subclasses
```

## Dunder (magic) methods
```python
def __repr__(self): ...   # debug:  repr(obj)
def __str__(self):  ...   # print:  str(obj)
def __eq__(self, other): ...   # ==
def __lt__(self, other): ...   # <  (enables sorting)
def __len__(self): ...         # len(obj)
def __add__(self, other): ...  # obj + other
```

## Dataclasses
```python
from dataclasses import dataclass, field

@dataclass(order=True)            # auto __init__/__repr__/__eq__/ordering
class Point:
    x: int
    y: int

@dataclass
class Bag:
    items: list = field(default_factory=list)   # mutable default
```

---

## Concurrency — pick the right tool
| Workload                    | Tool                         |
|-----------------------------|------------------------------|
| I/O-bound, moderate scale   | `ThreadPoolExecutor`         |
| I/O-bound, huge scale       | `asyncio`                    |
| CPU-bound                   | `ProcessPoolExecutor`        |
| Already fast / sequential   | no concurrency               |

> **GIL:** threads don't run Python bytecode in parallel — great for *waiting* (I/O),
> useless for *computing* (CPU). Use processes for CPU-bound work.

## Threads
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))        # ordered
    futures = [pool.submit(fetch, u) for u in urls]
    for f in as_completed(futures):              # as they finish
        print(f.result())

import threading
lock = threading.Lock()
with lock:                 # protect shared mutable state
    shared += 1
```

## asyncio
```python
import asyncio

async def fetch(x):
    await asyncio.sleep(1)         # non-blocking wait
    return x

async def main():
    results = await asyncio.gather(fetch(1), fetch(2), fetch(3))

asyncio.run(main())
# NEVER use blocking time.sleep / heavy CPU inside async code.
```

## Multiprocessing
```python
from concurrent.futures import ProcessPoolExecutor

def heavy(n): return sum(i*i for i in range(n))

if __name__ == "__main__":         # REQUIRED guard (Windows/macOS spawn)
    with ProcessPoolExecutor() as pool:
        results = list(pool.map(heavy, inputs))
```
