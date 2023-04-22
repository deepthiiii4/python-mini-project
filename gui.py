import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

###################################

brushThickness = 15
eraserThickness = 50

###################################



folderpath = "header"
mylist = os.listdir(folderpath)
print(mylist)


for impath in mylist:
      image = cv2.imread(f'{folderpath}/{impath}')
      overLayList.append(image)
print(len(overLayList))

header = overLayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(1)
cap.set(3 , 1280)
cap.sert(4, 720)
detector = htm.handDetector(detectionCon=0.85)
xp,yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while true:
    success, img = cap.read()
    img = cv2.flip(img,1) 

    img = detector.findHands(img)
    lnList = detector.findPosition(img , draw=False)

    if len(lnList)!= 0:
        print(lnList)


        x1,y1 = lnlist[0][1:]
        x2, y2 = lnList[12][1:]


        fingers = detector.fingersUp()
        

        if fingers[1] and fingers[2]:
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2+25), drawColor, cv2.FILLED)
            print("Selection Mode")
            if y1 < 125:
                if 250<x1<450:
                    header = overLayList[0]
                    drawColor = (255,0,255)
                elif  550< x1 < 750:
                    header = overLayList[1]
                    drawColor = (255,0,0)
                elif  880< x1 < 950:
                    header = overLayList[2]
                    drawColor = (0,255,0)
                elif  1050< x1 < 1200:
                    header = overLayList[3]
                    drawColor = (0,0,0)
            cv2.rectangle(img, (x1, y1), 15,, drawColor, cv2.FILLED)
                     


        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if xp==0 and yp==0:
                xp, yp = x1, y1

             if drawColor== (0,0,0):
                  cv2.line(img, (xp,yp), (x1,y1), drawColor, eraserThickness)
                  cv2.line(imgCanvas, (xp,yp), (x1,y1), drawColor, eraserThickness)
             else:
                  cv2.line(img, (xp,yp), (x1,y1), drawColor, brushThickness)
                  cv2.line(imgCanvas, (xp,yp), (x1,y1), drawColor, brushThickness)
            
            
            xp,yp = x1, y1
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imGray, 50, 255,cv2.THRESHOLD_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_and(img,imgCanvas)




    img[0:125 , 8:1288] = header
    img = cv2.addWeighted(img, 0.5, imgCnvas,0.5,0)
    cv2.imshow("image" , img)
    cv2.imshow("Canva" , imgCanvas)
    cv2.imshow("Inv" , imgInv)    
    cv2.waitkey(1)
