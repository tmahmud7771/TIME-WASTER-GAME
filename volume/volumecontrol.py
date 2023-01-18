import cv2 as cv 
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wcam,hcam = 1000,1000

cap  = cv.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)

cTime = 0 
pTime = 0

detactor = htm.HandDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]



while True:
    isTrue,img = cap.read()

    img = detactor.findHands(img)
    listLms = detactor.fingerPostion(img, draw=False)
    if len(listLms) !=0:
        x1 , y1 = listLms[4][1] , listLms[4][2]
        x2 , y2 = listLms[8][1] , listLms[8][2]
        cx , cy =  (x1+x2)//2 , (y1+y2)//2
    
        cv.circle(img,(x1,y1), 15,(255,0,255),cv.FILLED)
        cv.circle(img,(x2,y2), 15,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),2)
        cv.circle(img,(cx,cy), 15,(255,0,0),cv.FILLED)

        lenght = math.hypot(x2-x1,y2-y1)
        vol = np.interp(lenght,[20,200],[minVol,maxVol])
        volume.SetMasterVolumeLevel(vol, None)
            
    cTime = time.time()
    fps = 1 /(cTime - pTime)
    pTime = cTime

    cv.putText(img,str(int(fps)),(60,90), cv.FONT_HERSHEY_SIMPLEX ,2,(255,0,255),2)
    cv.imshow('Volume Control' , img)

    if cv.waitKey(1) & 0XFF == ord('f'):
        break