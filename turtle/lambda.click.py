from turtle import Turtle, Screen

def drawSquare(turtle):
    turtle.goto(100, 0)
    turtle.goto(100, 100)
    turtle.goto(0, 100)
    turtle.goto(0, 0)

screen = Screen()

screen.tracer(0, 0)

screen.onclick(lambda x, y: screen.update())

turtle = Turtle()

drawSquare(turtle)

screen.mainloop()
