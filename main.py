import cv2
import mediapipe as mp
import time
from HandLandmarkModule import handDetector

cap = cv2.VideoCapture(0)
yo = handDetector()

while True:
    success, img = cap.read()

    print(yo.findHands(img))