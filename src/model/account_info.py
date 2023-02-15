class AccountInfo:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def get_owner(self):
        return self.owner

    def get_balance(self):
        return self.balance