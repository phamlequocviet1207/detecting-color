import cv2
import numpy as np


cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    height, width, _ = frame.shape

    pixel_center = hsv[height//2,width//2]
    hue_value = pixel_center[0]

    color = "UNDEFINED"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    cv2.putText(frame, color, (10,50), 0,1, (255,0,0), 2)
    # print(pixel_center)
    # print(hsv_value)

    cv2.circle(frame,(width//2,height//2), 10, (0,255,0), 3)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()