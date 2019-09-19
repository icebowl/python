import random
random.seed()
a = random.randint(1,10)
b = random.randint(1,10)
print ("What is: " + str(a) + " X " + str(b) + "?")
ans = int(input("Your answer: "))
if (a * b == ans):
   print ("Correct!")
else:
   print ("Incorrect!")
