import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

previousTime = 0
currentTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmarks.landmark): # landmarks position
                height, width, channel = img.shape # height and width of window
                cx, cy = int(lm.x * width), int(lm.y * height) # landmaarks coordinates
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            mpDraw.draw_landmarks(img, handLandmarks, mpHands.HAND_CONNECTIONS)


    # calculating the fps
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    
    cv2.putText(img, str(int(fps)), (15, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
