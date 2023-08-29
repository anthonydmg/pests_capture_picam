from ultralytics import YOLO

model = YOLO("yolov8n.yaml")
model = YOLO("yolov8n.pt")
results = model("/home/pi/images/20230517-153745_rpi_cam.png", save = True)
print(results)
