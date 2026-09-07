import time
import functools
import requests

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Функція була викликана")
#         result = func(*args, **kwargs)
#         print(f"Результат: {result}")
#         return result
#     return wrapper
#
#
# @log_decorator
# def add(a, b):
#     print("Функція була викликана")
#     return a+b


# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         print(f"[timer] {func.__name__}: {time.perf_counter() - start:.4f} c")
#         return result
#     return wrapper
#
# @timer
# def slow_sum(n):
#     return sum(i * i for i in range(n))
#
# print(slow_sum(1_000_000))


# def logger(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         parts = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
#         print(f"-> {func.__name__}({', '.join(parts)})")
#         result = func(*args, **kwargs)
#         print(f"<- {result!r}")
#         return result
#     return wrapper
#
# @logger
# def divide(a, b=1):
#     return a / b
#
# divide(10, b=4)
# divide(15, b=1)
# divide(12, b=3)


# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             return [func(*args, **kwargs) for _ in range(times)]
#         return wrapper
#     return decorator
#
# @repeat(5)
# def roll_dice():
#     import random
#     return random.randint(1, 6)
#
# print(roll_dice())


# def retry(times=3, delay=1.0, exceptions=(Exception,)):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for attempt in range(1, times + 1):
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as e:
#                     print(f"  спроба {attempt}/{times} впала: {e}")
#                     if attempt == times:
#                         raise
#                     time.sleep(delay)
#         return wrapper
#     return decorator
#
# @retry(times=3, delay=0.5, exceptions=(ConnectionError,))
# def fetch_data(username: str):
#     url = f"https://api.github.com/users/{username}"
#
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         user_data = response.json()
#
#         # Print selected information
#         print(f"Name: {user_data.get('name')}")
#         print(f"Bio: {user_data.get('bio')}")
#         print(f"Public Repos: {user_data.get('public_repos')}")
#         print(f"Followers: {user_data.get('followers')}")
#     elif response.status_code == 404:
#         print("User not found.")
#     else:
#         print(f"Failed to fetch data. Status code: {response.status_code}")
#
#
# fetch_data("b7sj3o")

# from functools import lru_cache
#
# @lru_cache(maxsize=None)
# def calc(n):
#     return sum(i * i for i in range(n))
#
#
# print(calc(100_000_000))
# print(calc(100_000_000))


# def bold(func):
#     def wrapper(*args, **kwargs):
#         return "<b>" + func(*args, **kwargs) + "</b>"
#     return wrapper
#
# def italic(func):
#     def wrapper(*args, **kwargs):
#         return "<i>" + func(*args, **kwargs) + "</i>"
#     return wrapper
#
# @bold
# @italic
# def greet(name):
#     return f"Привіт, {name}!"
#
# print(greet("Оля"))

#
# def decA(func):
#     print("А Проміжок")
#     def wrapper():
#         print("А до")
#         func()
#         print("А після")
#     return wrapper
#
#
# def decB(func):
#     print("B Проміжок")
#     def wrapper():
#         print("B до")
#         func()
#         print("B після")
#     return wrapper
#
# @decA
# @decB
# def func():
#     print("Сама функція")
#
# func()


# @log_action
# @require_admin
# def delete_user_A(user, target): ...
#
# @require_admin
# @log_action
# def delete_user_B(user, target): ...

# Варіант A (@log_action зверху):
#   [LOG] Петро викликав delete_user_A
#   PermissionError: Петро: доступ заборонено
#
# Варіант B (@require_admin зверху):
#   PermissionError: Петро: доступ заборонено