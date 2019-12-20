first = input("What is your first name? ")
last = input("What is your last name? ")
idNum = int(input("Student ID: "))
stars = "*************************************************"
starends = "*                                               *"
print(stars)
print(starends)
print("*\t" + last + ", " + first+ "\t\tID: " + str(idNum) + "\t*")
print(starends)
print(stars)
print(starends)
stp = " "
room = 0
count = 1
while (stp != "STOP" ):
   stp = input ("Enter the next class, STOP to end: ")
   if (stp != "STOP"):
      rm = int(input("Enter the room number: "))
      print("*\tBlock " + str(count) + ": " + stp + "\tRoom: " + str(rm) +" \t*")
      count = count + 1
print(starends)
print(stars)
print(stars)
print(stars)
