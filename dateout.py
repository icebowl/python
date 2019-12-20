import datetime

def getTimeString():
	d = datetime.datetime.now()
	y = d.year - 2000 
	timestring = str(y) + str(d.month) + str(d.day)+"-"+str(d.hour)+str(d.minute)+"."+str(d.second)
	timestring = str(y) + str(d.month) + str(d.day)+"-"+str(d.hour)+str(d.minute)+"."+str(d.second)
	print(timestring)
	return timestring


def main():
	ts = getTimeString()
	print(ts)
	filename = ts+".txt"
	print(filename)

main()
###
