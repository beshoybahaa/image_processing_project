import numpy as np
import cv2
from matplotlib import pyplot as plt

def homogeneity_operator(image, threshold=30):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Get the dimensions of the image
    rows, cols = gray_image.shape
    
    # Create an empty image to store the result
    result = np.zeros((rows, cols), dtype=np.uint8)
    
    # Loop over each pixel in the image (excluding the border pixels)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # Get the center pixel value
            center_pixel = gray_image[i, j]
            
            # Get the neighboring pixel values
            neighbors = [
                gray_image[i-1, j-1], gray_image[i-1, j], gray_image[i-1, j+1],
                gray_image[i, j-1], gray_image[i, j+1],
                gray_image[i+1, j-1], gray_image[i+1, j], gray_image[i+1, j+1]
            ]
            
            # Calculate the maximum absolute difference
            max_diff = max([abs(center_pixel - neighbor) for neighbor in neighbors])
            
            # Apply the threshold
            if max_diff > threshold:
                result[i, j] = 255
            else:
                result[i, j] = 0
    
    return result

# Load the image
image = cv2.imread("./Grayscale_MainAfter.jpg")

# Apply the homogeneity operator
edges = homogeneity_operator(image, threshold=30)

# Display the result
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(edges, cmap='gray'), plt.title('Edges')
plt.show()
