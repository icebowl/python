c = 0 # c count
thePet = input("What pet do you have? ")
while (thePet != "rock"):
    c = c + 1
    print ("You have a " + thePet + " with a total of " + str(c) + " pet(s)")
    thePet = input("What pet do you have? ") 
