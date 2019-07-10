import random
random.seed()

# TODO: Update the following two lines with a call to a function
# from the random library that generates a random number between
# 1 and 10, inclusive.
#a = 6 # HINT: Replace 6 with a function call
#b = 3 # HINT: Replace 3 with a function call
import random
a = random.randint(1,10)
b = random.randint(1,10)


print ("What is: " + str(a) + " X " + str(b) + "?") 
ans = int(input("Your answer: ")) 
if (a * b == ans): 
    print ("Correct!") 
else: 
    print ("Incorrect!")
