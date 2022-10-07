#using SSD mobilenet from mediapipe API
import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

video = cv2.VideoCapture(0)
while True:
  ret, image = video.read()

  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = face_detection.process(image)

  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.detections:
    for detection in results.detections:
      mp_drawing.draw_detection(image, detection)
  cv2.imshow('MediaPipe Face Detection', image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break