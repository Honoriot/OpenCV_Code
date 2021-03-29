from cv2 import cv2
import numpy as np

IMG = cv2.imread("messi5.jpg", 1)

print(IMG.shape)
print(IMG.size)
print(IMG.dtype)
b, g, r = cv2.split(IMG)
IMG = cv2.merge((b, g, r))

ball = IMG[280:340, 330:390]  # upper left corner and bottom right corner
IMG[273:333, 100:160] = ball  

cv2.imshow("Frame", IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()