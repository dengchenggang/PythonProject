#!/usr/bin/python3
# -*-coding: utf-8 -*-
import cv2
import numpy as np

if __name__ == "__main__":
    img = np.zeros((720, 1920, 3), np.uint8)
    # cv2.circle(img, (171, 305), 1, color=(0, 0, 255), thickness=2)
    # cv2.circle(img, (255, 304), 1, color=(0, 0, 255), thickness=2)
    # cv2.circle(img, (276, 633), 1, color=(0, 0, 255), thickness=2)
    # cv2.circle(img, (242, 605), 1, color=(0, 0, 255), thickness=2)

    cv2.circle(img, (288, 299), 1, color=(0, 0, 255), thickness=2)
    cv2.circle(img, (1767, 92), 1, color=(0, 0, 255), thickness=2)
    cv2.circle(img, (310, 653), 1, color=(0, 0, 255), thickness=2)
    cv2.circle(img, (1060, 367), 1, color=(0, 0, 255), thickness=2)

    cv2.imshow('img', img)
    cv2.waitKey(0)