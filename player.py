from inventory import *

class Player:

    def __init__(self, name: str):
        self.name = name
        self.__inventory = Inventory.get_guns()["Machete"]
        self.xp = 0
        self.health = 100
        self.level = 0

    def get_inventory(self):
        return self.__inventory
