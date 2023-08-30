import cv2
import time
import os

path_videos = "./videos"
os.makedirs(path_videos)

video= cv2.VideoCapture(0)
width= int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"\nResolution Video:({width},{height})")
timestr =  time.strftime("%Y%m%d-%H%M%S")
writer= cv2.VideoWriter(f'{path_videos}/video_{timestr}.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 10, (width,height))

while True:
    ret,frame= video.read()

    writer.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(100) & 0xFF == ord('s'):
        break

video.release()
writer.release()
cv2.destroyAllWindows()
