# create three different files using the lambda quadtratic_function
# * * * * * * * * * * * * * * * * * * * * *
# file 1 : lambda1.py
x = lambda a, b, c : a + b + c
fx = x(5,6,2)
print(x)

# end of the lambda1.py files

# * * * * * * * * * * * * * * * * * * * * *
#file 2 : lambda2.py
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# * * * * * * * * * * * * * * * * * * * * *
#file 3 : quadratic_lambda.py

def quadtratic_function(a,b,c):
    return lambda x: a*(x**2) + b*x + c

a1 = quadtratic_function(1,2,1)
print(a1(1))
print("Input a,b and c from a quadratic equation in the form of ")
print("x =  ax^2 + bx + c")
# we have a problem here
a = input("Input a ")
b = input("Input b ")
c=  input("Input c ")
a2 = quadtratic_function(a,b,c)
fx = a2(1)
print("f(x) = ",fx)
# end of the quadratic.py files
