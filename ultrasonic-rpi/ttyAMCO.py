# ttyAMCO.py
import sys,os,serial
from datetime import datetime
import time

def getTimeString():
	now = datetime.now() # current date and time
	timeString = now.strftime("%Y~%m~%d~%H-%M-%S")
	print("date and time:",timeString)
	return timeString[2:len(timeString)]

def monitortty():
	ts = getTimeString()
	fileDate = ts+".txt"
	f = open(fileDate, "a")
	t_end = time.time() + 5 
	serial_port = '/dev/ttyACM0'
	baud_rate = 9600
	srl =serial.Serial(serial_port,baud_rate)
	while time.time() < t_end:
		sline = srl.readline()
		f.write(str(sline))
	ts = getTimeString()
	f.write(ts)
	f.close()
	
def testTimeLoop():
	ts = getTimeString()
	fileDate = ts+".txt"
	f = open(fileDate, "a")
	t_end = time.time() + 5 
	while time.time() < t_end:
		print(time.time())
		tnowString = str(time.time())
		# * * * * 
		f.write(tnowString+str("\n"))
		#print(tnowString,end="")
	f.close()
	
def main():
	print("Start Serial Monitor")
	ts = getTimeString()
	fileDate = ts+".txt"
	print(ts, fileDate)
	monitortty()
	#testTimeLoop()

if __name__ == '__main__':
	main()
