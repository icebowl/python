import turtle
import math
import random

def hexcon(num):
	key = "0123456789abcdef" # hex key
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h

def showPi(t,ratio):
	t.penup()
	x = -180; y = -220
	t.goto(x,y)
	t.color("#FDF6E3")
	t.begin_fill()
	t.pendown();t.goto(x+600,y);t.goto(x+600,y-55);t.goto(x,y-55);t.goto(x,y)
	t.end_fill()
	t.goto(-130,-280)
	t.color("#ff3300")
	style = ('Arial', 30, 'bold')
	t.write(str(ratio), font=style, align='left')
	t.penup()

def grid(t):
	t.penup()
	t.goto(0,0)

	for angle in range(0,360,90):
		t.color("#327FDC")
		t.pendown()
		t.seth(angle)
		print(angle)
		t.forward(200)
		t.backward(200)
		t.penup()
		t.goto(0,0)
		t.color("#7F32DC")
		for i in range (10,200,10):
			t.forward(10)
			t.pendown()
			t.left(90);t.forward(5);t.backward(10);t.forward(5);t.right(90)
			t.penup()
		t.goto(0,0)

def pi(t):
	#grid(t)
	alldots = 0
	hits = 0
	ratio = 0
	c = 0
	t.penup()
	while(c < 100000000):
		x = random.randint(-200,200)
		h = float (x/200)
		y = random.randint(-200,200)
		k = float(y/200)
		print(h,k)
		if (((h * h) + (k * k ))> 1.0):
			print("************** miss ****************")
			thecolor = "#505050"
		else:
			thecolor = "#32DC7F"
			hits = hits + 1
		alldots = alldots + 1
		ratio = float(hits/alldots)*4
		if(c % 1000 == 0):
			print(c)
			grid(t)
			showPi(t,ratio)
		t.color(thecolor)
		t.goto(x,y)
		t.pendown()
		t.dot()
		t.penup()
		c = c + 1

def main():
	w = turtle.Screen()
	w.clear()
	t = turtle.Turtle()
	t.speed(0)
	t.hideturtle()
	#t.penup()
	#red = 255;green = 0; blue = 0
	pi(t)
	w.exitonclick()

if __name__ == "__main__":
	main()
