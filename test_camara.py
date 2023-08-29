import cv2
import time

time_detectado=time.strftime("%Y%m%d-%H%M%S")

cap_web = cv2.VideoCapture(0)
ret,frame_web = cap_web.read()
cv2.imwrite(time_detectado+"test_cam_web_ID5.png", frame_web)

#def gstreamer_pipeline(
#    capture_width=640,
#    capture_height=480,
#    display_width=640,
#    display_height=480,
#    framerate=30,
#    flip_method=0,
#):
#    return (
#        "nvarguscamerasrc ! "
#        "video/x-raw(memory:NVMM), "
#        "width=(int)%d, height=(int)%d, "
#        "format=(string)NV12, framerate=(fraction)%d/1 ! "
#        "nvvidconv flip-method=%d ! "
#        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
#        "videoconvert ! "
#        "video/x-raw, format=(string)BGR ! appsink"
#        % (
#            capture_width,
#            capture_height,
#            framerate,
#            flip_method,
#            display_width,
#            display_height,
#        )
#    )

#cap_csi = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
#ret,frame_csi = cap_csi.read()

#cv2.imwrite(time_detectado+"test_cam_csi_ID5.png", frame_csi)

