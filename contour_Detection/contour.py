import cv2 as cv
import numpy as np
img=np.zeros((400,400),dtype="uint8")
img[100:200,100:200]=255

cv.rectangle(img,(100,200),(400,400),(255,255,255),-1)

_,threash=cv.threshold(img,127,255,cv.THRESH_BINARY)
contours,_=cv.findContours(threash,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
color=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
cv.drawContours(color,contours,-1,(0,255,0),5)

#cv.imshow("square",color)
#cv.waitKey(0)

def rec():
    capture = cv.VideoCapture(0)
    capture.set(cv.CAP_PROP_FRAME_WIDTH, 600)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, 800)
    capture.set(cv.CAP_PROP_FPS, 60)

    while True:
        _,fram=capture.read()
        frame=cv.flip(fram,1)
        frame1=cv.flip(fram,1)
        frame_grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        frame_grey1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

        frame_grey=cv.medianBlur(frame_grey,3)
        #_,threash=cv.threshold(frame,127,255,cv.THRESH_BINARY)
        threash=cv.adaptiveThreshold(frame_grey,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,41,12)
        ret, thresh = cv.threshold(frame_grey,102, 255, cv.THRESH_BINARY)

        cv.imshow("threash",threash)
        cv.imshow("threash2", thresh)
        canny=cv.Canny(frame_grey1,100,100)
       ## cv.imshow("canny", canny)
        #contours, _ = cv.findContours(threash, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours1,_= cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
       # cv.drawContours(frame, contours, -1, (0, 255, 0), 5)

        cv.drawContours(frame1, contours1, -1, (0, 255, 0), -1)

        black=np.zeros_like(frame)

        for c in contours1:
            epsion = 0.01 * cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, epsion, True)
            hull = cv.convexHull(c)
            cv.drawContours(black, [c], -1, (0, 255, 0), 2)
            cv.drawContours(black, [approx], -1, (255, 255, 0), 2)
            #cv.drawContours(black, [hull], -1, (0, 0, 255), 2)


        cv.imshow("using thresh",frame)
        cv.imshow("sdf",black)
        cv.imshow("using cammy",frame1)






        if cv.waitKey(1) & 0xFF == ord('d'):
            break

rec()
"""
img=cv.imread("IMG-2912.JPG")
img_grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
threash = cv.adaptiveThreshold(img_grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 41, 12)
ret, thresh = cv.threshold(cv.cvtColor(img, cv.COLOR_BGR2GRAY),
 127, 255, cv.THRESH_BINARY)

cv.imshow("threash1",threash)
cv.imshow("threash2",thresh)

contours, _ = cv.findContours(threash, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
black=np.zeros_like(img)

for c in contours:

    epsion=0.01* cv.arcLength(c,True)
    approx=cv.approxPolyDP(c,epsion,True)
    hull=cv.convexHull(c)
    #cv.drawContours(black, [c], -1, (0, 255, 0), 2)
    #cv.drawContours(black, [approx], -1, (255, 255, 0), 2)
    cv.drawContours(black, [hull], -1, (0, 0, 255), 2)

cv.imshow("contour",black)
cv.waitKey(0)
"""