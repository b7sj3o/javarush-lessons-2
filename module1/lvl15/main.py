
# УСПАДКУВАННЯ

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def greet(self):
#         return f"Привіт, {self.name}"
#
#     def __str__(self):
#         return f"{type(self).__name__}({self.name})"
#
# class Admin(User):
#     def __init__(self, name, email, access_level):
#         super().__init__(name, email)
#
#         self.access_level = access_level
#
# a = Admin("Оксана", "ok@mail.com", 4)
# print(a.greet())
# print(a)
#
#
# class Logger:
#     def __init__(self):
#         self.records = []
#
#     def log(self, msg):
#         self.records.append(msg)
#         print(f"[LOG] {msg}")
#
# class TimestampLogger(Logger):
#     """РОЗШИРЮЄ: додає своє і викликає батьківське"""
#
#     # "hello" -> "[12:30] hello"
#     def log(self, msg):
#         super().log(f"[12:30] {msg}")
#
# class SilentLogger(Logger):
#     """ПЕРЕВИЗНАЧАЄ: батьківське не викликається взагалі"""
#     def log(self, msg):
#         self.records.append(msg)
#
# class PlainLogger(Logger):
#     """УСПАДКОВУЄ: нічого не робить, бере як є"""
#     pass
#
# t = TimestampLogger(); t.log("старт"); print(t.records)
# s = SilentLogger();    s.log("тихо");  print(s.records)


# ПОЛІМОРФІЗМ

# class Cat:
#     def make_sound(self): return "Мяу"
#
# class Dog:
#     def make_sound(self): return "Гав"
#
# class Robot:
#     def beep(self): return "Біп"
#
#
# def process(obj):
#     print(dir(obj))
#     if hasattr(obj, "make_sound"):
#         print(obj.make_sound())
#     else:
#         print(f"{type(obj).__name__} не вміє говорити")
#
# for o in [Cat(), Dog(), Robot()]:
#     process(o)

# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         raise NotImplementedError(f"{type(self).__name__} мусить визначити area()")
#
#     def __str__(self):
#         return f"{self.name}: {self.area():.2f}"
#
# class Circle(Shape):
#     def __init__(self, r):
#         super().__init__("Коло")
#         self.r = r
#     def area(self):
#         return 3.14159 * self.r ** 2
#
# class Rect(Shape):
#     def __init__(self, w, h):
#         super().__init__("Прямокутник")
#         self.w, self.h = w, h
#     def area(self):
#         return self.w * self.h
#
# class Square(Rect):                  # успадкування на два поверхи
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.name = "Квадрат"

# shapes = [Circle(3), Rect(4, 5), Square(6)]
# for s in sorted(shapes, key=lambda x: x.area()):
#     print(s)
# print("Сума:", round(sum(s.area() for s in shapes), 2))


# print(isinstance(Square(2), Rect)) # True - Square прямий наслідник / Rect прямий батько
# print(isinstance(Square(2), Shape)) # True - через два батька
# print(isinstance(Rect(2, 3), Square)) # False - Rect є батьком Square, а не наоборот
# print(type(Square(2)) == Rect) # False


# Mixins

# class LoggerMixin:
#     def render(self):
#         print("LOG: рендеримо сторінку")
#         return super().render()
#
# class Page:
#     def render(self):
#         return "<html>вміст</html>"
#
#
# class LoggablePage(LoggerMixin, Page):
#     pass
#
# print(LoggablePage.mro())


# class A: pass
# class B(A): pass
# class C(A): pass
# class D(B, C): pass

# print(D.mro())


# class Base:
#     def __init__(self):
#         print("Base.__init__")
#
# class Left(Base):
#     def __init__(self):
#         print("Left.__init__ ->")
#         super().__init__()
#
# class Right(Base):
#     def __init__(self):
#         print("Right.__init__ ->")
#         super().__init__()
#
# class Bottom(Left, Right):
#     def __init__(self):
#         print("Bottom.__init__ ->")
#         super().__init__()

# Bottom()
# print(Bottom.mro())


# Класові атрибути спільні для різних об'єктів
# class Team:
#     members = []
#     MAX_TEAM_AMOUNT = 11
#
#     def add(self, name):
#         if len(self.members) < self.MAX_TEAM_AMOUNT:
#             self.members.append(name)
#
# a, b = Team(), Team()
# a.add("Ігор")
# print(b.members)


# class Cart:
#     def __init__(self, items=None):      # ← міна
#         if items is None:
#             items = []
#         self.items = items
#     def add(self, x):
#         self.items.append(x)
#
# a, b = Cart(), Cart()
# a.add("кава")
# print(b.items)


# class Counter:
#     total = 0
#     def bump(self):
#         Counter.total += 1
#
#
# c1, c2 = Counter(), Counter()
#
# c1.bump()
# c1.bump()
# c1.bump()
# print(c1.total)
#
# c2.bump()
# c2.bump()
# print(c2.total)
#
# print(Counter.total)


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
# pt = Point(1, 2)
# pt.y = 10
#
# print(pt.x, pt.y)


# class Money:
#     def __init__(self, amount):
#         self.amount = amount
#
#
#     def __eq__(self, other: "Money"):
#         return self.amount == other.amount
#
# print(Money(100) == Money(100))


class Date:
    def __init__(self, d, m, y):
        self.d, self.m, self.y = d, m, y

    @classmethod
    def from_string(cls, text):
        parts = text.split(".")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __repr__(self):
        return f"Date({self.d}, {self.m}, {self.y})"

print(Date.from_string("15.03.2024"))    # Date(15, 3, 2024)
print(Date.is_leap(2024), Date.is_leap(1900))    # True False

