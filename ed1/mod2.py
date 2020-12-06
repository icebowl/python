# Addition in Python
# Adding in Python has two meanings: adding strings, and adding numbers.  
# We can add using the '+' sign such as in the following examples:

x = 34
y = 12
print(x + y)

print (" * * * * * * * * * * * * * ") 

x = "hola "
y = "mundo"
print(x + y)

print (" * * * * * * * * * * * * * ") 
# We cannot add numbers to words.  
# If we wanted to add a number to the end of a string, 
# we need to first convert the number to a string by using the str function:

print("String " + str(34))


print (" * * * * * * * * * * * * * ") 

#Similarly, to numerically add string representations of numbers 
# (like what we get from input), we can convert strings to numbers using the int function. In the example below, we confirm that anything entered by the user is first changed to an integer, then add it to the integer 34:

y = int(input("Enter a value : " )) #user inputs a number
print(y + int("3000"))


# The '=' operator (such as in x = x + 1) evaluates the right side of the expression first, 
# and then sets the value of the variable on the left side to your result.

# Order of Operations
# Python follows an order of operations which is the same for mathematical expressions as in standard math. We can use parentheses to group expressions.



# c = (f – 32) * 5/9 : subtracts 32 from f first, multiplies by 5 the then divides by 9

# c = f – 32 * 5/9 : multiplies 32 by 5, divides that by 9, then subtracts this value from f

f = 33
c = (f - 32) * (5/9)
print(c)
c = f - 32 * 5/9 
print(c)
# Exponents are done using the '**' operator

print(7 ** 2)

print(" * * * * * * * * * * * * * ")

a = 100
print (a ** 0.5)




