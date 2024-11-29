import cv2

img = cv2.imread(r'/home/mohanamisra/Desktop/apple.jpg')
img = cv2.resize(img,(500,350))

# ROTATING IMAGE
angle = 45

h, w = img.shape[:2]

M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
rotated_img = cv2.warpAffine(img, M, (w, h))

cv2.imshow('img', img)
cv2.imshow('rotated_img', rotated_img)

# SCALING IMAGE

import numpy as np

rows, cols, _ = img.shape
img_shrinked = cv2.resize(img, (50, 50), interpolation = cv2.INTER_AREA)
cv2.imshow('img_shrinked', img_shrinked)

img_enlarged = cv2.resize(img, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('img_enlarged', img_enlarged)

# TRANSLATING IMAGE

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img_translated', dst)

# SHEARING IMAGE

M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))
cv2.imshow('sheared_img', sheared_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
