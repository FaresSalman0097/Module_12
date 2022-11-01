# pip install opencv-python

import cv2
import numpy as np
img = cv2.imread("C:\\Users\\ibrah\\OneDrive\\Pictures\\WhatsApp Image 2022-10-17 at 00.04.43.jpg")
window_name = 'image'
kernel = np.ones((5, 5), np.uint8)     # Unsigned integer - represents 8 bit binary value
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow(window_name,img)
cv2.waitKey(0)
cv2.imshow(window_name,img_erosion)
cv2.waitKey(0)
cv2.imshow(window_name,img_dilation)
cv2.waitKey(0)

