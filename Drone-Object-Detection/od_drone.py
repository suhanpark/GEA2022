from source import *

thres, nmsThres, configPath, weightsPath, classNames = configure()

net = detection_setup(configPath, weightsPath)

drone = connect_drone()
drone.streamon()

drone.takeoff()
drone.move_up(80)


while True:
    img = run(drone, net, thres, nmsThres, classNames)

    drone.send_rc_control(0, 0, 0, 0)

    cv2.imshow("Image", img)
    key = cv2.waitKey(5000)
    if key & 0xFF == ord('q'):
      break

