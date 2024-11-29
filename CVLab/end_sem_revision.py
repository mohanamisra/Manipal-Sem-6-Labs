import cv2
import numpy as np

cap = cv2.VideoCapture('/home/mohanamisra/Desktop/video.mp4')
ret, frame = cap.read()
frame = cv2.resize(frame, (300, 200))
old_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=False)

motion_thresh = 2
min_contour_area = 500

cv2.setUseOptimized(True)
cv2.setNumThreads(4)
tracker = cv2.legacy.MultiTracker_create()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (300, 200))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)

    flow = cv2.calcOpticalFlowFarneback(old_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    motion_mask = (mag > motion_thresh).astype(np.uint8) * fgmask
    contours, _ = cv2.findContours(motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for contour in contours:
        area = cv2.contourArea(contour)
        bbox = cv2.boundingRect(contour)
        if area > min_contour_area:
            detections.append(bbox)

    if len(tracker.getObjects()) == 0 or len(detections) > 0:
        for bbox in detections:
            tracker.add(cv2.legacy.TrackerKCF_create(), frame, bbox)

    success, boxes = tracker.update(frame)

    for i, bbox in enumerate(detections):
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
