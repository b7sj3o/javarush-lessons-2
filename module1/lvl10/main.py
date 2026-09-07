# my_set = {1, 2, 3}
from ctypes.macholib.framework import framework_info

# for i in my_set:
#     print(i)

# my_set.add(4)
#
# print(my_set)
# print(my_set[0]) # TypeError: 'set' object is not subscriptable

# my_set.remove(5) # KeyError: 5
# my_set.discard(5) # Помилки не буде

# my_set.discard(4)

# print(my_set)

# while my_set:
#     print(my_set.pop())

# my_set.clear()
# print(my_set)
#
# my_set.update([1,2,3], {4,5,6}, (7,8,9))
#
# print(my_set)

friends_anna = {"Олег", "Марія", "Іван", "Софія"}
friends_petro = {"Іван", "Софія", "Богдан", "Олег"}


# Спільні друзі (перетин)
# print(friends_anna.intersection(friends_petro))   # {'Олег', 'Іван', 'Софія'}
# print(friends_petro & friends_anna)

# "Можливо ви знайомі" — друзі Петра, яких немає в Анни (різниця)
# print(friends_petro.difference(friends_anna))   # {'Богдан'}
# print(friends_petro - friends_anna)

# Усі люди разом
# print(friends_petro.union(friends_anna))
# print(friends_petro | friends_anna)


order_before = {"хліб", "молоко", "яйця", "сир"}
order_after = {"молоко", "яйця", "масло", "сир"}

# print(order_before.symmetric_difference(order_after))
# print(order_before ^ order_after)

# all_students = {"Іван", "Олена", "Петро", "Катя", "Макс"}
# submitted = {"Олена", "Макс"}

# not_submitted = all_students.difference(submitted)
# print(f"Не здали ДЗ: {not_submitted}")   # {'Іван', 'Петро', 'Катя'}


passed_hr = {"Іван", "Марія", "Олег", "Софія"}
passed_tech = {"Марія", "Олег", "Богдан"}
passed_final = {"Олег", "Марія", "Ліза"}

# Хто пройшов усі три етапи?
# hired = passed_hr.intersection(passed_tech, passed_final)
# print(hired)   # {'Марія', 'Олег'}

# >>> [x * 2 for x in range(1, 11)]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# >>> {x * 2 for x in range(1 ,11)}
# {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# print({1,2,3} <= {1,2,3,4,5})

# a = {1,2,3}
# b = a
# b.add(4)
#
# print(a,b)
#
# print(sorted({1,2,3,4,5})) # ПОВЕРНЕ list

txt = 'hello hel world'

# print("world" in txt) # True
# print("World" in txt) # False

# print(txt.count("hel")) # 2

# print(txt.index("W")) # ValueError
# print(txt.find("W"))  # -1 - не знайдено

# def is_palindrome(txt: str) -> bool:
#     return txt == txt[::-1]

# print(is_palindrome("радар"))
# print(is_palindrome("привіт"))
# print(is_palindrome("lalal"))


# products = input("Введіть список покупок через кому: ").split(",")
# products = [x.strip() for x in products] # прибрали зайві пробіли
#
# for product in products:
#     printfproduct)

# url_parts = ["users", "42", "orders"]
# mywebsite.com/users/42/orders

# path = "/".join(url_parts)
# print("mywebsite.com/" + path)

# Завдання 1
# text = "кіт кіт собака Кіт птах собака КІТ"
#
# words = text.lower().split()
# unique_words = set(words)
#
# print(f"Всього слів: {len(words)}")
# print(f"Унікальних слів: {len(unique_words)}")

# word = "sit amet nisi eget, ornare vehicula neque. Nullam accumsan elementum elit. Vivamus blandit dui est, in imperdiet sem dictum nec. Vivamus eget dui sapien. Ut ac blandit ligula, vel gravida sapien. Suspendisse potenti. Morbi iaculis pharetra diam nec rutrum. Suspendisse potenti. Nulla vitae nisi odio. Praesent tempor vel lacus vitae maximus."
#
# print(f"К-сть символів в тексті: {len(set(word.lower()))}")

# digits = set("0123456789")
# special = set("!@#$%^&*()")
#
# def check_password(password: str) -> bool:
#     has_digit = not digits.isdisjoint(password)
#     has_special = not special.isdisjoint(password)
#
#     if len(password) < 8:
#         return False
#
#     return has_digit and has_special
#
# print(check_password("123456"))
# print(check_password("HelloWorld123"))
# print(check_password("Hello@123"))
# print(check_password("Hey@1"))

# 13. Знайти анаграми (★ СКЛАДНО)
# Дано список слів. Згрупуй ті, що є анаграмами (складаються з однакових букв). Підказка: множина букв — швидкий спосіб порівняти.

words = ["кіт", "тік", "сон", "нос", "рот"]
# "кіт" і "тік" — однакові букви
# "сон" і "нос" — однакові букви

result = []
pair = []

while words:
    current_word = words.pop(0)
    set_word = set(current_word)
    pair.append(current_word)

    for word in words.copy():
        if set_word == set(word):
            pair.append(word)
            words.remove(word)

    if len(pair) > 1:
        result.append(tuple(pair))

    pair.clear()


print(result)



