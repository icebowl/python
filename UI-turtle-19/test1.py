from tkinter import *
import turtle
 
  
def circle(t,x,y):
    print("circle")
    t.down()
    t.color("#ff0000")
    for i in range (0,20):
        t.forward(10)
        t.rt(18)
          
def turtle1():
    try:
        turtle.TurtleScreen._RUNNING = True
        x = 0; y = 0
        w = turtle.Screen()
        w.setup(800, 700)
        w.title("Welcome to the turtle zoo!")
        w.clear()
        w.bgcolor("#ffffff")
        w.visible = True
        t = turtle.Turtle()
        circle(t,x,y)
        w.exitonclick()
    finally:
        turtle.Terminator()
 
 
def newWin1(): # new window definition
    newwin = Toplevel()
    display = Label(newwin, text="Window 1")
    display.pack()    
  
def newWin2(): # new window definition
    newwin = Toplevel()
    display = Label(newwin, text="Window 2")
    display.pack()    
  
 
def main():
    root = Tk()
    import sys
    print(sys.version)
    button1 =Button(root, text ="Window 1", command =newWin1) 
    button2 =Button(root, text ="Window 2", command =newWin2) 
    button3 =Button(root, text ="Turtle Window", command =turtle1) 
    button1.pack()
    button2.pack()
    button3.pack()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
