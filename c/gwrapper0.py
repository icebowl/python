#cwc reset control+j
# https://www.youtube.com/watch?v=BK7YvpTT4Sw
import time
import curses

def main(stdscr):
	curses.curs_set(0)
	stdscr.addstr(15,5," 15 5 ")
	stdscr.refresh()
	while True:
		k = stdscr.get_wch()
		print(f'k: {k}')
		curses.flushinp()
		if (k == 'k'):
			stdscr.addstr(20,5," k 20 5 ")
		if( k == "q"):
			False
	
	#time.sleep(3)
	
curses.wrapper(main)
