import cv2
import time
import os

path_videos = "./videos"
os.makedirs(path_videos, exist_ok= True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"\nResolution Video:({width},{height})")
timestr =  time.strftime("%Y%m%d-%H%M%S")
writer= cv2.VideoWriter(f'{path_videos}/video_{timestr}.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

while True:
    ret,frame= cap.read()

    writer.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(50) & 0xFF == ord('s'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
