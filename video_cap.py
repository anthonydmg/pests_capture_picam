import cv2
import time
video= cv2.VideoCapture(0)

width= int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter('video_exmaple.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))


for i in range(100):
    ret,frame= video.read()

    writer.write(frame)
    time.sleep(0.2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break


video.release()
writer.release()
cv2.destroyAllWindows()
