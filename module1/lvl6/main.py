my_set = {1,1,2,3,3,4, "hello", "hello2", "hello"}

# print(my_set)

user = {
    "name": "Bob",
    "age": 20,
    "gender": "Male"
}

# print(user1)

# print(type("hello"))
# print(type(1))
# print(type(3.14))
# print(type([1,2,3]))
# print(type(my_set))
# print(type(user))
# print(type(b"hello"))

num1 = "123"
num2 = "123.45"
num3 = 123.45

# print(int(num1)) # 123
# print(int(num2)) # ValueError, не можемо перетворити
# print(float(num2)) # 123.45
# print(int(num3)) # 123

# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(1231231)) # True
# print(bool(-1231231)) # True
# print(bool("")) # False
# print(bool([])) # False
# print(bool({})) # False

# lst = []
# if lst: ... # Якщо список пустий - Умова не пройде

lst = [1, 2 ,5 ,2, 1, 1]

# print(len(set(lst)))
# coords = (1, 2)
# print(id(coords))
# coords = (3,4)
# print(id(coords))


# user_input = input("Введіть своє ім'я: ")

# print(f"Вас звати: {user_input or "Невідомо"}")

# # if not user_input:
# #     print("Ви не ввели своє ім'я")
# # else:
#     print(f"Вас звати: {user_input}")

# a = [1,2,3]
# b = a
# print(id(a))
# print(id(b))
#
# b.append(4)
# b.remove(4)
# b[0] = 100
# print(id(b))
#
#
# num = 123
# print(id(num))
# num = 456
# print(id(num))

user_age = int(input("Enter your age: "))

message = None

if user_age >= 18:
    message = "Привіт, ти маєш доступ"

if message is None:
    print("123")