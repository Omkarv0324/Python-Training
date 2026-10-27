"""Session 4.3 demo — race conditions and how a Lock fixes them.

Many threads updating shared state without a lock can lose updates because
read-modify-write is not atomic (read, compute, write — interruptible).

NOTE: a plain `counter += 1` loop may *look* safe on CPython because the GIL
often hides the race. To make the race reliably visible for teaching, the
unsafe version below does an explicit read -> yield -> write, which exposes
the lost-update problem the way real shared-state bugs behave.
"""

import threading
import time

# --- Without a lock: result is WRONG (lost updates) ---
counter = 0

def increment_unsafe():
    global counter
    for _ in range(50):
        current = counter       # read
        time.sleep(0)           # hint the scheduler to switch threads here
        counter = current + 1   # write (may overwrite another thread's update)

threads = [threading.Thread(target=increment_unsafe) for _ in range(8)]
for t in threads: t.start()
for t in threads: t.join()
print("Unsafe total (expected 400):", counter, "<- usually LESS (lost updates)")

# --- With a lock: always correct ---
counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(50):
        with lock:               # only one thread in the critical section
            current = counter
            time.sleep(0)
            counter = current + 1

threads = [threading.Thread(target=increment_safe) for _ in range(8)]
for t in threads: t.start()
for t in threads: t.join()
print("Safe total   (expected 400):", counter, "<- always correct")
