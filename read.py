import cv2 as cv
import os 

absolute_path = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(absolute_path,'Photos','cat.jpg')

print(f'Absolute path -->{image_path}')

image = cv.imread(image_path)
cv.imshow('Billi',image)
cv.waitKey(300)
cv.destroyAllWindows()
