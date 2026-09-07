

user = {
    "username": "Bob",
    "age": None,
    "wins": 5,
    "loses": 3,
    (1,2): True
}

print(user[(1,2)])

# user.setdefault("age", 30)

# try:
#     user['age']
# except KeyError:
#     user["age"] = 30

# print(user)

# empty_dict = {}

# print(user)
# print(type(user))

# keys = ["name", "age", "city"]
# default_value = None
# person = dict.fromkeys(keys, default_value)
# print(person)

# print(user.get("age", 0.00))
# print(user["wins"])
# print(user["sawasw"]) # рейзить KeyError, якщо ключа немає в словнику

# print(user.keys())
# print(user.values())
# print(list(user.items()))
#
# for key, value in user.items():
#     print(f"Ключ {key} має значення {value}")

# print(user.popitem())
# print(user.pop("age"))
# print(user) # -> age немає

# additional_user_data = {
#     "height": 165,
#     "weight": 80,
# }
#
# user.update(additional_user_data)
#
# print(user)

# text = "кіт пес кіт кіт пес"
# counts = {}
# for word in text.split():
    # if word in counts:
    #     counts[word] += 1
    # else:
    #     counts[word] = 1

#     counts[word] = counts.get(word, 0) + 1
#
# print(counts)

# person = {"name": "Alice", "age": 25}
#
# keys = person.keys()
# print(keys) # dict_keys(['name', 'age'])

# Додавання нового елемента
# person["city"] = "New York"
# print(keys) # dict_keys(['name', 'age', 'city'])
#
# print(keys[0])

# new_dct = {
#     "1": "4",
#     "2": "5",
#     "3": "6",
# }

# print("4" in new_dct)
# print("3" in new_dct)

# students = ["Оля", "Тарас", "Ніна"]
# dct = dict.fromkeys(students, False)

# students = [("Оля", "Київ"), ("Тарас", "Львів"), ("Ніна", "Київ")]
# by_city = {}
#
# for name, city in students:
#     by_city.setdefault(city, []).append(name)
#
# print(by_city)

# user = {
#     "username": "Bob",
#     "age": None,
#     "wins": 5,
#     "loses": 3,
# }
#
# while user:
#     print(user.popitem())

# en_to_ua = {"cat": "кіт", "dog": "пес"}
# ua_to_en = {v: k for k,v in en_to_ua.items()}

# print(ua_to_en)

data = ["name:Alice", "age:25", "city:New York"]
person = {item.split(":")[0]:item.split(":")[1] for item in data}

print(person)