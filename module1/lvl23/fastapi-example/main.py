import asyncio
import uvicorn
from time import perf_counter

from fastapi import FastAPI

app = FastAPI()

NAMES = ["users", "orders", "payments"]


async def fetch(name: str) -> str:
    await asyncio.sleep(1)
    return f"data from {name}"


async def one_by_one():
    for name in NAMES:
        yield await fetch(name)


async def all_at_once():
    tasks = [asyncio.create_task(fetch(name)) for name in NAMES]
    for task in tasks:
        yield await task


@app.get("/sequential")
async def sequential():
    started = perf_counter()
    results = []
    async for item in one_by_one():
        results.append(item)
    return {"elapsed": round(perf_counter() - started, 2), "results": results}


@app.get("/parallel")
async def parallel():
    started = perf_counter()
    results = [item async for item in all_at_once()]
    return {"elapsed": round(perf_counter() - started, 2), "results": results}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)