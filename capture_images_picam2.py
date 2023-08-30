import time
from picamera2 import Picamera2, Preview
import os

os.makedirs("./images", exist_ok=True)

picam = Picamera2()
capture_config = picam.create_still_configuration()
picam.start()

for i in range(10):
   time.sleep(2)
   timestr =  time.strftime("%Y%m%d-%H%M%S")
   image_path = f"./images/image_2mgpx_{timestr}.jpg"
   print("Image:", image_path)
   picam.switch_mode_and_capture_file(capture_config, image_path)


picam.close()
