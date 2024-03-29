# recursion
import turtle

def spiral(t,d,w,tn):
	t.color("#ff0000")
	t.width(w)
	t.fd(d)
	t.rt(tn)
	d = d + 0.5
	w = w + 0.25
	tn = tn + 0.1
	if (d < 70):
		spiral(t,d,w,tn)
	#stop recursion
	t.color("#000000")
	#t.width(1)
	#t.bk(d)
	t.circle(d)

def main():
	screen = turtle.Screen()
	t = turtle.Turtle()
	t.penup()
	t.goto(200,200)
	t.pendown()
	#spiral(turtle,distance,width,turn)
	spiral(t,1,1,1)
	screen.exitonclick()	
	
if __name__=="__main__":
	main()
