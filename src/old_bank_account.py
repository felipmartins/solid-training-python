# a classe BankAccount não encapsula adequadamente seus atributos 
# também não segue o princípio de responsabilidade única, 
# ou seja, ela tem métodos que vão além de suas responsabilidades.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def get_owner(self):
        return self.owner

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount