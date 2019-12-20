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
def plot(t): 
	d = [3.4, 6.5, 10.5, 20.5]
	c = [10.8, 20.7, 32.9, 64.3]
	for n in range (0,4):
		print(c[n]/d[n])
		
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		plot(t)
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
