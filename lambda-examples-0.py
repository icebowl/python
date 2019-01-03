# lambda-example-0.py

#  lambda base form
c = lambda a, b, c: a*a + b*b + c
print(c(1,2,3))

x = lambda a, b, c,x: a*x**2 + b*x + c
print(x(1,0,-9,0))
print(x(1,0,-9,1))

def multiple(n):
    #print("n",n)
    return lambda a : a * n
double = multiple(2)
print(double(11))

triple = multiple(3)
print(triple(11))

"""
The first expression x = lambda a, b, c: a*a + b*b + c
creates a function where the values of a,b, and c are used to
calculate a^2 + b^2 + c.
This is fine but I would like to build a quadtratic function and get a return values
based on the value of x.  This will do that: x = lambda a, b, c,x: a*x**2 + b*x + c

Now lets look at creating a function that  uses lambda and returns an inputself.
The following is used twice.
First to create a function based on n where n will be multiplies to the next input a.
def multiple(n):
    #print("n",n)
    return lambda a : a * n

multiple_of_five = multiple(5)
print(multiple_of_five(12))
What will this return.
"""
