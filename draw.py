import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank) # this is the blank image you can draw on
cv.waitKey(0)

# step 1 : paint the image a certain color
blank[:] = 0,255,0
# 0,0,255 red
blank[200:300,300:400] = 0,0,255 # coloring by range of pixels
cv.imshow('Green',blank)
cv.waitKey(0)

# step 2 : draw a rectangle
blank[:] = 0,0,0 #made it black again
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
#(250,500) is the origin
# thickness = cv.FILLED or -1 fills the rectangle 
cv.imshow('Rectangle', blank)
cv.waitKey(0)

# Step 3 : draw a circle
blank[:] = 0,0,0 #made it black again
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
# draws a circle around the center
cv.imshow('Circle', blank)
cv.waitKey(0)

# Step 4 : draw a line
blank[:] = 0,0,0 #made it black again
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
cv.imshow('Line', blank)
cv.waitKey(0)

# Step 5 : write text
blank[:] = 0,0,0 #made it black again
cv.putText(blank, 'Hello',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)