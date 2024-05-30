import cv2 as cv
import os 

absolute_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(absolute_path,'Photos','Boston.jpg')

image = cv.imread(image_path)

cv.imshow('Boston',image)

# Converting to Gray Scale
gray = cv.cvtColor(image,code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur 
blur = cv.GaussianBlur(image,ksize=(7,7),sigmaX=2,borderType=cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade
canny = cv.Canny(blur,threshold1=125,threshold2=175)
cv.imshow('Canny',canny)

# Dilating the images
dilated = cv.dilate(canny,kernel=(7,7),iterations=1)
cv.imshow('Dilated',dilated)

# Eroding

eroded = cv.erode(dilated,kernel=(7,7),iterations=1)
cv.imshow('Erroded',eroded)

# resize

resized = cv.resize(image,dsize=(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# cropped
cropped = image[100:400,500]
cv.imshow('Cropped',cropped)


cv.waitKey(0)
cv.destroyAllWindows()