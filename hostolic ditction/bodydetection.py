<<<<<<< HEAD
import cv2 as cv
import mediapipe as mp
import time 
import numpy

class bodyDetector():
    def __init__(self,mode=False,upperBody = False, smoothLandmarks = True, detectionCon = 0.5, trackingCon = 0.5):

        self.mode = mode
        self.upperBody = upperBody
        self.smoothLandmarks = smoothLandmarks
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpBody = mp.solutions.holistic
        self.body = self.mpBody.Holistic()
        self.mpDraw = mp.solutions.drawing_utils

    def findBody(self,img,draw =True):

        imgRgb = cv.cvtColor(img,cv.COLOR_RGB2BGR)
        results = self.body.process(imgRgb)
        if draw:
            self.mpDraw.draw_landmarks(img, results.face_landmarks, self.mpBody.FACE_CONNECTIONS)
            self.mpDraw.draw_landmarks(img, results.left_hand_landmarks, self.mpBody.HAND_CONNECTIONS)
            self.mpDraw.draw_landmarks(img, results.right_hand_landmarks, self.mpBody.HAND_CONNECTIONS)
            self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpBody.POSE_CONNECTIONS)
        return img

def main():
    cap = cv.VideoCapture(0)
    
    detactor = bodyDetector()
    while True:
        isTrue , img = cap.read()
        img = detactor.findBody(img)

        cv.imshow('Hostolic', img)

        if cv.waitKey(1) & 0xff == ord('f'):
            break


if __name__ == '__main__':
    main()
=======
import cv2 as cv
import mediapipe as mp
import time 
import numpy

class bodyDetector():
    def __init__(self,mode=False,upperBody = False, smoothLandmarks = True, detectionCon = 0.5, trackingCon = 0.5):

        self.mode = mode
        self.upperBody = upperBody
        self.smoothLandmarks = smoothLandmarks
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpBody = mp.solutions.holistic
        self.body = self.mpBody.Holistic()
        self.mpDraw = mp.solutions.drawing_utils

    def findBody(self,img,draw =True):

        imgRgb = cv.cvtColor(img,cv.COLOR_RGB2BGR)
        results = self.body.process(imgRgb)
        if draw:
            self.mpDraw.draw_landmarks(img, results.face_landmarks, self.mpBody.FACE_CONNECTIONS)
            self.mpDraw.draw_landmarks(img, results.left_hand_landmarks, self.mpBody.HAND_CONNECTIONS)
            self.mpDraw.draw_landmarks(img, results.right_hand_landmarks, self.mpBody.HAND_CONNECTIONS)
            self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpBody.POSE_CONNECTIONS)
        return img

def main():
    cap = cv.VideoCapture(0)
    
    detactor = bodyDetector()
    while True:
        isTrue , img = cap.read()
        img = detactor.findBody(img)

        cv.imshow('Hostolic', img)

        if cv.waitKey(1) & 0xff == ord('f'):
            break


if __name__ == '__main__':
    main()
>>>>>>> 4548fc9d6af6359635c79b43d52e09c24cc37d08
