import sys
import RPi.GPIO as GPIO
import time
GPIO.setup(triggerPIN,GPIO.OUT)
buzzer = GPIO.PWM(triggerPIN, 1000)
def sound():

    triggerPIN = 23
#GPIO.setmode(GPIO.BCM)
# Set frequency to 1 Khz
    buzzer.start(10) # Set dutycycle to 10
    time.sleep(2)
#GPIO.cleanup()
#sys.exit()
