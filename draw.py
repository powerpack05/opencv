import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)


# blank[:,:] = 0,0,255
# cv.imshow('Blank',blank)

# Draw a rectangle

cv.rectangle(img=blank,pt1=(0,0),pt2=(blank.shape[1]//2,blank.shape[0]//2),color=(0,223,0),thickness=cv.FILLED)
cv.imshow('rectangle',blank)

# Draw a circle

cv.circle(img=blank,center=(blank.shape[1]//2,blank.shape[0]//2),radius=40,color=(0,0,255),thickness=-1)
cv.imshow('circle',blank)

# Draw a line

cv.line(img=blank,pt1=(0,10),pt2=(250,250),color=(255,0,0),thickness=10)
cv.imshow('Line',blank)

# Draw a text

cv.putText(img=blank,
           text="Computer Vision Engineer",
           org=(100,400),
           fontFace=cv.FONT_HERSHEY_TRIPLEX,
           fontScale=1.0,
           color=(255,0,0),
           thickness=4)
cv.imshow('Text',blank)



cv.waitKey(0)
cv.destroyAllWindows()