#using SSD mobilenet from mediapipe API
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import mediapipe as mp

import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


Cam = PiCamera()
Cam.rotation = 180
Cam.resolution = (640, 480)
Cam.framerate = 32

RawCapture = PiRGBArray(Cam, size=(640, 480))
face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

for frame in Cam.capture_continuous(RawCapture, format="bgr", use_video_port = True):

    Img = frame.array
    RawCapture.truncate(0)

    image = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break