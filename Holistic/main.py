#using SSD mobilenet from mediapipe API
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

Cam = PiCamera()
Cam.rotation = 180
Cam.resolution = (640, 480)
Cam.framerate = 32

RawCapture = PiRGBArray(Cam, size=(640, 480))
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
pose = mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)

for frame in Cam.capture_continuous(RawCapture, format="bgr", use_video_port = True):

    image = frame.array
    RawCapture.truncate(0)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the face mesh annotations on the image.
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
        break
