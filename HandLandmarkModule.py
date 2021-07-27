import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,
                 mode = False,
                 maxHands = 1,
                 detectionConfidence = 0.5,
                 trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,
                                        self.maxHands,
                                        self.detectionConfidence,
                                        self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils

    def landmarkPositions(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        lmList = []
        if results.multi_hand_landmarks:
            for handLandmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(handLandmarks.landmark):  # landmarks position
                    height, width, channel = img.shape  # height and width of window
                    cx, cy = int(lm.x * width), int(lm.y * height)  # landmaarks coordinates
                    lmList.append((id, cx, cy))
            return lmList
