# plot-dictionary.py
import tkinter as tk
import turtle

def main():
	#table is a dictionary
	table = {1.0:0.0,
				0.966:0.259,
				0.866:0.5,
				0.707:0.707,
				0.5:0.866,
				0.259:0.966,
				0.0:1.0,
				-0.259:0.966,
				-0.5:0.866,
				-0.707:0.707,
				-0.866:0.5,
				-0.966:0.259,
				-1.0:0.0
			}
	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	#turtle graphics
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#tWin = turtle.Screen()
	for h,k in table.items():  #get the items in the dictionary
		print(h, k) # trace code
		#x,y = table[n]
		r = 100
		h = h * r
		k = k * r
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(4)
	for h,k in table.items():  #get the items in the dictionary
		print(h, k) # trace code
		#x,y = table[n]
		r = 100
		h = h * r
		k = (-1 * k) * r
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(4)
	twin.exitonclick()

main()

"""



(0, 1.0, 0.0)
(15, 0.9659258403858574, 0.258818992492582)
(30, 0.8660254582502496, 0.49999990566243635)
(45, 0.7071068967259818, 0.7071066656470943)
(60, 0.5000001886751095, 0.866025294852786)
(75, 0.25881930815220316, 0.9659257558050799)
(90, 3.2679489653813835e-07, 0.9999999999999466)
(105, -0.2588186768329332, 0.9659259249665316)
(120, -0.4999996226497098, 0.8660256216476206)
(135, -0.7071064345681316, 0.7071071278047935)
(150, -0.8660251314552299, 0.5000004716877294)

(165, -0.9659256712241994, 0.25881962381179674)
(180, -0.9999999999997864, 6.535897930762419e-07)
(195, -0.9659260095471028, -0.25881836117325646)
(210, -0.8660257850448994, -0.4999993396369297)
(225, -0.7071073588835299, -0.7071062034890931)
(240, -0.5000007547002956, -0.8660249680575813)
(255, -0.2588199394713623, -0.9659255866432157)
(270, -9.803846891701863e-07, -0.9999999999995194)
(285, 0.25881804551355275, -0.9659260941275707)
(300, 0.49999905662409616, -0.8660259484420856)
(315, 0.7071059724099793, -0.7071075899621907)
(330, 0.86602480465984, -0.5000010377128091)
(345, 0.9659255020621287, -0.25882025513090107)
This code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
Each key has a value of 0 as an integer.
To retrieve the values in the dictionary "table" a for loop is used.
The x cooridate on a python turtle screen corresponds to h while
the y value cooresponds to k.
**************************************
for h,k in table.items():  #get the items in the dictionary
		print(h, k) #trace code
h and k are then ploted using
		t.goto(h,k)
		t.pendown()
		t.circle(5)

Change the values from 0 to another integer.
Try to make something grovey.
"""
