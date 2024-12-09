import cv2 as cv
path = "Grayscale_MainAfter.jpg"
def halftoning_threshold(image_path):
    Threshold = 114.62288953993055
    img = cv.imread(image_path,cv.IMREAD_UNCHANGED)
    for indexI , i in enumerate(img):
        for indexJ , j in enumerate(i):
            if img[indexI,indexJ] >= Threshold:
                img[indexI,indexJ] =  255
            else:
                img[indexI,indexJ] =  0
    return img