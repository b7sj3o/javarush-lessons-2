from pybank.accounts import Account
from pybank.exceptions import AccountNotFound, LimitExceeded, BankError
from pybank.transactions import TransactionLog, Transaction
from pybank.utils import log_operation

TRANSFER_LIMIT = 50000


class Bank:
    def __init__(self, name):
        self.name = name
        self._accounts: list["Account"] = []
        self.log = TransactionLog()


    def open_account(self, account):
        self._accounts.append(account)
        return account


    def find_account(self, acc_number):
        for account in self._accounts:
            if account.acc_number == acc_number:
                return account
        raise AccountNotFound(acc_number)

    @property
    def total(self):
        return round(sum(acc.balance for acc in self._accounts), 2)
    
    @log_operation
    def withdraw(self, acc_number, amount):
        account = self.find_account(acc_number)
        new_balance = account.withdraw(amount)
        self.log.add(Transaction("WITHDRAW", amount, account))
        return new_balance


    @log_operation
    def deposit(self, acc_number, amount):
        account = self.find_account(acc_number)
        new_balance = account.deposit(amount)
        self.log.add(Transaction("DEPOSIT", amount, account))
        return new_balance


    @log_operation
    def transfer(self, source, target, amount):
        if amount > TRANSFER_LIMIT:
            raise LimitExceeded(amount, TRANSFER_LIMIT)

        source_account = self.find_account(source)
        target_account = self.find_account(target)

        source_account.withdraw(amount)
        try:
            target_account.deposit(amount)
        except BankError:
            source_account.deposit(amount)
            raise

        self.log.add(Transaction("TRANSFER", amount, source, target))
        return amount


    def __len__(self):
        return len(self._accounts)


    def __iter__(self):
        return iter(self._accounts)

    def __contains__(self, item):
        if isinstance(item, Account):
            acc_number = item.acc_number
        else:
            acc_number = item

        for account in self._accounts:
            if account.acc_number == acc_number:
                return True

        return False


    def __getitem__(self, acc_number):
        return self.find_account(acc_number)

    def __repr__(self):
        return f"Bank('{self.name}', рахунків: {len(self)})"



# bank = Bank("Mono")

#
# account1 = Account("Bob", 5000)
# account2 = Account("Alex", 5000)
#
# bank.open_account(account1)
# bank.open_account(account2)
#
# for account in bank:
#     print(account)