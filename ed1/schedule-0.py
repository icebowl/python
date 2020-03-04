#cwc
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
student_id = int(input("Student ID: "))
star49 = "*************************************************"
starEnd = "*                                               *"
print(star49)
print(starEnd)
print("*\t" + last_name + ", " + first_name+ " ID: " + str(student_id) )
print(starEnd)
print(star49)
print(starEnd)
myclass =""
roomNummber  = 0
while(myclass != "STOP"):
	myclass = input("Enter the next class,")
	if(myclass != "STOP"):
		roomNumber = input("Enter the room number: ")
		print(myclass + "\tRoom: " + roomNumber )

