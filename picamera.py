from picamera import PiCamera
import time

camera=PiCamera()
camera.vflip=True
camera.start_preview()
time.sleep(4)
camera.start_recording("face.h264")
time.sleep(20)
camera.stop_recording()

