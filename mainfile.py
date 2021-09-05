import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print ("LED on")
GPIO.output(17,GPIO.HIGH)
time.sleep(2)
print ("LED off")
GPIO.output(17,GPIO.LOW)
print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(2)
print ("LED off")
GPIO.output(18,GPIO.LOW)
print ("LED on")
GPIO.output(27,GPIO.HIGH)
time.sleep(2)
print ("LED off")
GPIO.output(27,GPIO.LOW)

import running
