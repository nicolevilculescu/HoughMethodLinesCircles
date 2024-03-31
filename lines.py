# Write an algorithm for line and circle detection using the Hough method and apply it to images that contain potential
# lines and circles. Vary the arguments given to the algorithms and see the results.

import cv2
import numpy as np

image = cv2.imread('photo-1559097622-2cff6decd452.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# probabilistic
img = cv2.imread('photo-1559097622-2cff6decd452.jpeg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

cv2.imshow("Result Image", img)
cv2.waitKey(0)

# standard
# Canny edge detector
edges = cv2.Canny(gray, 50, 200)

# Hough transform
lines = cv2.HoughLines(edges, 1, np.pi / 180.0, 120, np.array([]))

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)

    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("output", image)
cv2.waitKey(0)

cv2.destroyAllWindows()