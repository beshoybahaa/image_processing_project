import cv2 as cv
import numpy as np

def inverse(image_path):
    img = cv.imread(image_path,cv.IMREAD_UNCHANGED)
    if img is None:
        print("Error: Image could not be loaded.")
        return
    Row = img.shape[0]
    Col = img.shape[1]
    gray_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    for indexI in range(1, Row - 2):
        for indexJ in range(1, Col - 2):
            gray_img[indexI,indexJ]=255-int(img[indexI,indexJ])
    return gray_img
