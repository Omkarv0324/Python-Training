"""Session 4.3 demo — ThreadPoolExecutor: the modern, simpler threading API."""

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch(url):
    time.sleep(0.5)              # pretend network I/O
    return f"{url} -> 200 OK"


urls = [f"https://example.com/{i}" for i in range(6)]

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=6) as pool:
    # .map keeps input order and is the simplest pattern
    for result in pool.map(fetch, urls):
        print(result)

print(f"map() took {time.perf_counter() - start:.2f}s\n")

# .submit + as_completed when you want results as soon as each finishes
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=6) as pool:
    futures = [pool.submit(fetch, u) for u in urls]
    for future in as_completed(futures):
        print("completed:", future.result())
print(f"submit() took {time.perf_counter() - start:.2f}s")
