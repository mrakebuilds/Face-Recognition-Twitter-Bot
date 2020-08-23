import numpy as np
import cv2
from config import getApi
import os
from PIL import Image
import time
import random

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,)

    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        
        
        
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            time.sleep(2)
            
        
            im = Image.open (r"Twitter Notif.jpg") #place the picture location here
            im.show()
            api = getApi()

            def postStatus(update):
                stat  = api.PostUpdate(update)
                print (stat)
            
            statss = [f"guys, this person is staring like a weirdo", f"they keeps locking eyes with me", f"i see you dude, i see you", f"please stop staring at me", f"ong bro you kinda ugly", f"IS THERE A PROBLEM?", f"bro keep looking at me and imma act up"]
            stast = statss[random.randint(0,len(statss)-1)]
            postStatus(stast)  


    cv2.imshow('Facial Recognition',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()