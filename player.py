from random import randint

class Player():
    name = ""
    health = 100
    xp = 0
    seller_level = 0
    weapon = "machete"

    def __init__(self, name: str):
        self.name = name
    
    def getName(self) -> str:
        return self.name

    def getAttackDamage(self):
        weapons = {"machete": [45, 55]} # TODO: move this somewhere else, and expand to all weapons
        return randint(weapons[self.weapon][0], weapons[self.weapon][1])

