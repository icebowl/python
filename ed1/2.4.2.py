'''
Write a program that accepts a number as input, and prints just the decimal portion.
'''
import math
n = float(input("Input a decimal number : "))
ni = int(n)
n = ni - n
print(math.fabs(n))

'''
import math
x = float(input ("Enter a number: "))
y = int(x)
x = x - y
print(math.fabs(x))

'''
