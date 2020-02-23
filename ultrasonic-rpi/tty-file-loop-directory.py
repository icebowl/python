# ttyAMCO.py
# nohup python ttyAMCO-file-loop.py &
# ps aux|grep python
# kill <the pid>
import sys,os,serial
from datetime import datetime
import time

def getTimeString():
	now = datetime.now() # current date and time
	timeString = now.strftime("%Y%m%d-%H%M%S")
	#print("date and time:",timeString)
	return timeString[2:len(timeString)]

def monitortty(filepath,touch_ts_txt):
	ts = getTimeString()
	fileName = touch_ts_txt
	print("filename monitor contcatinated",fileName)
	print(" * * * ")
	f = open(fileName, "a")
	t_end = time.time() + 10 
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
	# create directory and cd into that directory
	nowDir = getTimeString()
	mk_nowDir = "mkdir "+nowDir
	os.system(mk_nowDir)
	nowDirHome = "~/data/"+nowDir+"/"
	DirHome = nowDir+"/"
	#print("nowDirHome",nowDirHome)
	#os.system(cd_nowDir)
	#os.system('pwd')
	for n in range (0,2):
		#monitortty(n)
		#testTimeLoop(n)
		ts = getTimeString()
		touch_theFileName = "touch "+nowDirHome+ts+".txt"
		theFileName = DirHome+ts+".txt"
		#print("touch_ts_txt ",touch_ts_txt)
		os.system(touch_theFileName)
		monitortty(nowDirHome,theFileName)
		#time.sleep(1)
		
if __name__ == '__main__':
	main()
