from picamera import PiCamera
import time
from time import sleep
import os

os.makedirs("./images", exist_ok=True)

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 30
camera.iso = 100

sleep(2)
for filename in camera.capture_continuous('./images/img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(300) # wait 5 minutes



