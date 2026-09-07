# def calculate_circle_area(radius):
#     area = 3.14 * radius * radius
#     return area
#
# print(calculate_circle_area(10))
#
# calculate_circle_area(5)
# calculate_circle_area(3)
# calculate_circle_area(2)

# a, b = (1,2)

# def check_password(password):
#     if len(password) < 8:
#         return " Занадто короткий пароль "
#     return "Пароль прийнято"
#
# print(check_password("1234"))
# print(check_password("123412341234"))

# def show_info(name, address="Невідомо"):
#     print(f"Ім'я = {name}, Адреса = {address}")
#
# show_info(
#     address="California",
#     name="Bob"
# ) # Ім'я = Bob, Адреса = California
# show_info("Alex") # Ім'я = Alex, Адреса = Невідомо

# x = "global" # Глобальна змінна
# def outer():
#     y = "outer local" # Локальна змінна зовнішньої функції
#     def inner():
#         z = "inner local" # Локальна змінна вкладеної функції
#         print(x) # Виводить "global"
#         print(y) # Виводить "outer local"
#     inner()
#     print(z) # Помилка: z не доступна в цій області видимості
#
# outer()

# sum = "hello global"

# def outer():
#     # sum = "hello outer"
#
#     def inner():
#         # sum = "hello inner"
#         print(sum)
#
#     inner()
#
# outer()


# hp = 100
#
# def increase(value):
#     global hp
#
#     hp = hp + value
#
# def decrease(value):
#     global hp
#
#     hp = hp - value
#
# print(hp)
# decrease(20)
# print(hp)
# increase(15)
# print(hp)


# counter = 0
#
# def outer():
#     counter = 0
#     def inner():
#         nonlocal counter
#
#         counter += 1


# def total(*args):
#     return sum(args)
#
# print(total(1,2,3))
# print(total(100, 200, 150, 400, -200, 100, -500, 200, 300))

#
# def introduce(name, city, job):
#     print(f"{name} з міста {city}, працює як {job}")
#
# data = ["Олег", "Львів", "дизайнер"]
# introduce(*data)   # * розпаковує список у три аргументи


# def build_button(text, **style):
#     print(f"Кнопка '{text}' зі стилями:")
#     for prop, value in style.items():
#         print(f"  {prop} = {value}")
#
#
# build_button("OK", color="green", width=100, rounded=True)


# def create_profile(name, age, job):
#     print(f"{name}, {age} р., {job}")
#
# user_data = {"name": "Ірина", "age": 28, "job": "аналітик"}
# create_profile(**user_data)

# def apply_discount(price: float, percent: int) -> float:
#     return price * (1 - percent / 100)
#
#
# def shout(text: str) -> str:
#     return text.upper()
#
#
# shouted_text = shout("hello")

# def test(a: int, b: int,c: int):
#     print(a, b, c)
#
# test(c = "5", b = 3, a = 5)


# ЗАДАЧА 1

# def is_even(num: int) -> bool:
#     return num % 2 == 0
#
# print(is_even(5))
# print(is_even(10))

# ЗАДАЧА 2

# def greet_user(name: str, language: str = "ua") -> None:
#     if language == "ua":
#         print(f"Привіт, {name}")
#     elif language == "en":
#         print(f"Hello, {name}")
#     elif language == "es":
#         print(f"Hola, {name}")
#     else:
#         print(f"Hello, {name}. I don't know this language")
#
#
#
# greet_user("Nazar", "es")
# greet_user("Bob", "ua")
# greet_user("Yura")
# greet_user("Alex", "fr")


# ЗАДАЧА 3

def find_max(*numbers: float|int) -> float|int:
    return max(numbers) if numbers else 0


print(find_max(1,2,3,4,5,6,7,8,9))
print(find_max(100, 200, 150, 500, -100, 20, 0))
print(find_max())