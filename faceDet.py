# import the opencv library 
import numpy as np
import cv2
import os
  
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# define a video capture object 
vid = cv2.VideoCapture(0) 

# vid.set(3, 1024)
# vid.set(4, 680)

while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (216, 0, 230), 5)
    
    # Display the resulting frame 
    cv2.imshow('DSP, Dr.Derakhshan', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
