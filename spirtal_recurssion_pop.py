import turtle

turt = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(turt, lineLen):
    if lineLen > 0:
        turt.forward(lineLen)
        turt.right(90)
        drawSpiral(turt,lineLen-5)


def main():
	lineLen = 100
	if lineLen > 0:
		turt.forward(lineLen)
		turt.right(90)
	drawSpiral(turt,100)
	myWin.exitonclick()

main()
