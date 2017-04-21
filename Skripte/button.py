import RPi.GPIO as GPIO 
import time 
import socket 


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

P = 7
loopbool = True
idleCounter = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(P, GPIO.IN)

while loopbool == True:
    value = GPIO.input(P)
    print(value)
    sock.sendto(str(value).encode("utf-8"),("192.168.0.21", 40))
    if value == 0:
        idleCounter += 1
        if idleCounter == 5:
            loopbool = False
            break
    else:
        idleCounter = 0        
    time.sleep(0.1)

GPIO.cleanup()
