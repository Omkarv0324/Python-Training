"""Session 4.4 demo — asyncio fundamentals: async def, await, the event loop."""

import asyncio
import time


async def boil_water():
    print("  put kettle on")
    await asyncio.sleep(2)       # non-blocking wait
    print("  water boiled")
    return "water"


async def toast_bread():
    print("  bread in toaster")
    await asyncio.sleep(1)
    print("  toast ready")
    return "toast"


async def main():
    start = time.perf_counter()

    # await one after another = sequential (3s total)
    # Instead, run them CONCURRENTLY:
    results = await asyncio.gather(boil_water(), toast_bread())

    print("Got:", results)
    print(f"Breakfast ready in {time.perf_counter() - start:.2f}s")
    # ~2s, not 3s — the two awaits overlapped on ONE thread.


asyncio.run(main())
