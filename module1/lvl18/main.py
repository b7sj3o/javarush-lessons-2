# file = open("data.txt", "w", encoding="utf-8")
#
# file.write("Привіт!")
#
# file.close()
#
#
# file = open("data.txt", "r", encoding="utf-8")
#
# print(file.read())
#
# file.close()


# OSError: [Errno 24] Too many open files: 'data.txt'
# files = []
# for i in range(10_000):
#     files.append(open("data.txt", "a+"))

# f = open("data.txt","r")

# for line in f:
#     print(line)

# while True:
#     line = f.readline()
#
#     print(f"{line!r}")
#
#     if line == "":
#         break

# f.read(10)
# f.read(10)

# print(f.readline())
# print(f.readline())
#
# for ind, line in enumerate(f):
#     if ind == 9:
#         print(line)
#         break

# f = None
# try:
#     f = open("data.txt", "a")
#     f.write("Hello again!\n")
# except FileNotFoundError:
#     print("Файл не знайдено")
# finally:
#     if f:
#         f.close()


# with open("data.txt", "a") as f:
#     f.write("Hello!\n")


# mgr = open("message.txt", "r")
# file = mgr.__enter__()
# try:
#     data = file.read()
#     ...
#     ...
# finally:
#     mgr.__exit__(None, None, None)

# class FileManager:
#     def __init__(self, filename, mode = "r"):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#
#     def __exit__(self, exc_type, exc, tb):
#         self.file.close()
#
#         if exc_type is not None:
#             raise exc
#
# with FileManager("data.txt", "a") as f:
#     f.write("hey!")


# Контекстний менеджер для роботи з БД
# with Session() as session:
#     session.execute("SELECT * FROM users")


# копіювання великого файлу без завантаження в пам'ять
# with open('video.mp4', 'rb') as src, open('copy.mp4', 'wb') as dst:
#     while chunk := src.read(64 * 1024):      # walrus, Python 3.8+
#         dst.write(chunk)


import os
#
# if os.path.exists("data123.txt"):
#     print("Існує")
# else:
#     print("Не існує")


# print(os.path.getsize("data.txt"))
# print(os.path.getmtime("data.txt"))
# print(os.path.getctime("data.txt"))


# os.mkdir("test_folder")
# os.makedirs("test_folder2/test1", exist_ok=True)

# os.rename("data2.txt", "copy_data.txt")

# os.remove("copy_data.txt")


import shutil

# shutil.copy("data.txt", "data_copy.txt")
# shutil.rmtree("test_folder")

# for root, dirs, files in os.walk("C:\\Users\\admin\\Downloads"):
#     print(root, dirs, files)


from pathlib import Path


# p = Path("D:\\Desktop\\javarush\\group_2\\module1\\lvl18\\data.txt")
#
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.parent)
# print(p.parts)
# print(p.absolute())
# print([x for x in p.parents[1].iterdir()])

# Path('archive.tar.gz').suffixes   # ['.tar', '.gz']   всі розширення
# p.parents[1]                      # /home/user        на два рівні вгору

# Path('data') / 'sub' / 'file.txt'    # data/sub/file.txt

# p.with_suffix('.md')      # /home/user/docs/report.md
# p.with_name('new.txt')    # /home/user/docs/new.txt
# p.with_stem('final')      # /home/user/docs/final.txt

# p.write_text('привіт', encoding='utf-8')
# p.read_text(encoding='utf-8')
#
# p.write_bytes(b'\x00\x01')
# p.read_bytes()

# p.exists()      # True
# p.is_file()     # True
# p.is_dir()      # False
# p.stat().st_size
# Path.cwd()      # поточна папка
# Path.home()     # домашня

# d.iterdir()          # усе в папці (не рекурсивно)
# d.glob('*.py')       # за маскою в цій папці
# d.rglob('*.py')      # РЕКУРСИВНО по всьому дереву

# d.mkdir(parents=True, exist_ok=True)   # створити з батьками, не падати якщо є
# p.rename(new)                          # перейменувати
# p.replace(new)                         # перейменувати з перезаписом
# p.unlink(missing_ok=True)              # видалити файл
# d.rmdir()

import json

user_data = {
    'username': "bob",
    "balace": 500
}

json.dump(user_data, open("user_data.json", "w"))