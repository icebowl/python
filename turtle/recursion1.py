# recursion
import turtle

def spiral(t,dist,w,turn):
	t.color("#ff0000")
	t.width(w)
	t.fd(dist)
	t.rt(turn)
	dist += 0.25
	w = w + 0.1
	if (dist < 40):
		spiral(t,dist,w,turn)
	#stop recursion
	t.penup()
	t.goto(-200,-200)
	t.pendown()
	t.color("#0000ff")
	t.width(1)
	t.fd(-5*dist)
	t.lt(turn*-1)
	
	

def main():
	screen = turtle.Screen()
	t = turtle.Turtle()
	t.penup()
	t.goto(200,200)
	t.pendown()
	#spiral(turtle,distance,width,turn)
	spiral(t,1,1,11.5)
	screen.exitonclick()	
	
if __name__=="__main__":
	main()



'''
#turtle.tracer(0, 0)


	#print(dist)
#turtle.update()

https://docs.python.org/2/library/turtle.html#turtle.delay

screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

'''
