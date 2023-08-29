import time

from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder

picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)})
#video_config.controls.FrameRate = 30
picam2.configure(video_config)
#picam2.video_configuration.controls.FrameRate = 30.0
picam2.start_preview()
encoder = JpegEncoder(q=70)

picam2.start_recording(encoder, 'inia1.mjpeg')
time.sleep(60)
picam2.stop_recording()
