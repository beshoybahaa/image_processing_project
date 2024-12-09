import cv2 as cv
import numpy as np
def hugh_filter(image_path):
    img = cv.imread(image_path,cv.IMREAD_UNCHANGED)
    Row = img.shape[0]
    Col = img.shape[1]

    kernal = [[0,-1,0],
            [-1,5,-1],
            [0,-1,0]]

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
            X = ((top_left*kernal[0][0])+(top_middle*kernal[0][1])+(top_right*kernal[0][2])+(left*kernal[1][0])+(middle*kernal[1][1])+(right*kernal[1][2])+(bottom_left*kernal[2][0])+(bottom_middle*kernal[2][1])+(bottom_right*kernal[2][2]))

            output_img[indexI,indexJ] = np.clip(X,0,255)
    return output_img