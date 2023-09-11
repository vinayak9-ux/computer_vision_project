import cv2 as cv
import numpy as np
import time
import chapter3

class CaptureMananger():

    def __init__(self, capture, WindowMangerObj=None, flip_img=False):
        self.capture = capture  # change it
        self.WindowManagerObj = WindowMangerObj
        self.flip_image = flip_img
        self.filename=""
        self.enterframe = None
        self.channel = 0
        self.screenshot_flag=False
        self.frame=None
        self.videofilename=""
        self.video_out=None
        self.videoflag=False


    @property
    def chann(self):
        pass

    @chann.getter
    def chann(self):
        return self.channel

    @chann.setter
    def chann(self,i):
        if self.channel!=i:
            self.channel=i

    @property
    def frame_create(self):
        if self.enterframe and self.frame is None:
            self.frame= self.capture.retrieve(self.frame, self.channel)
        return self.frame

    def enter_frame(self):
        self.enterframe = self.capture.grab()
        return self.enterframe



    def exitframe(self):

        if self.WindowManagerObj is not None:
            if self.flip_image == True:
                image = cv.flip(self.frame[1], 1)
            else:
                image = self.frame_create[1]

            self.WindowManagerObj.show(image)
            print(self.frame_create[0] ,type(self.frame))

        if self.screenshot_flag==True:
            cv.imwrite("C:\\Users\\Acer\\PycharmProjects\\opencv\\igig.png",cv.flip(self.frame[1],1))
            self.screenshot_flag=False


        self.writevideomain()
        self.enter_frame = None
        self.frame = None

    def writevideomain(self):

        if self.videoflag==False:
            return

        if self.video_out is None:
            size=(int(self.capture.get(cv.CAP_PROP_FRAME_WIDTH)),int(self.capture.get(cv.CAP_PROP_FRAME_HEIGHT)))
            self.video_out=cv.VideoWriter(self.videofilename,self.encoding,15,size)


        image=cv.flip(self.frame_create[1],1)
        self.video_out.write(image)





    def writeimage(self,filename):
        self.filename=filename
        self.screenshot_flag=True

    def startvideorecord(self,filename,encoding=cv.VideoWriter.fourcc('M','J','P','G')):
        self.videofilename=filename
        self.encoding=encoding
        self.videoflag=True

    def endvideorecord(self):
        self.videofilename=None
        self.encoding=None
        self.videoflag=False

class WindowManger():
    def __init__(self,windowname):
        self.windowname=windowname
        self.iswindowopen=False

    def createWindow(self):
        cv.namedWindow(self.windowname)
        self.iswindowopen=True
    def show(self,frame):
        cv.imshow(self.windowname,frame)
    @property
    def iswindowcreated(self):
        return self.iswindowopen
    def destroywindow(self):
        cv.destroyWindow(self.windowname)
        self.iswindowopen=False

class cameo():

    def __init__(self):
        capture=cv.VideoCapture(0,cv.CAP_DSHOW);
        capture.set(cv.CAP_PROP_FRAME_WIDTH,1200)
        capture.set(cv.CAP_PROP_FRAME_HEIGHT,800)
        self.window_manager=WindowManger("cameo")
        self.capture_manager=CaptureMananger(capture,self.window_manager,True)
        self.filter=chapter3.sharping()


    def run(self):

        self.window_manager.createWindow()

        while self.window_manager.iswindowcreated:
            self.capture_manager.enterframe=self.capture_manager.capture.grab()
            frame=self.capture_manager.frame_create

            if frame  is not None:
                chapter3.strokedge(frame[1],frame[1])
                #self.filter.apply(frame[1],frame[1])



            self.capture_manager.exitframe()
            self.onkeypress(cv.waitKey(1))

        #cv.destroyAllWindows()

    def onkeypress(self,keycode):
        if keycode==32:
            self.capture_manager.writeimage("C:\\Users\\Acer\\PycharmProjects\\opencv\\popo.img")
        elif keycode==9:
            self.capture_manager.startvideorecord("extra.avi")
        elif keycode==27:
            self.capture_manager.endvideorecord()
        elif keycode==13:
            self.window_manager.destroywindow()



cameo().run()

