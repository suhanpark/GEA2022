from movements import *
from capture import *

drone = start()
drone.streamon()

while True:
   stream(drone)
   vals = getKeybaordInput(drone)
   control(drone, vals)
   
   key = cv2.waitKey(1)
   if key & 0xFF == ord('q'):
      break
   