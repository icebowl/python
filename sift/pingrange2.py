# python2 pingrange.py
import subprocess

for ping in range(1,255):
    address = "192.168.1." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address],stdout=subprocess.PIPE)
    if res == 0:
        print ("ping to", address, "OK")
    elif res == 2:
        print ("no response from", address)
    else:
        print ("ping to", address, "failed!")
