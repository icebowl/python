# ulam turtle cwc
import turtle
import math




def isprime(n):
    nd = float(n)
    prime = True
    pivot = int(math.sqrt(nd))
    for d in range (2,n):
        d = float(d)
        #print ((nd / d),int(nd / d))
        if ((nd / d) == int(nd / d)):
            prime = False
            break
    return prime

def star(t,length,tcolor):
    t.penup
    t.goto(0,0)
    t.pendown()
    #t.dot()
    for a in range (0,360,15):
        t.seth(a)
        t.width(5)
        t.color(tcolor)
        t.forward(length)
        t.color("#ff7f00")
        t.width(1)
        t.back(length)

def main():
    x = -200; y = 0
    w = turtle.Screen()
    w.clear()
    w.bgcolor("#ffffff")
    t = turtle.Turtle()
    t.color("#000000")
    tcolor = "#00ddcc"
    star(t,100,tcolor)
        #print("number",i," prime = " ,prime )
    w.exitonclick()
main()
