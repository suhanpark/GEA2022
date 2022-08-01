from utils import *
import cv2
 
w,h,pid,pError,startCounter = components()
 
myDrone = initializeTello()
 
while True:
 
    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

tracker.py    show(myDrone, w, h, pid, pError)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        myDrone.land()
        break