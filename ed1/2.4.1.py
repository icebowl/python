'''
Write the code to input a number and print the square root. Use the absolute value function to make sure that if the user enters a negative number, the program does not crash.
'''
import math
v = float(input("Input a number to be squarerooted :"))
sv = math.sqrt(math.fabs(v))
print (sv)
