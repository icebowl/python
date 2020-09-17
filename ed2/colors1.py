import PySimpleGUI
#import simplegui
import random

frameWidth = 500

def draw_handler(canvas):

    for i in range (1, 3000):

        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)

        randRGBColor = "RGB( " + str(r) + "," + str(g) + "," + str(b) + ")"
        backg = "RGB( " + str(r) + "," + str(g) + "," + str(b) + ")"

        x = random.randint(2, frameWidth)
        y = random.randint(2, frameWidth)

        canvas.draw_point((x, y), randRGBColor)
        frame.set_canvas_background(backg)

frame = PySimpleGUI.create_frame('Colors', frameWidth, frameWidth) 
frame.set_draw_handler(draw_handler)
frame.start()
