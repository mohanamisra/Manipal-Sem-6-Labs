import cv2
import numpy as np

img = cv2.imread('/home/mohanamisra/Desktop/apple.jpg', 0)
img = cv2.resize(img, (500, 500))

# Negative Transformation
neg_img = cv2.bitwise_not(img)

# Log Transformation
c = 20
log_img = c * np.log(1 + img)
log_img = np.array(log_img, dtype=np.uint8)

# Power Law Transformation (Gamma)
gamma = 5
normalized_img = img / 255.0  # Normalize the image to [0, 1]
pwr_img = c * np.power(normalized_img, gamma)
pwr_img = np.clip(pwr_img * 255, 0, 255)  # Scale back to [0, 255]
pwr_img = np.array(pwr_img, dtype=np.uint8)

cv2.imshow('neg', neg_img)
cv2.imshow('log', log_img)
cv2.imshow('pw', pwr_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
