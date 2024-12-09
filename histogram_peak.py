import numpy as np
import cv2
from scipy.signal import find_peaks

def histogram_peak(image_path):
    def find_histogram_peaks(hist, distance=10):
        peaks, _ = find_peaks(hist, distance=distance)
        return peaks

    def peak_threshold_segmentation(image, low_threshold, high_threshold):
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Calculate the histogram
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256]).flatten()
        
        # Find the peaks in the histogram
        peaks = find_histogram_peaks(hist)
        
        # Sort peaks by height
        sorted_peaks = sorted(peaks, key=lambda x: hist[x], reverse=True)
        
        # Select the two highest peaks
        if len(sorted_peaks) >= 2:
            peak1, peak2 = sorted_peaks[:2]
            low_threshold = min(peak1, peak2)
            high_threshold = max(peak1, peak2)
        else:
            raise ValueError("Not enough peaks found in the histogram.")
        
        # Apply thresholding
        _, binary_image = cv2.threshold(gray_image, low_threshold, high_threshold, cv2.THRESH_BINARY)
        
        return binary_image, hist, peaks

    # Load the image
    image = cv2.imread(image_path)

    # Apply the peak threshold segmentation
    segmented_image, hist, peaks = peak_threshold_segmentation(image, low_threshold=0, high_threshold=255)
    return segmented_image