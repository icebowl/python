# elipse0.py cwc
# reference https://www.mathopenref.com/coordgeneralellipse.html
import turtle
import math

def elipse(t,a,b):
		t.penup()
		x = (a*-1); y = 0
		t.goto(0,0)
		t.pendown()
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

def callElipse():
	try:
		turtle.TurtleScreen._RUNNING = True
		w = turtle.Screen()
		w.title("Elipse")
		w.clear()
		t = turtle.Turtle()
		t.penup()
		t.color("#ff0000")
		t.goto(-200,300)
		style = ('Arial', 30, 'bold')
		t.color("#ff3300")
		t.write('Elipse', font=style, align='left')
		t.goto(-200,260)
		t.color("#ff7700")
		style = ('Arial', 14, 'bold')
		t.write('[TOP] y = ((b*b)*(1-((x*x)\/(a*a))))**0.5', font=style, align='left')
		t.goto(-200,240)
		t.write('[BOTTOM] y = (((b*b)*(1-((x*x)\/(a*a))))**0.5)*-1', font=style, align='left')
		a = 35; b = 70
		t.width(10)
		t.color("#0000dd")
		elipse(t,a,b)
		a = 27; b = 60
		t.width(7)
		t.color("#0077dd")
		elipse(t,a,b)
		a = 17; b = 50
		t.width(3.5)
		t.color("#00ffdd")
		elipse(t,a,b)
		w.exitonclick()
	finally:
		turtle.Terminator()

if __name__ == "__main__":
	callElipse()
