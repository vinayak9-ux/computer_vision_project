import cv2 as cv
import numpy as np
from face_and_hand_module import Hand

def empty(a):
    pass

cv.namedWindow("track")
cv.resizeWindow("track",(500,300))
cv.createTrackbar("Hue Min","track",0,179,empty)
cv.createTrackbar("Hue Max","track",179,179,empty)

cv.createTrackbar("Sat Min","track",0,255,empty)
cv.createTrackbar("Sat Max","track",255,255,empty)


cv.createTrackbar("Val Min","track",0,255,empty)
cv.createTrackbar("Val Max","track",255,255,empty)
cv.createTrackbar("GAP","track",1,10,empty)

cap=cv.VideoCapture("trial_video2.mp4")


while True:
    success,image=cap.read()


    if success:
        cv.flip(image, 1, image)

        background = np.zeros(image.shape, dtype="uint8")
        # image=cv.imread("hand1.jpg")
        cv.GaussianBlur(image, (5, 5), -1, image)
        # image=cv.resize(image,(800,600))
        image_HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        hue_min = cv.getTrackbarPos("Hue Min", "track")
        hue_max = cv.getTrackbarPos("Hue Max", "track")

        sat_min = cv.getTrackbarPos("Sat Min", "track")
        sat_max = cv.getTrackbarPos("Sat Max", "track")

        val_min = cv.getTrackbarPos("Val Min", "track")
        val_max = cv.getTrackbarPos("Val Max", "track")

        lower = np.array([hue_min, sat_min, val_min])
        upper = np.array([hue_max, sat_max, val_max])
        #lower = np.array([98, 73, 36])
        #upper = np.array([179, 255, 255])
        mask = cv.inRange(image_HSV, lower, upper)

        contour, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(image,contour,-1,(255,255,0),1)
        for c in contour:
            V=1
            for j in c:
                print(len(j[0]))
                V=V+1
                i=cv.getTrackbarPos("GAP", "track")

                if(V%i==0):
                  cv.circle(background,(j[0][0],j[0][1]),1,(0,255,0),-1)
            approx = cv.approxPolyDP(c, 0.001 * cv.arcLength(c, True), True)
            cv.drawContours(image, [approx], 0, (0, 0, 255), 5)

        cv.imshow("Sddd",background)
        cv.imshow("normal", image)
        # cv.imshow("mask",mask)
        # cv.imshow("hsv",mask1)

    else:
        cap.set(cv.CAP_PROP_POS_FRAMES,0)

    if cv.waitKey(60) & 0xFF==27:
        break
"""

image=cv.imread("LEAF1.jpeg")
image_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

image_hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)


green_low = np.array([36 , 50, 70] )
green_high = np.array([89, 255, 255])

mask=cv.inRange(image_hsv,green_low,green_high)

image_hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
#cv.imshow("final",mask)
#image_hsv=cv.bitwise_and(image_hsv,image_hsv,mask=mask)
image_hsv[mask > 0] = ([0,255,0])


image_final=cv.cvtColor(image_hsv,cv.COLOR_HSV2RGB)
image_final=cv.cvtColor(image_final,cv.COLOR_RGB2GRAY)
_,thresh=cv.threshold(image_final,190,255,cv.THRESH_BINARY)
#cv.imshow("t",thresh)
contour,x=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
image_final=cv.cvtColor(image_final,cv.COLOR_GRAY2RGB)

cv.drawContours(image,contour,-1,(255,0,255),-1)

cv.imshow("1",image)

#cv.imshow("final1",image_hsv)

_,thresh=cv.threshold(image_gray,90,255,cv.THRESH_BINARY)
#cv.imshow("dsf",thresh)

contour,x=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image,contour,-1,(0,0,255),-1)

cv.imshow("leaf1",image)



cv.waitKey(0)
"""