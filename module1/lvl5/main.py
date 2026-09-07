# name = input("Введіть ваше ім'я: ")
# age = int(input("Введіть ваш вік: "))

# print("Ваше ім'я " + name + ". Ваш вік: " + str(age))

# print(f"Ваше ім'я: {name}. Ваш вік: {age}")
# print("Ваше ім'я: {}. Ваш вік: {}".format(name, age))

# prompt = """
# Ти чат-бот
# Відповідай стисло
# Оберігайся від NSFW контенту
# ...
#
# {user_prompt}
# """
#
# prompt.format(user_prompt=prompt)

# pi = 3.14159
# print(f"Число PI={pi:.2f}") # заокруглює до 2 знаків після коми

# print("hello", 1, True, [1,2,3], sep=",", end="-")


# fruits = ["banana", "apple", "cherry", "pineapple"]
#
# for fruit in fruits:
#     print(fruit)
#
# print("Закінчено!")
# print(fruit)


# for i in range(10):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)


# n = int(input("Введіть число: "))
# result = 0
# for i in range(1, n+1):
#     result += i
# print(result)

# print(n * (n + 1) / 2)


# n = 5
#
# while n > 0:
#     print(n)
#     n -= 1

# num_to_find = 123
#
# for num in range(1, 10001):
#     if num == num_to_find:
#         print("Число знайдене!")
#         break # виходимо з циклу
#     else:
#         print(f"Число {num} не дорівнює {num_to_find}")

# users = [82, 13, 12, 62, 23, 45, 19, 83, 47, 59]
# balance = 0
# for user in users:
#     if user < 18:
#         continue
#
#     balance += 100

# if 1 == 2:
#     pass # просто заглушка, нічого не робить

# users = [82, 13, 12, 62, 23, 45, 19, 83, 47, 59]
#
# for user_age in users:
#     if user_age > 100:
#         print("Ми знайшли користувача якому більше 100 років")
#         break
# else:
#     print("У нас немає користувача з віком більше 100 років")

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i}*{j}={i*j}", end=" ")
#     print()

# nums = [1,2,3,4,5]
# target = 4

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])

# seen = set()
# for x in nums:
#     if target - x in seen:   # потрібне доповнення вже бачили?
#         pass
#     seen.add(x)


# ЗАДАЧІ

# 1

# suma = 0
#
# while True:
#     num = float(input("Введіть число (0 - щоб вийти): "))
#
#     if num == 0:
#         break
#
#     suma += num
# print(f"Сума: {suma}")

# 2
from random import randint

secret_num = randint(1, 100)

for i in range(8):
    num = int(input("Введіть число від 1 до 100: "))

    if num > secret_num:
        print("Менше")
    elif num < secret_num:
        print("Більше")
    else:
        print("Вітаю! Ви перемогли!")
        break
else:
    print(f"Ви програли. Загадане число: {secret_num}")


