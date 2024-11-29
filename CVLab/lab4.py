import cv2
import numpy as np

img = cv2.imread('/home/mohanamisra/Desktop/apple.jpg')
img = cv2.resize(img, (500, 350))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

medianblur_img = cv2.medianBlur(gray_img, 9)
gaussianblur_img = cv2.GaussianBlur(gray_img, (5,5), 0)
laplacian_img = cv2.Laplacian(gray_img, cv2.CV_64F)
laplacian_img = np.uint8(np.absolute(laplacian_img))
sharpened_img = cv2.addWeighted(medianblur_img, 1.5, laplacian_img, -0.5, 0)
# _, laplacian_img = cv2.threshold(laplacian_img, 10, 255, cv2.THRESH_BINARY)

# cv2.imshow('Original', img)
cv2.imshow('blur', medianblur_img)
cv2.imshow('sharpened_img', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()