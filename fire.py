from ultralytics import YOLO
import cv2
import math
from picamera2 import Picamera2
import time

picam2 = Picamera2()


model = YOLO('fire.pt')

classnames = ['fire']

def capture():
    picam2.start()
    time.sleep(1)
    picam2.capture_file('frame.jpg')
    picam2.stop()
    print('frame captured and saved')
    
def init_camera():
    preview_config = picam2.create_preview_configuration()
    picam2.configure(preview_config)

init_camera()
while False:#camera test
    capture()
    frame = cv2.imread("frame.jpg")
    #frame = cv2.resize(frame, (640, 480))
    cv2.imshow('frame',frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

while True:
    capture()
    frame = cv2.imread("frame.jpg")
    frame = cv2.resize(frame, (640, 480))
    result = model(frame,stream=True)

    # Getting bbox,confidence and class names informations to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            print(f"confidence {confidence}")
            Class = int(box.cls[0])
            if confidence > 5:
                x1,y1,x2,y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
                print(f"Bbox cordinates {x1}, {y1}, {x2}, {y2}")
                


    cv2.imshow('frame',frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
