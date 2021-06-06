class Account():
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withrawal(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withrawal accepted")
        else:
            print("Sorry, not enough balance")

    def __str__ (self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

my_account = Account("Rajeev",100)
print(my_account)
print(my_account.owner)
print(my_account.balance)

my_account.deposit(100)

my_account.withrawal(200)

my_account.withrawal(1)
