import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(0.1)
count = 0
background = 0
# CHANGE COLOR HERE
# HUE VALUE: RED:0~10+156~180, GREEN:35~77, BLUE:100~124
HUE_LOWER = 35
HUE_UPPER = 77
SATURATION_LOWER = 43
SATURATION_UPPER = 255
VALUE_LOWER = 46
VALUE_UPPER = 255
for i in range(3):
    ret, background = cap.read()
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    count += 1
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([HUE_LOWER, SATURATION_LOWER, VALUE_LOWER])
    upper = np.array([HUE_UPPER, SATURATION_UPPER, VALUE_UPPER])
    mask = cv2.inRange(hsv, lower, upper)
    mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('invisibility', final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
