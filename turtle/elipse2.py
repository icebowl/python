import turtle
import math

def elipse(t,a,b):
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

if __name__ == "__main__":
	w = turtle.Screen()
	w.clear()
	t = turtle.Turtle()
	a = 35; b = 70
	t.width(4)
	elipse(t,a,b)
	w.exitonclick()
