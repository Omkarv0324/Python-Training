"""Session 4.5 demo — WHY the tool must match the workload.

Shows measured timings for CPU-bound work using threads vs processes:
  - Threads do NOT speed up CPU-bound work (the GIL serializes bytecode).
  - Processes DO, because each has its own interpreter.

Compare with threadpool.py / asyncio_gather.py, where threads/async DID help
because that work was I/O-bound (waiting), not CPU-bound.
"""

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def cpu_task(n):
    return sum(i * i for i in range(n))


def main():
    work = [1_500_000] * 4

    # Baseline: sequential
    start = time.perf_counter()
    [cpu_task(n) for n in work]
    seq = time.perf_counter() - start
    print(f"Sequential:      {seq:.2f}s")

    # Threads (expected: NO improvement for CPU-bound — GIL)
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(cpu_task, work))
    threads = time.perf_counter() - start
    print(f"ThreadPool:      {threads:.2f}s  (CPU-bound -> GIL limits this)")

    # Processes (expected: faster — real parallelism)
    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        list(pool.map(cpu_task, work))
    procs = time.perf_counter() - start
    print(f"ProcessPool:     {procs:.2f}s  (true parallelism across cores)")

    print("\nTakeaway: for CPU-bound work, processes win; threads don't.")


if __name__ == "__main__":
    main()
