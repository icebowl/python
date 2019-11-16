import turtle

def hexcon(num):
	key = "0123456789abcdef" # hex key
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h


def grad(t,red, green, blue):
	thecolor = "#ff0000"
	y = 0
	while(y < 256):
		redHex = hexcon(red); greenHex = hexcon(green); blueHex = hexcon(blue)
		thecolor = "#"+redHex+greenHex+blueHex
		t.color(thecolor)
		print (y,red,green, blue)
		t.goto(-10,y)
		y = y + 1
		t.goto(10,y)
		red = red 
		green = green + 1
		blue = blue + 1
		if(red > 255):
			red = 0
		if(green > 255):
			green = 0
		if(blue > 255):
			blue = 0
		if(red > 255):
			red = 0
		if(green > 255):
			green = 0
		if(blue > 255):
			blue = 0

	
def main():
	w = turtle.Screen()
	w.clear()
	t = turtle.Turtle()
	t.speed(0)
	t.hideturtle()
	#t.penup()
	red = 255;green = 0; blue = 0
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
