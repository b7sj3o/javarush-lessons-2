
# users = [1,1,2,2,2,3,3,1,5,7,8]

# users.append(4)
# users.append(5)
#
# users.extend([1,2,3])
#
# users.insert(3, 6)

# users.remove(6) # Видалення по значенню
# users.pop(3) # Видалення по індексу
# users.clear()

# print(users.count(1))
#
# print(users)


# users = [6,2,5,1,8,5,3,5,2,87,12,51]
#
# users.sort(reverse=True)
#
# sorted_users = sorted(users, reverse=True)
#
# print(users)

# numbers = [1,2,3]
#
# numbers.reverse()
#
# reversed_numbers = reversed(numbers)
#
# print(numbers)

# numbers = [1,2,3, True]
#
# print(sorted(numbers))

# my_lst = [1,2,6, "hello", True, 5, [1,2,3], 5.3]
# suma = 0
#
# for i in my_lst:
#     if type(i) in [int, float]:
#         suma += i
#
# print(f"Сума: {suma}")


lst = [1,2,3,4,5,6,7,8,9,10]

# print(lst[0]) => 1
# print(lst[4]) => 5
# print(lst[7]) => 8

# lst[start:stop:step]
# print(lst[3::2]) => [4,6,8,10]
# print(lst[1:8:3]) => [2,5,8]

# fruits = ["яблуко", "банан", "вишня", "апельсин", "ківі"]
#           0         1        2         3          4
#          -5        -4       -3        -2         -1

# print(fruits[0])    # яблуко   (перший)
# print(fruits[2])    # вишня    (третій)
# print(fruits[-1])   # ківі     (останній)
# print(fruits[-2])   # апельсин (передостанній)

# print(fruits[::-1]) => Обертаємо задом наперед

# queue = ["Аня", "Богдан", "Віка"]
# queue.insert(0, "VIP")       # на початок
# print(queue)   # ['VIP', 'Аня', 'Богдан', 'Віка']


# fruits = ["яблуко", "банан", "вишня", "апельсин", "ківі"]

# fruits[2] = "вишні"
# fruits[2:4] = [1,2, 3, 4]

# while fruits:
#     fruit = fruits.pop(0)
#     print(fruit)

# for fruit in fruits:
#     print(fruit)

# my_list = ['a', 'b', 'c', 'd']
#
# for i in range(len(my_list)):
#     print(f'Index: {i}, Element: {my_list[i]}')
# print()
# for index, value in enumerate(my_list):
#     print(f'Index: {index}, Element: {value}')

# n = int(input("Enter N: "))

# Варіант 1
# squares = []
# for i in range(1, n+1):
#     squares.append(i**2)

# Варіант 2 (List Comprehension)
# squares = [i**2 for i in range(1, n+1)]


# З умовою (фільтр)
# nums = [1, 2, 3, 4, 5, 6]
# evens = [x for x in nums if x % 2 == 0]   # [2, 4, 6]

# Перетворення
# words = ["hello", "world"]
# upper = [w.upper() for w in words]        # ['HELLO', 'WORLD']
# lengths = [len(w) for w in words]         # [5, 5]

# labels = ["парне" if x % 2 == 0 else "непарне" for x in range(4)]

alist = ["banana", "Oranges", "Kiwi", "cherry"]
alist.sort()
print(alist)

numbers = [1, -1, 2, -2, 3, -3]
# Створюємо копію списку для безпечної ітерації
for number in numbers:
    if number < 0:
        numbers.remove(number)

print(numbers) # Виведе [1, 2, 3]