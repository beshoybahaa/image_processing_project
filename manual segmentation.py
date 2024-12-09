import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_based_segmentation(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    hist, bins = np.histogram(image.flatten(), 256, [0, 256])


    plt.figure(figsize=(10, 5))
    plt.title("Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    plt.plot(hist)
    plt.show()
    threshold = np.argmax(hist[100:]) + 100  # Adjust the range as needed


    segmented_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Segmented Image")
    plt.imshow(segmented_image, cmap='gray')
    plt.axis('off')

    plt.show()
histogram_based_segmentation('./Grayscale_MainAfter.jpg')