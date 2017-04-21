import RPi.GPIO as GPIO # GPIO Bibl i o the k impo r t i e r en
import time # Modul time impo r t i e r en

GPIO.setmode (GPIO.BOARD) # Verwende Board−Pinnummern
GPIO.setup (26,GPIO.OUT) # Se t z e Pin 26 (GPIO7) a l s Ausg
GPIO.output (26,True) # Lege 3 . 3V auf Pin 26
time.sleep (0.5)  # Warte 500ms
GPIO.output (26,False) # Lege 0V auf Pin 26
GPIO.cleanup () # Aufr ¨aumen