# lambda-sort-0.def foo():
def quadtratic_function(a,b,c):
    return lambda x: a*(x**2) + b*x + c

a1 = quadtratic_function(1,2,1)
print(a1(1))

a2 = quadtratic_function(1,2,1)(2)

print(a2)
