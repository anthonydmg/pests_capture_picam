from picamera import PiCamera
import time
from time import sleep
import os

os.makedirs("./images", exist_ok=True)

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 30
camera.iso = 100
camera.start_preview()

sleep(2)
while True:
    timestr =  time.strftime("%Y%m%d-%H%M%S")
    image_path = f"./images/image_5mgpx_{timestr}.jpg"
    camera.capture(image_path)


