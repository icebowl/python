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
	ra = random.randint(-1,1)
	ga = random.randint(-1,1)
	ba = random.randint(-1,1)
	t.penup()
	while(angle < 361):
		print (y,red,green, blue,ra,ga,ba)
		redHex = hexcon(red); greenHex = hexcon(green); blueHex = hexcon(blue)
		thecolor = "#"+redHex+greenHex+blueHex
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
		if(red > 255):
			ra = ra * -1
			#red = red + ra
		if(green > 255):
			ga = ga * -1
			#green = green + ra
		if(blue > 255):
			ba = ba * -1
			#blue = blue + ra
		if(red < 0):
			ra = ra * -1
			#red = red + ra
		if(green < 0 ):
			ga = ga * -1
			#green = green + ra
		if(blue < 0 ):
			ba = ba * -1
			#blue = blue + ra
		angle = angle + 1


def main():
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

if __name__ == "__main__":
	main()


'''
	t.goto(-255,y)
		t.color(#ff0000)
		t.down()
		#t.goto(255,y)
		if (y % 10 == 0):
			t.penup()
			#t.goto(0,y)
			t.color("#000000")
			#t.circle(10)
		y = y + 1


'''
