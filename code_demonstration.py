# all the necessary modules are imported
import cv2
import os
from keras.models import load_model
import numpy as np
import pygame
from pygame import mixer
import time



mixer.init()
sound = mixer.Sound('sound/alarm.wav')
model_path=os.getcwd()
pather=r""+model_path
face = cv2.CascadeClassifier(model_path+"\haarmodels/haarcascade_frontalface_alt.xml")
leye = cv2.CascadeClassifier(model_path+"\haarmodels/haarcascade_lefteye_2splits.xml")
reye = cv2.CascadeClassifier(model_path+"\haarmodels/haarcascade_righteye_2splits.xml")





model = load_model(model_path+"\cnnCat2.h5")


print("recieved the model,and casscade,and loaded the necessary packages")

cap = cv2.VideoCapture(0)
if cap.isOpened():
    sound.play()
    pygame.time.delay(2000)
    sound.stop()
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

score=0


height=480
width=640
while(True):
    localtime1=time.time()
    rpred=[0,32]
    lpred=[0,32]
    ret, frame = cap.read()




    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
    print("the number of faces detected is",len(faces))
    #left_eye = leye.detectMultiScale(gray)

    right_eye =  reye.detectMultiScale(gray)
    #print("the value of right eye",len(right_eye))



    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )
    for (x,y,w,h) in right_eye:


        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (0,0,255) , 1 )
        r_eye=frame[y:y+h,x:x+w]

        r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
        r_eye = cv2.resize(r_eye,(24,24))
        r_eye= r_eye/255
        r_eye=  r_eye.reshape(24,24,-1)
        r_eye = np.expand_dims(r_eye,axis=0)
        rpred = model.predict_classes(r_eye)

        break


    if(rpred[0]==0) or (len(faces)==0):
        print('eyes closed')
        score=score+1
        cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)


    else:
        print('eyes open')
        score=score-2
        cv2.putText(frame,"Open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)



    if(score<0):
        score=0
    cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,0,0),1,cv2.LINE_AA)
    if(score>50):
        score=50
        sound.play()


        #except:  # isplaying = False
            #pass
    else:
        sound.stop()

    cv2.imshow('frame',frame)
    localtime2=time.time()
    print(localtime2-localtime1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
