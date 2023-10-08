import cv2
import numpy as np
import time

cap = cv2.VideoCapture('AITrainer/curls.mp4')
img = cv2.imread('AITrainer/test.jpg')

while True:
    #success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)