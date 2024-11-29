import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/home/mohanamisra/Desktop/apple.jpg')
img = cv2.resize(img,(500,500))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.title('Original Image')
plt.imshow(img)

img_hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.subplot(222)
plt.title('Histogram 1')
plt.plot(img_hist)

plt.subplot(223)
plt.title('Histogram 2')
plt.hist(gray_img.ravel(), 256, [0, 256])

final_img = cv2.equalizeHist(gray_img)
plt.subplot(224)
plt.imshow(cv2.cvtColor(final_img, cv2.COLOR_BGR2RGB))

plt.show()
plt.savefig('/home/mohanamisra/Desktop/histogram.jpg')

cv2.imshow('Original Image', img)
cv2.imshow('Histogram Equalization', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
