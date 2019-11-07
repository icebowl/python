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
	

def pi(t):
	alldots = 0
	yellowdots = 0
	c = 0
	t.penup()
	while(c < 1000000):
		x = random.randint(-200,200)
		h = float (x/200)
		y = random.randint(-200,200)
		k = float(y/200)
		if (((h * h) + (k * k ))> 1):
			thecolor = "#ffff00" 
			yellowdots = yellowdots + 1
			
		else:
			thecolor = "#0000ff"
		alldots = alldots + 1
		ratio = alldots - (alldots - yellowdots)
		if(c % 1000 == 0):
			print(x,y,h,k,ratio)
		t.color(thecolor)
		t.goto(x,y)
		t.pendown()
		t.dot()
		t.penup()
							
	
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

