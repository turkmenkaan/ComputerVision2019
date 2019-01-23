import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('Colorbars', cv2.WINDOW_NORMAL)

hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd = 'Colorbars'

cv2.createTrackbar(hl, wnd, 0, 179, nothing)
cv2.createTrackbar(hh, wnd, 0, 179, nothing)
cv2.createTrackbar(sl, wnd, 0, 255, nothing)
cv2.createTrackbar(sh, wnd, 0, 255, nothing)
cv2.createTrackbar(vl, wnd, 0, 255, nothing)
cv2.createTrackbar(vh, wnd, 0, 255, nothing)

# set initial values for sliders
cv2.setTrackbarPos(hl, wnd, 0)
cv2.setTrackbarPos(hh, wnd, 179)
cv2.setTrackbarPos(sl, wnd, 0)
cv2.setTrackbarPos(sh, wnd, 255)
cv2.setTrackbarPos(vl, wnd, 0)
cv2.setTrackbarPos(vh, wnd, 255)

while True:
    
    _, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #read trackbar positions for each trackbar
    hul = cv2.getTrackbarPos(hl, wnd)
    huh = cv2.getTrackbarPos(hh, wnd)
    sal = cv2.getTrackbarPos(sl, wnd)
    sah = cv2.getTrackbarPos(sh, wnd)
    val = cv2.getTrackbarPos(vl, wnd)
    vah = cv2.getTrackbarPos(vh, wnd)

    #make array for final values
    HSVLOW = np.array([hul, sal, val])
    HSVHIGH = np.array([huh ,sah, vah])

    #create a mask for that range
    mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)

    res = cv2.bitwise_and(frame,frame, mask =mask)
    cv2.imshow(wnd, res)
    
    k = cv2.waitKey(5) & 0xFF
    
    if k == ord('q'):
        break
 
cv2.destroyAllWindows()

