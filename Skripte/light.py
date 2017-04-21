import RPi.GPIO as GPIO 
import time 
import socket 
import os


P = 7


GPIO.setmode(GPIO.BOARD)



def rc_time(pin):
    reading = 0
    GPIO.setup(P, GPIO.OUT)
    GPIO.output(P, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(P, GPIO.IN)
    while GPIO.input(P) == GPIO.LOW:
        reading += 1
    return reading

try:
    while True:
        print(rc_time(P))
except KeyboardInterrupt:
    pass
finally: 
    GPIO.cleanup()        