import turtle
import math
import random
#global variable(s)
wdth = 800; hgth = 800; bgstring = "#91d2ca"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"
def poly(t,sides,size):
	angl = (sides - 2) * 180 / sides
	for n in range (0,sides):
		t.forward(size)
		t.right(180-angl)
		
def fourLeaf(t,x,y,s,c):
	adj = -20
	t.penup()
	t.pensize(3)
	t.goto(x,y)
	f = s * 2
	t.color(c)
	t.setheading(0+adj)
	t.penup();t.forward(f);t.pendown()
	t.pendown();poly(t,18,s)
	t.setheading(90+adj)
	t.penup();t.forward(f);t.pendown()
	poly(t,18,s)
	t.setheading(180+adj)
	t.penup();t.forward(f);t.pendown()
	poly(t,18,s)
	t.setheading(270+adj)
	t.penup();t.forward(f);t.pendown()
	poly(t,18,s)		
def mike(t): 
	print(wdth,hgth,bgstring) #print global
	theta = 0
	fourLeaf(t,0,0,3,green)
	for n in range (0,15):
		t.penup()
		t.goto(0,0)
		t.setheading(theta)
		t.pendown()
		t.pensize(1)
		t.color(blue)
		t.forward(100)
		t.pencolor(red)
		poly(t,n+2,70)
		t.pencolor(blue)
		poly(t,5,90)
		t.pencolor(green)
		poly(t,36,5)
		theta = theta + 24
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
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

'''
five circles
five polygons
five line commands
two for loops
one global variable


'''
