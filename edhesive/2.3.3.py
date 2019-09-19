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
