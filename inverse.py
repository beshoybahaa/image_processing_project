import cv2 as cv
import numpy as np
path = "./Grayscale_MainAfter.jpg"
img = cv.imread(path,cv.IMREAD_UNCHANGED)
Row = img.shape[0]
Col = img.shape[1]
print(img.shape)
gray_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for indexI in range(1, Row - 2):
    for indexJ in range(1, Col - 2):
        gray_img[indexI,indexJ]=255-int(img[indexI,indexJ])
print(gray_img.shape)
cv.imwrite("inverse.jpg", gray_img)
