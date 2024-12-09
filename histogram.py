import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def histogram(image_path):
    # Load the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)

    # Compute the histogram
    histogram = np.zeros(256, dtype=int)  # For grayscale, intensity ranges from 0 to 255
    for pixel_value in image_array.ravel():  # Flatten the 2D array
        histogram[pixel_value] += 1

    # Plot the histogram
    plt.figure(figsize=(10, 5))
    plt.bar(range(256), histogram, color='gray')
    plt.title("Histogram of the Image")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

    # Analyze the histogram
    total_pixels = image_array.size
    dark_pixels = sum(histogram[:50]) / total_pixels
    bright_pixels = sum(histogram[205:]) / total_pixels
    contrast_range = np.ptp(image_array)  # Range of pixel intensities

    # Generate an alert based on analysis
    if dark_pixels > 0.5:
        alert = "The image is too dark. Most pixel intensities are low."
    elif bright_pixels > 0.5:
        alert = "The image is too bright. Most pixel intensities are high."
    elif contrast_range < 50:
        alert = "The image has low contrast. Pixel intensities are clustered."
    else:
        alert = "The histogram is well-distributed. The image has good contrast."

    print(alert)
    return histogram, alert