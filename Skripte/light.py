import RPi.GPIO as GPIO 
import time 
import socket 
import os
import thread

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Light = [32, 40, 37, 7, 38, 36, 31, 35, 33]
prev_Light = [1, 1, 1, 1, 1, 1, 1, 1, 1]
start_Light = [0, 0, 0, 0, 0, 0, 0, 0, 0]

average = 0

start = True
average_bool = True

loopbool = True

GPIO.setmode(GPIO.BOARD)



def rc_time(pin):
	reading = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.setup(pin, GPIO.IN)
	while GPIO.input(pin) == GPIO.LOW:
		reading += 1
	return reading

try:
	while True:
		for i in range(9):
			temp = rc_time(Light[i])
			if (start == True):
				start_Light[i] = temp
				print("Start {}: {}".format(i,start_Light[i]))
			elif (prev_Light[i] != temp and average > 0):
				prev_Light[i] = temp
				print("{}: {}".format(i,temp))
				if (temp > (2 * average)):
					print("{}: {}".format(i,1))
					sock.sendto(str(i).encode("utf-8"),("192.168.0.21", 40))
				else:
					print("{}: {}".format(i,0))
				
				
		start = False	
		if (start == False and average_bool == True):
			for i in range(9):
				average += start_Light[i]
			average /= 9
			average_bool = False
			print("Average: {}".format(average))
			
	#while loopbool == True:
		#sock.sendto(str(value).encode("utf-8"),("192.168.0.208", 40))
		#time.sleep(0.1)
except KeyboardInterrupt:
	pass
finally: 
	GPIO.cleanup()        