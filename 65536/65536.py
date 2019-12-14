#65536.py cwc
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
	filename = filename + ".txt"
	f = open(filename, "a")

	for i in range (0,65536):
		n =  random.randint(65, 65+25)
		c = chr(n)
		f.write(c)
		#print(c,end="")
	f.close()
	 
def main():
	createRandoms()

if __name__ == '__main__':
	main()

#python 65536.py > 191213-1302.txt
