hour = int(input("Hour : "))
minute = int(input("Minute : "))

totalminutes = (60*hour) + minute
totalminutes = totalminutes + 15

newhour = int(totalminutes / 60)
newminute = totalminutes % 60

print(newhour,newminute)
