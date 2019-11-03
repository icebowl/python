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
def square(t,x,y,length,tcolor):
    t.penup
    t.goto(x,y)
    t.pendown()
    #t.dot()
    t.color(tcolor)
    for i in range (0,4):
        t.forward(length)
        t.left( 90)


def main():
    x = -200; y = 0
    w = turtle.Screen()
    w.clear()
    w.bgcolor("#000000")
    t = turtle.Turtle()
    t.color("#ffffff")
    for i in range (1,50):
        prime = isprime(i)
        tcolor = "#0000ff"
        if(prime):
            tcolor = "#00ff00"
        square(t,x,y,40,tcolor)
        #print("number",i," prime = " ,prime )
        x = x + 40
    w.exitonclick()
main()
