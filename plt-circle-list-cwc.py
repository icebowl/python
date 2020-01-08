'''
plt-circle-list-cwc.py
Test this.
https://tritech-testsite.smapply.io/
Use your personal email.  Not your @ksd.org account.

python-circle-list-assignment.py
Get the code: 10.183.1.26 code python
Plot circle data using python
- Use your data
- Change the background color
- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with the text "Plotting Circumference and Diameter"
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py)

'''

import turtle
import math
wdth = 800; hgth = 800; bgstring = "#ffffed"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	t.penup()
	t.goto(-170,300)
	t.pendown()
	t.color('#00cc00')
	style = ('Courier', 30, 'bold')
	t.write('Circle Circumference and Diameter Plot', font=("Arial", 30, 'normal', 'bold',))
	t.color('#cc0000')
	t.goto(400,-400)
	t.write('C\ni\nr\nc\nu\nm\nf\ne\nr\ne\nn\nc\ne', font=("Arial", 30, 'normal', 'bold',))
	t.color('#cc00cc')
	t.write('Diameter', font=("Arial", 30, 'normal', 'bold',))
	t.hideturtle()
	t.penup()

def plotCircles(t):
	#list  named d and c
	d =  [35,34,12.8, 1.8, 19.8, 8.7] 
	c =  [111,108,37,  4.7, 57.1, 26.1] 
	# list dsorted and csorted
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(0,0)
	t.pendown()
	t.dot(3, red)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, red)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, red)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, red)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, red)
	t.goto(dsorted[4],csorted[4])
	t.dot(3, green)
	t.goto(dsorted[5],csorted[5])
	t.dot(3, green)
	
def main():
	try:
		turtle.tracer(0,0)
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.hideturtle()
		grid(t)
		plotCircles(t)
		turtle.update()
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
