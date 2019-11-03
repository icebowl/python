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
    vector = [0,90,180,180,270, \
                270,0,0,0,90, \
                90,90,180,180,180, \
                180, 270,270,270,270, \
                0,0,0,0]
    x = -400; y = 0
    w = turtle.Screen()
    w.setup(1000, 700)
    w.clear()
    w.bgcolor("#000000")
    t = turtle.Turtle()
    t.penup
    t.goto(0,0)
    t.speed(5)
    t.color("#ffffff")
    for i in range (1,25):
        prime = isprime(i)
        tcolor = "#0000ff"
        if(prime):
            tcolor = "#00ff00"
        square(t,x,y,30,tcolor)
        t.seth(vector[i])
        t.forward(30)
        #print("number",i," prime = " ,prime )

    w.exitonclick()
if __name__ == '__main__':
	main()
