# import os
import os.path
import time
import asyncio
from pathlib import Path
from dataclasses import dataclass

data = Path("data")

# рядки
# слова
# символи

@dataclass
class AnalyzedFile:
    rows_count: int
    words_count: int
    symbols_count: int
    filename: str


async def analyze_file(filename: str) -> AnalyzedFile:
    rows_count = 0
    words_count = 0
    symbols_count = 0
    # os.path.getsize(filename)
    with open(f"data/{filename}", "r", encoding="utf-8") as f:
        content = f.readlines()

        rows_count = len(content)

        for row in content:
            words_count += len(row.split())
            symbols_count += len(row)


    return AnalyzedFile(
        rows_count=rows_count,
        words_count=words_count,
        symbols_count=symbols_count,
        filename=filename
    )


async def main():
    start = time.perf_counter()

    files = next(data.walk())[2]
    tasks = [analyze_file(file) for file in files]

    results: list[AnalyzedFile] = await asyncio.gather(*tasks)
    # results = []
    # 
    # for file in files:
    #     results.append(await analyze_file(file))


    end = time.perf_counter()

    for result in results:
        print(result.filename + ":")
        print(f"  Рядків: {result.rows_count}")
        print(f"  Слів: {result.words_count}")
        print(f"  Символів: {result.symbols_count}")
        print()


    print("-------------")
    print(f"Рядків: {sum(result.rows_count for result in results)}")
    print(f"Слів: {sum(result.words_count for result in results)}")
    print(f"Символів: {sum(result.symbols_count for result in results)}")

    print(f"\nЦе зайняло: {end-start} секунд")



if __name__ == "__main__":
    asyncio.run(main())