#!/usr/bin/env python3
from time import sleep
def matrix():
  
	X = ["1002",
         "0000",
         "0000",
         "4003"]
	Y = ["0123",
         "4567",
         "89AB",
         "CDEF"]
	x,y = 10,10
	for h in range (0,4):
		y = y - 1
		for k  in range (0,4):
			x = x - 1
			#print(X[h][k]," ",end="")
			#print(h,",",k," ",end="")
			print(x,y," - ",end="")
			theBlock = X[h][k]
			c = 0  # wool 35,0  WHITE
			if (theBlock == "1"):
				c = 1 # wool 35,1  ORANGE
			if (theBlock == "2"):
				c = 2 # wool 35,2  DARK PINK 
			if (theBlock == "3"):
				c = 3 # wool 35,3  LIGHT BLUE 
			if (theBlock == "4"):
				c = 4 # wool 35,4  YELLOW
			print(" ",c," ",end="")
		print()
    
def main():
  matrix()


if __name__ == "__main__":
  main()
