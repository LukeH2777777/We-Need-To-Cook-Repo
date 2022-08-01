import time

"""
    printout
    desc: Prints out a string in the style of pokemon games. 
    args:
        s: The string to be printed
        newLine: Whether to insert a new line at the end of the print
        delay: How long to delay after the text has been printed.
"""
def printout(s: str, newLine: bool = True, delay: int = 0) -> None:
    for c in s:
        print(c, end="", flush=True)
        time.sleep(0.1)
    if newLine:
        print()
    time.sleep(delay)
