import led
led.blue()
led.red()
led.green()
import buzzer
buzzer.sound()
import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("camera is working")


else:
    print("camera is not working")

    

cap.release()
cv2.destroyAllWindows()
