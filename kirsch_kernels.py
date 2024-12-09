import cv2 as cv
import numpy as np
def kirsch_kernels(image_path):
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


    img = cv.imread(image_path,cv.IMREAD_UNCHANGED)
    Row = img.shape[0]
    Col = img.shape[1]

    kernels = [
        np.array([[5,  5,  5],
                [-3, 0, -3],
                [-3, -3, -3]]),  # North

        np.array([[-3, -3,  5],
                [-3, 0,  5],
                [-3, -3,  5]]),  # Northeast

        np.array([[-3, -3, -3],
                [-3, 0, -3],
                [ 5,  5,  5]]),  # East

        np.array([[-3, -3, -3],
                [ 5, 0, -3],
                [ 5,  5, -3]]),  # Southeast

        np.array([[-3, -3, -3],
                [-3, 0, -3],
                [-3,  5,  5]]),  # South

        np.array([[ 5, -3, -3],
                [ 5, 0, -3],
                [ 5, -3, -3]]),  # Southwest

        np.array([[ 5,  5, -3],
                [ 5, 0, -3],
                [-3, -3, -3]]),  # West

        np.array([[-3,  5,  5],
                [-3, 0,  5],
                [-3, -3, -3]])   # Northwest
    ]
    edges = np.zeros_like(img, dtype=np.float32)
    kernel_indices = np.zeros_like(img, dtype=np.int32)
    for kernal in kernels:
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
                pixel = (top_left*kernal[0][0])+(top_middle*kernal[0][1])+(top_right*kernal[0][2])+(left*kernal[1][0])+(middle*kernal[1][1])+(right*kernal[1][2])+(bottom_left*kernal[2][0])+(bottom_middle*kernal[2][1])+(bottom_right*kernal[2][2])
                output_img[indexI,indexJ] = np.clip(pixel,0,255)
        temp = edges
        edges = np.maximum(edges, output_img)
        if not np.array_equal(edges, temp):
            kernel_indices = kernal

    cv.imwrite("kernal.jpg", edges)
    u8 = edges.astype(np.uint8)
    return u8