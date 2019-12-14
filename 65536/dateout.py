import datetime

def getDateString():
	dt = datetime.datetime.now()
	y = dt.year - 2000 
	hr = dt.hour
	if hr < 10:
		hr = "0" + str(hr)
	me = dt.minute
	if me < 10:
		me = "0" + str(me)
	timestring = str(y) + str(dt.month) + str(dt.day)+"-"+str(hr)+str(me)+"."+str(dt.second)
	return timestring
	'''print(timestring)
	print(y)
	print(x)
	print(x.year)
	print(x.month)
	print(x.day)
	print(x.hour)
	print(x.minute)
	'''
def main():
	datetime = getDateString()
	print(datetime)
	
if __name__ == '__main__':
	main()
