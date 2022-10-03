from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2

import Camera

Cam = PiCamera()
Cam.rotation = 180
Cam.resolution = (640, 480)
Cam.framerate = 32

RawCapture = PiRGBArray(Cam, size=(640, 480))
for frame in Cam.capture_continuous(RawCapture, format="bgr", use_video_port = True):
    
    image = frame.array
    RawCapture.truncate(0)

    approx = Camera.LBdetection(image)

    cv2.imshow("Input", image)
    cv2.imshow("Output", approx)
    cv2.waitKey(1)