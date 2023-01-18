import cv2 as cv 
import numpy as np

#Griding method
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1],
                                                imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#text method
def text(img,text,cor=(7,90),font = cv.FONT_HERSHEY_SIMPLEX,size = 0.9,color=(255,0,255)):
    return cv.putText(img,text,cor,font,size,color)

#empty method for pass 
def empty(a):
    pass


cv.namedWindow("TaskBars")
cv.resizeWindow("TaskBars",640,240)
#first values staring point => 2nd val for counting 0-1-2-3----179
cv.createTrackbar("MIN HUE","TaskBars",0,179,empty) 
cv.createTrackbar("MAX HUE","TaskBars",56,179,empty)
cv.createTrackbar("MIN SAT","TaskBars",100,255,empty)
cv.createTrackbar("MAX SAT","TaskBars",255,255,empty)
cv.createTrackbar("MIN VAI","TaskBars",53,255,empty)
cv.createTrackbar("MAX VAI","TaskBars",255,255,empty)

#put your image relative path inside the quotation sign "relative path"
img = cv.imread(r"") 

while True:

    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    #setting values of hue - sat - vais
    h_min = cv.getTrackbarPos("MIN HUE","TaskBars") 
    h_max = cv.getTrackbarPos("MAX HUE","TaskBars")
    s_min = cv.getTrackbarPos("MIN SAT","TaskBars")
    s_max = cv.getTrackbarPos("MAX SAT","TaskBars")
    v_min = cv.getTrackbarPos("MIN VAI","TaskBars")
    v_max = cv.getTrackbarPos("MAX VAI","TaskBars")

    #lower range values array
    lower = np.array([h_min,s_min,v_min])
    #Upper range values array  
    upper = np.array([h_max,s_max,v_max])  
    
    #mask photo b&w
    mask = cv.inRange(imgHSV,lower,upper)
    #masked photo 
    maskedImage = cv.bitwise_and(img,img,mask=mask) 

    #putting text into image
    text(mask,"mask b&w")
    text(img,"main")
    text(maskedImage,"masked imgae")
    text(imgHSV,"image HSV")

    #grid funciton called
    grid = stackImages(0.7,([img,imgHSV,mask,maskedImage]))  

    cv.imshow("grid", grid) 
    #if "f" pressed code loop will stop
    if cv.waitKey(1) & 0xFF == ord("f"):  
        break
