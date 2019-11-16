# -*- coding: utf-8 -*-
"""HSV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/0B20zzeVCKx43R2U0ZjJPYUd2YzM3aXZSNGpUT29kYV8xSWc0
"""

import numpy as np

import cv2

import operator

img2 = cv2.imread('500_real.jpg')

cv2.imshow('img3',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()



hsv_img=cv2.cvtColor(img2, cv2.COLOR_RGB2HSV)

cv2.imshow('img3',hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

# edges = cv2.Canny(hsv_img,150,400)

# #edges=auto_canny(hsv_img)

# cv2.imshow('img3',edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

gray=cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

cv2.imshow('img3',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

surf = cv2.xfeatures2d.SURF_create(25000,upright=True)

(kps, descs) = surf.detectAndCompute(gray, None)

len(kps)

img3 = cv2.drawKeypoints(gray,kps,None,(255,0,0),4)

cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

A=[]
for i in kps:
    A.append(i.pt[0])
A.sort()
d={}
for i in A:
    try:
        d[i//10]+=1
    except:
        d[i//10]=1
print(d)
point=[]
imp_point=[]
for x,y in d.items():
    if y>4 and y<15:
        imp_point.append(x) 
print(imp_point)
for i in kps:
    if i.pt[0]//10 in imp_point:
        point.append(i)
img3 = cv2.drawKeypoints(gray,point,None,(255,0,0),4)

cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
shap=hsv_img.shape

hsv_img

saturation=np.zeros([shap[0],shap[1]])
print(saturation.shape)
for i in range(shap[0]):
    for j in range(shap[1]):
        saturation[i][j]=hsv_img[i][j][2]

saturation

print(np.mean(saturation))

