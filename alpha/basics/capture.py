from djitellopy import tello
import cv2

def config():
   me = tello.Tello()
   me.connect()
   print(me.get_battery)

   me.streamon()
   return me

def stream(drone):
   img = drone.get_frame_read().frame
   cv2.imshow("image", img)
   

   