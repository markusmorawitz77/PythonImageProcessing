import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
    	break

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()