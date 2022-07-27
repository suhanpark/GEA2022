import cv2
from djitellopy import tello

def configure():
    thres = 0.55
    nmsThres = 0.2

    classNames = []
    classFile = 'drone_od/coco.names'
    with open(classFile, 'rt') as f:
        classNames = f.read().split('\n')
    print(classNames)
    configPath = 'drone_od/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = "drone_od/frozen_inference_graph.pb"
    
    return thres, nmsThres, configPath, weightsPath, classNames

def detection_setup(configPath, weightsPath):
    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)
    return net
    
def connect_drone():
    me = tello.Tello()
    me.connect()
    print(me.get_battery())
    return me

def cornerRect(img, bbox, l=30, t=5, rt=1,
               colorR=(255, 0, 255), colorC=(0, 255, 0)):
    x, y, w, h = bbox
    x1, y1 = x + w, y + h
    if rt != 0:
        cv2.rectangle(img, bbox, colorR, rt)
    # Top Left  x,y
    cv2.line(img, (x, y), (x + l, y), colorC, t)
    cv2.line(img, (x, y), (x, y + l), colorC, t)
    # Top Right  x1,y
    cv2.line(img, (x1, y), (x1 - l, y), colorC, t)
    cv2.line(img, (x1, y), (x1, y + l), colorC, t)
    # Bottom Left  x,y1
    cv2.line(img, (x, y1), (x + l, y1), colorC, t)
    cv2.line(img, (x, y1), (x, y1 - l), colorC, t)
    # Bottom Right  x1,y1
    cv2.line(img, (x1, y1), (x1 - l, y1), colorC, t)
    cv2.line(img, (x1, y1), (x1, y1 - l), colorC, t)

    return img

def run(drone, net, thres, nmsThres, classNames):
    img = drone.get_frame_read().frame
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cornerRect(img, box)
            cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 2)
        return img
    except:
        pass

def drone_stream(img, drone):
    drone.send_rc_control(0, 0, 0, 0)
    cv2.imshow("Image", img)