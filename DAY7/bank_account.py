class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0) -> None:
        self.account_holder: str = account_holder
        self.balance: float = balance
    def deposit(self, amount: float) -> None:
        self.balance += amount
    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def get_balance(self) -> float:
        return self.balance
    def display(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}"
account = BankAccount("Adila", 1000)
account.deposit(500)
if account.withdraw(200):
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")
print("Current Balance:", account.get_balance())
print(account.display())