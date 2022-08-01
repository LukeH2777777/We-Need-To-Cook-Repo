import time
import utilities

def gamestart():
    command, argument = input().split()
    print(f"{command=}")
    print(f"{argument=}")

# TODO: do this function.
def parseCommand():
    pass

def tutorial():
    utilities.printout("Welcome to the tutorial!", delay=2)
    utilities.printout("First off, lets set your health to 100!", delay=2)
    gamestart()


# TODO: see if a save file exists, if so, load the file, else do this part.
def startgame():
    utilities.printout("Welcome to We Need To Cook!", delay=2)
    utilities.printout("Would you like a tutorial?", delay=1)
    utilities.printout("Y or N")
    if input().lower() in ["y", "yes"]:
        tutorial()

startgame()
