import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def error_diffusion_halftone(image_path):
    # Load the image and convert to grayscale
    image = Image.open(image_path).convert('L')
    image_array = np.array(image, dtype=np.float32)  # Use float for error calculation

    # Get the dimensions of the image
    height, width = image_array.shape

    # Create an empty binary output image
    halftone_image = np.zeros_like(image_array, dtype=np.uint8)

    # Define the Floyd-Steinberg error diffusion kernel
    error_diffusion_kernel = [
        (1, 0, 7/16),
        (-1, 1, 3/16),
        (0, 1, 5/16),
        (1, 1, 1/16)
    ]

    # Iterate over each pixel in the image
    for y in range(height):
        for x in range(width):
            # Threshold the current pixel
            old_pixel = image_array[y, x]
            new_pixel = 255 if old_pixel > 127 else 0
            halftone_image[y, x] = new_pixel

            # Calculate the error
            error = old_pixel - new_pixel

            # Diffuse the error to neighboring pixels
            for dx, dy, factor in error_diffusion_kernel:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    image_array[ny, nx] += error * factor



    # Save the halftone image
    halftone_image_pil = Image.fromarray(halftone_image)
    return halftone_image_pil