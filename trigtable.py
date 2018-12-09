# trigtable.py
import sys
import math
def cossin(t):
  radians = (t * (3.141592/180))
  h = math.cos(radians)
  k = math.sin(radians)
  return h,k

def main():
    for t in range (0,360,15):
        x,y = cossin(t)
        x = str(round(x, 3))
        y = str(round(y, 3))
        print (x+":"+y+",")


main()
