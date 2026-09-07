import time
import asyncio
#
#
# async def print_smth(s):
#     await asyncio.sleep(1)
#     print(s)
#
#
#
# async def main():
#     task1 = asyncio.create_task(print_smth("hello"))
#     task2 = asyncio.create_task(print_smth("world"))
#
#     await task1
#     await task2
#
#
# asyncio.run(main())

# async def main():
#     loop = asyncio.get_running_loop()          # саме get_running_loop, не get_event_loop
#     fut = loop.create_future()
#     loop.call_later(1, fut.set_result, 'готово')
#     print(await fut)


# async def fetch_data(url):
#     print(f"Fetching data from {url}")
#     await asyncio.sleep(1) # Симуляція завантаження даних
#     return f"Data from {url}"
#
# async def main():
#     task1 =asyncio.create_task(fetch_data("https://api.github.com/users"))
#     task2 = asyncio.create_task(fetch_data("https://api.python.org/pypi/"))
#
#     response1 = await task1
#     response2 = await task2
#
#     print(response1)
#     print(response2)
#
# if __name__ == "__main__":
#     asyncio.run(main())



# async def say(what, delay):
#     await asyncio.sleep(delay)
#     return what
#
# async def main():
#     task1 = asyncio.create_task(say('hello', 1))
#     task2 = asyncio.create_task(say('world', 2))
#     done, pending = await asyncio.wait([task1, task2],timeout=1.5)
#
#     for task in done:
#         print(task.result(), task.done())


# asyncio.run(main())


# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     return what
#
# async def main():
#     results = await asyncio.gather(
#         say_after(4, 'hello'),
#         say_after(5, 'world')
#     )
#     print(results)
#
# asyncio.run(main())


import httpx

urls = [
    "https://api.github.com",
    "https://api.github.com/users/octocat",
    "https://api.github.com/repos/python/cpython",
    "https://api.github.com/repos/fastapi/fastapi",
    "https://api.github.com/repos/django/django",

    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://jsonplaceholder.typicode.com/comments/1",

    "https://dummyjson.com/products/1",
    "https://dummyjson.com/products/2",
    "https://dummyjson.com/users/1",
    "https://dummyjson.com/users/2",
    "https://dummyjson.com/todos/1",

    "https://api.coindesk.com/v1/bpi/currentprice.json",
    "https://api.exchangerate-api.com/v4/latest/USD",

    "https://official-joke-api.appspot.com/random_joke",
    "https://catfact.ninja/fact",
    "https://dog.ceo/api/breeds/image/random",

    "https://randomuser.me/api/",
    "https://api.quotable.io/random",
    "https://www.boredapi.com/api/activity",

    "https://api.agify.io?name=michael",
    "https://api.genderize.io?name=alex",
    "https://api.nationalize.io?name=michael",
]

async def fetch(client, url):
    try:
        r = await client.get(url, timeout=10)
        return r.json()
    except httpx.ConnectError:
        return "Connection error"

async def main():
    async with httpx.AsyncClient() as client:
        start = time.time()
        # results = await asyncio.gather(*(fetch(client, u) for u in urls))
        for url in urls:
            await fetch(client, url)
        print(f"Це зайняло {time.time() - start} секунд")


if __name__ == '__main__':
    asyncio.run(main())