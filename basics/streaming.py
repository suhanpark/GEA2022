from capture import *

drone = config()

drone.takeoff()
drone.move_up(80)


while True:
   stream(drone)
   
   key = cv2.waitKey(1)
   if key & 0xFF == ord('q'):
      break

