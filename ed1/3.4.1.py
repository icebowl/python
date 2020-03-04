'''
Input a word. 
If it is "yellow" print "Correct", otherwise print "Nope". 
What happens if you type in YELLOW? YellOW? 
Does the capitalizing make a difference?
color = input("What color? ")

if (color == "yellow"):
    print ("Correct")
else:
    print ("Nope")

color = input("What color? ")
cString = color.lower()
print(cString)
if(cString == "yellow"):
    print("Correct")
else:
    print("Nope")


'''
cString = input("What color? ")
print(cString)
if(cString == "yellow"):
    print("Correct")
else:
    print("Nope")
