from inventory import *
from random import randint


class Dealer:

    def __init__(self, name) -> None:
        self.name = name
        self.__stock = {i: randint(1, 5) for i in Inventory.get_drugs()}

    def get_stock(self) -> dict:
        return self.__stock
