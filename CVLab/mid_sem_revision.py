import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/mohanamisra/Desktop/feather.jpg')
img = cv2.resize(img,(500,500))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(20,20))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img)

img_hist = cv2.calcHist([img1], [0], None, [256], [0, 256])
plt.subplot(2, 2, 2)
plt.title('Histogram')
plt.plot(img_hist)

plt.subplot(2, 2, 3)
plt.hist(img1.ravel(), 256, [0, 256])
plt.title('Also Histogram')

final_img = cv2.equalizeHist(img1)

cv2.imshow('Original Image', img)
cv2.imshow('final', final_img)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
