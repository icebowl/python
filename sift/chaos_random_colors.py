"""
Code and algorithm by Craig Coloeman
I created this Sierpinski's Triangle without looking at other code.
I wanted to figure this out as I did my version of the Ulam spiral.

Imagine 3 vertices of a triangle which are lableled 0,1, and 2.
You pick a a random point anywhere inside of the drawing window.
Then you randomly pick one of the three triangle vertices.
The next point will then be half way between the triangle vertex and 
the first random point.  This is the new point. Pick another random
vertex and the new point will be half the distance. If this is done 
thousands of times you will get the Sierpinski's Triangle .

What I am working on now is trying to optimize the algorithm or the 
equation to fill in the triangles pattern quicker.

Please read this code and run it.  
Change it in some way.

"""
from graphics import *
from random import randint
win = GraphWin("CHAOS", 650, 650) # Set parameters to make a window to draw in
win.setBackground("#000000") # Set the window background color.
def newpoint(plist):  # Define a function called newpoint
	vx =[300,600,0]  # Set the x values for triangle vertices.
	vy =[0,520,520]  # Set the y values for triangle vertices.
	px = plist[0] # Get the x value of a point
	py = plist[1] # Get the y value of a point
	random_point = randint(0,3) #Get one of 3 points.
	# Calculate half the distance from the current point to a Trianle vertex.
	if (random_point % 3 == 0):
		plist[0] = int((px + vx[0])/2)
		plist[1] = int((py + vy[0])/2)
	if (random_point % 3 == 1):
		plist[0] = int((px + vx[1])/2)
		plist[1] = int((py + vy[1])/2)
	if (random_point % 3 == 2):
		plist[0] = int((px + vx[2])/2)
		plist[1] = int((py + vy[2])/2)
	print(plist)  #print the new point
	return plist #Send the point (list) back to the calling function.
	
def main():
	h = randint(0,650) # Calculate a starting point for x
	k = randint(0,650) # Calculate a starting point for y
	alist =[h,k] # Assign the starting points to a list.
	count = 0
	while True:
		alist = newpoint(alist) # Get a new point from a function that is half way between the current point and a random vertex of a triangle.
		x = alist[0]+25 # Assign a new x value from the list alist[] to x
		y = alist[1]+25 # Assign a new y value from the list alist[] to y
		pt = Point(x, y)# Assign Point(x,y) to an object called pt
		pt.setFill("#00ff00") # Set the color to the point pt with pt.setFill(color)
		pt.draw(win) # Draw the point.
		if (count > 1000000000):
			break
	input("Press return to end")
	win.close()

main()


