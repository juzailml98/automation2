import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


def blue():
    GPIO.output(17,GPIO.HIGH)
    time.sleep(2)

    GPIO.output(17,GPIO.LOW)
def green():
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)

    GPIO.output(18,GPIO.LOW)
def red():
    GPIO.output(27,GPIO.HIGH)
    time.sleep(2)

    GPIO.output(27,GPIO.LOW)
