import cv2
import numpy as np

img = cv2.imread('/home/mohanamisra/Desktop/apple.jpg')
img = cv2.resize(img, (500, 350))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

row, column = img.shape
img1 = np.zeros((row, column), dtype = 'uint8')

min_range = 40
max_range = 140

for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255
        else:
            img1[i, j] = img[i - 1, j - 1]

cv2.imshow('Original', img)
cv2.imshow('Sliced', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()