__author__ = 'andy'
import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.medianBlur(frame,5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=5,maxRadius=20)

    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)

    # Our operations on the frame come here


    # Display the resulting frame
    cv2.imshow('detected circles',circles)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()