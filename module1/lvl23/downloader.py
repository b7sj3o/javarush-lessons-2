import os
import asyncio
import time

import aiohttp


URLS = [
    "https://drive.google.com/file/d/1g2QvBTiG22qQvjijFYLGoX6GaPziyvpr/view?usp=sharing",
    "https://drive.google.com/file/d/1RuMlSphWON6WJgAPJQHl6P0y8kii_938/view?usp=sharing",
    "https://drive.google.com/file/d/1KcIA6Le68b10p4LTrD7hzpVBNt1Wp8wF/view?usp=sharing",
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/users",
    "https://dummyjson.com/products",
    "https://dummyjson.com/users",
    "https://dummyjson.com/posts",
    "https://dummyjson.com/todos",
    "https://dummyjson.com/quotes",
    "https://dummyjson.com/carts",
    "https://dummyjson.com/products/1",
    "https://reqres.in/api/users",
    "https://reqres.in/api/products",
    "https://reqres.in/api/unknown",
    "https://catfact.ninja/fact",
    "https://catfact.ninja/breeds",
    "https://dog.ceo/api/breeds/image/random",
    "https://dog.ceo/api/breeds/list/all",
    "https://pokeapi.co/api/v2/pokemon/pikachu",
    "https://pokeapi.co/api/v2/pokemon/ditto",
    "https://pokeapi.co/api/v2/ability/65",
    "https://swapi.dev/api/people/1/",
    "https://swapi.dev/api/planets/1/",
    "https://swapi.dev/api/starships/9/",
    "https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json",
    "https://openlibrary.org/search.json?q=python",
    "https://www.googleapis.com/books/v1/volumes?q=python",
    "https://api.github.com/repos/python/cpython",
    "https://worldtimeapi.org/api/timezone/Europe/Kyiv",
    "https://worldtimeapi.org/api/timezone/Europe/London",
    "https://worldtimeapi.org/api/timezone/America/New_York",
    "https://worldtimeapi.org/api/timezone/Asia/Tokyo",
    "https://api.exchangerate-api.com/v4/latest/USD",
    "https://api.frankfurter.app/latest?from=USD",
    "https://api.frankfurter.app/latest?from=EUR",
    "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY",
    "https://official-joke-api.appspot.com/random_joke",
    "https://official-joke-api.appspot.com/jokes/programming/random",
    "https://randomuser.me/api/"
]
DIR_NAME = "downloads"

os.makedirs(DIR_NAME, exist_ok=True)

def save_to_file(content: str, filename: str):
    with open(f"{DIR_NAME}/{filename}", "w") as f:
        f.write(content)


async def download(session: aiohttp.ClientSession, url: str):
    try:
        async with session.get(url, timeout=10) as response:
            data = await response.text()

            filename = url.split("https://")[1].replace("/", "_")
            save_to_file(data, filename)
    except aiohttp.ClientConnectorError:
        print(f"{url} failed with ClientConnectorError")
    except aiohttp.ServerTimeoutError:
        print(f"{url} failed with Timeout")
    except Exception as e:
        print(f"{url} failed with {e}")


async def main():
    async with aiohttp.ClientSession() as session:
        start = time.perf_counter()
        tasks = [
            download(session, url)
            for url in URLS
        ]

        await asyncio.gather(*tasks)

        print(f"{time.perf_counter() - start} seconds")

if __name__ == '__main__':
    asyncio.run(main())
