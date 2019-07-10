'''
Write a program that accepts a number as input, and prints just the decimal portion.
'''
n = float(input("Input a decimal greater than 1 : "))
ni = int(n)
nd = n % ni

print(n,ni,nd)
