import time
import utilities as ut
from player import Player
import konami


def gamestart():
    command, argument = input().split()
    print(f"{command=}")
    print(f"{argument=}")

# TODO: do this function.
def parseCommand():
    pass

def tutorial():
    ut.printout("Welcome to the tutorial!", delay=2)
    ut.printout("First off, lets set your health to 100!", delay=2)
    gamestart()


# TODO: see if a save file exists, if so, load the file, else do this part.
def startgame():
    ut.printout("Welcome to We Need To Cook!", delay=2)
    ut.printout("Would you like a tutorial?", delay=1)
    ut.printout("Y or N")
    if input().lower() in ["y", "yes"]:
        tutorial()


#player = Player("Young lad")
#print(f"{player.getName()} swung for {player.getAttackDamage()} damage")

try:
    startgame()
except KeyboardInterrupt:
    print("Quitting....")
    #if you want to save stuff when the player quits
    #put your code here
