import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def generate_smoothing_kernel(size):
    """
    Generate a smoothing kernel (e.g., uniform averaging kernel).
    :param size: Size of the kernel (e.g., 3 for a 3x3 kernel)
    :return: 2D NumPy array representing the smoothing kernel
    """
    kernel = np.ones((size, size), dtype=np.float32)
    kernel /= np.sum(kernel)
    return kernel

def apply_smoothing(image_array, kernel):
    """
    Apply smoothing to an image using a given kernel.
    :param image_array: 2D NumPy array (grayscale image)
    :param kernel: Smoothing kernel
    :return: Smoothed image as a 2D NumPy array
    """
    return convolve2d(image_array, kernel, mode="same", boundary="symm")

def contrast_based_edge_detection(image_array, smoothing_kernel):
    """
    Apply contrast-based edge detection using a smoothing mask.
    :param image_array: 2D NumPy array (grayscale image)
    :param smoothing_kernel: Kernel for smoothing the image
    :return: Edge-detected image as a 2D NumPy array
    """
    # Step 1: Smooth the image
    smoothed_image = apply_smoothing(image_array, smoothing_kernel)

    # Step 2: Compute contrast-based edges
    edge_map = np.zeros_like(image_array, dtype=np.float32)
    rows, cols = image_array.shape

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Compute intensity difference between center pixel and neighbors
            neighbors = [
                smoothed_image[i - 1, j],  # top
                smoothed_image[i + 1, j],  # bottom
                smoothed_image[i, j - 1],  # left
                smoothed_image[i, j + 1],  # right
            ]
            contrast = max(abs(smoothed_image[i, j] - n) for n in neighbors)
            edge_map[i, j] = contrast

    return edge_map

def normalize_image(image_array):
    """
    Normalize image array to 0-255 range for visualization.
    """
    return (255 * (image_array - np.min(image_array)) / (np.ptp(image_array))).astype(np.uint8)

# Load the image and convert to grayscale
image = Image.open("./Grayscale_MainAfter.jpg").convert("L")
image_array = np.array(image)

# Generate a smoothing kernel (e.g., 3x3)
smoothing_kernel = generate_smoothing_kernel(3)

# Apply contrast-based edge detection
contrast_edges = contrast_based_edge_detection(image_array, smoothing_kernel)

# Normalize the result for visualization
normalized_edges = normalize_image(contrast_edges)

# Save or display the result
output_image = Image.fromarray(normalized_edges)
output_image.save("contrast_edge_detection.jpg")
output_image.show()