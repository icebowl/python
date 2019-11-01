# ############################################################## #
#                  - ABOUT THE PROGRAM -
# Program name : open new window app
# Program description : opens new window on button click
# Author : Abdur-Rahmaan Janhangeer
# Date : 7th of May 2017
# License : MIT with emphasis :
# You are free to modify and distribute the program provided that
# attribution is  C L E A R L Y  made.
# Python version : Python 3.4
# ############################################################# #
# ############################################################# #
#                      - INDEX -
# 1 import statement/s
# 2 root / master definition
# 3 Function definition
# 4 Button 
# 5 mainloop
# ############################################################# #
# ############################################################# #
#                   - CONVENTIONS USED -
# --- naming ---
# functions : function names end with F
# Button named button1 . . .
# ############################################################# #
# ############################################################# #
#                  - NOTES AND WARNINGS -
# ---warning---
# wildcard operator used in imports
# ---notes---
# one shot comments used
# ############################################################# #

from tkinter import *
import turtle
root = Tk()

def circle(t,x,y):
	print("circle")
	t.down()
	t.color("#ff0000")
	for i in range (0,20):
		t.forward(10)
		t.rt(18)
		
def turtle1():
    x = 0; y = 0
    w = turtle.Screen()
    w.setup(1000, 700)
    w.clear()
    w.bgcolor("#ffffff")
    t = turtle.Turtle()
    circle(t,x,y)
    w.exitonclick()
   
def newWin1(): # new window definition
    newwin = Toplevel(root)
    display = Label(newwin, text="Window 1")
    display.pack()    

def newWin2(): # new window definition
    newwin = Toplevel(root)
    display = Label(newwin, text="Window 2")
    display.pack()    

button1 =Button(root, text ="Window 1", command =newWin1) 
button2 =Button(root, text ="Window 2", command =newWin2) 
button3 =Button(root, text ="Window 3", command =turtle1) 
button1.pack()
button2.pack()
button3.pack()

root.mainloop()
