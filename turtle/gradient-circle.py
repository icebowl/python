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
	parity = random.randint(-1,1)
	ra = random.randint(1,5)*parity
	parity = random.randint(-1,1)
	ga = random.randint(1,5)*parity
	parity = random.randint(-1,1)
	ba = random.randint(1,5)*parity
	t.penup()
	while(angle < 361):
		redHex = hexcon(red); greenHex = hexcon(green); blueHex = hexcon(blue)
		thecolor = "#"+redHex+greenHex+blueHex
		t.color(thecolor)
		print (y,red,green, blue)
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
			red = 0
		if(green > 255):
			green = 0
		if(blue > 255):
			blue = 0
		if(red < 0):
			red = 255
		if(green < 0 ):
			green = 255
		if(blue < 0 ):
			blue = 255
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
