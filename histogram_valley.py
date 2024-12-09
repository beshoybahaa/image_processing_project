import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def histogram_valley(image_path):
    # Load the grayscale image
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image_array = np.array(image)

    # Calculate histogram
    histogram = np.zeros(256)
    for pixel in image_array.ravel():
        histogram[pixel] += 1

    # Find valleys (local minima) in the histogram
    valleys = []
    for i in range(1, len(histogram) - 1):
        if histogram[i] < histogram[i - 1] and histogram[i] < histogram[i + 1]:
            valleys.append(i)

    # Apply thresholds based on valleys
    thresholds = valleys
    segmented_image = np.zeros_like(image_array)

    # Segment based on thresholds
    for i, threshold in enumerate(thresholds):
        if i == 0:
            segmented_image[image_array <= threshold] = (i + 1) * (255 // (len(thresholds) + 1))
        else:
            segmented_image[(image_array > thresholds[i - 1]) & (image_array <= threshold)] = (i + 1) * (255 // (len(thresholds) + 1))
    segmented_image[image_array > thresholds[-1]] = 255  # Assign the brightest region
    return segmented_image