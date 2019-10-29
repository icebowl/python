
import curses, time

def main(stdscr):
    """checking for keypress"""
    stdscr.nodelay(True)  # do not wait for input when calling getch
    return stdscr.getch()

while True:
    print("key:", curses.wrapper(main)) # prints: 'key: 97' for 'a' pressed
                                        # '-1' on no presses
    time.sleep(1)
