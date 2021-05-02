import turtle
import random
import time
screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(0, 0)

for i in range(1000):
	t.goto(-100,-100)
	x = random.random()*500
	y = random.random()*500
	t.goto(x,y)

turtle.update()
screen.exitonclick()	



'''
https://docs.python.org/2/library/turtle.html#turtle.delay
'''
