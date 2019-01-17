# create three different files using the lambda quadtratic_function
# * * * * * * * * * * * * * * * * * * * * *
# file 1 : lambda1.py
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

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
#file 3 : quadratic.py

def quadtratic_function(a,b,c):
    return lambda x: a*(x**2) + b*x + c

a1 = quadtratic_function(1,2,1)
print(a1(1))
print("Input a,b and c from a quadratic equation in the form of ")
print("x =  ax^2 + bx + c")

a = input(" Input a ",end="")
b = input(" Input b ",end="")
c= input(" Input c ",end="")
a2 = quadtratic_function(1,2,1)(2)

# end of the quadratic.py files
