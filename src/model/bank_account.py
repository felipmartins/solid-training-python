from account_info import AccountInfo
from bank_transaction import BankTransaction
# BankAccount agora tem apenas a responsabilidade de manter informações da conta bancária,
# isso foi possível através do encapsulamento que foi realizado.
# Transações bancárias são tratadas pela classe BankTransaction, além de ter 
# se tornando expansível para outras transações bancárias.

class BankAccount:
    def __init__(self, owner, balance):
        self.info = AccountInfo(owner, balance)
        self.transaction = BankTransaction()

    def get_owner(self):
        return self.info.get_owner()

    def get_balance(self):
        return self.info.get_balance()

    def deposit(self, amount):
        self.transaction.deposit(amount, self.info)

    def withdraw(self, amount):
        self.transaction.withdraw(amount, self.info)

# Sobre SOLID:
# Princípio da Responsabilidade Única: Cada classe tem apenas uma responsabilidade.
# Princípio Aberto/Fechado: Temos classes extensíveis, sem mudança de código.
# Princípio da Substituição de Liskov: À princípio, poderíamos usar qualquer objeto do tipo
# SavingAccount em lugares que esperam objetos do tipo BankAccount.
# Princípio da Segregação de Interfaces: 
# Princípio da Inversão de Dependência: A classe BankAccount depende da interface AccountInfo,
# não importando como é feita sua importação.