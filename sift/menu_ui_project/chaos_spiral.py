import tkinter as tk
import turtle
from random import randint
# spiral * * * * * *

def drawSpiral(t, line_length):
    t.color("#dc322f")
    t.width(3)
    if line_length > 0:
        t.forward(line_length)
        t.right(36)
        drawSpiral(t,line_length-3) # this is the recusive call to drawSpiral(t,line_length)
    t.color("#268bd2")
    t.width(6)
    #the following line uses variables from the stack of activation records (line_length)
    t.forward((line_length/2)*-1)
    t.left(36)

def callSpiral():
    twin = turtle.Screen()
    twin.clear()
    twin.bgcolor("#fdf6e3")
    t0 = turtle.Turtle()
    #tWin = turtle.Screen()
    t0.penup()
    t0.goto(-100,250)
    t0.pendown()
    drawSpiral(t0,170)
    twin.exitonclick()

# chaos fractal cwc
def newpoint(x,y,tcolor):  # Define a function called newpoint
	vx =[0,201,-201]  # Set the x values for triangle vertices.
	vy =[201,-101,-101]  # Set the y values for triangle vertices.
	px = x # Get the x value of a point
	py = y # Get the y value of a point
	random_point = randint(0,3) #Get one of 3 points.
	# Calculate half the distance from the current point to a triangle vertex.
	if (random_point % 3 == 0):
		px = ((px + vx[0])/2)
		py = ((py + vy[0])/2)
		tcolor = "#2aa198"
	if (random_point % 3 == 1):
		px = ((px + vx[1])/2)
		py = ((py + vy[1])/2)
		tcolor = "#268bd2"
	if (random_point % 3 == 2):
		px = ((px + vx[2])/2)
		py = ((py + vy[2])/2)
		tcolor = "#859900"
	#print(plist,end='')  #print the new point
	return px,py,tcolor #Send the point (list) back to the calling function.

def chaos():
	w = turtle.Screen()
	w.clear()
	w.bgcolor("#fdf6e3")
	t = turtle.Turtle()
	t.speed(0)
	t.color("#ffffff")
	t.width(1)
	h = randint(-10,10) # Calculate a starting point for x
	k = randint(-10,10) # Calculate a starting point for y
	x,y = h,k # Assign the starting points to a list.
	tcolor = "#000000"
	count = 0
	while True:
		x,y,tcolor = newpoint(x,y,tcolor) # Get a new point from a function that is half way between the current point and a random vertex of a triangle.
		t.penup()
		t.color(tcolor)
		t.goto(x,y)
		t.pendown()
		t.fd(1)
		count = count + 1
		if (count > 100000):
			break
    #input("Press return to end")
	w.exitonclick()
    #w.close()
    #end Chaos


"""
$base03:    #002b36;
$base02:    #073642;
$base01:    #586e75;
$base00:    #657b83;
$base0:     #839496;
$base1:     #93a1a1;
$base2:     #eee8d5;
$base3:     #fdf6e3;
$yellow:    #b58900;
$orange:    #cb4b16;
$red:       #dc322f;
$magenta:   #d33682;
$violet:    #6c71c4;
$blue:      #268bd2;
$cyan:      #2aa198;
$green:     #859900;


"""
