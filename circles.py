import cv2
import numpy as np

image = cv2.imread('soap-bubbles-2417436_1920-e1593186009893.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blur
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny edge detector
edges = cv2.Canny(gray, 50, 150)

# Hough transform parameters
dp = 1  # Inverse ratio of the accumulator resolution to the image resolution
min_dist = 50  # Minimum distance between the center of the detected circles
param1 = 50  # First method-specific parameter
param2 = 30  # Second method-specific parameter
min_radius = 20  # Minimum radius of the circle to be detected
max_radius = 100  # Maximum radius of the circle to be detected

# Hough transform
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp, min_dist, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)

# Draw the circles on the input image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 0, 255), 2)
    cv2.imshow("output", image)
    cv2.waitKey(0)
else:
    print("No circles detected")
