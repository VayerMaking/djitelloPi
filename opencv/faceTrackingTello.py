from utils import *
import cv2

w,h = 360,240
pid = [0.4,0.4,0]
pError = 0
startCounter = 0  # for no Flight 1   - for flight 0

#start tello
myDrone = initializeTello()

while True:

    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1

    # get the frame
    img = telloGetFrame(myDrone,w,h)
    # get face info from the utils
    img, info = findFace(img)
    # generate and use coordinates to move the tello
    pError = trackFace(myDrone,info,w,pid,pError)
    # show tracking process on laptop screen
    cv2.imshow('Image',img)
    # quit and land drone with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break
