import numpy as np
import cv2
from matplotlib import pyplot as plt


def difference_operator(image_path, threshold=30):
    # Get the dimensions of the image
    image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    print(image.shape)
    rows, cols = image.shape

    # Create an empty image to store the result
    result = np.zeros((rows, cols), dtype=np.uint8)
    
    # Loop over each pixel in the image (excluding the border pixels)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            listOfMatrix = []
            listOfMatrix.append(abs(image[i-1, j-1]-image[i+1, j+1]))
            listOfMatrix.append(abs(image[i-1, j]-image[i+1, j]))
            listOfMatrix.append(abs(image[i, j-1]-image[i, j+1]))
            listOfMatrix.append(abs(image[i-1, j+1]-image[i+1, j-1]))
            # Calculate the maximum absolute difference
            max_diff = max(listOfMatrix)
            
            # Apply the threshold
            if max_diff > threshold:
                result[i, j] = 255
            else:
                result[i, j] = 0
    
    return result

