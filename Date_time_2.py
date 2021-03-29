import datetime
from cv2 import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    rel, frame = cam.read()
    if rel == True:
        text = str(datetime.datetime.now())
        font = cv2.FONT_ITALIC
        color = (200, 200, 200)
        frame = cv2.putText(frame, text, (0, 50), font, 0.7, color, 2, cv2.LINE_AA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()