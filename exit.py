import sys
import RPi.GPIO as GPIO
def final():
    GPIO.cleanup()
    sys.exit()
