import RPi.GPIO as GPIO 
import time 
import socket 
import os
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Light = [12, 16, 38, 40, 32, 37, 31, 33, 29]
prev_Light = [1, 1, 1, 1, 1, 1, 1, 1, 1]
start_Light = [0, 0, 0, 0, 0, 0, 0, 0, 0]

averageInt = 0

start = True
average_bool = True

GPIO.setmode(GPIO.BOARD)

def runSensor(i, pin):
	while True:
		temp = rc_time(pin, 0.6)
		print("{}: {}".format(i,temp))
		if (average != 0 and temp > (2 * averageInt)):
			print("{}: {}".format(i,1))
			sock.sendto(str(i).encode("utf-8"),("192.168.0.208", 40))
		else:
			print("{}: {}".format(i,0))
		
def rc_time(pin, delay):
	reading = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(delay)
	GPIO.setup(pin, GPIO.IN)
	while GPIO.input(pin) == GPIO.LOW:
		reading += 1
	return reading

def average():
	global start
	global average_bool
	global averageInt
	for k in range(9):
		temp = rc_time(Light[k], 0.1)
		if (start == True):
			start_Light[k] = temp
			print("Start {}: {}".format(k,start_Light[k]))
	start = False
	if (start == False and average_bool == True):
		for i in range(9):
			averageInt += start_Light[i]
		averageInt /= 9
		average_bool = False
		print("Average: {}".format(averageInt))
	
try:
	if __name__ == "__main__":
		average()
		for i in range(9):
			thread = Thread(target = runSensor, args=(i, Light[i],))
			thread.setDaemon(True)
			thread.start()
	while True:
		pass
except KeyboardInterrupt:
	pass
finally: 
	GPIO.cleanup()        