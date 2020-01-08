##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial

serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)

ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline();
    #line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    print(line);
