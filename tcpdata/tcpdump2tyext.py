# ttyAMCO.py
# nohup python ttyAMCO-file-loop.py &
# ps aux|grep python
# kill <the pid>
import sys,os
from datetime import datetime
import time

def getTimeString():
	now = datetime.now() # current date and time
	timeString = now.strftime("%Y%m%d-%H%M%S")
	#print("date and time:",timeString)
	return timeString[2:len(timeString)]

	
def main():
	# create directory and cd into that directory
	nowString = getTimeString()
	filePath = "~/tcpdata/"
	nowFile = nowString+".txt"
	tcpDumpCopmmand = "tcpdump -c 100 -x > "+filePath+nowFile
	os.system(tcpDumpCopmmand)
		
if __name__ == '__main__':
	main()
