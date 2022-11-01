import cv2
import numpy as np

# Load image, create mask, and draw white circle on mask
img = cv2.imread("C:\\Users\\ibrah\\OneDrive\\Pictures\\WhatsApp Image 2022-10-17 at 00.04.43.jpg")
window_name = 'image'
mask = np.zeros(img.shape, dtype=np.uint8)
mask = cv2.circle(mask, (260, 300), 225, (255,255,255), -1)
result = cv2.bitwise_and(img, mask)

cv2.imshow(window_name,img)
cv2.waitKey(0)
cv2.imshow(window_name,mask)
cv2.waitKey(0)
cv2.imshow(window_name,result)
cv2.waitKey(0)



