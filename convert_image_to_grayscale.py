import cv2 as cv
import numpy as np
path = "MainAfter.jpg"
img = cv.imread(path)
print(img.shape)
gray_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
for indexI , i in enumerate(img):
    for indexJ , j in enumerate(i):
        temp = (0.299*j[0])+(0.587*j[1])+(0.114*j[2])
        gray_img[indexI,indexJ]=temp
print(gray_img.shape)
cv.imwrite("Grayscale_MainAfter.jpg", gray_img)
