from math import sqrt
from typing import Tuple
import cv2
from face_recognition.api import face_locations
import numpy
import face_recognition
import math
import random_dot
import time

#webcam display size
def start(thresh = 10):
    wcam,hcam = 640,360

    #webcam
    cap  = cv2.VideoCapture(0)
    cap.set(3,wcam)
    cap.set(4,hcam)
    a = [(100,150),(100,335),(500,96),(500,400)]

    dot = random_dot.rand_dot(a)
    
    start = time.time()

    while True:
        isTrue,img = cap.read()
        img_s = cv2.resize(img,(0,0),None,0.25,0.25)
        img_s = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        shp = img.shape #image(height,weight)
        h,w = shp[0],shp[1]
        cv2.line(img,(w//2,0),(w//2,h),(255,0,255,2),1) # image center coordinate maping
        cv2.line(img,(0,h//2),(w,h//2),(255,0,255,2),1)
        
        cv2.circle(img,dot, 10, (0,0,255), -1)

        face_loc = face_recognition.face_locations(img_s)
        if len(face_loc) != 0:
            face_loc = face_loc[0]
            y1,x2,y2,x1 = face_loc
            scale = 1
            cv2.rectangle(img,(face_loc[3]*scale,face_loc[0]*scale),(face_loc[1]*scale,face_loc[2]*scale),(255,0,255,2),2) #to show where is the face
            mid_x = (face_loc[3]+face_loc[1])//2 #finding mid point
            mid_y = (face_loc[0]+face_loc[2])//2
            # cv2.line(img,(mid_x,face_loc[3]),(mid_x,face_loc[1]),(255,0,255,2),1) #face center coordinate maping
            # cv2.line(img,(face_loc[0],mid_y),(face_loc[2],mid_y),(255,0,255,2),1)
            cv2.circle(img, (w//2,h//2), 4, (0,0,255), -1)
            cv2.circle(img, (mid_x,mid_y), 4, (0,0,255), -1)
            cv2.line(img,(mid_x,mid_y),(w//2,h//2),(255,0,255,2),2)

            distance = ((mid_x+w//2)//2,(mid_y+h//2)//2) #distance form polting map center to the face center

            distance = math.sqrt((abs(mid_x-w//2))**2 + (abs(mid_y-h//2))**2 )

            #print(distance)
            cv2.rectangle(img, (0,0), (400, 30),(255, 255, 255), -1)
            cv2.putText(img,f"Try to touch the point with your nose",(30,25),cv2.FONT_HERSHEY_COMPLEX,0.5,(0, 0, 255),1)
            cv2.imshow("cam",img)
            cond1 = dot[0]-thresh < mid_x < dot[0]+thresh
            cond2 = dot[1]-thresh < mid_y < dot[1]+thresh
            
            if cond1 and cond2:
                end = time.time()
                result = end-start
                return result
            if cv2.waitKey(1) & 0XFF == ord('f'):
                break
        else:
            cv2.imshow("cam",img)