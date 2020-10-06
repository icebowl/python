#65536.py cwc
import os
import random
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

def createRandoms():
	filename = getDateString()
	filename = "touch "+filename + ".txt"
	os.system(filename)	
def main():
	createRandoms()

if __name__ == '__main__':
	main()

#python 65536.py > 191213-1302.txt

