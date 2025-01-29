class Account(object):

    def __init__(self, number, name, balance=0):
        self.account_number = number
        self.account_holder = name
        self.balance = balance

    def get_account_type(self):
        return "Generic Account"

    def __str__(self):
        return (f"Account number: {self.account_number}\n"
                f"Account holder: {self.account_holder}\n"
                f"Account type: {self.get_account_type()}\n"
                f"Balance: {self.balance:.2f}\n"
                f"{'='*50}")

class CurrentAccount(Account):

    def __init__(self, number, name, balance=0, overdraft_limit=1000):
        super().__init__(number, name, balance)
        self.overdraft_limit = overdraft_limit

    def get_account_type(self):
        return "Current"

    def __str__(self):
        return (super().__str__() + f"\nOverdraft limit: {self.overdraft_limit}\n{'='*50}")

class SavingsAccount(Account):
    interest_rate = 5  # Fixed interest rate for savings

    def get_account_type(self):
        return "Saving"

    def __str__(self):
        return (super().__str__() + f"\nInterest rate: {self.interest_rate}\n{'='*50}")

class InvestmentAccount(Account):

    def __init__(self, number, name, balance=0, interest_rate=3.0, transaction_limit=5):
        super().__init__(number, name, balance)
        self.interest_rate = interest_rate
        self.transaction_limit = transaction_limit
        self.transaction_count = 0

    def get_account_type(self):
        return "Investment"

    def __str__(self):
        return (super().__str__() + 
                f"\nInterest rate: {self.interest_rate}\n"
                f"Transactions done: {self.transaction_count} of {self.transaction_limit}\n"
                f"{'='*50}")
