import json

from health import Health
from items import (
    FoodItem,
    Narcotic
)

with open("food_items.json", "r") as f:

    food_basket = [FoodItem(**x) for x in json.load(f).get("items")]


def test_food_basics():

    test_player = Health()
    assert test_player.score == 100

    test_player.decrement(15)
    assert test_player.score == 85

    test_player.increment(25)
    assert test_player.score == 110


def test_narcotic_basics():

    cocaine = Narcotic("cocaine", "Coke", 30.0, 5)

    assert cocaine.cost == 150
