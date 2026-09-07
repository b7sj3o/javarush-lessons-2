# import asyncio
#
#
# class DatabaseConnection:
#     async def __aenter__(self):
#         print("Підключення до БД...")
#         await asyncio.sleep(1)
#
#         print("Підключено!")
#
#         return self
#
#     async def __aexit__(self, exc_type, exc, tb):
#         print("Закриваємо з'єднання...")
#         await asyncio.sleep(1)
#
#         print("З'єднання закрито")
#
#     async def execute(self, query):
#         print(f"Виконуємо: {query}")
#         await asyncio.sleep(1)
#
#         return ["Alice", "Bob"]
#
#
# async def main():
#     async with DatabaseConnection() as db:
#         users = await db.execute(
#             "SELECT * FROM users"
#         )
#
#         print(users)
#
#
# asyncio.run(main())


# import aiohttp
# import asyncio
#
# async def fetch_page(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return response
#         # res = await session.get(url)
#
# async def main():
#     results = await asyncio.gather(*[fetch_page('https://api.github.com/users/defunkt') for _ in range(10)])
#
#     for result in results:
#         print(result.status)
#
# asyncio.run(main())



# class UserIterator:
#     def __init__(self, users, batch_size):
#         self.users = users
#         self.batch_size = batch_size
#         self.position = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.position >= len(self.users):
#             raise StopIteration
#
#         batch = self.users[
#             self.position:
#             self.position + self.batch_size
#         ]
#
#         self.position += self.batch_size
#
#         return batch
#
#
# users = list(range(100))
#
#
# for batch in UserIterator(users, 10):
#     print(batch)


# def batches(data, batch_size):
#     for i in range(0, len(data), batch_size):
#         yield data[i:i + batch_size]


# import asyncio
#
#
# async def fetch_page(page):
#     print(f"Запит сторінки {page}")
#
#     await asyncio.sleep(1)
#
#     return [
#         f"user-{page}-1",
#         f"user-{page}-2",
#         f"user-{page}-3",
#     ]
#
#
# async def users(pages=3):
#     page = 1
#
#     while page <= pages:
#         data = await fetch_page(page)
#
#         for user in data:
#             yield user
#
#         page += 1
#
#
# async def main():
#     async for user in users(pages=5):
#         print(user)
#
#
# asyncio.run(main())


# import asyncio
#
#
# class MessageQueue:
#     def __init__(self):
#         self.queue = asyncio.Queue()
#
#     def __aiter__(self):
#         return self
#
#     async def __anext__(self):
#         message = await self.queue.get()
#
#         if message is None:
#             raise StopAsyncIteration
#
#         return message
#
#     async def put(self, message):
#         await self.queue.put(message)



# async def producer(queue):
#     for i in range(5):
#         await asyncio.sleep(1)
#         await queue.put(f"Message {i}")
#
#     await queue.put(None)
#
#
# async def consumer(queue):
#     async for message in queue:
#         print("Received:", message)
#
#
#
# async def main():
#     queue = MessageQueue()
#
#     await asyncio.gather(
#         producer(queue),
#         consumer(queue),
#     )
#
#
# asyncio.run(main())


# import time
#
#
# def calculate(start, end):
#     total = 0
#
#     for i in range(start, end):
#         total += i * i
#
#     return total
#
#
# start = time.perf_counter()
#
# calculate(0, 40_000_000)
#
# print(f"Time: {time.perf_counter() - start:.2f}s")


# import time
# from concurrent.futures import ProcessPoolExecutor
#
#
# def calculate(start, end):
#     total = 0
#
#     for i in range(start, end):
#         total += i * i
#
#     return total
#
#
# ranges = [
#     (0, 10_000_000),
#     (10_000_000, 20_000_000),
#     (20_000_000, 30_000_000),
#     (30_000_000, 40_000_000),
# ]
#
#
# start = time.perf_counter()
#
# with ProcessPoolExecutor(max_workers=4) as executor:
#     results = executor.map(
#         lambda args: calculate(*args),
#         ranges
#     )
#
#     print(results)
#
# print(f"Time: {time.perf_counter() - start:.2f}s")



import multiprocessing
import time


N = 80_000_000
WORKERS = 4


def calculate(start, end, results, index):
    total = 0

    for i in range(start, end):
        total += i * i

    results[index] = total


if __name__ == "__main__":
    chunk = N // WORKERS

    processes = []
    results = multiprocessing.Array("Q", WORKERS)

    start = time.perf_counter()

    for i in range(WORKERS):
        start_range = i * chunk
        end_range = (i + 1) * chunk

        process = multiprocessing.Process(
            target=calculate,
            args=(start_range, end_range, results, i)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total = sum(results)

    elapsed = time.perf_counter() - start

    print("Result:", total)
    print(f"Time: {elapsed:.3f}s")