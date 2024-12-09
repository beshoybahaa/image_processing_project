import cv2 as cv
import numpy as np

def inverse(image_path):
    img = cv.imread(image_path,cv.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Image could not be loaded.")
        return
    Row = img.shape[0]
    Col = img.shape[1]
    gray_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    print(gray_img.shape)
    print(img.shape)
    for indexI in range(1, Row - 2):
        for indexJ in range(1, Col - 2):
            gray_img[indexI,indexJ]=255-img[indexI,indexJ]
    return cv.cvtColor(gray_img, cv.IMREAD_GRAYSCALE)