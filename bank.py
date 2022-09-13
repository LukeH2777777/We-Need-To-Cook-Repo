import utilities as ut
"""
make sure you create an instance like this
bank = Bank()
or else it would throw a metric fuck tone of errors :)
"""


class Bank:

    def __init__(self,account=500,cash=500):
        self.account = account
        self.cash = cash

    def cash_balance(self):
        return self.cash
      
    def balance(self):
        return self.account

    def deposit(self,amount):
        if amount > self.cash:
            return
        else:
            self.account += amount
            self.cash -= amount

    def withdraw(self,amount):
        if amount > self.account:
            return
        else:
            self.account -= amount  
            amount += self.cash

    def dev_add(self, amount):
        self.account += amount 

    def to_dict(self):
        return {
            "Bank": self.account,
            "Cash": self.cash
        }


