#!/usr/bin/python3
import thread
import time
key = 0

# Define functions for each thread
def watch_keyboard(threadName, delay):	# THREAD 1 looks at keyboard every
	global key							# delay value
	while 1:
		time.sleep(delay)
