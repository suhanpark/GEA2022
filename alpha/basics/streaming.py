from capture import *

drone = config()

while True:
   stream(drone)
   
   key = cv2.waitKey(1)
   if key & 0xFF == ord('q'):
      break

