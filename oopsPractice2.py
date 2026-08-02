class Account:
    def __init__(self, bal, accNo):
        self.balance = bal
        self.account = accNo

    #debiting method
    def debit(self, amount):
        self.balance -= amount
        print("the amount decucted is: ", amount)
        print("total balence ", self.balance)

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("the amount added is: ", amount)
        print("total balence ", self.balance)

    def getbal(self):
        return self.balance

ac1 = Account(10000, 2141)

print(ac1.balance, ac1.account)
ac1.debit(1500)
ac1.credit(75)
ac1.getbal()