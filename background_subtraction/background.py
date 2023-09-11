import cv2 as cv
#from contour import rec
import numpy as np

erode_kernal=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

dilate_kernal=cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 600)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 800)
capture.set(cv.CAP_PROP_FPS, 60)

def empty():
    pass
for i in range(10):

    sucess,frame_background=capture.read()
    frame_background=cv.flip(frame_background,1)
    frame_background=cv.cvtColor(frame_background,cv.COLOR_BGR2GRAY)
#frame_background=cv.GaussianBlur(frame_background,(21,21),0)

print(frame_background.shape)




cv.namedWindow("track")
cv.resizeWindow("track", (500, 300))
cv.createTrackbar("Hue Min", "track", 0, 255, empty)


while True:
    _,fram=capture.read()

    frame=cv.flip(fram,1)
    #cv.imshow("df",frame)
    fram = cv.flip(fram, 1)

   # cv.imshow("dfd", frame)
    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
   # frame=cv.GaussianBlur(frame,(21,21),0)
    diff=cv.absdiff(frame_background,frame)

    b=cv.inRange(diff,8,130)
    cv.imshow("SDfs",b)

    i = cv.getTrackbarPos("Hue Min", "track")
    _,thresh=cv.threshold(diff,25,255,cv.THRESH_BINARY)
    #thresh=cv.adaptiveThreshold(frame,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,10)
    cv.erode(thresh, erode_kernal, thresh, iterations=1)
    #check if we only do one what will be the result

    cv.dilate(thresh, dilate_kernal, thresh, iterations=1)

    contours,_ = cv.findContours(thresh, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv.contourArea(c)>4000:
            x,y,w,h=cv.boundingRect(c)
            #cv.rectangle(fram,(x,y),(x+w,y+h),(0,255,0),1)
            c=cv.convexHull(c)
            cv.drawContours(fram, [c], -1, (0, 255, 0), 2)
    cv.imshow("final",fram)
    cv.imshow("finafdsfl", thresh)
    cv.imshow("finadsfsl", diff)
    k=cv.waitKey(1)
    if k==27:
        break