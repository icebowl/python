import tkinter as tk
import turtle
from random import randint
# chaos fractal cwc
def newpoint(plist):  # Define a function called newpoint
	vx =[0,300,-300]  # Set the x values for triangle vertices.
	vy =[300,-100,-100]  # Set the y values for triangle vertices.
	px = plist[0] # Get the x value of a point
	py = plist[1] # Get the y value of a point
	random_point = randint(0,3) #Get one of 3 points.
	# Calculate half the distance from the current point to a triangle vertex.
	if (random_point % 3 == 0):
		plist[0] = int((px + vx[0])/2)
		plist[1] = int((py + vy[0])/2)
		plist[2] = 0
	if (random_point % 3 == 1):
		plist[0] = int((px + vx[1])/2)
		plist[1] = int((py + vy[1])/2)
		plist[2] = 1
	if (random_point % 3 == 2):
		plist[0] = int((px + vx[2])/2)
		plist[1] = int((py + vy[2])/2)
		plist[2] = 2
	#print(plist,end='')  #print the new point
	return plist #Send the point (list) back to the calling function.

def chaos():
	try:
		turtle.TurtleScreen._RUNNING = True
		w = turtle.Screen()
		w.title("Chaos")
		w.clear()
		w.bgcolor("#FDF6E3")
		t = turtle.Turtle()
		t.ht()# hide turtle
		t.speed(0)
		t.penup()
		t.color("#50b3b3")
		t.goto(0,-300)
		style = ('Arial', 30, 'bold')
		t.write('Chaos - Sierpiński Triangle', font=style, align='center')
		t.color("#ffffff")
		t.width(1)
		h = randint(-10,10) # Calculate a starting point for x
		k = randint(-10,10) # Calculate a starting point for y
		c = ""
		alist =[h,k,c] # Assign the starting points to a list.
		count = 0
		while True:
			alist = newpoint(alist) # Get a new point from a function that is half way between the current point and a random vertex of a triangle.
			x = alist[0] # Assign a new x value from the list alist[] to x
			y = alist[1] # Assign a new y value from the list alist[] to y
			theColor = alist[2]
			t.penup()
			t.goto(x, y)
			t.pendown()
			if (theColor == 0):
				cs = "#32DC7F"
			elif (theColor == 1):
				cs = "#7F32DC"
			else:
				cs = "#DC327F"
			t.color(cs)	#32DC7F;#7F32DC;#DC327F;
			t.seth(90)
			#t.dot()
			t.fd(1)
			count = count + 1
			if (count > 1000000):
				break
	    #input("Press return to end")
		w.exitonclick()
	finally:
		turtle.Terminator()
    #w.close()
    #end Chaos
if __name__ == '__main__':
	chaos()
