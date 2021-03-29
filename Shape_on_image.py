from cv2 import cv2
import numpy as np

# IMG = cv2.imread("Lena_gray.png", 1)
IMG = np.zeros([512, 512, 3], np.uint8)

IMG = cv2.line(IMG, (0, 0), (200, 200), (200, 100, 100), 2)
IMG = cv2.arrowedLine(IMG, (2, 200), (200, 200), (0, 255, 0), 2)
IMG = cv2.rectangle(IMG, (200, 200), (400, 400), (0, 0, 200), 2)
IMG = cv2.putText(IMG, "Open CV", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 250, 200), 2, cv2.LINE_AA)
cv2.imshow("Lena", IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()