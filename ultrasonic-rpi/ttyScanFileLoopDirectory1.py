# ttyScanFileLoopDirecoty*.py
# nohup python ttyScanFileLoopDirecoty0.py &
# ps aux | grep python
# ps -ef | grep python
# kill <the pid>
import sys,os,serial
from datetime import datetime
import time

def getTimeString():
	now = datetime.now() # current date and time
	timeString = now.strftime("%Y%m%d-%H%M%S")
	#print("date and time:",timeString)
	return timeString[2:len(timeString)]

def monitortty(filepath,touch_ts_txt,time4while):
	ts = getTimeString()
	fileName = touch_ts_txt
	print("fileName ",fileName)
	print(" * * * ")
	f = open(fileName, "a")
	t_end = time.time() + time4while
	serial_port = '/dev/ttyACM0'
	baud_rate = 9600
	srl =serial.Serial(serial_port,baud_rate)
	while time.time() < t_end:
		sline = srl.readline()
		f.write(str(sline))
	ts = getTimeString()
	f.write(ts)
	f.close()
	
def main():
	# create directory and get path to the directory
	nowDir = getTimeString() # directory is the time string
	mk_nowDir = "mkdir /home/pi/data/"+nowDir # add mkdir to nowDir string
	os.system(mk_nowDir) # execute mkdir nowDir
	nowDirHome = "/home/pi/data/"+nowDir+"/"
	DirHome = "/home/pi/data/"+nowDir+"/" # add / to the end of nowDir
	print ("path and filename ",DirHome)
	for n in range (0,12):
		ts = getTimeString()
		touch_theFileName = "touch "+nowDirHome+ts+".txt"
		theFileName = DirHome+ts+".txt" #this sets the file name with path
		#print("touch_ts_txt ",touch_ts_txt)
		os.system(touch_theFileName)
		seconds2monitor = (60*5)
		monitortty(nowDirHome,theFileName,seconds2monitor)
		print("Debug nowDirHome  ",nowDirHome )
		os.system("tree /home/pi/data/")
	os.system("mv /home/pi/data/20* /home/pi/data/moveData")
if __name__ == '__main__':
	while(1):
		main()
