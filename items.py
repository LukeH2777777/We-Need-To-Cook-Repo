import uuid


class FoodItem:
    """
    Class representing a healing item
    """

    def __init__(self, name: str, display_name: str, heal_amount: int, cost: int, weight: float = 0.0):
        """
        Heals "heal_amount" when consumed. Self generates a UUID so each piece is unique. Weight included for future
        inventory/carry limits
        :param name:
        :param display_name:
        :param heal_amount:
        :param cost:
        :param weight:
        """

        self.id = uuid.uuid4().hex
        self.name = name
        self.display_name = display_name
        self.heal_amount = heal_amount
        self.cost = cost
        self.weight = weight

    def __repr__(self):

        return f"{self.display_name} - Heals: {self.heal_amount}, Cost: ${self.cost}, Weight: {self.weight}"

    def to_dict(self):
        """
        Convenience function to make it easier to dump/load from JSON save files etc
        :return:
        """
        return {
            "name": self.name,
            "display_name": self.display_name,
            "heal_amount": self.heal_amount,
            "cost": self.cost,
            "weight": self.weight
        }


class Narcotic:
    """
    Class representing a portion of a narcotic
    """

    def __init__(self, name: str, display_name: str, wholesale_price: float, weight: float):
        """
        Wholesale price/cost captured here - the idea being that when this portion is bought, the price at which it's
        acquired is fixed and becomes a fixed cost for ever. Leaving sell prices out of here so they can be
        supplied/controlled by a market and don't come into effect until this portion is sold
        :param name:
        :param display_name:
        :param wholesale_price:
        :param weight:
        """
        self.id = uuid.uuid4().hex
        self.name = name
        self.display_name = display_name
        self.wholesale_price = wholesale_price
        self.weight = weight
        self.cost = self.wholesale_price * self.weight

    def __repr__(self):

        return f"{self.weight}g {self.display_name} - " \
               f"Bought for: {self.wholesale_price}, Cost: ${self.cost}"

    def to_dict(self):
        """
        Convenience function to make it easier to dump/load from JSON save files etc
        :return:
        """
        return {
            "name": self.name,
            "display_name": self.display_name,
            "wholesale_price": self.wholesale_price,
            "cost": self.cost,
            "weight": self.weight
        }
