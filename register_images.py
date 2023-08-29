import cv2
import time
import os
import glob
from ultralytics import YOLO

#flag=0
model = YOLO("yolov8n.pt")

def generar_foto(dir,time_detec):

   cap = cv2.VideoCapture(0)
   #ret,frame = cap.read()
   if cap.isOpened():
      
      ret, frame = cap.read()
      #process_yolo(frame)
      if not ret:
         print("No se puedo recibir el frame")
         return
      path_image = f"{dir}/{time_detec}_rpi_cam.png"
      print("\nImage: ", path_image)
      cv2.imwrite(path_image, frame)
      cap.release()
   else:
      print("No se conecto a la camara")

def process_yolo(frame):
   #model = YOLO("yolov8n.yaml")
   #model = YOLO("yolov8n.pt")
   results = model(frame, save = True)
   #print(results)

def register_images(images_dir = "./images", delay_seconds = 10):
   os.makedirs(images_dir, exist_ok = True)
   while True:
      time.sleep(0.5)
      timestr =  time.strftime("%Y%m%d-%H%M%S")
      generar_foto(images_dir,timestr)
      files =  glob.glob(f"{images_dir}/*.png")
      if len(files) > 500:
         for f in files:
            os.remove(f)
register_images()
