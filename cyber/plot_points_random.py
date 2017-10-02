from graphics import *
from random import randint
win = GraphWin("PLOT RANDOM", 400, 400)
count = 0
while True:
	x = randint(0,400)
	y = randint(0,400)
	pt = Point(x, y)
	pt.draw(win)
	
input("Press return to end")

win.close()
