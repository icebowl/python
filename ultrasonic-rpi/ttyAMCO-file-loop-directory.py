# ttyAMCO.py
# nohup python ttyAMCO-file-loop.py &
# ps aux|grep python
# kill <the pid>
import sys,os,serial
from datetime import datetime
import time

def createDirectory():
	ts = getTimeString()
	os.system('ls')
	makeDir = "mkdir "+ts
	print(makeDir)
	return makeDir

def getTimeString():
	now = datetime.now() # current date and time
	timeString = now.strftime("%Y%m%d-%H%M%S")
	print("date and time:",timeString)
	return timeString[2:len(timeString)]

def monitortty(dirPath):
	ts = getTimeString()
	fileDate = ts+"n"+str(n)+".txt"
	f = open(fileDate, "a")
	addSeconds2loop =  3
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
	# create directory and cd into that directory
	nowDir = getTimeString()
	mk_nowDir = "mkdir "+nowDir
	os.system(mk_nowDir)
	nowDirHome = "/home/pi/data/"+nowDir+"/"
	print("nowDirHome",nowDirHome)
	#os.system(cd_nowDir)
	#os.system('pwd')
	for n in range (0,3):
		#monitortty(n)
		#testTimeLoop(n)
		ts = getTimeString()
		touch_ts_txt = "touch "+nowDirHome+ts+".txt"
		print("touch_ts_txt",touch_ts_txt)
		os.system(touch_ts_txt)
		time.sleep(1)
		
if __name__ == '__main__':
	main()
