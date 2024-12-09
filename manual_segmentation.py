import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def manual_segmentation(image_path, threshold=128):
    # Load the grayscale image
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)

    # Compute the histogram
    histogram = np.zeros(256, dtype=int)
    for value in image_array.ravel():
        histogram[value] += 1

    # Apply manual segmentation based on the threshold
    segmented_image = np.where(image_array > threshold, 255, 0).astype(np.uint8)
    return segmented_image