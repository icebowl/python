import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    # Proceed with your program
    print("Running some program")

# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!
wrapper(main)
