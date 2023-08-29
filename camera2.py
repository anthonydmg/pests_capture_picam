import time
from picamera2 import Picamera2, Preview
picam = Picamera2()
picam.start_and_capture_file("iamge_{:d}.jpg", delay=0, show_preview = False)
#config =  picam.create_preview_configuration()
#picam.configure(config)

#picam.start_preview(Preview.QTGL)
#picam.start()
#time.sleep(2)
#picam.capture_file("test_python.jpg")
#picam.close()
