import cv2

img1 = cv2.imread('/home/mohanamisra/Desktop/apple.jpg')
img1 = cv2.resize(img1,(700,500))
img2 = cv2.imread('/home/mohanamisra/Desktop/apple2.jpg')
img2 = cv2.resize(img2,(700,500))

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)
matched_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], img2, flags=2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('matched image', matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()