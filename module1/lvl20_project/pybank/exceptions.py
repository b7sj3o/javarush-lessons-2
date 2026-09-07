class BankError(Exception):
    """Кореневий вийняток Pybank"""


class AccountError(BankError):
    ...


class OperationError(BankError):
    ...


class StorageError(BankError):
    ...



class AccountNotFound(AccountError):
    def __init__(self, acc_number):
        super().__init__(f"Рахунок {acc_number} не знайдено")


class AccountBlocked(AccountError):
    def __init__(self, acc_number):
        super().__init__(f"Рахунок {acc_number} заблоковано")


class InvalidAmount(OperationError):
    def __init__(self, amount):
        super().__init__(f"некоректна сума: {amount!r}")


class InsufficientFunds(OperationError):
    def __init__(self, acc_number, amount, required):
        super().__init__(f"на {acc_number} бракує {required-amount:.2f} грн "
                         f"(доступно {amount:.2f} грн, потрібно {required:.2f} грн)")



class LimitExceeded(OperationError):
    def __init__(self,  amount, limit):
        super().__init__(f"Переказ на суму {amount:.2f} грн перевищує ліміт {limit:.2f} грн")
