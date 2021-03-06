# elipse0.py cwc
# reference https://www.mathopenref.com/coordgeneralellipse.html
import turtle
import math

def elipse(t,a,b):
	try:
		turtle.TurtleScreen._RUNNING = True
		t.penup()
		x = (a*-1); y = 0
		t.goto(0,0)
		t.pendown()
		t.color("#00ff00")
		start = 1
		while (x < (a+1)):
			y = ((b*b)*(1-((x*x)/(a*a))))**0.5
			y = int(y)
			if(start == 1):
				t.penup()
				start = 0
			else:
				t.pendown()
			t.goto(x,y)
			x = x + 1
		start = 1
		x = x - 1
		t.penup()
		while (x > -1*a - 1):
			y = (((b*b)*(1-((x*x)/(a*a))))**0.5)*-1
			y = int(y)
			if(start == 1):
				t.penup()
				start = 0
			else:
				t.pendown()
			t.goto(x,y)
			x = x - 1
		w.exitonclick()
	finally:
		turtle.Terminator()

	def callElipse():
		w = turtle.Screen()
		w.clear()
		t = turtle.Turtle()
		a = 35; b = 70
		t.width(4)
		elipse(t,a,b)
		a = 20; b = 40
		t.width(4)
		elipse(t,a,b)

if __name__ == "__main__":
	callElipse():
