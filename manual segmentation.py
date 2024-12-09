import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_based_segmentation(image_path, threshold_value):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Image could not be loaded.")
        return

    # Initialize a histogram with zeros for each intensity value from 0 to 255
    hist = np.zeros(256)

    # Calculate the histogram manually by iterating over all pixels
    for row in image:
        for pixel in row:
            hist[pixel] += 1

    # Plot the histogram manually
    plt.figure(figsize=(10, 6))
    plt.title("Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # Apply manual thresholding
    segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Save the segmented image
    cv2.imwrite("segmented_image.jpg", segmented_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = "./Grayscale_MainAfter.jpg"
threshold_value = 127  # Set your desired threshold value here
histogram_based_segmentation(image_path, threshold_value)