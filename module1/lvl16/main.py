# def calculate_user_age():
#     while True:
#         try:
#             age = int(input("введіть ваш рік народження: "))
#             print(f"{2026/age}")
#             print(f"Вам {2026-age} років")
#             return 2026-age
#         except ValueError:
#             print("Введіть валідне число")
#         except ZeroDivisionError:
#             print("Ви не могли народитись у 0-ву році!")
#         finally:
#             print("finally")

#
#
#
# calculate_user_age()


# try:
#     print("try")
#     1 / 0
# except ZeroDivisionError:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")


# def f():
#     try:
#         return "try"
#     finally:
#         return "finally"
#
# print(f())

# try:
#     f = open("нема.txt")
#     data = f.read()
# finally:
#     f.close()


# Практичні кейси

# conn = db.connect()
# try:
#     cursor = conn.cursor()
#     cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
#     conn.commit()
# except Exception:
#     conn.rollback()
#     raise
# finally:
#     conn.close()

# import os, tempfile
#
# path = tempfile.mktemp()
# try:
#     with open(path, "w", encoding="utf-8") as f:
#         f.write("тимчасові дані")
#     process(path)
# finally:
#     if os.path.exists(path):
#         os.remove(path)


# import time
#
# def handle_request(req):
#     start = time.perf_counter()
#     try:
#         return process(req)
#     finally:
#         elapsed = time.perf_counter() - start
#         metrics.record("request_duration", elapsed)


# while True:
#     try:
#         age = int(input("Вік: "))
#     except ValueError as e:
#         print(f"Введіть ціле число: {e}")
#         continue
#     if 0 < age < 130:
#         break
#     print("Вік поза межами розумного")
# print(f"Прийнято: {age}")


# import traceback
#
#
# def divide(x, y):
#     return x / y
#
#
# def calculate():
#     result = divide(10, 0)
#     return result
#
# try:
#     calculate()
# except ZeroDivisionError:
#     print("Сталася помилка: ділення на нуль!")
#     traceback.print_exc()



# class InvalidPasswordError(Exception):
#     pass
#
#
# our_password = "hello123"
#
# def check_password(password: str):
#     if password == our_password:
#         print("Доступ дозволено")
#         return True
#     raise InvalidPasswordError("Неправильний пароль")
#
#
# try:
#     check_password("hello")
# except InvalidPasswordError as e:
#     print(f"Помилка: {e}")



# class ConfigError(Exception):
#     """Помилка конфігурації застосунку."""
#
# def load_port(raw: str) -> int:
#     try:
#         return int(raw)
#     except ValueError as e:
#         raise ConfigError(f"PORT має бути числом, отримано {raw!r}") from e
#
# load_port("вісімдесят")

#
# import json, urllib.request, urllib.error
#
# def get_rate(currency: str) -> float:
#     url = f"https://api.example.com/rate/{currency}"
#     try:
#         with urllib.request.urlopen(url, timeout=5) as r:
#             return json.loads(r.read())["rate"]
#     except urllib.error.HTTPError as e:
#         raise RuntimeError(f"API повернуло {e.code}") from e
#     except (urllib.error.URLError, TimeoutError) as e:
#         raise RuntimeError("Немає зв'язку з API") from e
#     except (KeyError, json.JSONDecodeError) as e:
#         raise RuntimeError("API повернуло несподіваний формат") from e
#
# get_rate("uah")


class AppError(Exception):
    pass



class BankError(AppError):
    pass


class TransactionError(BankError):
    pass


class InsufficientBalanceError(TransactionError):
    def __init__(self, balance, transaction_amount):
        self.balance = balance
        self.transaction_amount = transaction_amount
        message = f"Недостатньо коштів ({balance} грн) при переказі на суму {transaction_amount} грн. Не вистачає {transaction_amount - balance} грн"
        super().__init__(message)


class SelfTransactionError(TransactionError):
    def __init__(self):
        super().__init__("Ви не можете переказати гроші самому собі")

users: list["User"] = []

class User:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.__balance = balance

        users.append(self)


    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def transfer(self, name, transaction_amount):
        if name == self.name:
            raise SelfTransactionError()
        if transaction_amount > self.__balance:
            raise InsufficientBalanceError(self.__balance, transaction_amount)

        if user := next(u for u in users if u.name == name):
            self.__balance -= transaction_amount
            user.__balance += transaction_amount

    def __str__(self):
        return self.name

user1 = User("Bob", 2000)
user2 = User("Yura", 10)

try:
    user1.transfer(user2.name, 3000)
except InsufficientBalanceError:
    print("Недостатньо коштів")

print(user1.balance)
print(user2.balance)
