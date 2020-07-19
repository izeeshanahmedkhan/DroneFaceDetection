import cv2
import numpy as np
import mail

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

global flag
global counter
global preflag
flag = 0
counter = 0

def sendemail(im, Id):
    global flag
    global counter
    if(flag > 0 and counter == 0):
        cv2.imwrite('test.jpg',im)
        mail.sendEmail(Id)
        print("Email Sent")
        counter = 1
    elif(flag > 0 and counter <= 50):
        counter = counter + 1
    elif(flag > 0 and counter > 50):
        flag = 0
        counter = 0

while True:
    ret, im =cam.read()
    #im = cv2.flip(im, -1)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        Id = recognizer.predict(gray[y:y+h,x:x+w])

        print(Id)
        if(Id[0] == 1):
            Id = "Zeeshan"
            flag = 1
        elif(Id[0] == 2):
            Id = "Farhat"
            flag = 2
        elif(Id[0] == 3):
            Id = "Bat Affleck"
            flag = 3
        elif(Id[0] == 4):
            Id = "Naveed"
            flag = 4
        elif(Id[0] == 5):
            Id = "Moiz"
            flag = 5
        else:
            Id = "Unknow"
        
        
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
        sendemail(im, Id)
        
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()