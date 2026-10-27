"""Session 4.3 demo — basic threading for I/O-bound work.

Simulates downloading several files. Each "download" is mostly waiting
(time.sleep), so threads let the waits overlap and finish much sooner.
"""

import threading
import time

def download(name, seconds):
    print(f"  start {name}")
    time.sleep(seconds)          # pretend this is network I/O
    print(f"  done  {name} ({seconds}s)")

jobs = [("a.zip", 1), ("b.zip", 1), ("c.zip", 1)]

# --- Sequential ---
start = time.perf_counter()
for name, secs in jobs:
    download(name, secs)
print(f"Sequential took {time.perf_counter() - start:.2f}s\n")

# --- Threaded ---
start = time.perf_counter()
threads = []
for name, secs in jobs:
    t = threading.Thread(target=download, args=(name, secs))
    t.start()
    threads.append(t)
for t in threads:
    t.join()                     # wait for all to finish
print(f"Threaded took {time.perf_counter() - start:.2f}s")
# Threaded ~1s vs sequential ~3s: the waiting overlapped.
