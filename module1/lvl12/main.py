# def price_with_tax(price: float, tax_rate: float = 0.2) -> float:
#     if price < 0:
#         raise ValueError("Price cannot be negative")
#     if not (1 >= tax_rate > 0):
#         raise ValueError("Tax rate cannot be greater than 0")
#
#     return price + price * tax_rate
#
# print(price_with_tax(100, 0.3))
# print(price_with_tax(150, 0.1))
# print(price_with_tax(600))

#
# def add(a, b):
#     return a+b
#
# add_lambda = lambda a,b: a+b
#
# print(add(5, 10))
# print(add_lambda(5, 10))


# ===== MAP =====
# user_input = input("Введіть числа через пробіл: ").split()
#
# numbers = sum(map(int, user_input))
#
# print(numbers)


# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x ** 2, numbers)
# print(list(squared_numbers)) # Виведення: [1, 4, 9, 16, 25]
#
# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers)) # Виведення: [2, 4]

# words = ["banana", "apple", "cherry", "date"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words) # Виведення: ['date', 'apple', 'banana', 'cherry']

# numbers = [1, 2, 3, 4, 5]
#
# # map/filter
# result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
#
# # comprehension — те саме, але читабельніше (так пишуть частіше)
# result = [x ** 2 for x in numbers if x % 2 == 0]
# print(result)   # [4, 16]


# ======= SORTED =======

users = [
    {"name": "Оля", "age": 25, "salary": 30000},
    {"name": "Тарас", "age": 19, "salary": 45000},
    {"name": "Ніна", "age": 31, "salary": 28000},
    {"name": "Олег", "age": 31, "salary": 25000},
]

# by_age = sorted(users, key=lambda u: u["age"])
# for user in by_age:
#     print(f'{user["name"]}: {user["age"]}, Зарплата: {user["salary"]}')

#
# by_salary = sorted(users, key=lambda u: u["salary"], reverse=True)
# for user in by_salary:
#     print(f'{user["name"]}: {user["age"]}, Зарплата: {user["salary"]}')


# by_both = sorted(users, key=lambda u: (u["age"], u["salary"]))
# for user in by_both:
#     print(f'{user["name"]}: {user["age"]}, Зарплата: {user["salary"]}')


# ============= ЗАМИКАННЯ =============

# def make_multiplier(n):
#     def multiplier(x):
#         return x * n      # n "запам'яталось" усередині
#     return multiplier
#
#
# double = make_multiplier(2)
# triple = make_multiplier(3)
#
# print(double(5))
# print(triple(10))
# print(triple(50))


# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count      # дозволяє змінювати зовнішню змінну
#         count += 1
#         return count
#
#     return counter
#
# click = make_counter()
#
# print(click())
# print(click())
# print(click())

# def make_tax_calculator(rate):
#     def calculate(amount):
#         return round(amount * (1 + rate), 2)
#     return calculate
#
# ua_tax = make_tax_calculator(0.20)
# pl_tax = make_tax_calculator(0.23)
#
# print(ua_tax(1000))   # 1200.0
# print(pl_tax(1000))   # 1230.0


# def logger(func):
#     def wrapper(*args):
#         print(f"Викликаю {func.__name__} з {args}")
#         result = func(*args)
#         print(f"Результат: {result}")
#         return result
#     return wrapper
#
# @logger
# def add(a, b):
#     return a + b


# def fibonacci():
#     a, b = 0, 1
#
#     while True:
#         yield a
#         a, b = b, a+b
#
#
# fib = fibonacci()
#
# for _ in range(10):
#     print(next(fib), end=" ")


# def natural_numbers(n):
#     counter = 0
#
#     while counter < n:
#         yield counter
#         counter += 1
#
#
#
# for i in natural_numbers(5):
#     print(i)


# def id_generator(prefix="ORD"):
#     n = 1
#     while True:
#         yield f"{prefix}-{n:05d}"
#         n += 1
#
# orders = id_generator()
# print(next(orders))   # ORD-00001
# print(next(orders))   # ORD-00002
# print(next(orders))   # ORD-00003


# numbers = (x for x in range(1, 1_000_000_000_000_000_000))
# evens = (x for x in numbers if x % 2 == 0)
# squares = (x ** 2 for x in evens)
#
# print(next(squares))
# print(next(squares))


# def generator1():
#     yield from range(3)
#     yield from "ABC"
#
# for value in generator1():
#     print(value)

# def flatten(items):
#     for item in items:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item
#
#
# nested = [1, [ 2, [ 3 ] ], 4]
# print(list(flatten(nested)))