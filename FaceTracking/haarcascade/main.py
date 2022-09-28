#haarcascade classifier xml: https://github.com/opencv/opencv/tree/4.x/data

import pantilthat
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2

#Cam = PiCamera()
#Cam.rotation = 180
#Cam.resolution = (640, 480)
#Cam.framerate = 32

#RawCapture = PiRGBArray(Cam, size=(640, 480))

video = cv2.VideoCapture(0)
  
while True:

    ret, Img = video.read()
    Img = cv2.flip(Img, 0)

    gray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    haar = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)

    for (x, y, w, h) in face:
        cv2.rectangle(Img, (x, y), (x+w, y+h), (0 ,255 ,0), thickness=2)

    cv2.imshow("Frame", Img)
    cv2.waitKey(1) #Terminate by Ctrl+C in terminal

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
video.release()
cv2.destroyAllWindows()