
import numpy as np
print(np.__path__)
import os
#file1 = os.startfinle("Day_15n_10_-3_RGB.jpg")

import cv2
# Save image in set directory
# Read RGB image
img = cv2.imread('Day_15_10_-3_RGB.jpg')
imS = cv2.resize(img, (int(img.shape[0]/10), int(img.shape[1]/10)))

cv2.imshow('my first image', imS)

cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()
i=1

cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
im = cv2.imread("earth.jpg")                        # Read image
imS = cv2.resize(img, (960, 540))                    # Resize image
cv2.imshow("output", imS)                            # Show image
cv2.waitKey(0)