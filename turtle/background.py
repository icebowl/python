import turtle

def hexcon(num):
	key = "0123456789abcdef" # hex key
	h = ""
	h16 = int(num/16)
	h1 = num % 16
	h = key[h16]+ key[h1]
	return h

def background(t,red, green, blue):
	thecolor = "#0000ff"
	y = -700
	while(y < 701):	
		print (y,red,green, blue,thecolor
		)
		redHex = hexcon(red); greenHex = hexcon(green); blueHex = hexcon(blue)
		thecolor = "#"+redHex+greenHex+blueHex
		t.color(thecolor)
		t.goto(-700,y)
		t.goto(700,y)
		y = y + 2
		red = red+ 10  
		green = int(green + 0.5)
		blue = blue + 1
		if(red > 255):
			red = 0
		if(green > 255):
			green = 100
		if(blue > 255):
			blue = 0
		if(red < 0):
			red = 255
		if(green < 0):
			green = 255
		if(blue < 0):
			blue = 255


def main():
	w = turtle.Screen()
	w.clear()
	t = turtle.Turtle()
	t.speed(0)
	t.hideturtle()
	#t.penup()
	red = 0;green = 0; blue = 200
	background(t,red, green, blue)
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
