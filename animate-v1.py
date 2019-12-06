import turtle
import math
import random
#global variable(s)
wdth = 800; hgth = 800; bgstring = "#ffff00"

def mike(t):
	#change global variables
    # example :  global xM = 200    
	print(wdth,hgth)
	t.forward(100)

def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		mike(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()
