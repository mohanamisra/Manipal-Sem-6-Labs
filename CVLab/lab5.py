import cv2
import numpy as np

img = cv2.imread('/home/mohanamisra/Desktop/apple.jpg')
img = cv2.resize(img, (500, 350))

blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
sobelx = cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize = 3)
sobely = cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize = 3)
edges = cv2.bitwise_or(sobelx, sobely)
edges = np.array(edges, dtype = 'uint8')
edges = cv2.Canny(blurred_img, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()