import cv2
import numpy as np
import mediapipe as mp
from HandLandmarkModule import handDetector

img = cv2.imread('16.jpg')
height, width, channels = img.shape
print('height =', height)
print('width =', width)
print('channels =', channels)

obj = handDetector()
positions = obj.landmarkPositions(img)
positions = np.array(positions)

min_y = min(positions[:, 2])
max_y = max(positions[:, 2])
min_x = min(positions[:, 1])
max_x = max(positions[:, 1])

cropped_image = img[min_y - 25 : max_y + 25, min_x - 25 : max_x + 25]



for i in range(len(positions)):
    print('id =', positions[i][0], '    x = ', positions[i][1], '    y = ', positions[i][2])

#print(type(positions))
#print(positions[:, 0])
#print('min x = ', min(positions[:, 1]))

cv2.imshow('image', img)
cv2.imshow('cropped image', cropped_image)
cv2.waitKey(0)
