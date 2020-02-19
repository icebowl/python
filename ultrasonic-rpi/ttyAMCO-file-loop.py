# ttyAMCO.py
# nohup python ttyAMCO-file-loop.py &
# ps aux|grep python
# kill <the pid>
import sys,os,serial
from datetime import datetime
import time

def getTimeString():
	now = datetime.now() # current date and time
	timeString = now.strftime("%Y~%m~%d~%H-%M-%S")
	print("date and time:",timeString)
	return timeString[2:len(timeString)]

def monitortty(n):
	ts = getTimeString()
	fileDate = ts+"n"+str(n)+".txt"
	f = open(fileDate, "a")
	addSeconds2loop = 60
	t_end = time.time() + addSeconds2loop
	serial_port = '/dev/ttyACM0'
	baud_rate = 9600
	srl =serial.Serial(serial_port,baud_rate)
	while time.time() < t_end:
		sline = srl.readline()
		f.write(str(sline))
	ts = getTimeString()
	f.write(ts)
	f.close()
	
def testTimeLoop(n):
	ts = getTimeString()
	fileDate = ts+"n"+str(n)+".txt"
	f = open(fileDate, "a")
	addSeconds2loop = 60
	t_end = time.time() + addSeconds2loop
	while time.time() < t_end:
		print(time.time())
		tnowString = str(time.time())
		# * * * * 
		f.write(tnowString+str("\n"))
		#print(tnowString,end="")
	ts = getTimeString()
	f.write(ts)
	f.close()
	
def main():
	print("Start Serial Monitor")
	ts = getTimeString()
	fileDate = ts+".txt"
	print(ts, fileDate)
	for n in range (0,5):
		#monitortty(n)
		testTimeLoop(n)

if __name__ == '__main__':
	main()
