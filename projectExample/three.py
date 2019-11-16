import turtle

def square(t,length):
	for side in range (0,4):
		t.forward(length)
		t.right(90)
		
def callLeo():
	try:
		turtle.TurtleScreen._RUNNING = True
		w = turtle.Screen()
		w.setup(700, 700)
		w.clear()
		w.title("three")
		w.bgcolor("#0000ff")
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
	callLeo()
	
if __name__ == '__main__':
	main()
	
