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

def getCosSin(angle,r):
	x = (math.cos(math.pi/180 * angle)) * r
	y = (math.sin(math.pi/180 * angle)) * r
	return x,y

def grad(t,red, green, blue):
	thecolor = "#ff0000"
	y = 0
	angle = 0
	h = k = 0
	t.width(10)
	ra = random.randint(0,1)
	if(ra == 0):
		ra = -1
	ga = random.randint(0,1)
	if(ga == 0):
		ga = -1
	ba = random.randint(0,1)
	if(ba == 0):
		ba =  -1
	redHex = hexcon(red); greenHex = hexcon(green); blueHex = hexcon(blue)
	print (y,red,green, blue,ra,ga,ba)
	#z = input("pause")
	thecolor = "#"+redHex+greenHex+blueHex
	t.penup()
	while(angle < 361):
		t.color(thecolor)
		a,b = getCosSin(angle,50)
		h,k = getCosSin(angle,200)
		t.goto(0+a,0+b)
		y = y + 1
		t.pendown()
		t.goto(h,k)
		red = red + ra
		green = green + ra
		blue = blue + ra
		print (y,red,green, blue,ra,ga,ba)
		if(red > 255):
			ra = ra * -1
			red = 255
		if(green > 255):
			ga = ga * -1
			green = 255
		if(blue > 255):
			ba = ba * -1
			blue = 255
		if(red < 0):
			ra = ra * -1
			red = 0
		if(green < 0 ):
			ga = ga * -1
			green = 0
		if(blue < 0 ):
			ba = ba * -1
			blue = 0
		redHex = hexcon(red); greenHex = hexcon(green); blueHex = hexcon(blue)
		thecolor = "#"+redHex+greenHex+blueHex
		angle = angle + 1


def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		w = turtle.Screen()
		w.clear()
		t = turtle.Turtle()
		t.speed(0)
		t.hideturtle()
		#t.penup()
		#red = 255;green = 0; blue = 0
		red = random.randint(0,255)
		green = random.randint(0,255)
		blue = random.randint(0,255)
		grad(t,red, green, blue)
		w.exitonclick()
	finally:
		turtle.Terminator()

if __name__ == "__main__":
	main()
