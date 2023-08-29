import cv2
import time

flag=0

def generar_foto(time_detec):

   cap = cv2.VideoCapture(0)
   ret,frame = cap.read()
   cv2.imwrite(time_detec+"_cam_csi_ID5.png", frame)
   cap.release()

   cap = cv2.VideoCapture(1)
   ret,frame = cap.read()
   cv2.imwrite(time_detec+"_cam_web_ID5.png", frame)
   cap.release()

for a in range(4):
   time.sleep(1)
   timestr = time.strftime("%Y%m%d-%H%M%S")
   generar_foto(timestr)
