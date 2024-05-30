import cv2 as cv
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(absolute_path,'Photos','cat.jpg')
video_path = os.path.join(absolute_path,'Video','VID_20191003_122448.mp4') 


img = cv.imread(image_path)


def resize_rescale_frame(frame,scaling_factor):
    
    width = int(frame.shape[1]*scaling_factor)
    height = int(frame.shape[0]*scaling_factor)
    
    dimensions = (width,height)
    
    resized = cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    
    return resized

# cv.imshow(f'Original Image -->{img.shape}',img)
# resized_image = resize_rescale_frame(img,scaling_factor=0.20)
# cv.imshow(f'Resized image -->{resized_image.shape}',resized_image)
# cv.waitKey(0)
# cv.destroyAllWindows()

capture = cv.VideoCapture(video_path)

if not capture.isOpened():
    
    print(f'Error video not captured')
    
while True:
    
    succcess,frame = capture.read()
    
    if not succcess:
        break
    
    cv.imshow('frame',frame)
    
    resized_frame = resize_rescale_frame(frame,scaling_factor=0.75)
    
    cv.imshow('Resized Frame',resized_frame)
    
    
    if cv.waitKey(25) & 0xFF == ord('d'):
        
        break
    
capture.release()
cv.destroyAllWindows()
    