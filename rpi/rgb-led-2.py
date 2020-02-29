import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

REDPIN = 25
GREENPIN = 24
BLUEPIN = 23
GPIO.setup(REDPIN, GPIO.OUT)
GPIO.output(REDPIN,0)
GPIO.setup(GREENPIN, GPIO.OUT)
GPIO.output(GREENPIN,0)
GPIO.setup(BLUEPIN, GPIO.OUT)
GPIO.output(BLUEPIN,0)

GPIO.output(REDPIN,0)
GPIO.output(GREENPIN,1)
GPIO.output(BLUEPIN,1)
'''
try:
	while(True):
		request = input("RGB--> ")
		print(request[0])
		print(request[1])
		print(request[2])
		
except KeyboardInterrupt:
	
'''
time.sleep(5)
GPIO.cleanup()
