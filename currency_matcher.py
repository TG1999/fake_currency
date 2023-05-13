# -*- coding: utf-8 -*-
"""Currency Matcher.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/0B20zzeVCKx43Mk9Gamc5WEYxT1ZhYnIwT2w3Y3lyYThjTUZv
"""

from matplotlib import pyplot as plt
import cv2
import math
import numpy as np

max_val = 8
max_pt = -1
max_kp = 0

orb = cv2.ORB_create()

x = input("Enter image path: ")

test_img = cv2.imread(x)

(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set=['face/100_gandhi.jpg','face/2000_gandhi.jpg','face/500_gandhi.jpg','face/200_gandhi.jpg']

for i in range(0, len(training_set)):
    train_img = cv2.imread(training_set[i])
    (kp2, des2) = orb.detectAndCompute(train_img, None)
    bf = cv2.BFMatcher()
    all_matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for (m, n) in all_matches:
        if m.distance < 0.789 * n.distance:
            good.append([m])
    if len(good) > max_val:
        max_val = len(good)
        max_pt = i
        max_kp = kp2
    print(i, ' ', training_set[i], ' ', len(good))
print(all_matches)
if max_val > 50 :
    print(training_set[max_pt])
    print('good matches ', max_val)

train_img = cv2.imread(training_set[max_pt])
img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
note = str(training_set[max_pt]).split('.')
note=note[0]
print('\nDetected denomination: Rs. ', note)

(plt.imshow(img3), plt.show())

