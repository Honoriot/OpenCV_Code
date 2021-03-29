from cv2 import cv2
import time

cam = cv2.VideoCapture(0)

while cam.isOpened():
    rel, frame = cam.read()
    if rel == True:
        text = time.ctime()
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 0, 0)
        frame = cv2.putText(frame, text, (0, 50), font, 0.7, color, 2, cv2.LINE_AA)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()