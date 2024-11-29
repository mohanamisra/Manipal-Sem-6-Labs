import cv2

# WHAT DOES im.read() DO?
img = cv2.imread('/home/mohanamisra/Desktop/apple.jpg')
print(type(img))
print(img.shape)

# TO RESIZE THE IMAGE CUZ IT IS TOO BIG TO DISPLAY
img = cv2.resize(img, (500, 350))

# imshow() works only with waitKey() as well
cv2.imshow('My Image', img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Black and white image', gray_img)
print(type(gray_img))
print(gray_img.shape)
cv2.waitKey()
cv2.destroyAllWindows()

# TO READ A VIDEO FILE
# capture = cv2.VideoCapture('/home/mohanamisra/Desktop/video.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#     if not isTrue:
#         break
#     frame = cv2.resize(frame, (500, 720))
#     cv2.imshow('Haan Ke Haan by T Series', frame)
#     if cv2.waitKey(5) & 0xFF == ord('x'):
#         break
# capture.release()
# cv2.destroyAllWindows()
