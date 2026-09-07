class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} is meow.")


    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


    def __repr__(self) -> str:
        return f"Cat(name={self.name}, age={self.age})"




barsik = Cat("Barsik", 18)
murzik = Cat("Murzik", 5)

# print(barsik.__dict__)
# barsik.color = "white"
# print(barsik.__dict__)

# barsik.meow()
# murzik.meow()

# print(repr(barsik))
# print(murzik.__repr__())


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner          # публічний — читай/міняй вільно
#         self._balance = balance     # "не чіпай" — домовленість
#         self.__pin = "1234"         # name mangling
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Сума має бути додатною")
#         self._balance += amount
#
#     def get_balance(self):
#         return self._balance
#
# acc = BankAccount("Віталій", 1000)
# acc.deposit(500)
# print(acc.get_balance())
# acc.deposit(-100000)

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price        # тут уже спрацює сетер!
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Ціна не може бути від'ємною")
#         self._price = value
#
# p = Product("Кава", 120)
# p.price = 150      # виглядає як звичайне присвоєння
# print(p.price)     # 150
# p.price = -50      # ValueError: Ціна не може бути від'ємною



# ❌ ДО: дублювання
# class Developer:
#     def __init__(self, name, salary): self.name, self.salary = name, salary
#     def info(self): return f"{self.name}, зп {self.salary} грн"
#
# class Manager:
#     def __init__(self, name, salary): self.name, self.salary = name, salary
#     def info(self): return f"{self.name}, зп {self.salary} грн"   # copy-paste


class Employee:                              # батьківський / базовий клас
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f"{self.name}, зп {self.salary} грн"

    def work(self):
        return f"{self.name} працює"


class Developer(Employee):                   # дочірній клас
    def __init__(self, name, salary, language):
        super().__init__(name, salary)       # ← викликаємо батьківський __init__
        self.language = language             # і додаємо своє

    def work(self):                          # ← перевизначення (override)
        return f"{self.name} пише код на {self.language}"


class Manager(Employee):
    def work(self):
        return f"{self.name} проводить зустріч"


# d = Developer("Оля", 60000, "Python")
# m = Manager("Дмитро", 20000)
# print(m.work())
# print(d.info())    # Оля, зп 60000 грн     ← метод дістався у спадок
# print(d.work())    # Оля пише код на Python ← а цей перевизначено


# ПОЛІМОРФІЗМ
# employees = [
#     Developer("Оля", 60000, "Python"),
#     Manager("Ігор", 70000),
#     Employee("Петро", 30000),
# ]
#
# for emp in employees:
#     print(emp.work())

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self): ...
#
#     def describe(self):
#         return f"{type(self).__name__}: площа {self.area():.2f}"
#
# class Circle(Shape):
#     def __init__(self, r): self.r = r
#     def area(self): return 3.14159 * self.r ** 2
#
# class Rect(Shape):
#     def __init__(self, w, h): self.w, self.h = w, h
#     def area(self): return self.w * self.h
#
# for s in (Circle(2), Rect(3, 4)):
#     print(s.describe())

import random

class Card:
    def __init__(self, rank, suit):
        self.rank, self.suit = rank, suit
    def __str__(self):  return f"{self.rank}{self.suit}"
    def __repr__(self): return str(self)      # щоб гарно виглядало у списку

    def is_black(self):
        return self.suit in ["♠","♣"]

class Deck:
    RANKS = ["6","7","8","9","10","J","Q","K","A"]     # атрибути КЛАСУ
    SUITS = ["♠","♥","♦","♣"]

    def __init__(self):
        self.cards = [Card(r, s) for s in self.SUITS for r in self.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        hand, self.cards = self.cards[:n], self.cards[n:]
        return hand

    def __len__(self):
        return len(self.cards)


deck = Deck()
print("Карт у колоді:", len(deck))    # 36
deck.shuffle()
print("Рука гравця:", deck.deal(6))   # [J♥, 8♥, J♠, 10♦, 6♥, 8♣]
print("Лишилось:", len(deck))         # 30
print("Рука гравця:", deck.deal(6))   # [J♥, 8♥, J♠, 10♦, 6♥, 8♣]
