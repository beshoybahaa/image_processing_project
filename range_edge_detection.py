import numpy as np
import cv2
import matplotlib.pyplot as plt

def range_edge_detection(image, kernel_size):
    """
    Apply range-based edge detection to an image.
    :param image: Input grayscale image (2D numpy array).
    :param kernel_size: Size of the local neighborhood (odd number).
    :return: Edge-detected image.
    """
    # Calculate padding size
    pad_size = kernel_size // 2
    
    # Pad the image
    padded_image = np.pad(image, pad_size, mode='reflect')
    
    # Create an output array
    edge_image = np.zeros_like(image, dtype=np.float32)
    
    # Traverse through the image
    for i in range(pad_size, padded_image.shape[0] - pad_size):
        for j in range(pad_size, padded_image.shape[1] - pad_size):
            # Extract local neighborhood
            neighborhood = padded_image[i-pad_size:i+pad_size+1, j-pad_size:j+pad_size+1]
            
            # Calculate range (max - min)
            edge_image[i-pad_size, j-pad_size] = neighborhood.max() - neighborhood.min()
    
    # Normalize the result to range [0, 255]
    edge_image = cv2.normalize(edge_image, None, 0, 255, cv2.NORM_MINMAX)
    return edge_image.astype(np.uint8)

# Load a sample image
image_path = './Grayscale_MainAfter.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply range-based edge detection
kernel_size = 5  # Neighborhood size
edges = range_edge_detection(image, kernel_size)

# Plot the original and edge-detected images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Edge-Detected Image (Range)")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()