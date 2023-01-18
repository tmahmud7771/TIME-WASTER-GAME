<<<<<<< HEAD
import cv2 as cv
import mediapipe as mp
import FaceAndHandDetectionModule as bfd

cap = cv.VideoCapture(0)
detector = bfd.

while True:
    isTrue , img = cap.read()

    cv.imshow("body", img)

    if cv.waitKey(1) & 0xFF == ord('f'):f
        break 
=======
import cv2 as cv
import mediapipe as mp
import FaceAndHandDetectionModule as bfd

cap = cv.VideoCapture(0)
detector = bfd.

while True:
    isTrue , img = cap.read()

    cv.imshow("body", img)

    if cv.waitKey(1) & 0xFF == ord('f'):f
        break 
>>>>>>> 4548fc9d6af6359635c79b43d52e09c24cc37d08
