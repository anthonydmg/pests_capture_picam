from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
camera.capture('./image_capture.jpg')
sleep(5)
camera.stop_preview()