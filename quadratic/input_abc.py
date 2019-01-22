# input_abc.py
# this python code uses class_quadtric.py
from class_quadratic  import *
def main():
    print("Input a,b and c from an equation ax^2 + bx + c :")
    # get inputs
    a = float(input("Input a: "))
    b = float(input("Input b: "))
    c = float(input("Input c: "))
    #end get inputs
    p1 = QuadraticEquation(a,b,c)
    x1 = p1.x1()
    x2 = p1.x2()
    print ("Discriminant = ",p1.discriminant())
    print ("x1 = ",x1," x2 = ",x2)

if __name__ == "__main__":
    main()
