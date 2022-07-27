from movements import *

drone = start()

while True:
   vals = getKeybaordInput(drone)
   control(drone, vals)
   