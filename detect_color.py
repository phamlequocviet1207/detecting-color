import cv2
from PIL import Image
from util import get_limits

#yellow in BGR colorspace
yellow = [0,255,255]

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    # cv2.imshow("mask", mask)
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    # print(bbox)

    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()