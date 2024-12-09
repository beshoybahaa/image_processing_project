import cv2 as cv
import numpy as np

def histogram_equalization(image_path):

    img = cv.imread(image_path,cv.IMREAD_GRAYSCALE)
    Row = img.shape[0]
    Col = img.shape[1]
    # Step 1: Calculate histogram
    hist = [0] * 256  # Assuming 8-bit grayscale image
    for i in range(Row):
        for j in range(Col):
            k = img[i][j]
            hist[k] += 1

    # Step 2: Calculate the cumulative distribution function (CDF)
    sum_of_hist = [0] * 256
    sum = 0
    for i in range(256):  # Assuming 256 gray levels
        sum += hist[i]
        sum_of_hist[i] = sum

    # Step 3: Transform input image to output image
    area = Row * Col
    Dm = 255  # Number of gray levels in output image (0-255 for 8-bit image)
    out_image = [[0] * Col for _ in range(Row)]
    for i in range(Row):
        for j in range(Col):
            k = img[i][j]
            out_image[i][j] = (Dm / area) * sum_of_hist[k]

    out_image = np.array(out_image)
    return out_image