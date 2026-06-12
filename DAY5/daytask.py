class InsufficientFundsError(Exception):
    pass
class bankaccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        self.history=[]
    def deposit(self,amount):
        self.balance+=amount
        self.history.append(f"deposite : {amount}")
    def withdraw(self,amount):
        if (amount > self.balance):
            raise InsufficientFundsError("insufficient balance")
        self.balance -= amount
        self.history.append(f"withdraw : {amount}")
    def get_balance(self):
        return self.balance
    def transaction_history(self):
        for transaction in self.history:
            print(transaction)
    def __str__(self):
        return f"account owner : {self.owner} balance : {self.balance}"
class SavingsAccount(bankaccount):
    def __init__(self, owner, balance, interest_rate):
            super().__init__(owner, balance)
            self.interest_rate = interest_rate
    def apply_interest(self):
            interest = self.balance * self.interest_rate /100
            self.balance+=interest
            self.history.append(f"interest : {interest}")
class CurrentAccount(bankaccount):
    def __init__(self, owner, balance, overdraft_limit):
        super(). __init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if(self.balance-amount <- self.overdraft_limit):
            raise InsufficientFundsError("overdraft limit exceeded")
        self.balance-=amount
        self.history.append(f"withdraw : {amount}")
print("\n BANK ACCOUNTS")
acc=bankaccount("john",1000)
acc.deposit(500)
acc.withdraw(300)
print(acc)
print("balance : ",acc.get_balance())
print("\ntransaction history")
acc.transaction_history()
print("\n SAVINGS ACCOUNT")
s=SavingsAccount("Anya", 2000, 2)
print("before interest : ",s.get_balance())
s.apply_interest()
print("after interest : ",s.get_balance())
print("\n transaction_history")
s.transaction_history()
print("CURRENT ACCOUNT")
c=CurrentAccount("riya", 10000, 300)
c.withdraw(250)
print(c)
print("Balance:", c.get_balance())
print( "\n transaction_history ")
c.transaction_history()
print("\n error test")
try:
    acc.withdraw(500)
except InsufficientFundsError as e:
    print("error :",e)
try:
    acc.withdraw(2000)
except InsufficientFundsError as e:
    print("error :",e)