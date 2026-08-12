# ⚡ Day 4 — Python Async Programming

> **Phase:** Python Foundations  
> **Status:** ✅ Completed

---

## 📖 Quick Definitions

| Concept | Definition |
|---|---|
| **Synchronous** | Tasks execute sequentially, with later work waiting for earlier work to finish. |
| **Asynchronous** | Allows a program to work on other available tasks while waiting for an I/O operation. |
| **I/O-bound** | Work that spends significant time waiting for external operations such as APIs or databases. |
| **`async`** | Defines an asynchronous function, also called a coroutine function. |
| **`await`** | Suspends the current coroutine until an awaitable operation completes. |
| **Coroutine** | An asynchronous computation that can pause and resume. |
| **Event Loop** | Schedules and coordinates asynchronous tasks. |
| **`asyncio`** | Python's standard-library framework for asynchronous programming. |
| **`asyncio.run()`** | Runs an asynchronous entry-point coroutine. |
| **`asyncio.gather()`** | Runs multiple awaitables concurrently and waits for their results. |

---

## 🔹 Basic Syntax

### `async`

```python
async def fetch_data():
    return "Data"
```

### `await`

```python
async def main():
    result = await fetch_data()
```

### `asyncio.run()`

```python
import asyncio

asyncio.run(main())
```

---

## 🔄 Synchronous vs Asynchronous

### Synchronous

```text
Task A → Wait → Task B → Wait → Task C
```

### Asynchronous

```text
Task A ────────────┐
Task B ────────────┤ → Waiting periods overlap
Task C ────────────┘
```

---

## 🚫 Blocking vs Non-Blocking

### Blocking

```python
import time

time.sleep(2)
```

Blocks the current thread.

### Async

```python
import asyncio

await asyncio.sleep(2)
```

Suspends the current coroutine and allows the event loop to run other available tasks.

---

## 🔄 `asyncio.gather()`

Use `asyncio.gather()` when multiple operations are independent.

```python
results = await asyncio.gather(
    task_a(),
    task_b(),
    task_c()
)
```

Conceptually:

```text
Task A ────────────────┐
Task B ────────────────┤
Task C ────────────────┘
          ↓
       Results
```

---

## 🧠 Important Rule

> **`async` does NOT automatically make code faster.**

Async is mainly useful when your application spends significant time waiting for I/O.

---

## 🌐 Good Use Cases for Async

- API requests
- LLM API calls
- Database queries
- Network operations
- WebSockets
- Multiple external services
- High-concurrency web applications

---

## ⚙️ CPU-Bound vs I/O-Bound

| I/O-Bound | CPU-Bound |
|---|---|
| API requests | Heavy calculations |
| Database queries | Large mathematical computations |
| Network operations | CPU-intensive algorithms |
| External service calls | Some heavy data processing |
| Good candidate for async | Async alone usually isn't the solution |

---

## 🤖 Async + GenAI

GenAI applications frequently wait for external services.

```text
+-------------+       Async Request       +-------------+
| FastAPI     | ------------------------> | LLM API     |
+-------------+                           +-------------+
       │                                         │
       │                                         │
       └------------- Other Requests ------------┘
```

Async can be useful when your application communicates with:

- LLM APIs
- Embedding APIs
- Vector databases
- External tools
- Multiple APIs

---

## 🚀 Typical AI Application

```text
+---------+     +----------+     +---------+
| Client  | --> | FastAPI  | --> | LLM API |
+---------+     +----------+     +---------+
                     |
                     v
              +-------------+
              | Vector DB   |
              +-------------+
```

If these external operations are independent, asynchronous programming can help overlap their waiting time.

---

## 💻 Important Code Pattern

```python
import asyncio


async def fetch_data(name, delay):
    print(f"Starting {name}")

    await asyncio.sleep(delay)

    print(f"Finished {name}")

    return f"{name} result"


async def main():

    results = await asyncio.gather(
        fetch_data("API 1", 2),
        fetch_data("API 2", 2),
        fetch_data("API 3", 2)
    )

    print(results)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## ⚠️ Common Mistakes

### Mistake 1

```python
time.sleep(2)
```

inside async code when you actually need non-blocking waiting.

Prefer:

```python
await asyncio.sleep(2)
```

for simulated async waiting.

---

### Mistake 2

Thinking this automatically runs tasks concurrently:

```python
await task_a()
await task_b()
await task_c()
```

These are awaited sequentially.

For independent tasks, consider:

```python
await asyncio.gather(
    task_a(),
    task_b(),
    task_c()
)
```

---

### Mistake 3

Thinking async is mainly for CPU-heavy calculations.

Async is primarily useful for **I/O-bound workloads**.

---

## 💼 Interview Questions

### What is asynchronous programming?

A programming model that allows an I/O operation to be suspended while other available work can proceed.

### What is `async`?

`async` defines a coroutine function.

### What is `await`?

`await` suspends the current coroutine until an awaitable operation completes.

### What is a coroutine?

An asynchronous computation that can pause and resume.

### What is an event loop?

A mechanism that schedules and coordinates asynchronous tasks.

### What is `asyncio`?

Python's standard-library framework for asynchronous programming.

### What is `asyncio.gather()`?

It runs multiple awaitables concurrently and waits for their results.

### Does async make CPU-intensive code faster?

No. Async primarily improves how I/O waiting is handled.

### Why is async important for GenAI?

GenAI applications frequently wait for LLM APIs, databases, vector databases, and external tools, making asynchronous I/O useful for handling concurrency efficiently.

---

## 📌 Quick Revision

```text
async
↓
Defines coroutine function

await
↓
Suspends current coroutine until awaitable completes

asyncio
↓
Python async framework

Event Loop
↓
Schedules and coordinates async work

asyncio.run()
↓
Runs the async entry point

asyncio.gather()
↓
Runs independent awaitables concurrently

I/O-bound
↓
Good use case for async

CPU-bound
↓
Async alone doesn't solve the problem
```

---

## 🎯 Key Takeaways

- ✅ Async programming is mainly about efficiently handling waiting.
- ✅ `async def` creates coroutine functions.
- ✅ `await` allows a coroutine to yield while waiting.
- ✅ The event loop coordinates asynchronous execution.
- ✅ `asyncio.gather()` is useful for independent concurrent operations.
- ✅ Async is especially useful for API-heavy applications.
- ✅ Async is highly relevant to FastAPI and GenAI applications.
- ✅ Async does not automatically make CPU-heavy operations faster.

---

## 🔗 Day 4 Progress

| Topic | Status |
|---|---|
| Synchronous Programming | ✅ |
| Asynchronous Programming | ✅ |
| `async` | ✅ |
| `await` | ✅ |
| Coroutines | ✅ |
| Event Loop | ✅ |
| `asyncio` | ✅ |
| `asyncio.run()` | ✅ |
| `asyncio.gather()` | ✅ |
| Blocking vs Non-Blocking | ✅ |
| I/O-bound vs CPU-bound | ✅ |
| Async + GenAI | ✅ |
| Practical Exercise | ✅ |

---

> **Core idea:** Async programming allows applications to make better use of time spent waiting for I/O.