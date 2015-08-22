import cv2
import numpy as np

# load original image
img = cv2.imread('../../images/redstar.jpg')

# convert to grayscale
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# convert to binary
ret,img_binary = cv2.threshold(img_grey,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

img_contours = img_binary.copy()
contours, hierachy = cv2.findContours(img_contours,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)

#img_contours = img.copy()
#cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)

cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original',img)

cv2.namedWindow('grey', cv2.WINDOW_NORMAL)
cv2.imshow('grey',img_grey)

cv2.namedWindow('binary', cv2.WINDOW_NORMAL)
cv2.imshow('binary',img_binary)

cv2.namedWindow('contours', cv2.WINDOW_NORMAL)
cv2.imshow('contours',img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()