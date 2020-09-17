# trigtable.py
import sys
import math
def cossin(t):
  radians = (t * (3.141592/180))
  h = math.cos(radians)*100
  k = math.sin(radians)*100
  return h,k

def main():
    for t in range (0,360,22):
        x,y = cossin(t)
        x = str(round(x, 3))
        y = str(round(y, 3))
        print (str(t)+" "+x+":"+y+",")


main()
