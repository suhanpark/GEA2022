from utils import *
import cv2
 
w,h,pid,pError,startCounter = components()
 
myDrone = initializeTello()
 
while True:
 
    if startCounter == 0:
        myDrone.takeoff()
        myDrone.move_down(20)
        startCounter = 1
        
    show(myDrone, w, h, pid, pError)

    key = cv2.waitKey(10000)
    if key & 0xFF == ord('q'):
        myDrone.land()
        break