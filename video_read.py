import cv2 as cv
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
print(f'Absolute path -->{absolute_path}')
video_path = os.path.join(absolute_path,'Video','dog.mp4')
print(f'Video paath -->{video_path}')

video = cv.VideoCapture(video_path)

if not video.isOpened():
    
    print(f'Error Occurred:Could not open video')
    
while True:
    
    isTrue,frame = video.read()
    
    if not isTrue:
        break
    
    cv.imshow('Frame',frame)
    
    if cv.waitKey(25) and 0xFF == ord('d'): 
        break
    
video.release()
cv.destroyAllWindows()