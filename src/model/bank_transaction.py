class BankTransaction:
    def deposit(self, amount, account_info):
        account_info.balance += amount

    def withdraw(self, amount, account_info):
        account_info.balance -= amount