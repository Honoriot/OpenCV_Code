import numpy as np
from cv2 import cv2


# for i in dir(cv2):
#     if 'EVENT' in i:
#         print(i)

def Mouse_Event1(Event, X, Y, flag, param):
    if Event == cv2.EVENT_LBUTTONDOWN:
        point1 = (X, Y)
        Point.append(point1)
        cv2.circle(IMG, (X, Y), 0.5, color, -1)
        if len(Point) > 1:
            cv2.line(IMG, Point[-1], Point[-2], color, 0.5, cv2.LINE_AA)
        cv2.imshow("Frame", IMG)
        

def Mouse_Event2(Event, X, Y, flag, param):
    if Event == cv2.EVENT_MOUSEMOVE:
        



Point = []
cv2.setMouseCallback("Frame", Mouse_Event1)