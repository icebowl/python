import datetime

def getTimeString():
	d = datetime.datetime.now()
	y = d.year - 2000 
	timestring = str(y) + str(x.month) + str(x.day)+"-"+str(x.hour)+str(x.minute)+".txt"
	print(timestring)
	return timestring

def main():
	ts = getTimeString()
	print(ts)

main()
###
