import tkinter as tk
import turtle
# *************************************************************************
# Resursion (Pop stack) cwc

def drawSpiral(t, line_length):
    t.color("#dc322f")
    t.width(1)
    if line_length > 0:
        t.forward(line_length)
        t.right(36)
        drawSpiral(t,line_length-3) # this is the recusive call to drawSpiral(t,line_length)
    t.color("#268bd2")
    t.width(2)
    #the following line uses variables from the stack of activation records (line_length)
    t.forward((line_length/2)*-1)
    t.left(36)

def callSpiral():
    twin = turtle.Screen()
    twin = background("#839496")
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
