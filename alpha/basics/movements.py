import basics.keymodule as km
from time import sleep
from djitellopy import tello

def start():
   km.init()
   me = tello.Tello()
   me.connect()
   me.takeoff()
   return me

def getKeybaordInput(drone):
   lr, fb, ud, yv = 0, 0, 0, 0
   speed = 50
   
   if km.getKey('LEFT'): lr = -speed
   elif km.getKey('RIGHT'): lr = speed
   
   if km.getKey('UP'): fb = speed
   elif km.getKey('DOWN'): fb = -speed
   
   if km.getKey('w'): ud = speed
   elif km.getKey('s'): ud = -speed
   
   if km.getKey('a'): yv = speed
   elif km.getKey('d'): yv = -speed
   
   if km.getKey('l'): drone.land()
   if km.getKey('t'): drone.takeoff()

   return [lr, fb, ud, yv]

def control(drone, vals):
   drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
   sleep(0.05)