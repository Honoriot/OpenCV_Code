import numpy as np
from cv2 import cv2

def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        color = (255, 0, 0)
        points.append((x, y))
        cv2.circle(IMG, (x, y), 2, color, -1)
        if len(points) > 1:
            cv2.line(IMG, points[-1], points[-2], color, 2, cv2.LINE_AA)
        cv2.imshow("Frame", IMG)

IMG = np.zeros((600, 600, 3), np.uint8)
cv2.imshow("Frame", IMG)
points = []
cv2.setMouseCallback("Frame", mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()