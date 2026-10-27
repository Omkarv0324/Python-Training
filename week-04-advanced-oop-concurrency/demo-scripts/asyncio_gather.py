"""Session 4.4 demo — asyncio.gather to fan out many I/O tasks on one thread.

Simulates fetching many URLs concurrently. With real code you'd use an async
HTTP client like aiohttp/httpx; here asyncio.sleep stands in for the network.
"""

import asyncio
import time


async def fetch(url, delay):
    await asyncio.sleep(delay)            # pretend network latency
    return f"{url} ({delay}s)"


async def main():
    tasks = [
        fetch("https://example.com/1", 1.0),
        fetch("https://example.com/2", 0.5),
        fetch("https://example.com/3", 1.5),
        fetch("https://example.com/4", 0.8),
    ]

    start = time.perf_counter()
    results = await asyncio.gather(*tasks)   # run all concurrently
    elapsed = time.perf_counter() - start

    for r in results:
        print("fetched:", r)
    # Total time ~= the SLOWEST task (1.5s), not the sum (3.8s).
    print(f"All {len(tasks)} done in {elapsed:.2f}s")


asyncio.run(main())
