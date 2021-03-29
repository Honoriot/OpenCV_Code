from cv2 import cv2

# print(cv2.__version__)
# cv2.IMREAD_COLOR      1    loads a color image
# cv2.IMREAD_GRAYSCALE  0    loads image in grayscale mode
# cv2.IMREAD_UNCHANGED  -1   loads image as such including alpha channel


img = cv2.imread("lena.jpg", 0)

# print(img)

cv2.imshow("Lena Image", img)
k = cv2.waitKey(0)        # 0 delay means, manually close window

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): 
    cv2.imwrite("Lena_gray.png", img)
    cv2.destroyAllWindows()