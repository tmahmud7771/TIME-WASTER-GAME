<<<<<<< HEAD
import cv2 as cv 
import mediapipe as mp
import time 

#video device set 

cap = cv.VideoCapture(0)

#dimennsion or resultaion set
cap.set(3,1000)
cap.set(4,1000)

#hands mediapipe setup 

mpHands = mp.solutions.hands

#obj setup

hands = mpHands.Hands(False,2,0.7,0.7)

mpDraw = mp.solutions.drawing_utils

# fps var setup 

cTime = 0 
pTime = 0

while True:
    isTrue , img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results)
    if results.multi_hand_landmarks : 
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h , w, c = img.shape
                cX , cY = int(lm.x*w) , int(lm.y*h)
                if id == 4 :
                    cv.circle(img,(cX,cY), 15, (255,0,255), cv.FILLED)

            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,mpDraw.DrawingSpec(color=(255,255,255), thickness=3 , circle_radius=4))   
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)   
    
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
f
=======
import cv2 as cv 
import mediapipe as mp
import time 

#video device set 

cap = cv.VideoCapture(0)

#dimennsion or resultaion set
cap.set(3,1000)
cap.set(4,1000)

#hands mediapipe setup 

mpHands = mp.solutions.hands

#obj setup

hands = mpHands.Hands(False,2,0.7,0.7)

mpDraw = mp.solutions.drawing_utils

# fps var setup 

cTime = 0 
pTime = 0

while True:
    isTrue , img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results)
    if results.multi_hand_landmarks : 
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h , w, c = img.shape
                cX , cY = int(lm.x*w) , int(lm.y*h)
                if id == 4 :
                    cv.circle(img,(cX,cY), 15, (255,0,255), cv.FILLED)

            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS,mpDraw.DrawingSpec(color=(255,255,255), thickness=3 , circle_radius=4))   
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)   
    
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
f
s
