from threading import Thread
import time

def runA():
    while True:
        print ('A')
        time.sleep (0.5)

def runB(arg):
    while True:
        print (arg)
        time.sleep (0.5)

if __name__ == "__main__":
    t1 = Thread(target = runB, args=(1,))
    t2 = Thread(target = runB, args=(2,))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass