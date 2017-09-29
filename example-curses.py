import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"MENU")
stdscr.addstr(1,10,"1 10x10")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(20, 20, "Up")
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(20, 20, "Down")
curses.endwin()
