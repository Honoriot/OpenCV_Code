import numpy as np
from cv2 import cv2

# Events = [i for i in dir(cv2) if 'EVENT' in i]
# print(Events)

def Mouse_Event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text_XY = str(x) + ",  " + str(y)
        font = cv2.FONT_ITALIC
        color = (255, 0, 0)
        cv2.putText(IMG, text_XY, (x, y), font, 0.5, color, 1, cv2.LINE_AA)
        cv2.imshow("Frame", IMG)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = IMG[y, x, 0]
        green = IMG[y, x, 1]
        red = IMG[y, x, 2]
        text_BGR = str(blue) + ", " + str(green) + ", " + str(red)
        font = cv2.FONT_HERSHEY_DUPLEX
        color = (200, 200, 200)
        cv2.putText(IMG, text_BGR, (x, y), font, 0.5, color, 1, cv2.LINE_8)
        cv2.imshow("Frame", IMG)

IMG = np.zeros((512, 512, 3), np.uint8)
# IMG = cv2.imread("D:\opencv-master\samples\data\opencv-logo-white.png", 1)

cv2.imshow("Frame", IMG)
cv2.setMouseCallback("Frame", Mouse_Event)

cv2.waitKey(0)
cv2.destroyAllWindows()