import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])

    lower_red1 = np.array([170,100,100])
    upper_red1 = np.array([179,255,255])

    lower_red2 = np.array([0,100,100])
    upper_red2 = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)

    maskgreen = cv2.inRange(hsv, lower_green, upper_green)

    maskred1 = cv2.inRange(hsv, lower_red1, upper_red1)
    maskred2 = cv2.inRange(hsv, lower_red2, upper_red2)
    maskred = cv2.bitwise_or(maskred1,maskred2)

    mask = cv2.bitwise_or(maskblue,maskgreen)
    mask = cv2.bitwise_or(mask,maskred)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()