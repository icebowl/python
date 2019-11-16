import turtle

def square(t,length):
	for side in range (0,4):
		t.forward(length)
		t.right(90)
		
def callMike():
	w = turtle.Screen()
	w.setup(700, 700)
	w.clear()
	w.bgcolor("#cccccc")
	t = turtle.Turtle()
	t.penup()
	x = 100
	y = 0
	count = 0
	t.color("#ff0000")
	while (count < 10):
		t.width(count+1)
		t.goto(x,y)
		t.pendown()
		t.circle(50)
		square(t,50)
		count = count + 1
		x = x - 10
		y = y + 10
		if (count > 5):
			t.color("#0000ff")
		print(x,y,count)
	w.exitonclick()
	

def main():
	callMike()
	
if __name__ == '__main__':
	main()
	
