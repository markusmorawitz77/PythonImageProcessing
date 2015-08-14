import numpy as np
import cv2

# Load an image

#img = cv2.imread('DSC03972.jpg', cv2.IMREAD_COLOR)
#img = cv2.imread('DSC03972.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.imread('DSC03972.jpg', cv2.IMREAD_GRAYSCALE)

#img = cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)

# Display image and save 
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('DSC03972_gray.png',img)
    cv2.destroyAllWindows()
