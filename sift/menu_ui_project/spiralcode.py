import tkinter as tk
import turtle
# *************************************************************************
# Resursion (Pop stack) cwc

def drawSpiral(t, line_length):
    t.color("#ff0000")
    t.width(1)
    if line_length > 0:
        t.forward(line_length)
        t.right(36)
        drawSpiral(t,line_length-3) # this is the recusive call to drawSpiral(t,line_length)
    t.color("#0000ff")
    t.width(2)
    #the following line uses variables from the stack of activation records (line_length)
    t.forward((line_length/2)*-1)
    t.left(36)

def callSpiral():
    twin = turtle.Screen()
    twin.clear()
    t = turtle.Turtle()
    #tWin = turtle.Screen()
    t.penup()
    t.goto(-100,250)
    t.pendown()
    drawSpiral(t,170)
    twin.exitonclick()
# end Recursion
# *************************************************************************
