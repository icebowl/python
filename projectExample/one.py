import turtle

def callMike():
	try:
		turtle.TurtleScreen._RUNNING = True
		w = turtle.Screen()
		w.setup(700, 700)
		w.clear()
		w.title("one")
		w.bgcolor("#ff0000")
		t = turtle.Turtle()
		t.pendown()
		x = 100
		y = 0
		count = 0
		t.width(10)
		t.color("#ffffff")
		t.circle(50)
		w.exitonclick()
	finally:
		turtle.Terminator()

def main():
	callMike()
	
if __name__ == '__main__':
	main()
	
