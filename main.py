#!/usr/bin/python3
# -*-coding: utf-8 -*-
import cv2
import numpy as np

#  wolrdPos:(-4.383876, -1.700000, 2.995136), uvPos:(171.545532, 305.912537, 1.000000) 
# ARRenderer::OverlayCreate: type 0 
#  wolrdPos:(-3.813700, -1.700000, 3.794065), uvPos:(255.660950, 304.677124, 1.000000) 
# ARRenderer::OverlayCreate: type 0 
#  wolrdPos:(-3.813700, -0.000000, 3.794065), uvPos:(276.038635, 633.218750, 1.000000) 
# ARRenderer::OverlayCreate: type 0 
#  wolrdPos:(-4.383876, 0.000000, 2.995136), uvPos:(242.404419, 605.591064, 1.000000) 

if __name__ == "__main__":
    img = np.zeros((720, 1920, 3), np.uint8)
    cv2.circle(img, (171, 305), 1, color=(0, 0, 255), thickness=2)
    cv2.circle(img, (255, 304), 1, color=(0, 0, 255), thickness=2)
    cv2.circle(img, (276, 633), 1, color=(0, 0, 255), thickness=2)
    cv2.circle(img, (242, 605), 1, color=(0, 0, 255), thickness=2)
    cv2.imshow('img', img)
    cv2.waitKey(0)