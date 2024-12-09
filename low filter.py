import cv2 as cv
import numpy as np

def matrixmultiply(matrix1, matrix2):
    # Resultant matrix initialized to 0
    result = [[0 for matrix1 in range(3)] for matrix1 in range(3)]

    # Perform matrix multiplication
    for i in range(3):  # Row of matrix1
        for j in range(3):  # Column of matrix2
            for k in range(3):  # Iterate through row-column pairs
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    value = 0
    for i in range(3):
         for j in range(3):
              value = value + result[i][j]
    return value

path = "Grayscale_MainAfter.jpg"
img = cv.imread(path,cv.IMREAD_UNCHANGED)
Row = img.shape[0]
Col = img.shape[1]

kernal = [[0,1,0],
          [1,2,1],
          [0,1,0]]
kernal_value = 1/6

output_img = np.copy(img)
for indexI in range(1, Row - 2):
    for indexJ in range(1, Col - 2):
        # if not i==0 and not i==Row-1:
        #     if not j==0 and not j==Col-1:
        top_left = img[indexI-1,indexJ-1]
        top_middle = img[indexI,indexJ-1]
        top_right = img[indexI+1,indexJ-1]
        left = img[indexI-1,indexJ]
        middle = img[indexI,indexJ]
        right = img[indexI+1,indexJ]
        bottom_left = img[indexI-1,indexJ+1]
        bottom_middle = img[indexI,indexJ+1]
        bottom_right = img[indexI+1,indexJ+1]
        pixel_matrix = [[top_left,top_middle,top_right],
                        [left,middle,right],
                        [bottom_left,bottom_middle,bottom_right]]
        # result = matrixmultiply(pixel_matrix,kernal)
        X = kernal_value*((top_left*kernal[0][0])+(top_middle*kernal[0][1])+(top_right*kernal[0][2])+(left*kernal[1][0])+(middle*kernal[1][1])+(right*kernal[1][2])+(bottom_left*kernal[2][0])+(bottom_middle*kernal[2][1])+(bottom_right*kernal[2][2]))

        output_img[indexI,indexJ] = np.clip(X,0,255)
cv.imwrite("kernal.jpg", output_img)