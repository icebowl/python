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

try:
	while(True):
		request = input("RGB *** >")
		print(request)
		if(len(request) == 3):
			GPIO.output(REDPIN,int(request[0]))
			GPIO.output(GREENPIN,int(request[1]))
			GPIO.output(BLUEPIN,int(request[2]))
except KeyboardInterrupt:
	GPIO.cleanup()
