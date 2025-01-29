import Account as Acc

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def load_accounts(self, infile):
        with open(infile, "r") as file:
            for line in file:
                values = line.split()
                acc_type = int(values[0])
                acc_num = values[1]
                name = values[2]
                balance = float(values[3])

                if acc_type == 1:
                    overdraft_limit = float(values[4])
                    account = Acc.CurrentAccount(acc_num, name, balance, overdraft_limit)
                elif acc_type == 2:
                    interest_rate = float(values[4])
                    account = Acc.SavingsAccount(acc_num, name, balance)
                elif acc_type == 3:
                    interest_rate = float(values[4])
                    transaction_count = int(values[5])
                    account = Acc.InvestmentAccount(acc_num, name, balance, interest_rate)
                    account.transaction_count = transaction_count
                else:
                    print(f"Unknown account type: {acc_type}. Skipping line.")
                    continue

                self.accounts.append(account)

    def list_accounts(self):
        print(f"\nAll accounts in {self.name}")
        print("=" * 50)
        for account in self.accounts:
            print(account)

if __name__ == "__main__":
    bank = Bank("My Bank")
    bank.load_accounts("accounts.txt")
    bank.list_accounts()

