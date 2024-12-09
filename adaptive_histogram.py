import cv2
import numpy as np
from skimage.util import view_as_blocks
def adaptive_histogram(image_path):
    # Function for histogram equalization
    def my_hist_eq(img):
        # Convert to grayscale if the image is colored
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Get the dimensions of the image
        x, y = img.shape

        # Calculate the frequency of each intensity value
        freq = np.zeros(256, dtype=int)
        for i in range(x):
            for j in range(y):
                freq[img[i, j]] += 1

        # Calculate the PDF (Probability Density Function)
        total_pixels = x * y
        pdf = freq / total_pixels

        # Calculate the CDF (Cumulative Distribution Function)
        cdf = np.cumsum(pdf)

        # Map the CDF to intensity values (0-255) and round off
        result = np.round(cdf * 255).astype(np.uint8)

        # Apply the transformation to the image
        new_img = np.zeros_like(img, dtype=np.uint8)
        for i in range(x):
            for j in range(y):
                new_img[i, j] = result[img[i, j]]

        return new_img

    # Utility function for block processing with adaptive histogram equalization
    def block_process(img, block_size):
        # Convert to grayscale if the image is colored
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Calculate padding required to make the dimensions divisible by block_size
        pad_height = (block_size[0] - img.shape[0] % block_size[0]) % block_size[0]
        pad_width = (block_size[1] - img.shape[1] % block_size[1]) % block_size[1]

        # Pad the image
        padded_img = np.pad(img, ((0, pad_height), (0, pad_width)), mode='constant', constant_values=0)

        # Divide the padded image into blocks
        blocks = view_as_blocks(padded_img, block_shape=block_size)

        # Process each block with histogram equalization
        processed_img = np.zeros_like(padded_img)
        for i in range(blocks.shape[0]):
            for j in range(blocks.shape[1]):
                block = blocks[i, j]
                processed_block = my_hist_eq(block)
                processed_img[i * block_size[0]:(i + 1) * block_size[0],
                            j * block_size[1]:(j + 1) * block_size[1]] = processed_block

        # Remove padding to return the image to its original size
        return processed_img[:img.shape[0], :img.shape[1]]


    # Main script to read images and apply histogram equalization
    

    # Read the image
    img = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
    print(img)
    # Apply adaptive histogram equalization with block size
    block_size = (100, 100)
    ahe_img = block_process(img, block_size)
    return ahe_img
        # Display the results
        # cv2.imshow("Original Image", img)
        # cv2.imshow("Adaptive Histogram Equalized Image", ahe_img)

        # # Wait for 10 seconds and close all windows
        # cv2.waitKey(10000)
        # cv2.destroyAllWindows()
