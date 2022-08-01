import json

from health import (
    PlayerHealth,
    FoodItem
)

with open("food_items.json", "r") as f:

    food_basket = [FoodItem(**x) for x in json.load(f).get("items")]


def test_basics():

    test_player = PlayerHealth()
    assert test_player.score == 100

    test_player.decrement(15)
    assert test_player.score == 85

    test_player.increment(25)
    assert test_player.score == 110
