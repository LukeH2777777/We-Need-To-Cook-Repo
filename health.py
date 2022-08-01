import uuid


class FoodItem:

    def __init__(self, name: str, display_name: str, heal_amount: int, cost: int):

        self.id = uuid.uuid4().hex
        self.name = name
        self.display_name = display_name
        self.heal_amount = heal_amount
        self.cost = cost

    def __repr__(self):

        return f"{self.display_name} - Heals: {self.heal_amount}, Cost: ${self.cost}"

    def to_dict(self):

        return {
            "name": self.name,
            "display_name": self.display_name,
            "heal_amount": self.heal_amount,
            "cost": self.cost
        }


class PlayerHealth:

    def __init__(self, score: int = 100):

        self.score = score

    def decrement(self, dmg_amount: int):

        self.score -= dmg_amount

    def increment(self, heal_amount: int):

        self.score += heal_amount

    def heal_from_item(self, item: FoodItem):

        self.score += item.heal_amount

    def to_dict(self):

        return {
            "health": self.score
        }
