<<<<<<< HEAD
import cv2 as cv 
import mediapipe as mp
import time 

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
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks: 
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
                
    def fingerPostion(self,img,handNum=0,draw = True):
        listLms = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNum]
            for id, lm in enumerate(myHand.landmark):
                h , w, c = img.shape
                cX , cY = int(lm.x*w) , int(lm.y*h)
                listLms.append([id,cX,cY])

                if draw:
                    cv.circle(img,(cX,cY), 15, (255,0,255), cv.FILLED)
        return listLms

                   
    

def main():
    #video device set 
    cap = cv.VideoCapture(0)
    detector = HandDetector()
    #dimennsion or resultaion set
    cap.set(3,1000)
    cap.set(4,1000)
    # fps var setup 
    cTime = 0 
    pTime = 0
    while True:
        isTrue , img = cap.read()
        img = detector.findHands(img)
        listLms = detector.fingerPostion(img)
        if len(listLms) !=0:
            print(listLms[4])
        #fps alogorithm
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
    
        #puttext call
        cv.putText(img,str(int(fps)),(60,90),cv.FONT_HERSHEY_SIMPLEX,3,(30, 132, 73),3) 
    
        #display box call 
        cv.imshow('hand',img)

        # program break rules ord("f/d/any keybaord alphabetical and numerical key")
        if cv.waitKey(1) & 0xFF == ord('f'):
            break 


if __name__ == "__main__":
    main()
=======
import cv2 as cv 
import mediapipe as mp
import time 

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
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks: 
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
                
    def fingerPostion(self,img,handNum=0,draw = True):
        listLms = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNum]
            for id, lm in enumerate(myHand.landmark):
                h , w, c = img.shape
                cX , cY = int(lm.x*w) , int(lm.y*h)
                listLms.append([id,cX,cY])

                if draw:
                    cv.circle(img,(cX,cY), 15, (255,0,255), cv.FILLED)
        return listLms

                   
    

def main():
    #video device set 
    cap = cv.VideoCapture(0)
    detector = HandDetector()
    #dimennsion or resultaion set
    cap.set(3,1000)
    cap.set(4,1000)
    # fps var setup 
    cTime = 0 
    pTime = 0
    while True:
        isTrue , img = cap.read()
        img = detector.findHands(img)
        listLms = detector.fingerPostion(img)
        if len(listLms) !=0:
            print(listLms[4])
        #fps alogorithm
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
    
        #puttext call
        cv.putText(img,str(int(fps)),(60,90),cv.FONT_HERSHEY_SIMPLEX,3,(30, 132, 73),3) 
    
        #display box call 
        cv.imshow('hand',img)

        # program break rules ord("f/d/any keybaord alphabetical and numerical key")
        if cv.waitKey(1) & 0xFF == ord('f'):
            break 


if __name__ == "__main__":
    main()
>>>>>>> 4548fc9d6af6359635c79b43d52e09c24cc37d08
