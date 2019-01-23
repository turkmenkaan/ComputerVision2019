import cv2 as cv
import numpy as np
import math

#def distance((x1, y1), (x2, y2)):
#    return math.sqrt(math.fabs(x2 - x1) ** 2 + math.fabs(y2 - y1) ** 2)

def findRed(frame):
    maxcontour = None
    red = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    redLow = np.array([126, 162, 97])
    redHigh = np.array([179, 255, 255])
    return cv.inRange(red, redLow, redHigh)
    # res = cv.bitwise_and(frame, frame, mask=mask)

def findYellow(frame):
    maxcontour = None
    yellow = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    yellowLow = np.array([23, 125, 107])
    yellowHigh = np.array([31, 205, 200])
    return cv.inRange(yellow, yellowLow, yellowHigh)
    # res = cv.bitwise_and(frame, frame, mask=mask)

def findContours(frame, mask):
    _, contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 1000:
             cv.drawContours(frame, contour, -1, (0, 255, 0))



cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    blurredFrame = cv.GaussianBlur(frame, (7, 7), 0)

    mask = findYellow(blurredFrame)
    findContours(blurredFrame, mask)


    cv.namedWindow('Frame',cv.WINDOW_NORMAL)
    cv.resizeWindow('Frame', 600, 400)
    cv.imshow("Frame", blurredFrame)

    cv.namedWindow('Mask',cv.WINDOW_NORMAL)
    cv.resizeWindow('Mask', 600, 400)
    cv.imshow("Mask", mask)
    
    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
