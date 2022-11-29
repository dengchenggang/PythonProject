#!/usr/bin/python3
# -*-coding: utf-8 -*-

import numpy as np
import cv2

np.set_printoptions(suppress=True)

pts_in = np.float32([[0, 0], [650, 0],
                   [0, 200], [650, 200]])
pts_out = np.float32([[0, 0], [1079, 0],
                   [(1079-1010)/2, 309], [(1079+1010)/2, 309]])
pts_out = pts_out * 650 / 1079
print(pts_out)

T = cv2.getPerspectiveTransform(pts_in, pts_out)
print(T)
img = cv2.imread('/Users/banma-1574/LearnOpenGL/src/data/resources/textures/aa.png')
h = img.shape[0]
w = img.shape[1]
img_out = cv2.warpPerspective(img, T, (w,h))

cv2.imshow('img_out', img_out)
cv2.waitKey(0)