from inventory import *


class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.__inventory = Inventory.get_guns()["Machete"]
        self.xp = 0
        self.health = 100
        self.level = 0

    def get_inventory(self) -> dict:
        return self.__inventory
