from player import *
from npc import *

player = Player("will")
dealer = Dealer("john")

commands = {
    "inventory": player.get_inventory(),
    "drugs": dealer.get_stock()
}

print(player.get_inventory())
print(dealer.get_stock())
