import cv2
import numpy as np

# reads image
hwy = cv2.imread('Homework 4/HWY447.png')

# converts color image to grayscale
gray = cv2.cvtColor(hwy, cv2.COLOR_BGR2GRAY)

# applies guassian blur to remove background noise
blur = cv2.medianBlur(gray,5)

# canny edge detection: minVal=50, maxVal=150
edges = cv2.Canny(blur, 50, 150)

# applies probabilistic hough line transform method on 'edges' to obtain line end points
# returns list of x,y coordinates of endpoints of each line
lines = cv2.HoughLinesP(edges,
            1, # Distance resolution in pixels
            np.pi / 180, # Angle resolution in radians
            threshold = 100, # Min number of votes for valid line
            minLineLength = 40, # Min allowed length of line
            maxLineGap = 20 # Max allowed gap between line for joining them
            )

# iterates over lines, draws the
lines_array = []
for points in lines:
    # Extracted points nested in the array
    x1,y1,x2,y2 = points[0]
    # Draw the lines joing the points on the original image
    cv2.line(hwy, (x1,y1), (x2,y2), (0,255,0), 2)
    # Maintain a simple lookup list for points
    lines_array.append([(x1,y1), (x2,y2)])
     
# Save the result image as 'detectedLines.png'
cv2.imwrite('Homework 4/detectedLines.png',hwy)