import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def manual_segmentation(image_path, threshold):
    # Load the grayscale image
    image = Image.open(image_path).convert('L')
    image_array = np.array(image)

    # Compute the histogram
    histogram = np.zeros(256, dtype=int)
    for value in image_array.ravel():
        histogram[value] += 1

    # Apply manual segmentation based on the threshold
    segmented_image = np.where(image_array > threshold, 255, 0).astype(np.uint8)

    # Visualize results
    plt.figure(figsize=(12, 6))

    # Original Image
    plt.subplot(2, 2, 1)
    plt.title("Original Image")
    plt.imshow(image_array, cmap='gray')
    plt.axis('off')

    # Histogram
    plt.subplot(2, 2, 2)
    plt.title("Histogram")
    plt.bar(range(256), histogram, color='black')
    plt.axvline(x=threshold, color='red', linestyle='--', label=f'Threshold: {threshold}')
    plt.legend()

    # Segmented Image
    plt.subplot(2, 2, 3)
    plt.title("Segmented Image")
    plt.imshow(segmented_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    return segmented_image