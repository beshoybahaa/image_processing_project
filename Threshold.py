import cv2 as cv
def threshold(image_path):
    img = cv.imread(image_path,cv.IMREAD_UNCHANGED)
    print(img.shape)
    sumOfPixels = 0
    for indexI , i in enumerate(img):
        for indexJ , j in enumerate(i):
            sumOfPixels = sumOfPixels + img[indexI,indexJ]
    Threshold = sumOfPixels/(img.shape[0]*img.shape[1])
    return Threshold