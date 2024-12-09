import numpy as np
from PIL import Image

def calculate_local_variance(image_array, kernel_size):
    """
    Apply variance-based edge detection.
    :param image_array: 2D NumPy array (grayscale image)
    :param kernel_size: Size of the kernel (e.g., 3 for a 3x3 kernel)
    :return: Variance edge map as a 2D NumPy array
    """
    rows, cols = image_array.shape
    edge_map = np.zeros_like(image_array, dtype=np.float32)
    pad_size = kernel_size // 2

    # Pad the image to handle edges
    padded_image = np.pad(image_array, pad_size, mode='reflect')

    # Traverse each pixel
    for i in range(rows):
        for j in range(cols):
            # Extract the neighborhood
            neighborhood = padded_image[i:i + kernel_size, j:j + kernel_size]
            
            # Compute mean and variance
            local_mean = np.mean(neighborhood)
            local_variance = np.mean((neighborhood - local_mean) ** 2)
            
            # Set the variance as the edge strength
            edge_map[i, j] = local_variance

    return edge_map

def normalize_image(image_array):
    """
    Normalize image array to 0-255 range for visualization.
    """
    return (255 * (image_array - np.min(image_array)) / (np.ptp(image_array))).astype(np.uint8)

def variance(image_path):
    # Load the image and convert to grayscale
    image = Image.open(image_path).convert("L")
    image_array = np.array(image)

    # Apply variance-based edge detection
    kernel_size = 3  # Define kernel size
    variance_edges = calculate_local_variance(image_array, kernel_size)

    # Normalize the result for visualization
    normalized_edges = normalize_image(variance_edges)

    # Save or display the result
    u8 = normalized_edges.astype(np.uint8)
    return u8