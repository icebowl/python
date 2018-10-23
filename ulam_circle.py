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
    t.penup()
    t.begin_fill()
    #t.dot()
    t.color(tcolor)
    t.circle(15)
    t.end_fill()
def main():
    vector = [-1,0,90,180,180,270, \
                270,0,0,0,90, \
                90,90,180,180,180, \
                180,270,270,270,270, \
                0,0,0,0,0]
    x = -400; y = 0
    w = turtle.Screen()
    w.setup(1000, 700)
    w.clear()
    w.bgcolor("#ffffff")
    t = turtle.Turtle()
    t.penup()
    t.goto(0,0)
    t.speed(0)
    t.pendown()
    for i in range (1,26):
        prime = isprime(i)
        print(prime)
        tcolor = "#0000ff"
        if((prime == True) and (i  > 1)):
            tcolor = "#00ff00"
        t.color(tcolor)
        t.dot()
        #t.circle(15)
        t.seth(vector[i])
        tcolor = "#0000ff"
        t.color(tcolor)
        t.forward(30)
        #print("number",i," prime = " ,prime )

    w.exitonclick()
main()
