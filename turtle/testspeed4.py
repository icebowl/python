import turtle
import random
import time
screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(0, 0)

dist = 2
for i in range(1000):
	t.fd(dist)
	t.rt(45)
	dist += 0.25
	#print(dist)
#turtle.update()
screen.exitonclick()	



'''
https://docs.python.org/2/library/turtle.html#turtle.delay

screen.tracer(8, 25)
>>> dist = 2
>>> for i in range(200):
...     fd(dist)
...     rt(90)
...     dist += 2

'''
