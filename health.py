import items


class Health:

    def __init__(self, score: int = 100):

        self.score = score

    def decrement(self, dmg_amount: int):

        self.score -= dmg_amount

    def increment(self, heal_amount: int):

        self.score += heal_amount

    def heal_from_item(self, item: items.FoodItem):

        self.score += item.heal_amount

    def to_dict(self):

        return {
            "health": self.score
        }

