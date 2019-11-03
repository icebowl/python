import turtle
import math

def elipse(t,x,y,r):
	thx = 0; thy = 0
	adj = 1
	t.penup()
	t.goto(x+r,y)
	t.pendown()
	t.color("#00ff00")
	while (thx < 2*math.pi):
		h = (math.cos(thx) * r) + x
		k = (math.sin(thy) * ry) + y 
		ry = ry + adj
		thx = thx + (math.pi/25)
		thy = thy + (math.pi/25)
		t.goto(h,k)
		if( thy > math.pi/2 ):
			adj = adj * -1
		
if __name__ == "__main__":
	w = turtle.Screen()
	w.clear()
	t = turtle.Turtle()
	elipse(t,0,0,60)
	w.exitonclick()
