from cv2 import cv2

cam = cv2.VideoCapture(0)   # 0 for default camera, -1 for default camera if 0 is not working
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))



while cam.isOpened():
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # for gray source image
        # print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # can also set window size
        # cam.set(3, 1280)  , 3 defines here for width
        # cam.set(4, 700)  , 4 defines here for height
        out.write(frame)
        cv2.imshow("Frame", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break

cam.release()
out.release()
cv2.destroyAllWindows()