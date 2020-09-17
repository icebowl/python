import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(130)
tommy.ht()
'''
0 100.0:0.0,
22 92.718:37.461,
44 71.934:69.466,
66 40.674:91.355,
88 3.49:99.939,
'''
draw_circle(tommy, "#000000", 130, 0, -117)

draw_circle(tommy, "#2C3E50", 13, 100, 0)
draw_circle(tommy, "#34495E", 13, 93, 37)
draw_circle(tommy, "#7F8C8D", 13, 71, 70)
draw_circle(tommy, "#95A5A6", 13, 41, 91)

draw_circle(tommy, "#BDC3C7", 13, -3, 100)
draw_circle(tommy, "#E0E0E0", 13, -41, 91)
draw_circle(tommy, "#F5F5F5", 13, -72, 70)
draw_circle(tommy, "#E74C3C", 13, -93, 37)

draw_circle(tommy, "#E67E22", 13, -100, 0)
draw_circle(tommy, "#F1C40F", 13, -93, -37)
draw_circle(tommy, "#2ECC71", 13, -71, -70)
draw_circle(tommy, "#1ABC9C", 13, -41, -91)

draw_circle(tommy, "#3498DB", 13, 3, -100)
draw_circle(tommy, "#9B59B6", 13, 41, -91)
draw_circle(tommy, "#BE643C", 13, 71, -70)
draw_circle(tommy, "#71B09F", 13, 93, -37)

w = turtle.Screen()
w.exitonclick()
'''
0 100.0:0.0,
22 92.718:37.461,
44 71.934:69.466,
66 40.674:91.355,
88 3.49:99.939,
110 -34.202:93.969,
132 -66.913:74.315,
154 -89.879:43.837,
176 -99.756:6.976,
198 -95.106:-30.902,
220 -76.604:-64.279,
242 -46.947:-88.295,
264 -10.453:-99.452,
286 27.564:-96.126,
308 61.566:-78.801,
330 86.602:-50.0,
352 99.027:-13.917,


#2C3E50 base00
#34495E base01
#7F8C8D base02
#95A5A6 base03
#BDC3C7 base04
#e0e0e0 base05
#f5f5f5 base06

#ECF0F1 base07

#E74C3C base08
#E67E22 base09
#F1C40F base0a
#2ECC71 base0b
#1ABC9C base0c
#3498DB base0d
#9B59B6 base0e
#be643c base0f
#71b09f celeste

'''
