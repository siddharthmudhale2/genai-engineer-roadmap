import asyncio
import time


async def fetch_data(name, delay):
    print(f"Starting {name}")

    await asyncio.sleep(delay)

    print(f"Finished {name}")
    return f"{name} result"


async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 2),
        fetch_data("API 3", 2)
    )

    elapsed = time.perf_counter() - start

    print("\nResults:")
    print(results)

    print(f"\nTime taken: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())