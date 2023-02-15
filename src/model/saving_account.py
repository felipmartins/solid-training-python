from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float) -> None:
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.balance += interest