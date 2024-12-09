import numpy as np
import cv2

def add_image(image_path):
    print(image_path)
    # Load the original image
    original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if original_image is None:
        print("Error: Image could not be loaded.")
        return
    # Make a copy of the original image
    copied_image = original_image.copy()
    # Add the original image and its copy
    added_image = cv2.add(original_image, copied_image)
    # Save the resulting image
    cv2.imwrite("added_image.png", added_image)
    return added_image
