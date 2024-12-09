import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def generate_gaussian_kernel(size, sigma):
    """
    Generate a Gaussian kernel.
    :param size: Size of the kernel (e.g., 7 for a 7x7 kernel)
    :param sigma: Standard deviation of the Gaussian
    :return: 2D NumPy array representing the Gaussian kernel
    """
    k = size // 2
    x, y = np.meshgrid(np.arange(-k, k+1), np.arange(-k, k+1))
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    kernel /= np.sum(kernel)
    return kernel

def apply_gaussian_blur(image_array, kernel):
    """
    Apply Gaussian blur to an image using a given kernel.
    :param image_array: 2D NumPy array (grayscale image)
    :param kernel: Gaussian kernel
    :return: Blurred image as a 2D NumPy array
    """
    return convolve2d(image_array, kernel, mode="same", boundary="symm")

def difference_of_gaussians(image_array, kernel1, kernel2):
    """
    Apply Difference of Gaussians (DoG).
    :param image_array: 2D NumPy array (grayscale image)
    :param kernel1: Gaussian kernel for first blur
    :param kernel2: Gaussian kernel for second blur
    :return: DoG result as a 2D NumPy array
    """
    blur1 = apply_gaussian_blur(image_array, kernel1)
    blur2 = apply_gaussian_blur(image_array, kernel2)
    return blur1 - blur2

def normalize_image(image_array):
    """
    Normalize image array to 0-255 range for visualization.
    """
    return (255 * (image_array - np.min(image_array)) / (np.ptp(image_array))).astype(np.uint8)

# Load the image and convert to grayscale
image = Image.open("./Grayscale_MainAfter.jpg").convert("L")
image_array = np.array(image)

# Generate Gaussian kernels (7x7 and 9x9)
kernel_7x7 = generate_gaussian_kernel(7, sigma=1.0)
kernel_9x9 = generate_gaussian_kernel(9, sigma=2.0)

# Apply Difference of Gaussians
dog_result = difference_of_gaussians(image_array, kernel_7x7, kernel_9x9)

# Normalize the result for visualization
normalized_dog = normalize_image(dog_result)

# Save or display the result
output_image = Image.fromarray(normalized_dog)
output_image.save("dog_edge_detection.jpg")
output_image.show()