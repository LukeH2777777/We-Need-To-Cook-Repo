import utilities as ut
"""
make sure you create an instance like this

Bank = Bank()

or else it would throw a metric fuck tone of errors :)

"""


class Bank:

    def __init__(self,money=0,cash=1000):
        self.money = money
        self.cash = cash

    def cash_balance(self):
        ut.printout(f"you got {self.cash} in cash")
      
    def balance(self):
        ut.printout(f"your balance is {self.money}.")

    def deposit(self,amount):
        if amount > self.cash:
            ut.printout("insufficient funds")
        else:
            self.money += amount
            self.cash -= amount
            ut.printout(f"{amount} has been credited to your account.")

    def withdraw(self,amount):
        if amount > self.money:
            ut.printout("insufficient funds")
        else:
            self.money -= amount
            self.money += self.cash
            ut.printout(f"{amount} has been withdrawn from your account.")
    
    def to_dict(self):
        return {
            "Bank": self.money,
            "Cash": self.cash
        }



#for testing remove on release.
"""
Bank = Bank()
Bank.balance()
Bank.cash_balance()
Bank.withdraw(1000)
Bank.deposit(10000000)
"""
