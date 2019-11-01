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

def circler(t,x,y,r,tcolor):
    t.penup()
    t.goto(x,y)
    increment = (5*math.pi/180)
    d = 0
    while(d <= 2*math.pi):
        if (d == 0):
            t.penup()
            t.goto(x+r,y)
        h = int(math.cos(d)*r)
        k = int(math.sin(d)*r)
        #print("d ",x,y)
        t.pendown()
        t.goto(h+x,k+y)
        d = d + increment
    t.penup()
    #t.begin_fill()
    #t.dot()
    #t.end_fill()

def ulam():

    vector = [-1,0,90,180,180,270, \
                270,0,0,0,90, \
                90,90,180,180,180, \
                180,270,270,270,270, \
                0,0,0,0,0]
    x = -400; y = 0
    w = turtle.Screen()
    #w.setup(1000, 700)
    w.clear()
    w.bgcolor("#fdf6e3")
    t = turtle.Turtle()
    t.penup()
    t.goto(0,0)
    t.speed(0)
    t.pendown()
    for i in range (1,26):
        prime = isprime(i)
        #print(prime)
        tcolor = "#268bd2"
        if((prime == True) and (i  > 1)):
            x,y = t.pos()
            x = int(x); y = int(y)
            #print(x,y)
            tcolor = "#859900"
            circler(t,x,y,10,tcolor)
            t.goto(x,y)
        t.color(tcolor)
        t.dot()
        #t.circle(15)
        t.pendown()
        t.seth(vector[i])
        tcolor = "#268bd2"
        t.color(tcolor)
        t.forward(30)
        #print("number",i," prime = " ,prime )
    w.exitonclick()
ulam()
