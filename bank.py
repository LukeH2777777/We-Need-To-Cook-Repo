import utilities as ut
"""
make sure you create an instance like this

Bank = Bank()

or else it would throw a metric fuck tone of errors :)

To deposit:
Bank.deposit(1000)

To withdraw:
Bank.withdraw(1000)

To check balance:
Bank.balance()

"""


class Bank:

    def __init__(self,money=1000):
        self.money = money

    def deposit(self,amount):
        self.money += amount
        ut.printout(f"{amount} has been credited to your account.")

    def withdraw(self,amount):
        if amount > self.money:
            print("insufficient balance")
        else:
            self.money -= amount
            ut.printout(f"{amount} has been withdrawn from your account.")
    
    def balance(self):
        ut.printout(f"your balance is {self.money}.")

    def to_dict(self):
        return {
            "Bank": self.money
        }
