"""Session 4.5 demo — multiprocessing for CPU-bound work (real parallelism).

ProcessPoolExecutor runs work in separate processes, each with its own Python
interpreter — so the GIL does NOT block them. This is the right tool for
CPU-heavy tasks like number crunching or image processing.

Guarded by if __name__ == "__main__": — REQUIRED for multiprocessing to work
correctly on Windows and macOS (spawn start method).
"""

import time
from concurrent.futures import ProcessPoolExecutor


def heavy(n):
    """A deliberately CPU-bound task: sum of squares."""
    return sum(i * i for i in range(n))


def main():
    numbers = [2_000_000] * 4

    # Sequential
    start = time.perf_counter()
    seq = [heavy(n) for n in numbers]
    seq_time = time.perf_counter() - start
    print(f"Sequential: {seq_time:.2f}s")

    # Parallel across CPU cores
    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        par = list(pool.map(heavy, numbers))
    par_time = time.perf_counter() - start
    print(f"Parallel:   {par_time:.2f}s")

    print("Results equal:", seq == par)
    if par_time > 0:
        print(f"Speedup: {seq_time / par_time:.1f}x")


if __name__ == "__main__":
    main()
