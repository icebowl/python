import datetime

x = datetime.datetime.now()
y = x.year - 2000 
timestring = str(y) + str(x.month) + str(x.day)+"-"+str(x.hour)+str(x.minute)+".txt"
print(timestring)
print(y)
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)

