import cv2
import mediapipe as mp
import time
from HandLandmarkModule import handDetector
from CropHand import CropHand

cap = cv2.VideoCapture(0)

cropped = CropHand()

while True:
    success, img = cap.read()
    cropped_img = cropped.crop(img)

    cv2.imshow('image', img)
    cv2.waitKey(1)
    if cropped_img.size:
        cv2.imshow('cropped imge', cropped_img)

    