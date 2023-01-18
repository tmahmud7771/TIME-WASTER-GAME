import cv2 as cv 
import mediapipe as mp
import time


class faceDetector():

    def __init__(self,mode = False, maxface = 1 , detectionCon = 0.5 , trackingCon = 0.5):
        self.mode = mode
        self.maxface = maxface
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        
        self.mpFace = mp.solutions.face_mesh
        self.face = self.mpFace.FaceMesh(self.mode,self.maxface,self.detectionCon,self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findFace(self,img,draw = True): 
        imgRgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        results = self.face.process(imgRgb)
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceLms,self.mpFace.FACE_CONNECTIONS,
                    self.mpDraw.DrawingSpec(color=(255,255,255), thickness=1 , circle_radius=1),
                    self.mpDraw.DrawingSpec(color=(255,255,255), thickness=1))
        return img

class HandDetector(): 
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackingCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        
        #hands mediapipe setup 
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        if results.multi_hand_landmarks: 
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
                    self.mpDraw.DrawingSpec(color=(0,0,0), thickness=1 , circle_radius=6),
                    self.mpDraw.DrawingSpec(color=(255,255,255), thickness=1 , circle_radius=1))
        return img
                
                
                # for id, lm in enumerate(handLms.landmark):
                #     h , w, c = img.shape
                #     cX , cY = int(lm.x*w) , int(lm.y*h)
                #     if id == 4 :
                #         cv.circle(img,(cX,cY), 15, (255,0,255), cv.FILLED)

    

def main():
    detectorFace = faceDetector()
    detectorHands = HandDetector()
    cap = cv.VideoCapture(0)
    cap.set(3,1000)
    cap.set(4,1000)
    #fps 
    cTime = 0
    pTime = 0 

    while True:
        isTrue , img = cap.read()
        img = detectorFace.findFace(img)
        img = detectorHands.findHands(img)
        #########################
        cTime = time.time()
        fps = 1/ (cTime - pTime)
        pTime = cTime

        ########################
        cv.putText(img,str(int(fps)),(60,80), cv.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)
        cv.imshow('face detection', img )

        if cv.waitKey(1) & 0xFF == ord('f'):
            break


if __name__ == "__main__":
    main()