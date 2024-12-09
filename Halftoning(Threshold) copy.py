import cv2 as cv
path = "Grayscale_MainAfter.jpg"
img = cv.imread(path,cv.IMREAD_UNCHANGED)
# Initialize error propagation and generation matrices
R = img.shape[0]
C = img.shape[1] # Example dimensions, adjust as needed
Ep = [[0 for _ in range(C)] for _ in range(R)]
Eg = [[0 for _ in range(C)] for _ in range(R)]
threshold = 128  # Example threshold, adjust as needed

# Example image matrix I
I = img

# Loop over each row
for m in range(R):
    # Loop over each column
    for n in range(C):
        # Calculate the total propagated error at (m, n)
        total_error = Ep[m][n]
        
        # Sum the current pixel value and the total propagated error
        T = I[m][n] + total_error
        
        if T > threshold:
            # Set pixel (m, n) on
            I[m][n] = 255
            # Calculate error generated at current location
            Eg[m][n] = T - 2 * threshold
        else:
            # Set pixel (m, n) off
            I[m][n] = 0
            # Calculate error generated at current location
            Eg[m][n] = threshold
        
        # Propagate the error to neighboring pixels (example for Floyd-Steinberg dithering)
        if n + 1 < C:
            Ep[m][n + 1] += Eg[m][n] * 7 / 16
        if m + 1 < R:
            if n > 0:
                Ep[m + 1][n - 1] += Eg[m][n] * 3 / 16
            Ep[m + 1][n] += Eg[m][n] * 5 / 16
            if n + 1 < C:
                Ep[m + 1][n + 1] += Eg[m][n] * 1 / 16

cv.imwrite("Halftoning(Threshold).jpg", img)