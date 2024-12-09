import numpy as np
import cv2

def add_image_and_copy(image_path):
    # Load the original image
    original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if original_image is None:
        print("Error: Image could not be loaded.")
        return

    # Make a copy of the original image
    copied_image = original_image.copy()

    # Add the original image and its copy
    added_image = cv2.subtract(original_image, copied_image)

    # Save the resulting image
    cv2.imwrite("subtracted_image.png", added_image)
add_image_and_copy("./Grayscale_MainAfter.jpg")