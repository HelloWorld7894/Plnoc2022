#Too lazy to implement model from tensorflow model garden,
#used ImageAI TinyYOLOv3 model instead (https://github.com/OlafenwaMoses/ImageAI)

from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo-tiny.h5"))
detector.loadModel()

Cam = PiCamera()
Cam.rotation = 180
Cam.resolution = (640, 480)
Cam.framerate = 32

RawCapture = PiRGBArray(Cam, size=(640, 480))

for frame in Cam.capture_continuous(RawCapture, format="bgr", use_video_port = True):

    Img = frame.array
    RawCapture.truncate(0)

    Image, Detections = detector.detectObjectsFromImage(output_type="array", input_image=Img, input_type="array", minimum_percentage_probability=50)
    cv2.imshow("Frame", Image)
    cv2.waitKey(1) #Terminate by Ctrl+C in terminal