# Pure Python 3.x demo, 256 colors
# Works with bash under Linux and MacOS

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

def print_six(row, format):
    for col in range(6):
        color = row*6 + col + 4
        if color>=0:
            text = "{:3d}".format(color)
            print (format(text,color), end=" ")
        else:
            print("   ", end=" ")

for row in range(-1,42):
    print_six(row, fg)
    print("",end=" ")
    print_six(row, bg)
    print()

# Simple usage: print(fg("text", 160))
