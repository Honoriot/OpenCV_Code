import numpy as np
from cv2 import cv2

def Mouse_Event(Event, X, Y, Flags, param):
    if Event == cv2.EVENT_LBUTTONDOWN:
        blue = IMG[Y, X, 0]
        green = IMG[Y, X, 1]
        red = IMG[Y, X, 2]
        Color_window = np.zeros((300, 300, 3), np.uint8)
        Color_window[:] = [blue, green, red]
        cv2.imshow("Color_Frame", Color_window)

IMG = cv2.imread("lena.jpg", 1)
cv2.imshow("Frame", IMG)
cv2.setMouseCallback("Frame", Mouse_Event)

cv2.waitKey(0)
cv2.destroyAllWindows()