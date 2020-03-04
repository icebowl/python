# your code goes here
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))

totalminutes = (60*hours) + minutes
totalminutes = totalminutes + 15

newhour = int(totalminutes / 60)
newminute = int(totalminutes % 60)

if(newhour > 12):
    newhour = newhour - 12;

print("Hours: "+str(newhour))
print("Minutes: "+str(newminute))

'''
hour = int(input("Enter the hours: "))
minute = int(input("Enter the minutes: "))
minute = minute + 15
hour = int((hour - 1) + minute / 60) % 12 + 1
minute = minute % 60

print ("Hours: " + str(hour) )
print  ("Minutes: "+ str(minute))

'''
