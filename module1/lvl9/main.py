from itertools import chain


lst = [123, True, "string", []]
lst[0] = 321

tpl = (123, True, "string", [])
# tpl[0] = 321 # !!! ПОМИЛКА

coords = (10, 20, 30, 40, 50)
x,*y,z = coords
# print(x, y, z)

# print(coords[0], coords[2], coords[-1]) # 10 30 50

# print(coords[1:4:])

# shop_fruits = ["банан", "яблуко", "ківі", "апельсин", "мандарин", "кавун"]
# user_input = input("Введіть фрукт: ")
#
# for fruit in shop_fruits:
#     if user_input == fruit:
#         print("Фрукт є в магазині")
#         break
# else:
#     print("Фрукту немає в магазині")

# users = ("user1", "user2", "user3")
# users = list(users)
# users.append("user4")
# users = tuple(users)
# print(users)

# a = 10
# b = 15
#
# a, b = b, a
# print(a, b)


# def get_or_create():
#     return is_created, obj
#
# is_created, obj = get_or_create()

# students = [("Аня", 85), ("Іван", 40), ("Ліза", 72)]
#
# for name, grade in students:      # кожну пару одразу розпаковуємо
#     status = "склав" if grade >= 60 else "не склав"
#     print(f"{name}: {grade} — {status}")


# nested_tuple = ((1,2,3), (4,5,6), (7,8,9))
#
# for inner_tuple in nested_tuple:
#     for item in inner_tuple:
#         print(item)

# Рекурсія

#
# print(nested_tuple[1][2])

# board = [
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
# ]

# def min_max(numbers: list[int]) -> tuple[int, int]:
#     return min(numbers), max(numbers)

# leaderboard = [1500, 2000, 1200, 600, 1270, 860, 985]
# leaderboard = (100, )
#
# low, high = min_max(leaderboard)
#
# print(f"Найнижче: {low}")
# print(f"Найкраще: {high}")



flights = (
    ("Київ", 9, 2),
    ("Львів", 7, 9),
    ("Одеса", 10, 20),
)

flights = sorted(flights, key=lambda x: x[1] + x[2])

for city, time, hours in flights:
    print(f"{city}: відправлення {time} - приблизне прибуття {(time+hours)%24}")


