import tkinter as tk
import turtle
# *************************************************************************
# Resursion (Pop stack) cwc

def drawSpiral(t, line_length,w):
    #32DC7F;#7F32DC;#DC327F;
    t.color("#32DC7F")
    t.width(w)
    if line_length > 0:
        t.forward(line_length)
        t.right(36)
        drawSpiral(t,line_length-3,w+1) # this is the recusive call to drawSpiral(t,line_length)
    t.color("#DC327F")
    t.width(w-1)
    #the following line uses variables from the stack of activation records (line_length)
    t.forward((line_length/2)*-1)
    t.left(36)

def callSpiral():
    try:
        turtle.TurtleScreen._RUNNING = True
        w = turtle.Screen()
        w.title("Recursion")
        w.clear()
        w.bgcolor("#505050")
        t = turtle.Turtle()
        t.color("#FFEDBF")
        t.penup()
        t.goto(0,300)
        style = ('Arial', 30, 'bold')
        t.write('Recursion Example - Spiral', font=style, align='center')
        t.penup()
        t.goto(-100,250)
        t.pendown()
        drawSpiral(t,170,1)
        w.exitonclick()
    finally:
        turtle.Terminator()
# end Recursion
def main():
	callSpiral()
# *************************************************************************
if __name__ == '__main__':
	main()
