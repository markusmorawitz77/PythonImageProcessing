import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# Setting the color mode (last argument of VideoWriter) correct is IMPORTANT
fourcc = cv2.cv.CV_FOURCC(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480), False)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # make some operations on the frame
        #frame = cv2.flip(frame,0)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # write frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()